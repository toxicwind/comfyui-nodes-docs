# Documentation
- Class name: CalculateFrameOffset
- Category: FizzNodes 📅🅕🅝/HelperNodes
- Output node: False
- Repo Ref: https://github.com/FizzleDorf/ComfyUI_FizzNodes

CalculateFrameofset is designed to calculate and assign frame numbers in a sequence based on the current frame, the maximum number of frames and potential input quantities. It plays a key role in managing the sequence of frame-related operations.

# Input types
## Required
- current_frame
    - The Current_frame parameter specifies the current position in the frame sequence. This is essential to determine the starting point of the frame number allocation.
    - Comfy dtype: INT
    - Python dtype: int
- max_frames
    - The max_frames parameter has a frame number ceiling. This is essential to ensure that frame numbers remain within valid limits.
    - Comfy dtype: INT
    - Python dtype: int
- num_latent_inputs
    - Num_latent_inputs parameters indicate the amount of potential input to be used for frame calculations. It significantly affects the distribution of frame numbers within the sequence.
    - Comfy dtype: INT
    - Python dtype: int
- index
    - The index parameter represents the specific index in the potential input. It is used to calculate the deviation of the assigned frame number.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- frame_offset
    - The frame_offset output is a frame number given for the input calculation. It is important for the follow-up and processing of the frame in the sequence.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class CalculateFrameOffset:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'current_frame': ('INT', {'default': 0, 'min': 0}), 'max_frames': ('INT', {'default': 18, 'min': 0}), 'num_latent_inputs': ('INT', {'default': 4, 'min': 0}), 'index': ('INT', {'default': 4, 'min': 0})}}
    RETURN_TYPES = ('INT',)
    FUNCTION = 'assignFrameNum'
    CATEGORY = 'FizzNodes 📅🅕🅝/HelperNodes'

    def assignFrameNum(self, current_frame, max_frames, num_latent_inputs, index):
        if current_frame == 0:
            return (index,)
        else:
            start_frame = (current_frame - 1) * (num_latent_inputs - 1) + (num_latent_inputs - 1)
            return ((start_frame + index) % max_frames,)
```