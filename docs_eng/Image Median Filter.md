# Documentation
- Class name: WAS_Image_Median_Filter
- Category: WAS Suite/Image/Filter
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

WAS_Image_Median_Filter applies the median filter to input images, which is a non-linear operation that replaces each pixel with the median value of the surrounding pixels. This is very useful in reducing image noise while retaining edges. The node is designed to process a group of images and provide powerful solutions for image pre-processing tasks.

# Input types
## Required
- image
    - The image parameter is the core input of the node, which represents the image data to be processed. It is essential for the execution of the node, as it determines the object of the medium filter operation. The quality and properties of the input image directly influence the results of the filtering process.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
## Optional
- diameter
    - The diameter parameter specifies the size of the filter core to be used in the medium filtering process. This is an important adjustment parameter, which affects the extent of noise reduction and preservation of image details. The greater the diameter, the stronger the noise inhibition, it may also lead to the loss of more finer details.
    - Comfy dtype: INT
    - Python dtype: int
- sigma_color
    - The sigma_color parameter defines the sensitivity of the filter to color changes within the image. This is a key parameter in controlling the colour of the filter process, allowing adjustments to be made to the specific characteristics of the input image.
    - Comfy dtype: FLOAT
    - Python dtype: float
- sigma_space
    - The sigma_space parameter controls the sensitivity of the filter to spatial changes within the image. It is essential to fine-tune the spatial aspects of the median filter, ensuring that the operation adapts to the content and structure of the image.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- output_image
    - Output_image is the result of an input medium-value filter. It represents a processed image with a reduced noise and a reserved edge that is suitable for further analysis or presentation.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Image_Median_Filter:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'image': ('IMAGE',), 'diameter': ('INT', {'default': 2.0, 'min': 0.1, 'max': 255, 'step': 1}), 'sigma_color': ('FLOAT', {'default': 10.0, 'min': -255.0, 'max': 255.0, 'step': 0.1}), 'sigma_space': ('FLOAT', {'default': 10.0, 'min': -255.0, 'max': 255.0, 'step': 0.1})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'apply_median_filter'
    CATEGORY = 'WAS Suite/Image/Filter'

    def apply_median_filter(self, image, diameter, sigma_color, sigma_space):
        tensor_images = []
        for img in image:
            img = tensor2pil(img)
            tensor_images.append(pil2tensor(medianFilter(img, diameter, sigma_color, sigma_space)))
        tensor_images = torch.cat(tensor_images, dim=0)
        return (tensor_images,)
```