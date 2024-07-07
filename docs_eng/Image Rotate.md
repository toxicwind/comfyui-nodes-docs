# Documentation
- Class name: WAS_Image_Rotate
- Category: WAS Suite/Image/Transform
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The image rotation method is designed to apply the specified rotation to a group of images. It functions intelligently by adjusting the angle to the nearest 90 degrees and using the specified resampling filter to maintain image quality. The function of the node is essential for image pre-processing and for image operations that require a reorientation.

# Input types
## Required
- images
    - The parameter 'images' is the sequence of images to be rotated. It plays a vital role because all operations at the node are around this input. The quality and format of these images directly influence the outcome of the rotation process.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- rotation
    - The parameter 'rotation' assigns a rotation angle in degrees. It is vital because it determines the degree of rotation to be applied to the image. Any rotation value that cannot be divided by 90 is adjusted to the nearest 90 multipliers for standard processing.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- mode
    - Parameter'mode' determines the rotation strategy: 'internal' for standard rotation, 'transpose' for rotation using image conversion methods. It is important because it determines the bottom algorithm to be used for rotation.
    - Comfy dtype: COMBO['transpose', 'internal']
    - Python dtype: str
- sampler
    - The parameter'sampler' defines the re-sampler filter used during rotation. It is important because it affects the quality of the image after rotation. Different samplers provide different trade-offs between speed and image authenticity.
    - Comfy dtype: COMBO['nearest', 'bilinear', 'bicubic']
    - Python dtype: str

# Output types
- images
    - Output 'images' contains a rotating image batch. It is the main result of node operations and is important because it represents post-conversion data that can be further processed or analysed.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Image_Rotate:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'images': ('IMAGE',), 'mode': (['transpose', 'internal'],), 'rotation': ('INT', {'default': 0, 'min': 0, 'max': 360, 'step': 90}), 'sampler': (['nearest', 'bilinear', 'bicubic'],)}}
    RETURN_TYPES = ('IMAGE',)
    RETURN_NAMES = ('images',)
    FUNCTION = 'image_rotate'
    CATEGORY = 'WAS Suite/Image/Transform'

    def image_rotate(self, images, mode, rotation, sampler):
        batch_tensor = []
        for image in images:
            image = tensor2pil(image)
            if rotation > 360:
                rotation = int(360)
            if rotation % 90 != 0:
                rotation = int(rotation // 90 * 90)
            if sampler:
                if sampler == 'nearest':
                    sampler = Image.NEAREST
                elif sampler == 'bicubic':
                    sampler = Image.BICUBIC
                elif sampler == 'bilinear':
                    sampler = Image.BILINEAR
                else:
                    sampler == Image.BILINEAR
            if mode == 'internal':
                image = image.rotate(rotation, sampler)
            else:
                rot = int(rotation / 90)
                for _ in range(rot):
                    image = image.transpose(2)
            batch_tensor.append(pil2tensor(image))
        batch_tensor = torch.cat(batch_tensor, dim=0)
        return (batch_tensor,)
```