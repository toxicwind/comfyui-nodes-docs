# Documentation
- Class name: SquareWave
- Category: FizzNodes 📅🅕🅝/WaveNodes
- Output node: False
- Repo Ref: https://github.com/FizzleDorf/ComfyUI_FizzNodes

The SquareWave node is designed to generate a square wave model. It produces a square wave shape by adjusting the phase, amplitude and peaceful transfer, which is essential for signal processing and wave-shaped analysis. The function of the node is essential for the creation or manipulation of the application of the side wave signal.

# Input types
## Required
- phase
    - The phase parameter determines the position of the wave cycle, which is essential for determining the timing of the wave conversion. It affects the frequency and starting point of the wave shape.
    - Comfy dtype: FLOAT
    - Python dtype: float
- amplitude
    - The amplitude sets the heights of the wave peaks and valleys, which are very important for defining the strength of the signal. It is a key factor in the shape and characteristics of the wave as a whole.
    - Comfy dtype: FLOAT
    - Python dtype: float
- x_translation
    - This parameter is essential to align the waveform with other signals or components of the system.
    - Comfy dtype: FLOAT
    - Python dtype: float
- y_translation
    - Y moves the wave shape up or down along the Y axis, affecting the vertical position of the wave shape. It is an important parameter for adjusting the wave shape to the position of other elements.
    - Comfy dtype: FLOAT
    - Python dtype: float
- current_frame
    - The current frame parameters indicate the current position in the wave-shaped sequence, which is critical to the progress and timing of the square-wave model over time.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- output
    - The output of the SquareWave node represents the calculation value of the wave below the specified parameter, which is essential for further signal processing or analysis.
    - Comfy dtype: FLOAT
    - Python dtype: float
- int_output
    - Integer output provides a discrete version of wave value, which is very useful for applications that require a quantitative or integer expression of the signal.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class SquareWave:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'phase': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 9999.0, 'step': 1.0}), 'amplitude': ('FLOAT', {'default': 0.5, 'min': 0.0, 'max': 9999.0, 'step': 0.1}), 'x_translation': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 9999.0, 'step': 1.0}), 'y_translation': ('FLOAT', {'default': 0.5, 'min': 0.0, 'max': 9999.0, 'step': 0.05}), 'current_frame': ('INT', {'default': 1.0, 'min': 0.0, 'max': 9999.0, 'step': 1.0})}}
    RETURN_TYPES = ('FLOAT', 'INT')
    FUNCTION = 'Wave'
    CATEGORY = 'FizzNodes 📅🅕🅝/WaveNodes'

    def Wave(self, phase, amplitude, x_translation, y_translation, current_frame):
        output = y_translation + amplitude * 0 ** 0 ** (0 - np.sin(np.pi * current_frame / phase - x_translation))
        print(output)
        return (output, int(output))
```