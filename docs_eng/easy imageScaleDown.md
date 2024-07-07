# Documentation
- Class name: imageScaleDown
- Category: EasyUse/Image
- Output node: False
- Repo Ref: https://github.com/yolain/ComfyUI-Easy-Use.git

The node is intended to adjust the image to the specified width and height, and may be used as a central crop to preserve the integrity of the ratio. This is critical for pre-processing image data to fit the input dimensions required for various machine learning models and applications.

# Input types
## Required
- images
    - Images to be reduced. This parameter is essential because the node directly affects the image data and affects the size and quality of the output.
    - Comfy dtype: COMBO[Tensor]
    - Python dtype: torch.Tensor
- width
    - The expected width of the image after zooming. This parameter is critical because it sets the horizontal dimensions that affect the process of resizing.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - Scales the image's expected height. This parameter is critical because it sets the vertical dimension of the output and affects the process of resizing.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- crop
    - Adjusts the method of cropping applied over a larger hour. This parameter is important because it determines whether the image is in the middle before scaling, which enhances the visual presentation of the output.
    - Comfy dtype: ENUM
    - Python dtype: str

# Output types
- IMAGE
    - Resizes the image. This is the main output of the node, representing the converted data ready for further processing or analysis.
    - Comfy dtype: COMBO[Tensor]
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class imageScaleDown:
    crop_methods = ['disabled', 'center']

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'images': ('IMAGE',), 'width': ('INT', {'default': 512, 'min': 1, 'max': MAX_RESOLUTION, 'step': 1}), 'height': ('INT', {'default': 512, 'min': 1, 'max': MAX_RESOLUTION, 'step': 1}), 'crop': (s.crop_methods,)}}
    RETURN_TYPES = ('IMAGE',)
    CATEGORY = 'EasyUse/Image'
    FUNCTION = 'image_scale_down'

    def image_scale_down(self, images, width, height, crop):
        if crop == 'center':
            old_width = images.shape[2]
            old_height = images.shape[1]
            old_aspect = old_width / old_height
            new_aspect = width / height
            x = 0
            y = 0
            if old_aspect > new_aspect:
                x = round((old_width - old_width * (new_aspect / old_aspect)) / 2)
            elif old_aspect < new_aspect:
                y = round((old_height - old_height * (old_aspect / new_aspect)) / 2)
            s = images[:, y:old_height - y, x:old_width - x, :]
        else:
            s = images
        results = []
        for image in s:
            img = tensor2pil(image).convert('RGB')
            img = img.resize((width, height), Image.LANCZOS)
            results.append(pil2tensor(img))
        return (torch.cat(results, dim=0),)
```