# Documentation
- Class name: ConvertAnything
- Category: EasyUse/Logic
- Output node: True
- Repo Ref: https://github.com/yolain/ComfyUI-Easy-Use.git

This node can convert the given input to the specified output type, providing a multifunctional solution for the data conversion task. It performs the operation by interpreting the input and converting it to the required category (e.g. string, integer, floating point or boolean value) according to the user's choice.

# Input types
## Required
- anything
    - The `anything' parameter is essential, and it represents the input to be converted. Its role in node operations is to provide data that will experience the conversion process.
    - Comfy dtype: *
    - Python dtype: Union[str, int, float, bool, torch.Tensor, np.ndarray, Decimal, List, Tuple, Dict[Any, Any]]
- output_type
    - The 'output_type'parameter determines the desired outcome of the conversion process. It is essential in guiding nodes to produce the right type of output.
    - Comfy dtype: COMBO[string,int,float,boolean]
    - Python dtype: Union[str, int, float, bool]

# Output types
- *
    - The output of this node is the converted data, reflecting the result of the input conversion to the specified type.
    - Comfy dtype: *
    - Python dtype: Union[str, int, float, bool, torch.Tensor, np.ndarray, Decimal, List, Tuple, Dict[Any, Any]]

# Usage tips
- Infra type: CPU

# Source code
```
class ConvertAnything:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'anything': (AlwaysEqualProxy('*'),), 'output_type': (['string', 'int', 'float', 'boolean'], {'default': 'string'})}}
    RETURN_TYPES = ((AlwaysEqualProxy('*'),),)
    RETURN_NAMES = ('*',)
    OUTPUT_NODE = True
    FUNCTION = 'convert'
    CATEGORY = 'EasyUse/Logic'

    def convert(self, *args, **kwargs):
        print(kwargs)
        anything = kwargs['anything']
        output_type = kwargs['output_type']
        params = None
        if output_type == 'string':
            params = str(anything)
        elif output_type == 'int':
            params = int(anything)
        elif output_type == 'float':
            params = float(anything)
        elif output_type == 'boolean':
            params = bool(anything)
        return (params,)
```