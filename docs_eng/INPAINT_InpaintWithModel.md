# Documentation
- Class name: InpaintWithModel
- Category: inpaint
- Output node: False
- Repo Ref: https://github.com/Acly/comfyui-inpaint-nodes

It adapts to different model structures and ensures that the output is seamlessly integrated with the original image.

# Input types
## Required
- inpaint_model
    - The restoration model is essential for the function of the node, which defines the specific depth learning architecture used to generate the restoration content. The structure of the model has a direct impact on the quality and accuracy of the restoration results.
    - Comfy dtype: INPAINT_MODEL
    - Python dtype: PyTorchModel
- image
    - The input image is the primary data for node operations, and the restoration process is designed to maintain the overall structure and beauty while filling the missing parts. The quality and size of the image directly influences the restoration results.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- mask
    - Mask defines the area in the image that needs to be repaired. It is a key parameter, as the guiding model focuses on a particular area to ensure that the restoration is targeted and relevant.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Output types
- output_image
    - The output image is the result of the restoration process, and the initial masked or missing area is now filled with content that matches the surrounding content. It represents the main output of the node and is essential for further image analysis or display.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class InpaintWithModel:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'inpaint_model': ('INPAINT_MODEL',), 'image': ('IMAGE',), 'mask': ('MASK',)}}
    RETURN_TYPES = ('IMAGE',)
    CATEGORY = 'inpaint'
    FUNCTION = 'inpaint'

    def inpaint(self, inpaint_model: PyTorchModel, image: Tensor, mask: Tensor):
        if inpaint_model.model_arch == 'MAT':
            required_size = 512
        elif inpaint_model.model_arch == 'LaMa':
            required_size = 256
        else:
            raise ValueError(f'Unknown model_arch {inpaint_model.model_arch}')
        (image, mask) = to_torch(image, mask)
        image_device = image.device
        (original_image, original_mask) = (image, mask)
        (image, mask, original_size) = resize_square(image, mask, required_size)
        mask = mask.floor()
        device = get_torch_device()
        inpaint_model.to(device)
        image = inpaint_model(image.to(device), mask.to(device))
        inpaint_model.cpu()
        image = undo_resize_square(image.to(image_device), original_size)
        image = original_image + (image - original_image) * original_mask.floor()
        return (to_comfy(image),)
```