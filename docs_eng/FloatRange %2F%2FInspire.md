# Documentation
- Class name: FloatRange
- Category: InspirePack/Util
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Inspire-Pack.git

The node generates a series of floating points within the specified range and adjusts the spacing according to the parameters defined by the user to facilitate various mathematical and computational tasks.

# Input types
## Required
- start
    - . It sets the starting point of the node that begins to generate the number, which is essential to define the bottom of the sequence.
    - Comfy dtype: FLOAT
    - Python dtype: float
- stop
    - . It marks the upper limit of the range and determines when the node should cease to generate a number.
    - Comfy dtype: FLOAT
    - Python dtype: float
- step
    - The increment between each number in the sequence. It determines the spacing and is essential for generating the density of the number within the range of control.
    - Comfy dtype: FLOAT
    - Python dtype: float
- limit
    - The maximum number of values generated. It limits the total output and ensures that the sequence does not exceed the predefined length.
    - Comfy dtype: INT
    - Python dtype: int
- ensure_end
    - A sign indicates whether the end value is included in the sequence. If enabled, it influences the final output by ensuring that the sequence includes the specified stop value.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- sequence
    - A list of floating point numbers generated within the specified range represents the output of the node operation.
    - Comfy dtype: FLOAT
    - Python dtype: List[float]

# Usage tips
- Infra type: CPU

# Source code
```
class FloatRange:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'start': ('FLOAT', {'default': 0.0, 'min': -100.0, 'max': 100.0, 'step': 1e-09}), 'stop': ('FLOAT', {'default': 1.0, 'min': -100.0, 'max': 100.0, 'step': 1e-09}), 'step': ('FLOAT', {'default': 0.01, 'min': 0.0, 'max': 100.0, 'step': 1e-09}), 'limit': ('INT', {'default': 100, 'min': 2, 'max': 4096, 'step': 1}), 'ensure_end': ('BOOLEAN', {'default': True, 'label_on': 'enable', 'label_off': 'disable'})}}
    RETURN_TYPES = ('FLOAT',)
    OUTPUT_IS_LIST = (True,)
    FUNCTION = 'doit'
    CATEGORY = 'InspirePack/Util'

    def doit(self, start, stop, step, limit, ensure_end):
        if start >= stop or step == 0:
            return ([start],)
        res = []
        x = start
        last = x
        while x <= stop and limit > 0:
            res.append(x)
            last = x
            limit -= 1
            x += step
        if ensure_end and last != stop:
            if len(res) >= limit:
                res.pop()
            res.append(stop)
        return (res,)
```