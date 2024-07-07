# Documentation
- Class name: SawtoothWave
- Category: FizzNodes 📅🅕🅝/WaveNodes
- Output node: False
- Repo Ref: https://github.com/FizzleDorf/ComfyUI_FizzNodes

Sampling nodes generate wave-shaped patterns based on the assigned phase, step-increment and displacement, which assist in signal processing or wave-generation tasks in the system.

# Input types
## Required
- phase
    - The phase parameters determine the cyclicality of the sawing wave, affecting the overall shape and frequency of the output wave.
    - Comfy dtype: FLOAT
    - Python dtype: float
- step_increment
    - Step increment parameters control the amplitude change of each cycle, affecting the steepness of wave-shaped rises and declines.
    - Comfy dtype: FLOAT
    - Python dtype: float
- x_translation
    - x_translation moves the wave shape horizontally and adjusts the position of the wave pattern within the time frame.
    - Comfy dtype: FLOAT
    - Python dtype: float
- start_value
    - The start_value parameter sets the initial level of the wave shape and determines the baseline for wave-shaped oscillation.
    - Comfy dtype: FLOAT
    - Python dtype: float
- current_frame
    - The Current_frame parameter represents the current point of time and is used to calculate the position of the waveform at a particular moment in its cycle.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- output
    - The output represents the calculation value of the current frame sawtooth wave, which can be used for further signal processing or as input for other nodes.
    - Comfy dtype: FLOAT
    - Python dtype: float
- int_output
    - Integer values provided by int_output indicate that they apply to discrete operations or serve as a basis for numerical analysis.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class SawtoothWave:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'phase': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 9999.0, 'step': 1.0}), 'step_increment': ('FLOAT', {'default': 0.5, 'min': 0.0, 'max': 9999.0, 'step': 0.1}), 'x_translation': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 9999.0, 'step': 1.0}), 'start_value': ('FLOAT', {'default': 0.5, 'min': 0.0, 'max': 9999.0, 'step': 0.05}), 'current_frame': ('INT', {'default': 1.0, 'min': 0.0, 'max': 9999.0, 'step': 1.0})}}
    RETURN_TYPES = ('FLOAT', 'INT')
    FUNCTION = 'Wave'
    CATEGORY = 'FizzNodes 📅🅕🅝/WaveNodes'

    def Wave(self, phase, step_increment, x_translation, start_value, current_frame):
        output = start_value + (step_increment * (current_frame % phase) - x_translation)
        print(output)
        return (output, int(output))
```