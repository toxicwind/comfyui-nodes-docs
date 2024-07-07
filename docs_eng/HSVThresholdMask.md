# Documentation
- Class name: HSVThresholdMask
- Category: postprocessing/Masks
- Output node: False
- Repo Ref: https://github.com/EllangoK/ComfyUI-post-processing-nodes

The node class covers the operation of thresholds within the HSV colour space, enabling the creation of a two-value mask based on a particular hue, saturation, or brightness range. This is essential to divide and separate areas of interest in the image, facilitating multiple image processing tasks such as object identification and noise reduction.

# Input types
## Required
- image
    - The image parameter is critical to the HSV threshold processing process because it provides source data that divides the threshold. It affects the entire operation by deciding which areas of the image will be treated by the mask criteria.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- low_threshold
    - The low-threshold parameter sets the lower limit of the HSV channel value and plays a crucial role in defining the range of pixel values to be considered for masking.
    - Comfy dtype: FLOAT
    - Python dtype: float
- high_threshold
    - High-threshold parameters establish the upper limit of HSV channel values, and together with low-threshold values determine the final mask.
    - Comfy dtype: FLOAT
    - Python dtype: float
- hsv_channel
    - The hsv_channel parameter indicates which channel will be used for threshold processing in HSV colour space, which has a significant impact on the resulting mask and its applicability in the current image processing task.
    - Comfy dtype: COMBO['hue', 'saturation', 'value']
    - Python dtype: str

# Output types
- result
    - Outcome parameters, representing a double mask generated through the application of HSV threshold criteria, are important tools for further image analysis and operation.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class HSVThresholdMask:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'low_threshold': ('FLOAT', {'default': 0.2, 'min': 0, 'max': 1, 'step': 0.1}), 'high_threshold': ('FLOAT', {'default': 0.7, 'min': 0, 'max': 1, 'step': 0.1}), 'hsv_channel': (['hue', 'saturation', 'value'],)}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'hsv_threshold'
    CATEGORY = 'postprocessing/Masks'

    def hsv_threshold(self, image: torch.Tensor, low_threshold: float, high_threshold: float, hsv_channel: str):
        (batch_size, height, width, _) = image.shape
        result = torch.zeros(batch_size, height, width)
        if hsv_channel == 'hue':
            channel = 0
            (low_threshold, high_threshold) = (int(low_threshold * 180), int(high_threshold * 180))
        elif hsv_channel == 'saturation':
            channel = 1
            (low_threshold, high_threshold) = (int(low_threshold * 255), int(high_threshold * 255))
        elif hsv_channel == 'value':
            channel = 2
            (low_threshold, high_threshold) = (int(low_threshold * 255), int(high_threshold * 255))
        for b in range(batch_size):
            tensor_image = (image[b].numpy().copy() * 255).astype(np.uint8)
            hsv_image = cv2.cvtColor(tensor_image, cv2.COLOR_RGB2HSV)
            mask = cv2.inRange(hsv_image[:, :, channel], low_threshold, high_threshold)
            tensor = torch.from_numpy(mask).float() / 255.0
            result[b] = tensor
        return (result,)
```