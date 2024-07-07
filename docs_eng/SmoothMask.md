# Documentation
- Class name: SmoothMask
- Category: ♾️Mixlab/Mask
- Output node: False
- Repo Ref: https://github.com/shadowcz007/comfyui-mixlab-nodes.git

SmoothMask is a node that handles image masks to reduce noise and detail, providing more smooth visual output. It achieves this by applying Gaussian ambiguity to input masks, effectively softens their edges and reduces high-frequency information. This node is essential to prepare for the need for a more gradual transition between masked and non-shadowed areas, improving the visual quality of the final image.

# Input types
## Required
- mask
    - The mask parameter is a source image for smoothing operations. It is vital because it defines the initial state of the image to be processed by nodes. The quality and resolution of the mask directly influences the validity of smooth processing.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image
## Optional
- smoothness
    - The smoothness parameter controls the degree of obscurity that should be applied to the mask. It is an important factor because it determines the extent to which the mask edges are softened. Higher values create a more blurred and smooth mask, while lower values retain more details of the original mask.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- MASK
    - The output of the SmoothMask node is a modified version of the input mask, with reduced noise and a smoother edge. This smooth mask can be used in a variety of image-processing tasks, requiring a more fine transition between the mask and the unshaded area.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image

# Usage tips
- Infra type: CPU

# Source code
```
class SmoothMask:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'mask': ('MASK',), 'smoothness': ('INT', {'default': 1, 'min': 0, 'max': 150, 'step': 1, 'display': 'slider'})}}
    RETURN_TYPES = ('MASK',)
    FUNCTION = 'run'
    CATEGORY = '♾️Mixlab/Mask'
    INPUT_IS_LIST = False
    OUTPUT_IS_LIST = (False,)

    def run(self, mask, smoothness):
        print('SmoothMask', mask.shape)
        mask = tensor2pil(mask)
        feathered_image = mask.filter(ImageFilter.GaussianBlur(smoothness))
        mask = pil2tensor(feathered_image)
        return (mask,)
```