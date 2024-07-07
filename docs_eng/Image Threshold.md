# Documentation
- Class name: WAS_Image_Threshold
- Category: WAS Suite/Image/Process
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Image_Threshold node is designed to treat images by applying thresholds, which is very useful for creating binary images from greyscale input. It plays a key role in image partitioning and feature extraction tasks by simplifying the image as its core structure by specifying thresholds.

# Input types
## Required
- image
    - The image parameter is essential for the operation of the node, because it is the input that will be processed. It is implemented by determining the content that will be subject to the threshold, which is essential for the clarity and detail of the final output.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image
## Optional
- threshold
    - The threshold parameter is important because it determines the cut-off point for the classification of pixels in the image. It directly influences the output of nodes by controlling the greyscale value to black or white (based on whether they meet or exceed the threshold).
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- thresholded_image
    - Threshold image output represents the result of which the image is entered after applying the threshold. It is important because it provides a binary version of the input, which is usually used for further analysis or as a step in a more complex image processing workflow.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Image_Threshold:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'image': ('IMAGE',), 'threshold': ('FLOAT', {'default': 0.5, 'min': 0.0, 'max': 1.0, 'step': 0.01})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'image_threshold'
    CATEGORY = 'WAS Suite/Image/Process'

    def image_threshold(self, image, threshold=0.5):
        return (pil2tensor(self.apply_threshold(tensor2pil(image), threshold)),)

    def apply_threshold(self, input_image, threshold=0.5):
        grayscale_image = input_image.convert('L')
        threshold_value = int(threshold * 255)
        thresholded_image = grayscale_image.point(lambda x: 255 if x >= threshold_value else 0, mode='L')
        return thresholded_image
```