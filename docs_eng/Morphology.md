# Documentation
- Class name: Morphology
- Category: image/postprocessing
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The morphology node is designed to perform various morphological operations for images, such as corrosion, inflation, start-up and shut-down operations, which are used in image processing to change the shape or size of features in images and are the basic operations in image processing. Using custom-made cores to apply these operations, it provides a multifunctional tool for image reprocessing tasks.

# Input types
## Required
- image
    - Enter the image as the main data to be used for morphology operations. This is a key parameter, because all functions of the node revolve around the manipulation of the image.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- operation
    - The operating parameter specifies the type of morphological change that you want to execute. It is very important because it determines the nature of the changes that will be made to the input image.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- kernel_size
    - The size of the core determines the size of the structural elements used for morphological operations. It is an important parameter because it affects the scope of the changes applied to the image.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- output_image
    - The output image is the result of the application of the selected morphological operation to the input of the image. It represents the final state of the processed image.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class Morphology:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'operation': (['erode', 'dilate', 'open', 'close', 'gradient', 'bottom_hat', 'top_hat'],), 'kernel_size': ('INT', {'default': 3, 'min': 3, 'max': 999, 'step': 1})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'process'
    CATEGORY = 'image/postprocessing'

    def process(self, image, operation, kernel_size):
        device = comfy.model_management.get_torch_device()
        kernel = torch.ones(kernel_size, kernel_size, device=device)
        image_k = image.to(device).movedim(-1, 1)
        if operation == 'erode':
            output = erosion(image_k, kernel)
        elif operation == 'dilate':
            output = dilation(image_k, kernel)
        elif operation == 'open':
            output = opening(image_k, kernel)
        elif operation == 'close':
            output = closing(image_k, kernel)
        elif operation == 'gradient':
            output = gradient(image_k, kernel)
        elif operation == 'top_hat':
            output = top_hat(image_k, kernel)
        elif operation == 'bottom_hat':
            output = bottom_hat(image_k, kernel)
        else:
            raise ValueError(f"Invalid operation {operation} for morphology. Must be one of 'erode', 'dilate', 'open', 'close', 'gradient', 'tophat', 'bottomhat'")
        img_out = output.to(comfy.model_management.intermediate_device()).movedim(1, -1)
        return (img_out,)
```