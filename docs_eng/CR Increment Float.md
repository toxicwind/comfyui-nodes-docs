# Documentation
- Class name: CR_IncrementFloat
- Category: Comfyroll/Animation/Interpolate
- Output node: True
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_InclementFloat is a node designed to adjust floating point values gradually over a specified duration. It smooths the transition from a starting value to an increment value, building on the current frame within the animated timeline, and facilitates dynamic and time-based animation creation.

# Input types
## Required
- start_value
    - The initial value of the increment starts. It acts as a reference point for node operations, affecting the starting point of the animation sequence.
    - Comfy dtype: FLOAT
    - Python dtype: float
- step
    - The incremental step value defines the change in the number of floating points per frame. It is critical in determining the rate of increase or decrease in animation.
    - Comfy dtype: FLOAT
    - Python dtype: float
- start_frame
    - The frame number in which the incremental process begins. It determines when the animated incremental change begins.
    - Comfy dtype: INT
    - Python dtype: int
- frame_duration
    - The total number of incremental frames that occur. It sets the duration of the incremental animation effect.
    - Comfy dtype: INT
    - Python dtype: int
- current_frame
    - The current frame in the animated timeline. It is used to calculate the current value of the increment based on progress in the frame.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- FLOAT
    - The result of the incremental floating point values obtained by applying the incremental logic on the basis of the current frame.
    - Comfy dtype: FLOAT
    - Python dtype: float
- show_help
    - is the URL link to the node document for further help and information about its use.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_IncrementFloat:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'start_value': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 9999.0, 'step': 0.001}), 'step': ('FLOAT', {'default': 0.1, 'min': -9999.0, 'max': 9999.0, 'step': 0.001}), 'start_frame': ('INT', {'default': 0.0, 'min': 0.0, 'max': 9999.0, 'step': 1.0}), 'frame_duration': ('INT', {'default': 1.0, 'min': 0.0, 'max': 9999.0, 'step': 1.0}), 'current_frame': ('INT', {'default': 0.0, 'min': 0.0, 'max': 9999.0, 'step': 1.0})}}
    RETURN_TYPES = ('FLOAT', 'STRING')
    RETURN_NAMES = ('FLOAT', 'show_help')
    OUTPUT_NODE = True
    FUNCTION = 'increment'
    CATEGORY = icons.get('Comfyroll/Animation/Interpolate')

    def increment(self, start_value, step, start_frame, frame_duration, current_frame):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Interpolation-Nodes#cr-increment-float'
        if current_frame < start_frame:
            return (start_value, show_help)
        current_value = start_value + (current_frame - start_frame) * step
        if current_frame <= start_frame + frame_duration:
            current_value += step
            return (current_value, show_help)
        return (current_value, show_help)
```