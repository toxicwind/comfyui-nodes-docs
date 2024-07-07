# Documentation
- Class name: Lerp
- Category: FizzNodes 📅🅕🅝/WaveNodes
- Output node: False
- Repo Ref: https://github.com/FizzleDorf/ComfyUI_FizzNodes

Lerp nodes perform linear plugs between two values, providing a smooth transition from the strength parameters and the current frame effect in the image sequence. It is usually used in animation and data visualization to create gradual changes from one state to another.

# Input types
## Required
- num_Images
    - An image number parameter defines the total number of frames or images in the sequence, which affects the length of the plug value. This is essential for determining the particle size of the transition between values.
    - Comfy dtype: FLOAT
    - Python dtype: float
- strength
    - The strength parameter controls the degree of interpolation between the starting and end values. It is a key factor in the speed of transition in the image sequence.
    - Comfy dtype: FLOAT
    - Python dtype: float
- current_frame
    - The current frame parameter specifies the current position in the image sequence. It is essential to calculate the current state of any given time point plugin.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- output
    - The output of the Lerp node is the result of a linear plug that provides a value that represents the current state of transition based on input parameters.
    - Comfy dtype: FLOAT
    - Python dtype: float
- frame_index
    - The frame index output instruction calculates the frame number of the current plug-in status, which is very useful for alignment with other sequence-based processes.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class Lerp:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'num_Images': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 9999.0, 'step': 1.0}), 'strength': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 10.0, 'step': 0.01}), 'current_frame': ('INT', {'default': 1.0, 'min': 0.0, 'max': 9999, 'step': 1.0})}}
    RETURN_TYPES = ('FLOAT', 'INT')
    FUNCTION = 'lerp'
    CATEGORY = 'FizzNodes 📅🅕🅝/WaveNodes'

    def lerp(self, num_Images, strength, current_frame):
        step = strength / num_Images
        output = strength - step * current_frame
        return (output, int(output))
```