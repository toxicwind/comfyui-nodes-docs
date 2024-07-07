# Documentation
- Class name: IFUnet_VFI
- Category: ComfyUI-Frame-Interpolation/VFI
- Output node: False
- Repo Ref: https://github.com/Fannovel16/ComfyUI-Frame-Interpolation

The IFUnet_VFI node is designed to implement video frame plugs to enhance the smoothness and continuity of video transitions by generating an intermediate frame. It uses a deep learning model to predict and insert the frame between existing frames, thereby improving the overall visual quality and fluidity of the video sequence.

# Input types
## Required
- ckpt_name
    - Checkpoint name parameters are essential for identifying specific model weights for frame plug value. They point nodes to the correct pre-training model to ensure the accuracy and efficiency of the frame generation process.
    - Comfy dtype: str
    - Python dtype: str
- frames
    - The frame parameters are necessary because they provide the input frame at which the node will process the plug value. The quality and resolution of the input frame directly influences the visual appearance of the output frame.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
## Optional
- clear_cache_after_n_frames
    - Clear_cache_after_n_frames parameters are very important in managing memory use during frame plug-in. It helps to maintain systemic performance by clearing caches after processing a certain number of frames.
    - Comfy dtype: INT
    - Python dtype: int
- multiplier
    - The multiplier parameter determines the number of intermediate frames that are generated between successive frames. It is a key factor in controlling the density of the frame and, in turn, the smoothness of the video.
    - Comfy dtype: INT
    - Python dtype: int
- scale_factor
    - Scale_factor parameters adjust the scale of the input frame before processing. This is an important factor that affects the details and resolution of the plug-in frame.
    - Comfy dtype: FLOAT
    - Python dtype: float
- ensemble
    - The Esmble parameter enables an integrated method to increase the stability and quality of the frame of the plug. It is an optional feature that enhances the performance of nodes under certain conditions.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- optional_interpolation_states
    - General_interposition_states parameters provide additional control over the plug-in process and allow custom frames to be generated according to specific requirements or constraints.
    - Comfy dtype: INTERPOLATION_STATES
    - Python dtype: InterpolationStateList

# Output types
- output_frames
    - The output_frames parameter represents the result of the frame plug-in process. It contains the original frame and the newly generated middle frame, which enhances video continuity and visual appeal.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class IFUnet_VFI:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'ckpt_name': (CKPT_NAMES,), 'frames': ('IMAGE',), 'clear_cache_after_n_frames': ('INT', {'default': 10, 'min': 1, 'max': 1000}), 'multiplier': ('INT', {'default': 2, 'min': 2, 'max': 1000}), 'scale_factor': ('FLOAT', {'default': 1.0, 'min': 0.1, 'max': 100, 'step': 0.1}), 'ensemble': ('BOOLEAN', {'default': True})}, 'optional': {'optional_interpolation_states': ('INTERPOLATION_STATES',)}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'vfi'
    CATEGORY = 'ComfyUI-Frame-Interpolation/VFI'

    def vfi(self, ckpt_name: typing.AnyStr, frames: torch.Tensor, clear_cache_after_n_frames: typing.SupportsInt=1, multiplier: typing.SupportsInt=2, scale_factor: typing.SupportsFloat=1.0, ensemble: bool=True, optional_interpolation_states: InterpolationStateList=None, **kwargs):
        from .IFUNet_arch import IFUNetModel
        model_path = load_file_from_github_release(MODEL_TYPE, ckpt_name)
        interpolation_model = IFUNetModel()
        interpolation_model.load_state_dict(torch.load(model_path))
        interpolation_model.eval().to(get_torch_device())
        frames = preprocess_frames(frames)

        def return_middle_frame(frame_0, frame_1, timestep, model, scale_factor, ensemble):
            return model(frame_0, frame_1, timestep=timestep, scale=scale_factor, ensemble=ensemble)
        args = [interpolation_model, scale_factor, ensemble]
        out = postprocess_frames(generic_frame_loop(frames, clear_cache_after_n_frames, multiplier, return_middle_frame, *args, interpolation_states=optional_interpolation_states, dtype=torch.float32))
        return (out,)
```