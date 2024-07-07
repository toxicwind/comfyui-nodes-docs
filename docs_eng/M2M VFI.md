# Documentation
- Class name: M2M_VFI
- Category: ComfyUI-Frame-Interpolation/VFI
- Output node: False
- Repo Ref: https://github.com/Fannovel16/ComfyUI-Frame-Interpolation

The M2M_VFI node is designed to insert frames between the given two video frames to enhance the smoothness and continuity of the video sequence. It uses the deep learning model to generate intermediate frames that do not exist in the raw material, thus creating a more fluid visual experience.

# Input types
## Required
- ckpt_name
    - The check point name parameter is essential for determining a specific pre-training model for frame plugs. It ensures that the right weights and configurations are loaded to achieve the desired plug-in results.
    - Comfy dtype: str
    - Python dtype: str
- frames
    - The frame parameter is necessary because it represents a node that will process the input frame of the plug value. The input frame quality and resolution directly influences the output of the plug value, making this parameter very important for node execution.
    - Comfy dtype: torch.Tensor
    - Python dtype: torch.Tensor
## Optional
- clear_cache_after_n_frames
    - Clear_cache_after_n_frames parameters determine the frequency of node clean-up caches to manage memory use. This is important for maintaining performance, especially when processing large amounts of video data.
    - Comfy dtype: int
    - Python dtype: int
- multiplier
    - Multiplier parameters affect the number of intermediate frames that are generated between the input frames. The higher the value, the more the plug-in frames are generated, a smoother transition can be achieved, but it may also increase the computational need.
    - Comfy dtype: int
    - Python dtype: int
- optional_interpolation_states
    - The output_interposition_states parameter provides a method of defining the value-plug-in process by specifying certain states or conditions. This advanced function allows for greater control of the output frame to meet specific project needs.
    - Comfy dtype: InterpolationStateList
    - Python dtype: InterpolationStateList

# Output types
- output_frames
    - The output_frames parameter represents the result of the frame plug-in process. It contains the original frame and the newly generated middle frame, providing a complete and enhanced video sequence.
    - Comfy dtype: torch.Tensor
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class M2M_VFI:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'ckpt_name': (CKPT_NAMES,), 'frames': ('IMAGE',), 'clear_cache_after_n_frames': ('INT', {'default': 10, 'min': 1, 'max': 1000}), 'multiplier': ('INT', {'default': 2, 'min': 2, 'max': 1000})}, 'optional': {'optional_interpolation_states': ('INTERPOLATION_STATES',)}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'vfi'
    CATEGORY = 'ComfyUI-Frame-Interpolation/VFI'

    def vfi(self, ckpt_name: typing.AnyStr, frames: torch.Tensor, clear_cache_after_n_frames: typing.SupportsInt=1, multiplier: typing.SupportsInt=2, optional_interpolation_states: InterpolationStateList=None, **kwargs):
        from .M2M_arch import M2M_PWC
        model_path = load_file_from_github_release(MODEL_TYPE, ckpt_name)
        interpolation_model = M2M_PWC()
        interpolation_model.load_state_dict(torch.load(model_path))
        interpolation_model.eval().to(get_torch_device())
        frames = preprocess_frames(frames)

        def return_middle_frame(frame_0, frame_1, int_timestep, model):
            tenSteps = [torch.FloatTensor([int_timestep] * len(frame_0)).view(len(frame_0), 1, 1, 1).to(get_torch_device())]
            return model(frame_0, frame_1, tenSteps)[0]
        args = [interpolation_model]
        out = postprocess_frames(generic_frame_loop(frames, clear_cache_after_n_frames, multiplier, return_middle_frame, *args, interpolation_states=optional_interpolation_states, dtype=torch.float32))
        return (out,)
```