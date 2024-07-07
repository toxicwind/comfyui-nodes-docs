# Documentation
- Class name: SDXLResolution
- Category: math/graphics
- Output node: False
- Repo Ref: https://github.com/evanspearman/ComfyMath

The node is intended to interpret the resolution string and convert it to the appropriate width and height integer values. It plays a key role in ensuring that graphic output follows the specified dimensions and promotes seamless integration of visual elements in the system.

# Input types
## Required
- resolution
    - The resolution parameter is essential because it defines the dimensions of the graphic output. It is expected to be a string in a format called 'Wide x Height', and nodes will then be divided into separate width and height values.
    - Comfy dtype: str
    - Python dtype: str

# Output types
- width
    - The width output parameter represents the horizontal dimension of the graphic resolution. It is important because it directly affects the scaling and layout of the application or displaying the visual content.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - The high output parameter represents the vertical dimension of the graphic resolution. It is essential to determine the vertical scope of the visual content and to ensure an appropriate display format.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class SDXLResolution:

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {'required': {'resolution': ([f'{res[0]}x{res[1]}' for res in SDXL_SUPPORTED_RESOLUTIONS],)}}
    RETURN_TYPES = ('INT', 'INT')
    RETURN_NAMES = ('width', 'height')
    FUNCTION = 'op'
    CATEGORY = 'math/graphics'

    def op(self, resolution: str) -> tuple[int, int]:
        (width, height) = resolution.split('x')
        return (int(width), int(height))
```