# Documentation
- Class name: AbsCosWave
- Category: FizzNodes 📅🅕🅝/WaveNodes
- Output node: False
- Repo Ref: https://github.com/FizzleDorf/ComfyUI_FizzNodes

This node generates a wave-shaped model based on a set of input parameters, which simulates oscillating behaviour with modifiable properties.

# Input types
## Required
- phase
    - The phase parameters determine the spacing of wave oscillations and influence the frequency and periodicity of wave patterns.
    - Comfy dtype: FLOAT
    - Python dtype: float
- amplitude
    - The amplitude controls the size of the wave, determining the peak and grain size of the wave pattern.
    - Comfy dtype: FLOAT
    - Python dtype: float
- x_translation
    - X_translation moves waves along x-axis horizontally, changing the position of wave mode without changing its shape.
    - Comfy dtype: FLOAT
    - Python dtype: float
- max_value
    - The maximum value parameter sets the upper limit of the wave to ensure that the output remains within the defined range.
    - Comfy dtype: FLOAT
    - Python dtype: float
- current_frame
    - The current frame represents the wave as it progresses over time, with each frame corresponding to one point in the wave cycle.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- output
    - Output represents the calculation value of the current frame wave, reflecting the processing of input parameters by nodes.
    - Comfy dtype: FLOAT
    - Python dtype: float
- int_output
    - The integer output is the rounded value of the output calculated by the wave, which provides the discrete expression of the wave mode.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class AbsCosWave:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'phase': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 9999.0, 'step': 1.0}), 'amplitude': ('FLOAT', {'default': 0.5, 'min': 0.0, 'max': 9999.0, 'step': 0.1}), 'x_translation': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 9999.0, 'step': 1.0}), 'max_value': ('FLOAT', {'default': 0.5, 'min': 0.0, 'max': 9999.0, 'step': 0.05}), 'current_frame': ('INT', {'default': 1.0, 'min': 0.0, 'max': 9999.0, 'step': 1.0})}}
    RETURN_TYPES = ('FLOAT', 'INT')
    FUNCTION = 'Wave'
    CATEGORY = 'FizzNodes 📅🅕🅝/WaveNodes'

    def Wave(self, phase, amplitude, x_translation, max_value, current_frame):
        output = max_value - np.abs(np.cos(current_frame / phase)) * amplitude
        print(output)
        return (output, int(output))
```