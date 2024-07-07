# Documentation
- Class name: CAIN_VFI
- Category: ComfyUI-Frame-Interpolation/VFI
- Output node: False
- Repo Ref: https://github.com/Fannovel16/ComfyUI-Frame-Interpolation

CAIN_VFI nodes are designed to implement frame plugs for a range of images, increasing the smoothness and continuity of the transition between frames. It uses the CAIN architecture to generate intermediate frames that do not exist in the original sequence, thereby creating more intensive and detailed motion expressions.

# Input types
## Required
- ckpt_name
    - The check point name is essential for the pre-training model weights required to load frame plugs. It identifies the particular model to be used in the operation.
    - Comfy dtype: str
    - Python dtype: str
- frames
    - The input frame indicates the image sequence that will be processed for the frame plug-in. This input is essential because it forms the basis for generating a new frame.
    - Comfy dtype: torch.Tensor
    - Python dtype: torch.Tensor
## Optional
- clear_cache_after_n_frames
    - This parameter determines the frequency of clearing caches during processing to manage memory usage. It affects the performance and memory efficiency of nodes.
    - Comfy dtype: int
    - Python dtype: int
- multiplier
    - The multiplier factor determines the number of intermediate frames to be generated between each input frame. It directly affects the density of the output frame sequence.
    - Comfy dtype: int
    - Python dtype: int
- optional_interpolation_states
    - This optional parameter provides additional control over the frame plug-in process and allows custom plug-in status.
    - Comfy dtype: InterpolationStateList
    - Python dtype: InterpolationStateList

# Output types
- output_frames
    - The output_frames parameters contain the resulting plug-in frame sequences, including the original frame and the newly created intermediate frame.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class CAIN_VFI:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'ckpt_name': (CKPT_NAMES,), 'frames': ('IMAGE',), 'clear_cache_after_n_frames': ('INT', {'default': 10, 'min': 1, 'max': 1000}), 'multiplier': ('INT', {'default': 2, 'min': 2, 'max': 1000})}, 'optional': {'optional_interpolation_states': ('INTERPOLATION_STATES',)}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'vfi'
    CATEGORY = 'ComfyUI-Frame-Interpolation/VFI'

    def vfi(self, ckpt_name: typing.AnyStr, frames: torch.Tensor, clear_cache_after_n_frames: typing.SupportsInt=1, multiplier: typing.SupportsInt=2, optional_interpolation_states: InterpolationStateList=None, **kwargs):
        from .cain_arch import CAIN
        model_path = load_file_from_github_release(MODEL_TYPE, ckpt_name)
        sd = torch.load(model_path)['state_dict']
        sd = {key.replace('module.', ''): value for (key, value) in sd.items()}
        global interpolation_model
        interpolation_model = CAIN(depth=3)
        interpolation_model.load_state_dict(sd)
        interpolation_model.eval().to(get_torch_device())
        del sd
        frames = preprocess_frames(frames)

        def return_middle_frame(frame_0, frame_1, timestep, model):
            return model(frame_0.detach().clone(), frame_1.detach().clone())[0]
        args = [interpolation_model]
        out = postprocess_frames(generic_frame_loop(frames, clear_cache_after_n_frames, multiplier, return_middle_frame, *args, interpolation_states=optional_interpolation_states, use_timestep=False, dtype=torch.float32))
        return (out,)
```