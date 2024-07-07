# Documentation
- Class name: NearestSDXLResolution
- Category: math/graphics
- Output node: False
- Repo Ref: https://github.com/evanspearman/ComfyMath

The NearestSDXLReference node is designed to select the most supported resolution close to the input resolution. It is achieved by calculating the width ratio of the input image and comparing it with the supported resolution list, and then selecting the least variable resolution. The function of the node is essential to ensure compatibility and optimal display quality in graphic processing applications.

# Input types
## Required
- image
    - The 'image'parameter is essential because it is an input for the node. This is an image whose resolution matches the supported resolution. The node is fully dependent on this input because it determines the most recent choice of resolution support.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Output types
- width
    - The 'width' parameter represents the width of the selected resolution. It is a key output because it defines the horizontal dimensions of the image after the resolution matching process. This output is important for any subsequent graphic operation that relies on the image size.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - The 'height' parameter indicates the height of the selected resolution. Similar to the 'width' parameter, it is an important output that determines the vertical dimensions of the image for further processing. It ensures that the width ratio of the image is maintained after resolution selection.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class NearestSDXLResolution:

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {'required': {'image': ('IMAGE',)}}
    RETURN_TYPES = ('INT', 'INT')
    RETURN_NAMES = ('width', 'height')
    FUNCTION = 'op'
    CATEGORY = 'math/graphics'

    def op(self, image) -> tuple[int, int]:
        image_width = image.size()[2]
        image_height = image.size()[1]
        print(f'Input image resolution: {image_width}x{image_height}')
        image_ratio = image_width / image_height
        differences = [(abs(image_ratio - resolution[2]), resolution) for resolution in SDXL_SUPPORTED_RESOLUTIONS]
        smallest = None
        for difference in differences:
            if smallest is None:
                smallest = difference
            elif difference[0] < smallest[0]:
                smallest = difference
        if smallest is not None:
            width = smallest[1][0]
            height = smallest[1][1]
        else:
            width = 1024
            height = 1024
        print(f'Selected SDXL resolution: {width}x{height}')
        return (width, height)
```