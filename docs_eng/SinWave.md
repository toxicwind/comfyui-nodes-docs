# Documentation
- Class name: SinWave
- Category: FizzNodes 📅🅕🅝/WaveNodes
- Output node: False
- Repo Ref: https://github.com/FizzleDorf/ComfyUI_FizzNodes

SinWave node is designed to generate a sine wave mode. It simulates the behaviour of the wave by calculating the y position of the given frame, based on the parameters provided. This node is particularly suitable for applications that require a cycle function to simulate oscillation or create visual effects.

# Input types
## Required
- phase
    - The phase parameter determines the wave cycle. It is vital because it determines the frequency of oscillation, which affects the overall shape and pattern of the wave.
    - Comfy dtype: FLOAT
    - Python dtype: float
- amplitude
    - The amplitude sets the peak of the wave and controls the height of the oscillation. It is a key parameter that affects the intensity of the wave shape.
    - Comfy dtype: FLOAT
    - Python dtype: float
- current_frame
    - The current frame parameter specifies the frame to be calculated by wave. This is essential for determining the position of y in a given time point wave.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- x_translation
    - X-altitude allows the movement of waves along the X-axis level. This can be used to adjust the position of the waveform to meet specific design requirements.
    - Comfy dtype: FLOAT
    - Python dtype: float
- y_translation
    - Y shifting is responsible for moving the wave vertically along the Y axis so that the starting point of the wave can be adjusted.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- output
    - Output indicates the position of the current frame wave to calculate y. It is important because it provides real value for further processing or visualization.
    - Comfy dtype: FLOAT
    - Python dtype: float
- int_output
    - Integer output is the transfer of the wave's y position to an integer number, which is useful in the context of the need for discrete values.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class SinWave:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'phase': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 9999.0, 'step': 1.0}), 'amplitude': ('FLOAT', {'default': 0.5, 'min': 0.0, 'max': 9999.0, 'step': 0.1}), 'x_translation': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 9999.0, 'step': 1.0}), 'y_translation': ('FLOAT', {'default': 0.5, 'min': 0.0, 'max': 9999.0, 'step': 0.05}), 'current_frame': ('INT', {'default': 1.0, 'min': 0.0, 'max': 9999.0, 'step': 1.0})}}
    RETURN_TYPES = ('FLOAT', 'INT')
    FUNCTION = 'Wave'
    CATEGORY = 'FizzNodes 📅🅕🅝/WaveNodes'

    def Wave(self, phase, amplitude, x_translation, y_translation, current_frame):
        output = y_translation + amplitude * np.sin(2 * np.pi * current_frame / phase - x_translation)
        print(output)
        return (output, int(output))
```