# Documentation
- Class name: WAS_Image_To_Mask
- Category: WAS Suite/Image/Masking
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The `image_to_mask'method is designed to extract a particular colour channel from a set of images and convert it to a mask. This process is essential for the application of specific components of the image to be isolated, for example, in the image partition or object identification task. The node operates by selecting the desired channel and converting it into a binary mask, which can then be further analysed or operated.

# Input types
## Required
- images
    - The 'images'parameter is essential because it represents the input image that the node will process. It is necessary for the node to run and directly affects the output mask, which determines the source material for the mask operation.
    - Comfy dtype: IMAGE
    - Python dtype: List[torch.Tensor]
- channel
    - The 'channel'parameter determines the colour channel to be extracted to form a mask. This is a key option that affects the appearance of the ultimate mask and its usefulness in the next step.
    - Comfy dtype: COMBO['alpha', 'red', 'green', 'blue']
    - Python dtype: str

# Output types
- MASKS
    - The `MASKS'output consists of the generation mask derived from the selected colour channel in which the image is entered. These masks are important for tasks involving the isolation and analysis of specific parts of the image.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Image_To_Mask:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'images': ('IMAGE',), 'channel': (['alpha', 'red', 'green', 'blue'],)}}
    CATEGORY = 'WAS Suite/Image/Masking'
    RETURN_TYPES = ('MASK',)
    RETURN_NAMES = ('MASKS',)
    FUNCTION = 'image_to_mask'

    def image_to_mask(self, images, channel):
        mask_images = []
        for image in images:
            image = tensor2pil(image).convert('RGBA')
            (r, g, b, a) = image.split()
            if channel == 'red':
                channel_image = r
            elif channel == 'green':
                channel_image = g
            elif channel == 'blue':
                channel_image = b
            elif channel == 'alpha':
                channel_image = a
            mask = torch.from_numpy(np.array(channel_image.convert('L')).astype(np.float32) / 255.0)
            mask_images.append(mask)
        return (torch.cat(mask_images, dim=0),)
```