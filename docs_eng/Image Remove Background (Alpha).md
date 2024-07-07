# Documentation
- Class name: WAS_Remove_Background
- Category: WAS Suite/Image/Process
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Remove_Background node is designed to handle images by removing background and achieving prospective extraction. By converting images to greyscale maps, it uses Gaussian blurry and uses a two-value threshold to create a mask to isolate the required elements. This node is particularly suitable for tasks that require clean future objects without background interference.

# Input types
## Required
- images
    - The `images' parameter is essential for the node, as it represents the input image that the node will process. The function of the node revolves around the operation of these images to remove the background, making this parameter essential to the execution of the node.
    - Comfy dtype: IMAGE
    - Python dtype: List[PIL.Image.Image]
## Optional
- mode
    - The `mode' parameter determines whether the node will remove the image from its background or future. This is an optional parameter that can influence the behaviour of the node depending on the desired outcome and allows flexibility in processing different types of images.
    - Comfy dtype: STRING
    - Python dtype: str
- threshold
    - The `threshold' parameter is essential to control the sensitivity of the removal process in the background. It sets the level at which the greyscale is considered to be the background or perspective, directly affecting the ability of the nodes to distinguish between the two.
    - Comfy dtype: INT
    - Python dtype: int
- threshold_tolerance
    - The 'threshold_tolerance' parameter defines the hyperbolic radius used to smooth images before applying thresholds. It affects the ability of nodes to process noise and details in images and plays an important role in the quality of the final output.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- images
    - The `images' output parameter contains the processing image after the background is removed. It is the final result of the node operation and represents the main result of the image processing task.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Remove_Background:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'images': ('IMAGE',), 'mode': (['background', 'foreground'],), 'threshold': ('INT', {'default': 127, 'min': 0, 'max': 255, 'step': 1}), 'threshold_tolerance': ('INT', {'default': 2, 'min': 1, 'max': 24, 'step': 1})}}
    RETURN_TYPES = ('IMAGE',)
    RETURN_NAMES = ('images',)
    FUNCTION = 'image_remove_background'
    CATEGORY = 'WAS Suite/Image/Process'

    def image_remove_background(self, images, mode='background', threshold=127, threshold_tolerance=2):
        return (self.remove_background(images, mode, threshold, threshold_tolerance),)

    def remove_background(self, image, mode, threshold, threshold_tolerance):
        images = []
        image = [tensor2pil(img) for img in image]
        for img in image:
            grayscale_image = img.convert('L')
            if mode == 'background':
                grayscale_image = ImageOps.invert(grayscale_image)
                threshold = 255 - threshold
            blurred_image = grayscale_image.filter(ImageFilter.GaussianBlur(radius=threshold_tolerance))
            binary_image = blurred_image.point(lambda x: 0 if x < threshold else 255, '1')
            mask = binary_image.convert('L')
            inverted_mask = ImageOps.invert(mask)
            transparent_image = img.copy()
            transparent_image.putalpha(inverted_mask)
            images.append(pil2tensor(transparent_image))
        batch = torch.cat(images, dim=0)
        return batch
```