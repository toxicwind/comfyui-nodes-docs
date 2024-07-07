# Documentation
- Class name: ImpactConvertDataType
- Category: ImpactPack/Logic
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The ImpactConvertDataType node is designed to convert input data into various data types. It wisely determines whether input can be interpreted as a number and converts it to string, floating point, integer and boolean expressions. The node plays a key role in the pre-processing of data, applying to applications that require consistent data types between different input types.

# Input types
## Required
- value
    - The `value' parameter is the core input of the ImpactConvertDataType node. It can be any data type and is essential for the operation of the node, as it determines the source material of the conversion process. The function of the node relies heavily on this input in order to accurately execute its type conversion.
    - Comfy dtype: any
    - Python dtype: Any

# Output types
- converted_value
    - The `converted_value' output, which comes from the ImpactConvertDataType node, provides a set of widgets containing the original string values and their transformation forms (floats, integers, and booleans). This comprehensive output meets a variety of downstream processing needs to ensure that the data is properly formatted for further analysis or operation.
    - Comfy dtype: COMBO[string, float, int, boolean]
    - Python dtype: Tuple[str, float, int, bool]

# Usage tips
- Infra type: CPU

# Source code
```
class ImpactConvertDataType:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'value': (any_typ,)}}
    RETURN_TYPES = ('STRING', 'FLOAT', 'INT', 'BOOLEAN')
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Logic'

    @staticmethod
    def is_number(string):
        pattern = re.compile('^[-+]?[0-9]*\\.?[0-9]+$')
        return bool(pattern.match(string))

    def doit(self, value):
        if self.is_number(str(value)):
            num = value
        elif str.lower(str(value)) != 'false':
            num = 1
        else:
            num = 0
        return (str(value), float(num), int(float(num)), bool(float(num)))
```