# Documentation
- Class name: WAS_Latent_Size_To_Number
- Category: WAS Suite/Number/Operations
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The `latent_width_height' method of the WAS_Latent_Size_To_Nummer node is designed to extract and provide width and altitude dimensions from the given count, which represents potential spatial data. This is essential for operations that require space dimensions for further processing or analysis in the WAS package.

# Input types
## Required
- samples
    - The “samples” parameter is essential because it is an input length that contains potential spatial data. Node relies on it to calculate width and altitude dimensions, which are essential for subsequent numerical operations or analysis.
    - Comfy dtype: LATENT
    - Python dtype: Union[torch.Tensor]

# Output types
- tensor_w_num
    - The "tensor_w_num " output parameter represents the width of the space dimension of the tension. It is important for applications that need to know the width of the tension for further processing.
    - Comfy dtype: INT
    - Python dtype: int
- tensor_h_num
    - The output parameter "tensor_h_num" indicates the height of the space dimension of the mass. It plays a key role in the application that requires the height to follow the task.
    - Comfy dtype: INT
    - Python dtype: int
- width_float
    - The " width_float " output provides the width of the input length in float-point format. This is useful for algorithms that require decimal accuracy to measure the width.
    - Comfy dtype: FLOAT
    - Python dtype: float
- height_float
    - In particular, it applies to applications that require accurate decimals of height.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Latent_Size_To_Number:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'samples': ('LATENT',)}}
    RETURN_TYPES = ('NUMBER', 'NUMBER', 'FLOAT', 'FLOAT', 'INT', 'INT')
    RETURN_NAMES = ('tensor_w_num', 'tensor_h_num')
    FUNCTION = 'latent_width_height'
    CATEGORY = 'WAS Suite/Number/Operations'

    def latent_width_height(self, samples):
        size_dict = {}
        i = 0
        for tensor in samples['samples'][0]:
            if not isinstance(tensor, torch.Tensor):
                cstr(f'Input should be a torch.Tensor').error.print()
            shape = tensor.shape
            tensor_height = shape[-2]
            tensor_width = shape[-1]
            size_dict.update({i: [tensor_width, tensor_height]})
        return (size_dict[0][0], size_dict[0][1], float(size_dict[0][0]), float(size_dict[0][1]), size_dict[0][0], size_dict[0][1])
```