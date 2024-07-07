# Documentation
- Class name: CR_GradientFloat
- Category: Comfyroll/Animation/Interpolate
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

The CR_GradientFloat node is designed to generate a smooth transition between two floating point values during the specified duration. It calculates the current value based on the start and end value, the frame at which the transition begins, and the total duration of the transition. This node is particularly suitable for creating dynamic changes in time for animation parameters.

# Input types
## Required
- start_value
    - The starting value parameter defines the initial value of the gradient. It is essential for setting the base point at which the transition begins.
    - Comfy dtype: FLOAT
    - Python dtype: float
- end_value
    - The end-value parameter specifies the final value that the gradient will reach at the end of the transition. It is essential to determine the range of changes.
    - Comfy dtype: FLOAT
    - Python dtype: float
- start_frame
    - Starts the frame parameter to indicate the frame number in which the gradient transition will begin. It is important for the start of the periodic animation effect.
    - Comfy dtype: INT
    - Python dtype: int
- frame_duration
    - Frame duration parameters determine the number of frames in which a gradient transition occurs. It affects the speed of the transition.
    - Comfy dtype: INT
    - Python dtype: int
- current_frame
    - The current frame parameter represents the current frame number in the sequence. It is used to calculate the current status of the gradient at this point.
    - Comfy dtype: INT
    - Python dtype: int
- gradient_profile
    - Gradient profile parameters define the type of plug-in method used for gradients. It affects the way values are calculated between start and end.
    - Comfy dtype: COMBO['Lerp']
    - Python dtype: str

# Output types
- FLOAT
    - The FLOAT output provides the calculation value for the current frame gradient, representing the current state of the transition.
    - Comfy dtype: FLOAT
    - Python dtype: float
- show_help
    - Show_help output provides URLs that point to the node document page, providing additional information and guidance on how to use them.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_GradientFloat:

    @classmethod
    def INPUT_TYPES(s):
        gradient_profiles = ['Lerp']
        return {'required': {'start_value': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 9999.0, 'step': 0.01}), 'end_value': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 9999.0, 'step': 0.01}), 'start_frame': ('INT', {'default': 0.0, 'min': 0.0, 'max': 9999.0, 'step': 1.0}), 'frame_duration': ('INT', {'default': 1.0, 'min': 0.0, 'max': 9999.0, 'step': 1.0}), 'current_frame': ('INT', {'default': 0.0, 'min': 0.0, 'max': 9999.0, 'step': 1.0}), 'gradient_profile': (gradient_profiles,)}}
    RETURN_TYPES = ('FLOAT', 'STRING')
    RETURN_NAMES = ('FLOAT', 'show_help')
    FUNCTION = 'gradient'
    CATEGORY = icons.get('Comfyroll/Animation/Interpolate')

    def gradient(self, start_value, end_value, start_frame, frame_duration, current_frame, gradient_profile):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Interpolation-Nodes#cr-gradient-float'
        if current_frame < start_frame:
            return (start_value, show_help)
        if current_frame > start_frame + frame_duration:
            return (end_value, show_help)
        step = (end_value - start_value) / frame_duration
        current_step = current_frame - start_frame
        float_out = start_value + current_step * step
        return (float_out, show_help)
```