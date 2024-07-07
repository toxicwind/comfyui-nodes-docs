# Documentation
- Class name: GreyScale
- Category: image/postprocessing
- Output node: False
- Repo Ref: https://github.com/Jordach/comfy-plasma.git

The node is intended to convert the coloured images entered into greyscale images and to increase the clarity of visual details by focusing on brightness changes. It is the basic step in the image processing process, allowing subsequent tasks, such as feature extraction and image analysis, to be performed more effectively on simplified greyscale data.

# Input types
## Required
- IMAGE
    - The IMAGE parameter is necessary because it provides the original input into the greyscale conversion process. It affects the overall operation of the node and determines the size and quality of the output image.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image

# Output types
- IMAGE
    - The output IMAGE is a greyscale processing version of the input image, which is essential for the subsequent image analysis task and serves as the base layer in the image processing warehouse.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image

# Usage tips
- Infra type: CPU

# Source code
```
class GreyScale:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'IMAGE': ('IMAGE',)}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'process_image'
    CATEGORY = 'image/postprocessing'

    def process_image(self, IMAGE):
        cimg = conv_tensor_pil(IMAGE)
        gimg = ImageOps.grayscale(cimg)
        rgbimg = Image.new('RGB', (gimg.width, gimg.height))
        rgbimg.paste(gimg)
        return conv_pil_tensor(rgbimg)
```