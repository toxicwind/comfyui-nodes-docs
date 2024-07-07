# Documentation
- Class name: CR_GradientInteger
- Category: Comfyroll/Animation/Interpolate
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_GradientInteger provides a method for interpolating two integer values over a specified duration, through the starting and duration of the frame. It is designed to provide a smooth transition from the starting to the end value, which is particularly useful in animation and time-based visual effects.

# Input types
## Required
- start_value
    - The initial integer value, which starts with the plug value. It is essential to establish the initial conditions for the transition.
    - Comfy dtype: INT
    - Python dtype: int
- end_value
    - The plug value is the end integer value that you want to achieve. It defines the final state of transition after the frame duration.
    - Comfy dtype: INT
    - Python dtype: int
- start_frame
    - The frame number where the plug value should start. It is essential for synchronizing the transition with animated or sequence time lines.
    - Comfy dtype: INT
    - Python dtype: int
- frame_duration
    - The number of frames in which the plug-in occurs. It determines the length of the transition between the starting and the closing values.
    - Comfy dtype: INT
    - Python dtype: int
- current_frame
    - The current frame in the sequence of the plug value is used to calculate the current steps in the transition.
    - Comfy dtype: INT
    - Python dtype: int
- gradient_profile
    - The plugin profile defines the rate of change between the start and end values. It affects the way transitions progress over time.
    - Comfy dtype: COMBO['Lerp']
    - Python dtype: str

# Output types
- INT
    - The integer value of the current frame is the result of the transition between the starting and closing values.
    - Comfy dtype: INT
    - Python dtype: int
- show_help
    - Provides an additional document or URL string to help with the plug-in process.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_GradientInteger:

    @classmethod
    def INPUT_TYPES(s):
        gradient_profiles = ['Lerp']
        return {'required': {'start_value': ('INT', {'default': 1.0, 'min': 0.0, 'max': 9999.0, 'step': 1.0}), 'end_value': ('INT', {'default': 1.0, 'min': 0.0, 'max': 9999.0, 'step': 1.0}), 'start_frame': ('INT', {'default': 0.0, 'min': 0.0, 'max': 9999.0, 'step': 1.0}), 'frame_duration': ('INT', {'default': 1.0, 'min': 0.0, 'max': 9999.0, 'step': 1.0}), 'current_frame': ('INT', {'default': 0.0, 'min': 0.0, 'max': 9999.0, 'step': 1.0}), 'gradient_profile': (gradient_profiles,)}}
    RETURN_TYPES = ('INT', 'STRING')
    RETURN_NAMES = ('INT', 'show_help')
    FUNCTION = 'gradient'
    CATEGORY = icons.get('Comfyroll/Animation/Interpolate')

    def gradient(self, start_value, end_value, start_frame, frame_duration, current_frame, gradient_profile):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Interpolation-Nodes#cr-gradient-integer'
        if current_frame < start_frame:
            return (start_value, show_help)
        if current_frame > start_frame + frame_duration:
            return (end_value, show_help)
        step = (end_value - start_value) / frame_duration
        current_step = current_frame - start_frame
        int_out = start_value + int(current_step * step)
        return (int_out, show_help)
```