# Documentation
- Class name: InvCosWave
- Category: FizzNodes 📅🅕🅝/WaveNodes
- Output node: False
- Repo Ref: https://github.com/FizzleDorf/ComfyUI_FizzNodes

InvCosWave nodes generate wave shapes based on an arc cosine function. It is designed to provide a cyclical output that can be adjusted by phase, amplitude and shift parameters. This node is particularly suitable for applications that require smooth oscillating mode over time.

# Input types
## Required
- phase
    - The phase parameter determines the wave-shaped cycle. It affects the frequency of wave-shaped oscillations and is essential for setting the time-to-time frequency of the mode.
    - Comfy dtype: FLOAT
    - Python dtype: float
- amplitude
    - The amplitude parameter controls the peak of the wave shape. It is important to define the range of oscillations and can be adjusted to zoom out.
    - Comfy dtype: FLOAT
    - Python dtype: float
- x_translation
    - x_translation parameters move waveforms along the x-axis. It is essential for positioning waveform patterns within a given frame or space.
    - Comfy dtype: FLOAT
    - Python dtype: float
- y_translation
    - y_translation parameters adjust the vertical position of the waveform. It is important to align the waveform mode with other visual elements or data points.
    - Comfy dtype: FLOAT
    - Python dtype: float
- current_frame
    - The Current_frame parameter is the current time step in the animation or sequence. It is essential for generating the right phase of the wave shape at any given time.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- output
    - The output of the InvCosWave node is a float number that represents the current value of the wave shape at the specified frame. It is important for further processing or visualization of the waveform mode.
    - Comfy dtype: FLOAT
    - Python dtype: float
- int_output
    - Att_output is an integer of wave-shaped values that are useful when indexing is required or when integer accuracy is required.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class InvCosWave:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'phase': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 9999.0, 'step': 1.0}), 'amplitude': ('FLOAT', {'default': 0.5, 'min': 0.0, 'max': 9999.0, 'step': 0.1}), 'x_translation': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 9999.0, 'step': 1.0}), 'y_translation': ('FLOAT', {'default': 0.5, 'min': 0.0, 'max': 9999.0, 'step': 0.05}), 'current_frame': ('INT', {'default': 1.0, 'min': 0.0, 'max': 9999.0, 'step': 1.0})}}
    RETURN_TYPES = ('FLOAT', 'INT')
    FUNCTION = 'Wave'
    CATEGORY = 'FizzNodes 📅🅕🅝/WaveNodes'

    def Wave(self, phase, amplitude, x_translation, y_translation, current_frame):
        output = y_translation + amplitude * -np.cos(-1 * (2 * np.pi * current_frame / phase - x_translation))
        print(output)
        return (output, int(output))
```