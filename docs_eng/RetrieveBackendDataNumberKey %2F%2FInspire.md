# Documentation
- Class name: RetrieveBackendDataNumberKey
- Category: Data Retrieval
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Inspire-Pack.git

The node is intended to extract numerical data from back-end services based on the keys provided to facilitate access to specific information without the need for complex data-processing procedures.

# Input types
## Required
- key
    - The `key' parameter is essential because it only identifies the data needed from the back end. It serves as a reference for node positioning and retrieval of the correct values.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- data
    - Output'data' represents the values obtained from the backend that correspond to the input 'key'. It is a direct result of node execution and is valuable for further data analysis or processing.
    - Comfy dtype: NUMBER
    - Python dtype: Union[int, float]

# Usage tips
- Infra type: CPU

# Source code
```
class RetrieveBackendDataNumberKey(RetrieveBackendData):

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'key': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615})}}
```