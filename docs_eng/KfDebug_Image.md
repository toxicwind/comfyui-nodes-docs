# Documentation
- Class name: KfDebug_Image
- Category: Debugging
- Output node: True
- Repo Ref: https://github.com/dmarx/ComfyUI-Keyframed

KfDebug_Image nodes are designed to make image data visible in the workflow and provide a means of checking and validating image input or output at different stages of processing. By providing a clear visual representation of images, it enhances the debugging process to ensure that image data are properly processed and meets expected standards.

# Input types
## Required
- image
    - An image parameter is essential for KfDebug_Image node, as it is the main visualised input to the node. By allowing nodes to display images for inspection, it ensures that image data meet expectations and helps to identify any potential problems or differences, affecting the entire debugging process.
    - Comfy dtype: COMBO[numpy.ndarray,PIL.Image,torch.Tensor]
    - Python dtype: Union[numpy.ndarray, PIL.Image, torch.Tensor]

# Output types
- image
    - The output image of KfDebug_Image node is a visual confirmation of the status of the input image. It is very important because it provides a means of verifying the integrity and accuracy of the image data after transmitting it in the workflow to ensure that it is not altered or damaged.
    - Comfy dtype: IMAGE
    - Python dtype: Union[numpy.ndarray, PIL.Image]

# Usage tips
- Infra type: CPU

# Source code
```
class KfDebug_Image(KfDebug_Passthrough):
    RETURN_TYPES = ('IMAGE',)
```