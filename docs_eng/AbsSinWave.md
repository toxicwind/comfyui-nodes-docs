# Documentation
- Class name: AbsSinWave
- Category: FizzNodes 📅🅕🅝/WaveNodes
- Output node: False
- Repo Ref: https://github.com/FizzleDorf/ComfyUI_FizzNodes

Generates an absolute sine wave mode that oscillates between the specified maximum and zero, influenced by phase, amplitude and conversion parameters. This node is designed to provide multifunctional waveforms for various applications, such as signal processing or animation.

# Input types
## Required
- phase
    - The phase parameter determines the period of the sine wave, influencing the frequency and overall pattern of the wave. This is essential for adjusting the time of oscillation in the wave shape.
    - Comfy dtype: FLOAT
    - Python dtype: float
- amplitude
    - The amplitude sets the height of the sine wave and controls the range of the oscillation. It is the basic parameter that defines wave strength.
    - Comfy dtype: FLOAT
    - Python dtype: float
- x_translation
    - The x_translation parameter moves the waveform along the x-axis, allowing horizontal movement within the waveform mode. It is important for positioning the waveform in the given context.
    - Comfy dtype: FLOAT
    - Python dtype: float
- max_value
    - The max_value establishes the upper limit of the wave, defining the maximum point that a sine wave can reach. It is the key parameter for setting the size of the wave.
    - Comfy dtype: FLOAT
    - Python dtype: float
- current_frame
    - The Current_frame parameter indicates the current position in the time or sequence, which is used by the wave function to calculate its output. It is essential for generating the correct wave shape at a given time.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- output
    - The output provides the calculation value of the current frame absolute sine wave, representing the y-coordinate of the wave shape.
    - Comfy dtype: FLOAT
    - Python dtype: float
- int_output
    - Att_output is an integer of output and is useful for applications that require discrete rather than continuous values.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class AbsSinWave:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'phase': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 9999.0, 'step': 1.0}), 'amplitude': ('FLOAT', {'default': 0.5, 'min': 0.0, 'max': 9999.0, 'step': 0.1}), 'x_translation': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 9999.0, 'step': 1.0}), 'max_value': ('FLOAT', {'default': 0.5, 'min': 0.0, 'max': 9999.0, 'step': 0.05}), 'current_frame': ('INT', {'default': 1.0, 'min': 0.0, 'max': 9999.0, 'step': 1.0})}}
    RETURN_TYPES = ('FLOAT', 'INT')
    FUNCTION = 'Wave'
    CATEGORY = 'FizzNodes 📅🅕🅝/WaveNodes'

    def Wave(self, phase, amplitude, x_translation, max_value, current_frame):
        output = max_value - np.abs(np.sin(current_frame / phase)) * amplitude
        print(output)
        return (output, int(output))
```