# Documentation
- Class name: WAS_Image_Displacement_Warp
- Category: WAS Suite/Image/Transform
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Image_Displacement_Warp node is designed to apply the displacement effect to a given set of images. It uses a displacement map and amplitude factors to determine the extent of the deformation, thus generating a visually distorted output that can be used for various creative and technological applications.

# Input types
## Required
- images
    - You want to apply the input images of the displacement effect. These images form the base layer of the transformation process.
    - Comfy dtype: IMAGE
    - Python dtype: List[torch.Tensor]
- displacement_maps
    - Bitmap instructions apply to the direction and intensity of the transformation effect of the input image. Each pixel value in the map corresponds to a bit shift vector.
    - Comfy dtype: IMAGE
    - Python dtype: List[torch.Tensor]
## Optional
- amplitude
    - An amplitude parameter controls the strength of the shift effect. The higher the value, the more visible the deformation; the lower the value, the more subtle the effect.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- images
    - The output image is the result of the application of the transformation effect to the input image, using the specified movement map and amplitude.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Image_Displacement_Warp:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'images': ('IMAGE',), 'displacement_maps': ('IMAGE',), 'amplitude': ('FLOAT', {'default': 25.0, 'min': -4096, 'max': 4096, 'step': 0.1})}}
    RETURN_TYPES = ('IMAGE',)
    RETURN_NAMES = ('images',)
    FUNCTION = 'displace_image'
    CATEGORY = 'WAS Suite/Image/Transform'

    def displace_image(self, images, displacement_maps, amplitude):
        WTools = WAS_Tools_Class()
        displaced_images = []
        for i in range(len(images)):
            img = tensor2pil(images[i])
            if i < len(displacement_maps):
                disp = tensor2pil(displacement_maps[i])
            else:
                disp = tensor2pil(displacement_maps[-1])
            disp = self.resize_and_crop(disp, img.size)
            displaced_images.append(pil2tensor(WTools.displace_image(img, disp, amplitude)))
        displaced_images = torch.cat(displaced_images, dim=0)
        return (displaced_images,)

    def resize_and_crop(self, image, target_size):
        (width, height) = image.size
        (target_width, target_height) = target_size
        aspect_ratio = width / height
        target_aspect_ratio = target_width / target_height
        if aspect_ratio > target_aspect_ratio:
            new_height = target_height
            new_width = int(new_height * aspect_ratio)
        else:
            new_width = target_width
            new_height = int(new_width / aspect_ratio)
        image = image.resize((new_width, new_height))
        left = (new_width - target_width) // 2
        top = (new_height - target_height) // 2
        right = left + target_width
        bottom = top + target_height
        image = image.crop((left, top, right, bottom))
        return image
```