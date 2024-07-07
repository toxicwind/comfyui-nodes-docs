# Documentation
- Class name: FLAVR_VFI
- Category: ComfyUI-Frame-Interpolation/VFI
- Output node: False
- Repo Ref: https://github.com/Fannovel16/ComfyUI-Frame-Interpolation

The FLAVR_VFI node is designed to implement frame plugs in the input frame sequence to enhance the smoothness and continuity of the animation. It uses the bottom model to create an intermediate frame that effectively doubles the frame rate. This node is essential for applications that require fluid movement without the need for a large amount of computational resources.

# Input types
## Required
- ckpt_name
    - Checkpoint name parameters are essential for identifying specific model weights for frame plugs. It ensures that the correct model configuration is loaded to handle frames.
    - Comfy dtype: str
    - Python dtype: str
- frames
    - The frames parameter is a key input that contains an image sequence for the plug value. It forms the basis for the plug-in process, and the nodes generate additional frames between the frames provided in order to achieve a smoother transition.
    - Comfy dtype: torch.Tensor
    - Python dtype: torch.Tensor
## Optional
- clear_cache_after_n_frames
    - Clear_cache_after_n_frames parameters determine how often the GPU cache is cleared during the processing period to maintain optimal performance. It helps to effectively manage memory use and prevent potential slowdowns or crashes due to RAM.
    - Comfy dtype: int
    - Python dtype: int
- multiplier
    - The multiplier parameter specifies that the frame rate should be multiplied. At present, the node only supports a multiplier of 2, which doubles the frame rate of the input sequence.
    - Comfy dtype: int
    - Python dtype: int
- duplicate_first_last_frames
    - When set to true, the duplicate_first_last_frames parameters reproduce the first and last frames in the output sequence. This is very useful for maintaining the consistent beginning and end of the plug-in animation.
    - Comfy dtype: bool
    - Python dtype: bool
- optional_interpolation_states
    - The option_interpolation_states parameter provides a way to specify which frames should be skipped or included from the definition plug-in process. This allows fine-tuning plugins to meet specific creative requirements.
    - Comfy dtype: InterpolationStateList
    - Python dtype: InterpolationStateList

# Output types
- interpolated_frames
    - These frames include the original input frame and the newly generated intermediate frame, which provides a smoother and more continuous visual output.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class FLAVR_VFI:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'ckpt_name': (CKPT_NAMES,), 'frames': ('IMAGE',), 'clear_cache_after_n_frames': ('INT', {'default': 10, 'min': 1, 'max': 1000}), 'multiplier': ('INT', {'default': 2, 'min': 2, 'max': 2}), 'duplicate_first_last_frames': ('BOOLEAN', {'default': False})}, 'optional': {'optional_interpolation_states': ('INTERPOLATION_STATES',)}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'vfi'
    CATEGORY = 'ComfyUI-Frame-Interpolation/VFI'

    def vfi(self, ckpt_name: typing.AnyStr, frames: torch.Tensor, clear_cache_after_n_frames=10, multiplier: typing.SupportsInt=2, duplicate_first_last_frames: bool=False, optional_interpolation_states: InterpolationStateList=None, **kwargs):
        if multiplier != 2:
            warnings.warn('Currently, FLAVR only supports 2x interpolation. The process will continue but please set multiplier=2 afterward')
        assert_batch_size(frames, batch_size=4, vfi_name='ST-MFNet')
        interpolation_states = optional_interpolation_states
        model_path = load_file_from_github_release(MODEL_TYPE, ckpt_name)
        model = build_flavr(model_path)
        frames = preprocess_frames(frames)
        padder = InputPadder(frames.shape, 16)
        frames = padder.pad(frames)
        number_of_frames_processed_since_last_cleared_cuda_cache = 0
        output_frames = []
        for frame_itr in range(len(frames) - 3):
            if interpolation_states is not None and interpolation_states.is_frame_skipped(frame_itr) and interpolation_states.is_frame_skipped(frame_itr + 1):
                continue
            (frame0, frame1, frame2, frame3) = (frames[frame_itr:frame_itr + 1].float(), frames[frame_itr + 1:frame_itr + 2].float(), frames[frame_itr + 2:frame_itr + 3].float(), frames[frame_itr + 3:frame_itr + 4].float())
            new_frame = model([frame0.to(device), frame1.to(device), frame2.to(device), frame3.to(device)])[0].detach().cpu()
            number_of_frames_processed_since_last_cleared_cuda_cache += 2
            if frame_itr == 0:
                output_frames.append(frame0)
                if duplicate_first_last_frames:
                    output_frames.append(frame0)
                output_frames.append(frame1)
            output_frames.append(new_frame)
            output_frames.append(frame2)
            if frame_itr == len(frames) - 4:
                output_frames.append(frame3)
                if duplicate_first_last_frames:
                    output_frames.append(frame3)
            if number_of_frames_processed_since_last_cleared_cuda_cache >= clear_cache_after_n_frames:
                print('Comfy-VFI: Clearing cache...', end=' ')
                soft_empty_cache()
                number_of_frames_processed_since_last_cleared_cuda_cache = 0
                print('Done cache clearing')
            gc.collect()
        dtype = torch.float32
        output_frames = [frame.cpu().to(dtype=dtype) for frame in output_frames]
        out = torch.cat(output_frames, dim=0)
        out = padder.unpad(out)
        print('Comfy-VFI: Final clearing cache...', end=' ')
        soft_empty_cache()
        print('Done cache clearing')
        return (postprocess_frames(out),)
```