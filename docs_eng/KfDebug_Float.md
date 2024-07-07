# Documentation
- Class name: KfDebug_Float
- Category: Debugging
- Output node: True
- Repo Ref: https://github.com/dmarx/ComfyUI-Keyframed

The KfDebug_Float node is intended to facilitate the debugging process by providing a method for checking and analysing the number of floating points in the data-processing stream. It is a key tool for developers to validate the completeness and behaviour of numerical data at various stages.

# Input types
## Required
- input_float
    - The input_float parameter is essential for the operation of the node because it indicates the number of floating points that need to be debugled. It plays a central role in the implementation of the node and is the main data to be checked and analysed.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- output_float
    - The output_float parameter is important because it represents the number of debugging floating points processed by nodes. It is essential for downstream processes because it ensures continuity and reliability of data streams.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Usage tips
- Infra type: CPU

# Source code
```
class KfDebug_Float(KfDebug_Passthrough):
    RETURN_TYPES = ('FLOAT',)
```