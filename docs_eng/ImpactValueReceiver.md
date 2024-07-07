# Documentation
- Class name: ImpactValueReceiver
- Category: ImpactPack/Logic
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The ImpactValueReceiver node 'doit' method is designed to process and convert input values according to the specified type. It plays a key role in ensuring that the data format of the input system is correct, thus facilitating seamless integration and operation of the data within the ImpactPack framework.

# Input types
## Required
- typ
    - The parameter'typ's instruction'doit' method will perform the type of conversion for input 'value'. It is essential for node implementation because it determines how the data entered are processed and converted.
    - Comfy dtype: STRING
    - Python dtype: str
- value
    - The parameter 'value' means the data to be converted by the 'doit' method. The correct input is essential for the node to produce the expected output, as it directly affects the operation of the node and the results produced.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- link_id
    - The parameter'link_id' is used in the system as an optional identifier for connection. It can be used to track or refer to specific data points and help to organize and manage node execution as a whole.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- converted_value
    - The output parameter 'converted_value' represents the result of the 'doit' conversion process. It is important because it reflects the ability of nodes to accurately convert the input data according to the specified type, ensuring the integrity and availability of the output.
    - Comfy dtype: COMBO[STRING, INT, FLOAT, BOOLEAN]
    - Python dtype: Union[str, int, float, bool]

# Usage tips
- Infra type: CPU

# Source code
```
class ImpactValueReceiver:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'typ': (['STRING', 'INT', 'FLOAT', 'BOOLEAN'],), 'value': ('STRING', {'default': ''}), 'link_id': ('INT', {'default': 0, 'min': 0, 'max': sys.maxsize, 'step': 1})}}
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Logic'
    RETURN_TYPES = (any_typ,)

    def doit(self, typ, value, link_id=0):
        if typ == 'INT':
            return (int(value),)
        elif typ == 'FLOAT':
            return (float(value),)
        elif typ == 'BOOLEAN':
            return (value.lower() == 'true',)
        else:
            return (value,)
```