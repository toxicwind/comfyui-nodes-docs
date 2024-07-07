# Documentation
- Class name: KfDebug_Int
- Category: Debug
- Output node: True
- Repo Ref: https://github.com/dmarx/ComfyUI-Keyframed

The KfDebug_Int node is designed to make it easier for users to check and analyse the whole value in the calculation chart. It allows users to monitor and understand the flow of integer data and to ensure the correctness of the integer-related operations in the model. The node helps to debug by providing a clear and focused view of integer processing and conversion, avoiding the complexity of other data types.

# Input types
## Required
- input
    - The input parameter is the key element for entering the whole value into the KfDebug_Int node. It is essential for the function of the node, as it allows the node to monitor and analyse the whole number. The input plays a key role in determining the output of the node and the insight it provides during the debugging process.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- output
    - The output of KfDebug_Int node is the processed integer value that is checked and analysed. It serves as confirmation of node operations and proof of the completeness of the whole value in the calculation chart. The output is important because it provides the basis for further debugging or validation of the model's performance.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class KfDebug_Int(KfDebug_Passthrough):
    RETURN_TYPES = ('INT',)
```