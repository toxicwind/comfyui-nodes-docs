# Documentation
- Class name: InvSinWave
- Category: FizzNodes 📅🅕🅝/WaveNodes
- Output node: False
- Repo Ref: https://github.com/FizzleDorf/ComfyUI_FizzNodes

The InvSinWave node is designed to generate an inverted sine-wave model. It uses wave phase, amplitude and peaceful transfer to achieve the desired output, which is particularly useful in signal processing and wave-form analysis applications.

# Input types
## Required
- phase
    - The phase parameter determines the frequency of the wave, which affects the number of times that the wave completes a full cycle within the given time frame. It is essential for controlling the frequency of the wave.
    - Comfy dtype: FLOAT
    - Python dtype: float
- amplitude
    - The amplitude sets the height of the peak, affecting the intensity of the wave. It is an important parameter for adjusting the size of the wave.
    - Comfy dtype: FLOAT
    - Python dtype: float
- x_translation
    - X moves the wave along the X-axis level and allows positioning of the wave within the given space. It is important for aligning the wave shape with a specific coordinate.
    - Comfy dtype: FLOAT
    - Python dtype: float
- y_translation
    - Y moves vertically along the Y axis, affecting the starting point of wave oscillation. It is important for adjusting the vertical position of the wave form.
    - Comfy dtype: FLOAT
    - Python dtype: float
- current_frame
    - The current frame parameter specifies the current position in the time series, which is essential for generating waves at a particular time of animation or simulation.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- output
    - Output is the value of the inverted sine wave calculated under the specified parameter, which can be used for further analysis or as input for other nodes.
    - Comfy dtype: FLOAT
    - Python dtype: float
- int_output
    - Integer output is an integer version of the wave value and may be useful for applications that require discrete rather than continuous values.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class InvSinWave:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'phase': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 9999.0, 'step': 1.0}), 'amplitude': ('FLOAT', {'default': 0.5, 'min': 0.0, 'max': 9999.0, 'step': 0.1}), 'x_translation': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 9999.0, 'step': 1.0}), 'y_translation': ('FLOAT', {'default': 0.5, 'min': 0.0, 'max': 9999.0, 'step': 0.05}), 'current_frame': ('INT', {'default': 1.0, 'min': 0.0, 'max': 9999.0, 'step': 1.0})}}
    RETURN_TYPES = ('FLOAT', 'INT')
    FUNCTION = 'Wave'
    CATEGORY = 'FizzNodes 📅🅕🅝/WaveNodes'

    def Wave(self, phase, amplitude, x_translation, y_translation, current_frame):
        output = y_translation + amplitude * -np.sin(-1 * (2 * np.pi * current_frame / phase - x_translation))
        print(output)
        return (output, int(output))
```