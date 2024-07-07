# Documentation
- Class name: Canny
- Category: image/preprocessors
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The Canny node is designed to detect the edges of the image using the Canny algorithm, a popular margin detection technique. It enhances the clarity of the edges of the input image by applying multi-stage processes that include Gaussian filtering, gradient calculation, non-extreme inhibition and processing of the lag threshold. The node plays a key role in the pre-processing of the image, applying to applications such as signature detection, partitioning and image analysis.

# Input types
## Required
- image
    - The input image is the basis for the Canny node operation, as it is the primary data for the margin test. The quality and resolution of the input image directly influences the accuracy and detail of the edge detected.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- low_threshold
    - The low-threshold parameter is essential for the initial phase of the margin test, which defines the lower limit of the margin identification. It works with the high-threshold value to fine-tune the detection process and to control the sensitivity of the margin detection.
    - Comfy dtype: FLOAT
    - Python dtype: float
- high_threshold
    - A high threshold is essential to fine-tune the detected edges, setting the upper limit of the margin to be accepted. It helps to control the number of pseudo edges and ensures that only the most significant edges are retained in the final output.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- image
    - An output image of a Canny node is a peripheral version of the input, in which the edges are detected and highlighted. This output is important for further image analysis or as input to other processing nodes that require marginal information.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class Canny:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'low_threshold': ('FLOAT', {'default': 0.4, 'min': 0.01, 'max': 0.99, 'step': 0.01}), 'high_threshold': ('FLOAT', {'default': 0.8, 'min': 0.01, 'max': 0.99, 'step': 0.01})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'detect_edge'
    CATEGORY = 'image/preprocessors'

    def detect_edge(self, image, low_threshold, high_threshold):
        output = canny(image.to(comfy.model_management.get_torch_device()).movedim(-1, 1), low_threshold, high_threshold)
        img_out = output[1].to(comfy.model_management.intermediate_device()).repeat(1, 3, 1, 1).movedim(1, -1)
        return (img_out,)
```