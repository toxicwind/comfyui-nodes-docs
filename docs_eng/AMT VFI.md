# Documentation
- Class name: AMT_VFI
- Category: ComfyUI-Frame-Interpolation/VFI
- Output node: False
- Repo Ref: https://github.com/Fannovel16/ComfyUI-Frame-Interpolation

The AMT_VFI node is designed to perform video frame plugs, increase the smoothness of the transition between frames and effectively increase the frame rate of the video sequence. It uses pre-training models to generate intermediate frames that do not exist in the raw material, contributing to a more fluid visual effect.

# Input types
## Required
- ckpt_name
    - Checkpoint name parameters are essential for identifying specific model configurations for frame plugs. They point nodes to the right pre-training models to ensure the required output quality and performance.
    - Comfy dtype: str
    - Python dtype: str
- frames
    - The frame parameters are necessary because it means that the node will process the input of the plug value into the video frame. The quality and resolution of the input frame directly influences the final plugin output.
    - Comfy dtype: torch.Tensor
    - Python dtype: torch.Tensor
## Optional
- clear_cache_after_n_frames
    - Clear_cache_after_n_frames parameters are used to optimize memory use by clearing caches after processing a specified number of frames. This helps to prevent overloading during a dense frame plug-in task.
    - Comfy dtype: int
    - Python dtype: int
- multiplier
    - The multiplier parameter determines the number of intermediate frames that are generated between the two existing frames. The higher the value, the higher the frame rate of the output video, it may also add to the computational complexity.
    - Comfy dtype: int
    - Python dtype: int
- optional_interpolation_states
    - General_interpolation_states parameters provide additional control over frame-plug-in processes and allow custom-plug-in behaviour for specific frames.
    - Comfy dtype: InterpolationStateList
    - Python dtype: InterpolationStateList

# Output types
- interpolated_frames
    - The interpolated_frames output contains the original video frame and the newly generated middle frame, resulting in a smoother and higher frame-rate video sequence.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class AMT_VFI:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'ckpt_name': (list(CKPT_CONFIGS.keys()),), 'frames': ('IMAGE',), 'clear_cache_after_n_frames': ('INT', {'default': 1, 'min': 1, 'max': 100}), 'multiplier': ('INT', {'default': 2, 'min': 2, 'max': 1000})}, 'optional': {'optional_interpolation_states': ('INTERPOLATION_STATES',)}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'vfi'
    CATEGORY = 'ComfyUI-Frame-Interpolation/VFI'

    def vfi(self, ckpt_name: typing.AnyStr, frames: torch.Tensor, clear_cache_after_n_frames: typing.SupportsInt=1, multiplier: typing.SupportsInt=2, optional_interpolation_states: InterpolationStateList=None, **kwargs):
        model_path = load_file_from_direct_url(MODEL_TYPE, f'https://huggingface.co/lalala125/AMT/resolve/main/{ckpt_name}')
        ckpt_config = CKPT_CONFIGS[ckpt_name]
        interpolation_model = ckpt_config['network'](**ckpt_config['params'])
        interpolation_model.load_state_dict(torch.load(model_path)['state_dict'])
        interpolation_model.eval().to(get_torch_device())
        frames = preprocess_frames(frames)
        padder = InputPadder(frames.shape, 16)
        frames = padder.pad(frames)

        def return_middle_frame(frame_0, frame_1, timestep, model):
            return model(frame_0, frame_1, embt=torch.FloatTensor([timestep] * frame_0.shape[0]).view(frame_0.shape[0], 1, 1, 1).to(get_torch_device()), scale_factor=1.0, eval=True)['imgt_pred']
        args = [interpolation_model]
        out = generic_frame_loop(frames, clear_cache_after_n_frames, multiplier, return_middle_frame, *args, interpolation_states=optional_interpolation_states, dtype=torch.float32)
        out = padder.unpad(out)
        out = postprocess_frames(out)
        return (out,)
```