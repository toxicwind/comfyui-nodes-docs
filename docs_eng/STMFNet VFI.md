# Documentation
- Class name: STMFNet_VFI
- Category: ComfyUI-Frame-Interpolation/VFI
- Output node: False
- Repo Ref: https://github.com/Fannovel16/ComfyUI-Frame-Interpolation

The STMFNet_VFI node is designed to perform video frame plugs to increase the smoothness of the transition between frames in the video sequence. It does so by generating intermediate frames that do not exist in the raw material, thereby increasing frame rates and improving overall visual quality.

# Input types
## Required
- ckpt_name
    - The name of the check point is essential for the pre-training model weights needed to load the frame plug-in process. It ensures that the model has the parameters necessary to generate an accurate middle frame.
    - Comfy dtype: str
    - Python dtype: str
- frames
    - The input frame is the original video data that the node processes to create the plug-in frame. The quality and resolution of these frames directly influences the output of the plug-in value.
    - Comfy dtype: torch.Tensor
    - Python dtype: torch.Tensor
## Optional
- clear_cache_after_n_frames
    - This parameter determines how often the system clears the cache during the processing period, which helps to manage memory use. This is particularly important for long video sequences to prevent overloading.
    - Comfy dtype: int
    - Python dtype: int
- multiplier
    - Multipliers are used to determine the number of times the frame rate will increase. However, the current achievement supports only 2 multipliers.
    - Comfy dtype: int
    - Python dtype: int
- duplicate_first_last_frames
    - When this option is enabled, it reproduces the first and last frames in the output, which provides a smoother start and end for the plug-in video sequence.
    - Comfy dtype: bool
    - Python dtype: bool
- optional_interpolation_states
    - This optional parameter allows a custom plug-in state to skip some frames during the plug-in according to specific criteria.
    - Comfy dtype: InterpolationStateList
    - Python dtype: InterpolationStateList

# Output types
- interpolated_frames
    - The output of the STMFNet_VFI node is the video frame after the plug value. These frames are the result of the frame plug-in process and are prepared for video editing or play.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class STMFNet_VFI:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'ckpt_name': (['stmfnet.pth'],), 'frames': ('IMAGE',), 'clear_cache_after_n_frames': ('INT', {'default': 10, 'min': 1, 'max': 1000}), 'multiplier': ('INT', {'default': 2, 'min': 2, 'max': 2}), 'duplicate_first_last_frames': ('BOOLEAN', {'default': False})}, 'optional': {'optional_interpolation_states': ('INTERPOLATION_STATES',)}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'vfi'
    CATEGORY = 'ComfyUI-Frame-Interpolation/VFI'

    def vfi(self, ckpt_name: typing.AnyStr, frames: torch.Tensor, clear_cache_after_n_frames=10, multiplier: typing.SupportsInt=2, duplicate_first_last_frames: bool=False, optional_interpolation_states: InterpolationStateList=None, **kwargs):
        from .stmfnet_arch import STMFNet_Model
        if multiplier != 2:
            warnings.warn('Currently, ST-MFNet only supports 2x interpolation. The process will continue but please set multiplier=2 afterward')
        assert_batch_size(frames, batch_size=4, vfi_name='ST-MFNet')
        interpolation_states = optional_interpolation_states
        model_path = load_file_from_github_release(MODEL_TYPE, ckpt_name)
        model = STMFNet_Model()
        model.load_state_dict(torch.load(model_path))
        model = model.eval().to(device)
        frames = preprocess_frames(frames)
        number_of_frames_processed_since_last_cleared_cuda_cache = 0
        output_frames = []
        for frame_itr in range(len(frames) - 3):
            if interpolation_states is not None and interpolation_states.is_frame_skipped(frame_itr) and interpolation_states.is_frame_skipped(frame_itr + 1):
                continue
            (frame0, frame1, frame2, frame3) = (frames[frame_itr:frame_itr + 1].float(), frames[frame_itr + 1:frame_itr + 2].float(), frames[frame_itr + 2:frame_itr + 3].float(), frames[frame_itr + 3:frame_itr + 4].float())
            new_frame = model(frame0.to(device), frame1.to(device), frame2.to(device), frame3.to(device)).detach().cpu()
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
                print('Comfy-VFI: Clearing cache...')
                soft_empty_cache()
                number_of_frames_processed_since_last_cleared_cuda_cache = 0
                print('Comfy-VFI: Done cache clearing')
            gc.collect()
        dtype = torch.float32
        output_frames = [frame.cpu().to(dtype=dtype) for frame in output_frames]
        out = torch.cat(output_frames, dim=0)
        print('Comfy-VFI: Final clearing cache...')
        soft_empty_cache()
        print('Comfy-VFI: Done cache clearing')
        return (postprocess_frames(out),)
```