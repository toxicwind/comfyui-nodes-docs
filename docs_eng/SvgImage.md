# Documentation
- Class name: SvgImage
- Category: ♾️Mixlab/Image
- Output node: False
- Repo Ref: https://github.com/shadowcz007/comfyui-mixlab-nodes.git

The node is designed to process SVG images and convert them to a volume format suitable for further operation and analysis in the neural network framework. It emphasizes the conversion and adaptation of SVG data in order to integrate with the in-depth learning model.

# Input types
## Required
- upload
    - The `upload' parameter is essential to the operation of the node, which contains SVG image data and associated metadata. It directly affects the ability of the node to process and convert SVG to volume.
    - Comfy dtype: Dict[str, Any]
    - Python dtype: Dict[str, Any]

# Output types
- IMAGE
    - The `IMAGE' output provides a stencil for the input of SVG images, which can be used for further processing in the depth learning environment.
    - Comfy dtype: Tensor
    - Python dtype: torch.Tensor
- layers
    - The `layers' output contains individual components or layers extracted from SVG data that can be used for detailed analysis or operation of image structures.
    - Comfy dtype: List[Any]
    - Python dtype: List[Any]

# Usage tips
- Infra type: CPU

# Source code
```
class SvgImage:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'upload': ('SVG',)}}
    RETURN_TYPES = ('IMAGE', 'LAYER')
    RETURN_NAMES = ('IMAGE', 'layers')
    FUNCTION = 'run'
    CATEGORY = '♾️Mixlab/Image'
    INPUT_IS_LIST = False
    OUTPUT_IS_LIST = (False, True)

    def run(self, upload):
        layers = []
        image = base64_to_image(upload['image'])
        image = image.convert('RGB')
        image = pil2tensor(image)
        for layer in upload['data']:
            layers.append(layer)
        return (image, layers)
```