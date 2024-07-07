# Documentation
- Class name: RIFE_VFI
- Category: ComfyUI-Frame-Interpolation/VFI
- Output node: False
- Repo Ref: https://github.com/Fannovel16/ComfyUI-Frame-Interpolation

The RIFE_VFI node is designed to perform video frame plugs using the specified check-point model. It generates the plug-in between input frames, effectively doubling the frame rate. The node operates by sequentially processing each frame and creating a new frame, increasing the smoothness and continuity of the video sequence.

# Input types
## Required
- ckpt_name
    - The ckpt_name parameter is essential for selecting an appropriate check-point model for frame plug-in values. It determines that node will be applied to generate the specific weight and structure of the plug-in frame.
    - Comfy dtype: str
    - Python dtype: str
- frames
    - The frame parameters are necessary because they contain the input frame that the node will process. The quality and resolution of the input frame directly influences the output of the plug value, making this parameter very important to the operation of the node.
    - Comfy dtype: torch.Tensor
    - Python dtype: torch.Tensor
## Optional
- clear_cache_after_n_frames
    - Clear_cache_after_n_frames is an optional setting that helps manage memory use during plug-in. It specifies the number of frames to be processed before clearing the CUDA cache to prevent an overflow of memory, which can be adjusted according to the memory capacity of the system and the number of frames entered.
    - Comfy dtype: int
    - Python dtype: int
- multiplier
    - Multiplier parameters determine the number of times to be multiplied when input frames are generated. For example, using a multiplier of two, each input frame produces two output frames, effectively creating a plug-in frame between them.
    - Comfy dtype: int
    - Python dtype: int
- fast_mode
    - Thefast_mode parameter is an optional boolean symbol that allows for faster, but possibly less precise, plug-in processes when set to True. This is very useful for quick previewing or processing of a large number of frames.
    - Comfy dtype: bool
    - Python dtype: bool
- ensemble
    - The ensemble parameter allows the combination of multiple plug-in models to improve the quality of the plug-in frame. When enabled, it may increase processing time, but it can lead to more stable and more authentic outcomes.
    - Comfy dtype: bool
    - Python dtype: bool
- scale_factor
    - Scale_factor parameters adjust the resolution of the input frame before processing. It is particularly suitable for processing different frame sizes and can affect the clarity and detail of the final output.
    - Comfy dtype: float
    - Python dtype: float
- optional_interpolation_states
    - General_interpolation_states parameters provide a method of using the extra-state custom plug-in process. This may include specific instructions or conditions that influence the frame plug-in mode and allow for more finer particle size control of output.
    - Comfy dtype: INTERPOLATION_STATES
    - Python dtype: InterpolationStateList

# Output types
- interpolated_frames
    - The interpolated_frames parameter represents the output of the frame plug-in process. It contains the original input frame and the newly generated intermediate frame, which effectively creates a more smooth video sequence.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class RIFE_VFI:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'ckpt_name': (sorted(list(CKPT_NAME_VER_DICT.keys()), key=lambda ckpt_name: version.parse(CKPT_NAME_VER_DICT[ckpt_name])), {'default': 'rife47.pth'}), 'frames': ('IMAGE',), 'clear_cache_after_n_frames': ('INT', {'default': 10, 'min': 1, 'max': 1000}), 'multiplier': ('INT', {'default': 2, 'min': 1}), 'fast_mode': ('BOOLEAN', {'default': True}), 'ensemble': ('BOOLEAN', {'default': True}), 'scale_factor': ([0.25, 0.5, 1.0, 2.0, 4.0], {'default': 1.0})}, 'optional': {'optional_interpolation_states': ('INTERPOLATION_STATES',)}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'vfi'
    CATEGORY = 'ComfyUI-Frame-Interpolation/VFI'

    def vfi(self, ckpt_name: typing.AnyStr, frames: torch.Tensor, clear_cache_after_n_frames=10, multiplier: typing.SupportsInt=2, fast_mode=False, ensemble=False, scale_factor=1.0, optional_interpolation_states: InterpolationStateList=None, **kwargs):
        """
        Perform video frame interpolation using a given checkpoint model.
    
        Args:
            ckpt_name (str): The name of the checkpoint model to use.
            frames (torch.Tensor): A tensor containing input video frames.
            clear_cache_after_n_frames (int, optional): The number of frames to process before clearing CUDA cache
                to prevent memory overflow. Defaults to 10. Lower numbers are safer but mean more processing time.
                How high you should set it depends on how many input frames there are, input resolution (after upscaling),
                how many times you want to multiply them, and how long you're willing to wait for the process to complete.
            multiplier (int, optional): The multiplier for each input frame. 60 input frames * 2 = 120 output frames. Defaults to 2.
    
        Returns:
            tuple: A tuple containing the output interpolated frames.
    
        Note:
            This method interpolates frames in a video sequence using a specified checkpoint model. 
            It processes each frame sequentially, generating interpolated frames between them.
    
            To prevent memory overflow, it clears the CUDA cache after processing a specified number of frames.
        """
        from .rife_arch import IFNet
        model_path = load_file_from_github_release(MODEL_TYPE, ckpt_name)
        arch_ver = CKPT_NAME_VER_DICT[ckpt_name]
        interpolation_model = IFNet(arch_ver=arch_ver)
        interpolation_model.load_state_dict(torch.load(model_path))
        interpolation_model.eval().to(get_torch_device())
        frames = preprocess_frames(frames)

        def return_middle_frame(frame_0, frame_1, timestep, model, scale_list, in_fast_mode, in_ensemble):
            return model(frame_0, frame_1, timestep, scale_list, in_fast_mode, in_ensemble)
        scale_list = [8 / scale_factor, 4 / scale_factor, 2 / scale_factor, 1 / scale_factor]
        args = [interpolation_model, scale_list, fast_mode, ensemble]
        out = postprocess_frames(generic_frame_loop(frames, clear_cache_after_n_frames, multiplier, return_middle_frame, *args, interpolation_states=optional_interpolation_states, dtype=torch.float32))
        return (out,)
```