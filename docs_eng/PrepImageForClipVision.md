# Documentation
- Class name: PrepImageForClipVision
- Category: ipadapter/utils
- Output node: False
- Repo Ref: https://github.com/cubiq/ComfyUI_IPAdapter_plus.git

The node is designed to pre-process images for the ClipVision model to ensure that they are properly formatted for analysis. It focuses on resizeing, cropping and sharpening images to enhance their characteristics and to meet model input requirements.

# Input types
## Required
- image
    - The image parameter is essential because it is the main input for node processing. It affects the overall operation of the node and determines the quality and characteristics of the output.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image or torch.Tensor
## Optional
- interpolation
    - Plug-in mode defines how the image should be resized, which significantly affects the clarity and detail of the result image. This is an optional parameter that allows the image's appearance to be controlled after the resize.
    - Comfy dtype: COMBO[('LANCZOS', 'BICUBIC', 'HAMMING', 'BILINEAR', 'BOX', 'NEAREST')]
    - Python dtype: str
- crop_position
    - The crop location determines the way the image is cropped after the size has been adjusted. This affects the image's configuration and focus, ensuring that the most relevant features are centred or properly located.
    - Comfy dtype: COMBO[('top', 'bottom', 'left', 'right', 'center', 'pad')]
    - Python dtype: str
- sharpening
    - Sharpen the contrast of the image to increase its edge and detail. This parameter allows fine-tuning of the visual clarity of the image and significantly improves the ability of the model to characterize it.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- output
    - The output is a processed image that is now formatted and ready for ClipVision model analysis. It represents the crystallization of node processing and contains all the adjustments to the original image.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class PrepImageForClipVision:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'interpolation': (['LANCZOS', 'BICUBIC', 'HAMMING', 'BILINEAR', 'BOX', 'NEAREST'],), 'crop_position': (['top', 'bottom', 'left', 'right', 'center', 'pad'],), 'sharpening': ('FLOAT', {'default': 0.0, 'min': 0, 'max': 1, 'step': 0.05})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'prep_image'
    CATEGORY = 'ipadapter/utils'

    def prep_image(self, image, interpolation='LANCZOS', crop_position='center', sharpening=0.0):
        size = (224, 224)
        (_, oh, ow, _) = image.shape
        output = image.permute([0, 3, 1, 2])
        if crop_position == 'pad':
            if oh != ow:
                if oh > ow:
                    pad = (oh - ow) // 2
                    pad = (pad, 0, pad, 0)
                elif ow > oh:
                    pad = (ow - oh) // 2
                    pad = (0, pad, 0, pad)
                output = T.functional.pad(output, pad, fill=0)
        else:
            crop_size = min(oh, ow)
            x = (ow - crop_size) // 2
            y = (oh - crop_size) // 2
            if 'top' in crop_position:
                y = 0
            elif 'bottom' in crop_position:
                y = oh - crop_size
            elif 'left' in crop_position:
                x = 0
            elif 'right' in crop_position:
                x = ow - crop_size
            x2 = x + crop_size
            y2 = y + crop_size
            output = output[:, :, y:y2, x:x2]
        imgs = []
        for img in output:
            img = T.ToPILImage()(img)
            img = img.resize(size, resample=Image.Resampling[interpolation])
            imgs.append(T.ToTensor()(img))
        output = torch.stack(imgs, dim=0)
        del imgs, img
        if sharpening > 0:
            output = contrast_adaptive_sharpening(output, sharpening)
        output = output.permute([0, 2, 3, 1])
        return (output,)
```