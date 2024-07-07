# Documentation
- Class name: APISR_Zho
- Category: 🔎APISR
- Output node: False
- Repo Ref: https://github.com/ZHO-ZHO-ZHO/ComfyUI-APISR.git

The node is designed to improve the resolution of the image using the specified model, focusing on improving the clarity and detail of the input image. It adjusts the image to meet the requirements of the model and applies the enhancement process to produce an ultra-resolution image.

# Input types
## Required
- pipe
    - The `pipe' parameter represents the model used for image ultra-resolution. It is essential because it defines the basic architecture and learning outcomes that will be applied to enhance images.
    - Comfy dtype: APISRMODEL
    - Python dtype: torch.nn.Module
- image
    - The 'image'parameter is an input image that is processed by a node. Its quality and dimensions directly affect the output of the super-resolution.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image or torch.Tensor
- dtype
    - The 'dtype'parameter specifies the model weight and type of data to enter the image length. It affects the accuracy of the calculation and may affect the quality of the ultra-resolution image.
    - Comfy dtype: COMBO[float32, float16]
    - Python dtype: str
## Optional
- crop_for_4x
    - The `crop_for_4x' parameter determines whether the input image should be trimmed to a multi-digit size of 4 in order to optimize the processing of a particular model.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- super_resolved_img
    - The'suber_resolved_img' parameter is an output of nodes, representing an enhanced image with an improved resolution. It is the result of applying the model's ultra-resolution capability to the input image.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class APISR_Zho:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'pipe': ('APISRMODEL',), 'image': ('IMAGE',), 'crop_for_4x': ('BOOLEAN', {'default': True}), 'dtype': (['float32', 'float16'],)}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'sr_image'
    CATEGORY = '🔎APISR'

    def sr_image(self, pipe, image, crop_for_4x, dtype):
        if dtype == 'float32':
            weight_dtype = torch.float32
        elif dtype == 'float16':
            weight_dtype = torch.float16
        pipe = pipe.to(device=device, dtype=weight_dtype)
        img_tensor = image.permute(0, 3, 1, 2).to(device=device, dtype=weight_dtype)
        if crop_for_4x:
            (_, _, h, w) = img_tensor.shape
            if h % 4 != 0:
                img_tensor = img_tensor[:, :, :4 * (h // 4), :]
            if w % 4 != 0:
                img_tensor = img_tensor[:, :, :, :4 * (w // 4)]
        super_resolved_img = pipe(img_tensor)
        super_resolved_img_nhwc = super_resolved_img.permute(0, 2, 3, 1).cpu()
        return (super_resolved_img_nhwc,)
```