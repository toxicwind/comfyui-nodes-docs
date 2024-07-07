# Documentation
- Class name: IPAdapterWeights
- Category: ipadapter/utils
- Output node: False
- Repo Ref: https://github.com/cubiq/ComfyUI_IPAdapter_plus.git

The `weights'method at the IPAdapterWeights node is designed to process and insert a range of weights according to the specified time function. It accepts a weight string, a time parameter and frame details to generate a list of weights that can be applied to a series of frames. This method is essential for time adjustments of the impact of different components of the model or system, allowing dynamic adjustments.

# Input types
## Required
- weights
    - The 'weights' parameter is a string that contains a comma-separated list of floating points. It is essential to define the initial weights that nodes will process and insert values over time. These weights are applied in a way that significantly influences the output of the systems or models they integrate.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- timing
    - The `timing' parameter determines the time function to be used when assigning weights to the frame. It can be one of several predefined options, each of which produces a different rate of weight change over time. This parameter is important for controlling the rhythm of transition between different weights.
    - Comfy dtype: COMBO['custom', 'linear', 'ease_in_out', 'ease_in', 'ease_out', 'reverse_in_out', 'random']
    - Python dtype: str
- frames
    - The 'frames' parameter specifies the total number of frames in which weights will be applied. It is an integer value that sets a ceiling on the duration of the weight series. This parameter is important for defining the range of weight applications and ensuring that they are consistent with the system's time series.
    - Comfy dtype: INT
    - Python dtype: int
- start_frame
    - It allows custom weights to be applied at the start of the entire frame series. This is particularly useful for synchronizing weight applications with other events or processes in the system.
    - Comfy dtype: INT
    - Python dtype: int
- end_frame
    - The `end_frame' parameter defines the frame number for the end of the weight sequence. It is used at the end of the control heavy application to ensure that the weight is applied only to a particular point in the frame sequence. This helps to create a more detailed and controlled effect in the system.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- weights
    - The output 'weights' is a list of floating points, representing the weight of the processed and plugged values that will be applied to the frame sequence. This output is very important because it directly affects the behaviour of the model or system in which the weight is integrated.
    - Comfy dtype: FLOAT
    - Python dtype: List[float]

# Usage tips
- Infra type: CPU

# Source code
```
class IPAdapterWeights:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'weights': ('STRING', {'default': '1.0', 'multiline': True}), 'timing': (['custom', 'linear', 'ease_in_out', 'ease_in', 'ease_out', 'reverse_in_out', 'random'],), 'frames': ('INT', {'default': 0, 'min': 0, 'max': 9999, 'step': 1}), 'start_frame': ('INT', {'default': 0, 'min': 0, 'max': 9999, 'step': 1}), 'end_frame': ('INT', {'default': 9999, 'min': 0, 'max': 9999, 'step': 1})}}
    RETURN_TYPES = ('FLOAT',)
    FUNCTION = 'weights'
    CATEGORY = 'ipadapter/utils'

    def weights(self, weights, timing, frames, start_frame, end_frame):
        import random
        weights = weights.replace('\n', ',')
        weights = [float(weight) for weight in weights.split(',') if weight.strip() != '']
        if timing != 'custom':
            start = 0.0
            end = 1.0
            if len(weights) > 0:
                start = weights[0]
                end = weights[-1]
            weights = []
            end_frame = min(end_frame, frames)
            duration = end_frame - start_frame
            if start_frame > 0:
                weights.extend([start] * start_frame)
            for i in range(duration):
                n = duration - 1
                if timing == 'linear':
                    weights.append(start + (end - start) * i / n)
                elif timing == 'ease_in_out':
                    weights.append(start + (end - start) * (1 - math.cos(i / n * math.pi)) / 2)
                elif timing == 'ease_in':
                    weights.append(start + (end - start) * math.sin(i / n * math.pi / 2))
                elif timing == 'ease_out':
                    weights.append(start + (end - start) * (1 - math.cos(i / n * math.pi / 2)))
                elif timing == 'reverse_in_out':
                    weights.append(start + (end - start) * (1 - math.sin((1 - i / n) * math.pi / 2)))
                elif timing == 'random':
                    weights.append(random.uniform(start, end))
            weights[-1] = end if timing != 'random' else weights[-1]
            if end_frame < frames:
                weights.extend([end] * (frames - end_frame))
        if len(weights) == 0:
            weights = [0.0]
        return (weights,)
```