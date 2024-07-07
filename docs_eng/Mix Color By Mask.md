# Documentation
- Class name: MixColorByMask
- Category: Masquerade Nodes
- Output node: False
- Repo Ref: https://github.com/BadCafeCode/masquerade-nodes-comfyui

The'mix'method of the MixColorByMask node is designed to mix the input image with the pure color according to the mask provided. It adjusts the colour channel of the image to the specified RGB value, and then uses the mask to selectively group the original image with the new colour layer. This node is particularly suitable for creating synthetic images, in which certain areas need to be highlighted or modified with specific colours.

# Input types
## Required
- image
    - The 'image'parameter is an input image that is operated by a node. It is essential because it is the basis for a colour blending operation. The node combinations provide colour values and masks to process the image in order to achieve the required visual effects.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- r
    - The 'r' parameter specifies the strength of the red channel in the colour that you want to mix with the image. It plays a key role in determining that you will overwrite the image according to the mask. This parameter directly influences the colour output of node operations.
    - Comfy dtype: INT
    - Python dtype: int
- g
    - The 'g' parameter defines the strength of the green channel that the colour covers. It works with the red and blue channel, creating the required colour that will be applied to the image through the mask. The selection of the green intensity is essential to achieve the colour effect.
    - Comfy dtype: INT
    - Python dtype: int
- b
    - The 'b' parameter is set to apply to the blue channel strength of the colour of the image. It is a key component of the colour mixing process, ensuring that the colour mix is consistent with the creative vision. The value of the blue channel is essential to accurately present the final colour.
    - Comfy dtype: INT
    - Python dtype: int
- mask
    - The'mask' parameter is a binary image that indicates which parts of the input image will receive colour coverage. It is a key element because it controls the area in the image that will be affected by colour mixing. The mask pattern determines the area that the new colour will see.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Output types
- output_image
    - 'output_image' is the result of a colour mixing process in which the original image is combined with the specified colour, guided by the mask. It represents the final visual result of the node operation and shows the creative application of colour to a particular area of the image.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class MixColorByMask:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'image': ('IMAGE',), 'r': ('INT', {'default': 0, 'min': 0, 'max': 255, 'step': 1}), 'g': ('INT', {'default': 0, 'min': 0, 'max': 255, 'step': 1}), 'b': ('INT', {'default': 0, 'min': 0, 'max': 255, 'step': 1}), 'mask': ('IMAGE',)}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'mix'
    CATEGORY = 'Masquerade Nodes'

    def mix(self, image, r, g, b, mask):
        (r, g, b) = (r / 255.0, g / 255.0, b / 255.0)
        image_size = image.size()
        image2 = torch.tensor([r, g, b]).to(device=image.device).unsqueeze(0).unsqueeze(0).unsqueeze(0).repeat(image_size[0], image_size[1], image_size[2], 1)
        (image, image2) = tensors2common(image, image2)
        mask = tensor2batch(tensor2mask(mask), image.size())
        return (image * (1.0 - mask) + image2 * mask,)
```