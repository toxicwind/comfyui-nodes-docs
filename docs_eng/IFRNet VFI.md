# Documentation
- Class name: IFRNet_VFI
- Category: ComfyUI-Frame-Interpolation/VFI
- Output node: False
- Repo Ref: https://github.com/Fannovel16/ComfyUI-Frame-Interpolation

The IFRNet_VFI node is designed to implement video frame plugs to increase the smoothness of the transition between frames in the video sequence. It uses a deep learning model to create an intermediate frame, thereby increasing the frame rate without sacrificing visual quality. This node is particularly suitable for applications that require high frame-rate video in order to gain better motion clarity.

# Input types
## Required
- ckpt_name
    - The check point name parameter is essential for the pre-training model weights needed to load the frame plug-in process. It determines the particular model structure to be used at the node and its corresponding weights.
    - Comfy dtype: str
    - Python dtype: str
- frames
    - The frame parameters are necessary because they represent the node that will process the input frame of the plug value. The quality and resolution of the input frame directly influences the output of the plug value.
    - Comfy dtype: torch.Tensor
    - Python dtype: torch.Tensor
## Optional
- clear_cache_after_n_frames
    - Clear_cache_after_n_frames parameters are used to optimize memory use during frame plug-in. It specifies the number of frames that are empty to release memory.
    - Comfy dtype: int
    - Python dtype: int
- multiplier
    - The multiplier parameter defines the rate at which a new frame is inserted between the original frame. A higher multiplier results in a higher frame rate for the output of the video.
    - Comfy dtype: int
    - Python dtype: int
- scale_factor
    - The scale_factor parameter is used to adjust the resolution of the input frame before processing. It can be used to zoom in or narrow the frame as required.
    - Comfy dtype: float
    - Python dtype: float
- optional_interpolation_states
    - The optional_interpolation_states parameter provides additional control over the frame-plug-in process. It allows custom states or conditions to be specified for certain frames during the plug-in period.
    - Comfy dtype: InterpolationStateList
    - Python dtype: InterpolationStateList

# Output types
- output_frames
    - The output_frames parameter is the result of the frame-plug-in process. It contains the original frame and the newly created middle frame, resulting in a more smooth video sequence.
    - Comfy dtype: torch.Tensor
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class IFRNet_VFI:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'ckpt_name': (CKPT_NAMES,), 'frames': ('IMAGE',), 'clear_cache_after_n_frames': ('INT', {'default': 10, 'min': 1, 'max': 1000}), 'multiplier': ('INT', {'default': 2, 'min': 2, 'max': 1000}), 'scale_factor': ([0.25, 0.5, 1.0, 2.0, 4.0], {'default': 1.0})}, 'optional': {'optional_interpolation_states': ('INTERPOLATION_STATES',)}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'vfi'
    CATEGORY = 'ComfyUI-Frame-Interpolation/VFI'

    def vfi(self, ckpt_name: typing.AnyStr, frames: torch.Tensor, clear_cache_after_n_frames: typing.SupportsInt=1, multiplier: typing.SupportsInt=2, scale_factor: typing.SupportsFloat=1.0, optional_interpolation_states: InterpolationStateList=None, **kwargs):
        from .IFRNet_S_arch import IRFNet_S
        from .IFRNet_L_arch import IRFNet_L
        model_path = load_file_from_github_release(MODEL_TYPE, ckpt_name)
        interpolation_model = IRFNet_S() if 'S' in ckpt_name else IRFNet_L()
        interpolation_model.load_state_dict(torch.load(model_path))
        interpolation_model.eval().to(get_torch_device())
        frames = preprocess_frames(frames)

        def return_middle_frame(frame_0, frame_1, timestep, model, scale_factor):
            return model(frame_0, frame_1, timestep, scale_factor)
        args = [interpolation_model, scale_factor]
        out = postprocess_frames(generic_frame_loop(frames, clear_cache_after_n_frames, multiplier, return_middle_frame, *args, interpolation_states=optional_interpolation_states, dtype=torch.float32))
        return (out,)
```