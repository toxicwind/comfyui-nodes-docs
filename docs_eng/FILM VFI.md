# Documentation
- Class name: FILM_VFI
- Category: ComfyUI-Frame-Interpolation/VFI
- Output node: False
- Repo Ref: https://github.com/Fannovel16/ComfyUI-Frame-Interpolation

The FILM_VFI node is designed to increase the smoothness and smoothness of the frame without sacrificing the quality of the visual. It is achieved through a complex model that uses machine-learning techniques to create an intermediate frame between existing frames, resulting in a more fluid and real motor effect for the video sequence.

# Input types
## Required
- ckpt_name
    - The ckpt name is a key parameter used to specify a pre-training model for frame plugs. It directly affects the quality and accuracy of the frame plugs, as different models may train or use different algorithms on different data sets.
    - Comfy dtype: STRING
    - Python dtype: str
- frames
    - The input frames are the source material of the frame plug-in process. They are essential because they provide the visual context in which nodes generate extra frames, thereby enhancing the entire video sequence. The quality and resolution of the input frames play an important role in determining the visual authenticity of the output.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
## Optional
- clear_cache_after_n_frames
    - This parameter helps to manage computing resources by specifying how often a cache should be cleared during the frame plug-in process. It indirectly affects the performance and memory use of nodes and ensures that they operate within available system resources.
    - Comfy dtype: INT
    - Python dtype: int
- multiplier
    - Multiplier parameters determine the additional frames to be generated between each input frame. It is essential to control the density of the output video, and higher values can lead to more smooth motion, but at the cost of increasing the complexity of calculations.
    - Comfy dtype: INT
    - Python dtype: int
- optional_interpolation_states
    - This parameter allows the custom frame plug-in process by specifying which frames should skip or not jump over. It provides a certain level of control over the final output, allowing nodes to meet the specific requirements or limitations of the video content.
    - Comfy dtype: INTERPOLATION_STATES
    - Python dtype: InterpolationStateList

# Output types
- output_frames
    - Output_frames represents the results of the frame plug-in process, including the original input frame and the newly generated middle frame. This output is important because it provides a higher frame-rate video that enhances the smoothness of visual experience and motion.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class FILM_VFI:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'ckpt_name': (['film_net_fp32.pt'],), 'frames': ('IMAGE',), 'clear_cache_after_n_frames': ('INT', {'default': 10, 'min': 1, 'max': 1000}), 'multiplier': ('INT', {'default': 2, 'min': 2, 'max': 1000})}, 'optional': {'optional_interpolation_states': ('INTERPOLATION_STATES',)}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'vfi'
    CATEGORY = 'ComfyUI-Frame-Interpolation/VFI'

    def vfi(self, ckpt_name: typing.AnyStr, frames: torch.Tensor, clear_cache_after_n_frames=10, multiplier: typing.SupportsInt=2, optional_interpolation_states: InterpolationStateList=None, **kwargs):
        interpolation_states = optional_interpolation_states
        model_path = load_file_from_github_release(MODEL_TYPE, ckpt_name)
        model = torch.jit.load(model_path, map_location='cpu')
        model.eval()
        model = model.to(DEVICE)
        dtype = torch.float32
        frames = preprocess_frames(frames)
        number_of_frames_processed_since_last_cleared_cuda_cache = 0
        output_frames = []
        for frame_itr in range(len(frames) - 1):
            if interpolation_states is not None and interpolation_states.is_frame_skipped(frame_itr):
                continue
            frame_0 = frames[frame_itr:frame_itr + 1].to(DEVICE).float()
            frame_1 = frames[frame_itr + 1:frame_itr + 2].to(DEVICE).float()
            relust = inference(model, frame_0, frame_1, multiplier - 1)
            output_frames.extend([frame.detach().cpu().to(dtype=dtype) for frame in relust[:-1]])
            number_of_frames_processed_since_last_cleared_cuda_cache += 1
            if number_of_frames_processed_since_last_cleared_cuda_cache >= clear_cache_after_n_frames:
                print('Comfy-VFI: Clearing cache...')
                soft_empty_cache()
                number_of_frames_processed_since_last_cleared_cuda_cache = 0
                print('Comfy-VFI: Done cache clearing')
            gc.collect()
        output_frames.append(frames[-1:].to(dtype=dtype))
        output_frames = [frame.cpu() for frame in output_frames]
        out = torch.cat(output_frames, dim=0)
        print('Comfy-VFI: Final clearing cache...')
        soft_empty_cache()
        print('Comfy-VFI: Done cache clearing')
        return (postprocess_frames(out),)
```