# Documentation
- Class name: ImageColorTransfer
- Category: ♾️Mixlab/Image
- Output node: False
- Repo Ref: https://github.com/shadowcz007/comfyui-mixlab-nodes.git

The ImageColorTransfer node is designed to re-colour the image by passing the palette from one image to another. It achieves this by using the colour transfer algorithm, which operates the colour distribution of the source image to match the target image, generating a visually consistent and styled change of output.

# Input types
## Required
- source
    - The source parameter is an image that is to be replaced with a colour. It plays a key role in the colour shift because it determines the original colour palette that will be changed.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- target
    - The target parameter represents the colour palette that will be applied to the image in the source image. It is essential to define the colour scheme that should be reflected in the output image.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Output types
- result
    - Reult parameter is a colour-shifted output image. It marks the final product of node operations and displays a source image that is adapted to colour from the target image.
    - Comfy dtype: IMAGE
    - Python dtype: List[torch.Tensor]

# Usage tips
- Infra type: CPU

# Source code
```
class ImageColorTransfer:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'source': ('IMAGE',), 'target': ('IMAGE',)}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'run'
    CATEGORY = '♾️Mixlab/Image'
    INPUT_IS_LIST = True
    OUTPUT_IS_LIST = (True,)

    def run(self, source, target):
        res = []
        target = target[0][0]
        print(target.shape)
        target = tensor2pil(target)
        for ims in source:
            for im in ims:
                image = tensor2pil(im)
                image = color_transfer(image, target)
                image = pil2tensor(image)
                res.append(image)
        return (res,)
```