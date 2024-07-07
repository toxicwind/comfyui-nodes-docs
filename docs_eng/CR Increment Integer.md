# Documentation
- Class name: CR_IncrementInteger
- Category: Comfyroll/Animation/Interpolate
- Output node: True
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_Inclement Integer node is intended to increase an integer value from a given frame during the specified frame duration. It is particularly suitable for creating animations, with values that need to increase over time.

# Input types
## Required
- start_value
    - The start-up integer value is defined by the start-up increment parameter. It is essential for setting the starting point of the animation sequence.
    - Comfy dtype: INT
    - Python dtype: int
- step
    - The Step parameter specifies the incremental amount of each frame start_value. It determines the rate of change in the whole animated value.
    - Comfy dtype: INT
    - Python dtype: int
- start_frame
    - Start_frame parameters indicate an increment of the frame number. It is essential for the start of the time animation.
    - Comfy dtype: INT
    - Python dtype: int
- frame_duration
    - The frame_duration parameter sets the number of frames increment. It determines the length of the animation sequence.
    - Comfy dtype: INT
    - Python dtype: int
- current_frame
    - The Current_frame parameter represents the current frame number in the animation. It is used to calculate the current value of the whole value based on progress in the frame.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- INT
    - The INT output provides an increment of the current integer value, reflecting the progress of the current frame animation.
    - Comfy dtype: INT
    - Python dtype: int
- show_help
    - Show_help output is a string that contains a node document URL that provides additional information and guidance on how to use it.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_IncrementInteger:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'start_value': ('INT', {'default': 1.0, 'min': 0.0, 'max': 9999.0, 'step': 1.0}), 'step': ('INT', {'default': 1.0, 'min': -9999.0, 'max': 9999.0, 'step': 1.0}), 'start_frame': ('INT', {'default': 0.0, 'min': 0.0, 'max': 9999.0, 'step': 1.0}), 'frame_duration': ('INT', {'default': 1.0, 'min': 0.0, 'max': 9999.0, 'step': 1.0}), 'current_frame': ('INT', {'default': 0.0, 'min': 0.0, 'max': 9999.0, 'step': 1.0})}}
    RETURN_TYPES = ('INT', 'STRING')
    RETURN_NAMES = ('INT', 'show_help')
    OUTPUT_NODE = True
    FUNCTION = 'increment'
    CATEGORY = icons.get('Comfyroll/Animation/Interpolate')

    def increment(self, start_value, step, start_frame, frame_duration, current_frame):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Interpolation-Nodes#cr-increment-integer'
        if current_frame < start_frame:
            return (start_value, show_help)
        current_value = start_value + (current_frame - start_frame) * step
        if current_frame <= start_frame + frame_duration:
            current_value += step
            return (current_value, show_help)
        return (current_value, show_help)
```