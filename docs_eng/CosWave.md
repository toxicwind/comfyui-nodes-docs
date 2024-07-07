# Documentation
- Class name: CosWave
- Category: FizzNodes 📅🅕🅝/WaveNodes
- Output node: False
- Repo Ref: https://github.com/FizzleDorf/ComfyUI_FizzNodes

CosWave nodes generate cosine waves through a variety of parameters that can be adjusted to achieve the required changes. It is mainly used to create oscillating effects that can be synchronized with time-based variables.

# Input types
## Required
- phase
    - The phase parameter determines the period of the cosine wave and affects the frequency of oscillation. It is a key factor in shaping the temporal properties of the wave.
    - Comfy dtype: FLOAT
    - Python dtype: float
- amplitude
    - The amplitude sets the peak of the wave and controls the range of oscillations from their average position. It is essential to define the intensity of the wave.
    - Comfy dtype: FLOAT
    - Python dtype: float
- x_translation
    - X-altitude allows the movement of waveforms along the X-axis level to provide control over wave position without affecting its shape.
    - Comfy dtype: FLOAT
    - Python dtype: float
- y_translation
    - Y shifts to adjust the vertical position of the wave along the Y axis to allow fine-tune the starting point of the wave.
    - Comfy dtype: FLOAT
    - Python dtype: float
- current_frame
    - The current frame parameter is used to synchronize the phase of the wave with the progress of the sequence or animation, allowing changes over time.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- output
    - The output of the CosWave node represents the result wave shape value under the specified frame and can be used for further processing or visualization.
    - Comfy dtype: FLOAT
    - Python dtype: float
- int_output
    - Integer output is a version of the wave value converted to integer, which is very useful for applications requiring discrete values.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class CosWave:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'phase': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 9999.0, 'step': 1.0}), 'amplitude': ('FLOAT', {'default': 0.5, 'min': 0.0, 'max': 9999.0, 'step': 0.1}), 'x_translation': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 9999.0, 'step': 1.0}), 'y_translation': ('FLOAT', {'default': 0.5, 'min': 0.0, 'max': 9999.0, 'step': 0.05}), 'current_frame': ('INT', {'default': 1.0, 'min': 0.0, 'max': 9999.0, 'step': 1.0})}}
    RETURN_TYPES = ('FLOAT', 'INT')
    FUNCTION = 'Wave'
    CATEGORY = 'FizzNodes 📅🅕🅝/WaveNodes'

    def Wave(self, phase, amplitude, x_translation, y_translation, current_frame):
        output = y_translation + amplitude * np.cos(2 * np.pi * current_frame / phase - x_translation)
        print(output)
        return (output, int(output))
```