# Documentation
- Class name: WAS_Mask_Paste_Region
- Category: WAS Suite/Image/Masking
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Mask_Past_Region node is designed to operate image masks by pasting the cropped area to the base mask. It processes mixing and sharpening to ensure that the pasted area is seamlessly integrated into the original mask. This node is particularly suitable for applications that require precise control over mask changes, such as in image editing or graphic design.

# Input types
## Required
- mask
    - The mask parameter is the key input for the node, which represents the base mask to which the cropped area is pasted. It is essential to determine the final appearance of the output mask.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor
- crop_mask
    - The crop_mask parameter defines the area to be pasted to the base mask. It plays an important role in the overall operation, as it directly affects the content and structure of the result mask.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor
## Optional
- crop_data
    - The crop_data parameter provides information on the size and location of the area to be cropped and pasted. It is optional, but when used it affects the alignment of the paste area with the base mask.
    - Comfy dtype: CROP_DATA
    - Python dtype: Tuple[int, Tuple[int, int, int, int]]
- crop_blending
    - Crop_blending controls the mixing strength of the crop area when it is pasted to the base mask. It allows a fine-tune transition between the area and the surrounding mask.
    - Comfy dtype: FLOAT
    - Python dtype: float
- crop_sharpening
    - The crop_sharping parameter determines the acute level to be applied to the crop area before pasting. It enhances the detail of the pasting area to obtain better visual clarity.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- result_mask
    - The result_mask output parameter is the final mask after pasting. It is a key output because it reflects the manipulation of the original mask and crop area by nodes.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor
- result_crop_mask
    - The result_crop_mask output parameter provides a mask for the area to be pasted after all processing steps. It is important for applications that require separate action to paste the area mask.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Mask_Paste_Region:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'mask': ('MASK',), 'crop_mask': ('MASK',), 'crop_data': ('CROP_DATA',), 'crop_blending': ('FLOAT', {'default': 0.25, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'crop_sharpening': ('INT', {'default': 0, 'min': 0, 'max': 3, 'step': 1})}}
    RETURN_TYPES = ('MASK', 'MASK')
    FUNCTION = 'mask_paste_region'
    CATEGORY = 'WAS Suite/Image/Masking'

    def mask_paste_region(self, mask, crop_mask, crop_data=None, crop_blending=0.25, crop_sharpening=0):
        if crop_data == False:
            cstr('No valid crop data found!').error.print()
            return (pil2mask(Image.new('L', (512, 512), 0)).unsqueeze(0).unsqueeze(1), pil2mask(Image.new('L', (512, 512), 0)).unsqueeze(0).unsqueeze(1))
        mask_pil = Image.fromarray(np.clip(255.0 * mask.cpu().numpy().squeeze(), 0, 255).astype(np.uint8))
        mask_crop_pil = Image.fromarray(np.clip(255.0 * crop_mask.cpu().numpy().squeeze(), 0, 255).astype(np.uint8))
        (result_mask, result_crop_mask) = self.paste_image(mask_pil, mask_crop_pil, crop_data, crop_blending, crop_sharpening)
        return (pil2mask(result_mask).unsqueeze(0).unsqueeze(1), pil2mask(result_crop_mask).unsqueeze(0).unsqueeze(1))

    def paste_image(self, image, crop_image, crop_data, blend_amount=0.25, sharpen_amount=1):

        def lingrad(size, direction, white_ratio):
            image = Image.new('RGB', size)
            draw = ImageDraw.Draw(image)
            if direction == 'vertical':
                black_end = int(size[1] * (1 - white_ratio))
                range_start = 0
                range_end = size[1]
                range_step = 1
                for y in range(range_start, range_end, range_step):
                    color_ratio = y / size[1]
                    if y <= black_end:
                        color = (0, 0, 0)
                    else:
                        color_value = int((y - black_end) / (size[1] - black_end) * 255)
                        color = (color_value, color_value, color_value)
                    draw.line([(0, y), (size[0], y)], fill=color)
            elif direction == 'horizontal':
                black_end = int(size[0] * (1 - white_ratio))
                range_start = 0
                range_end = size[0]
                range_step = 1
                for x in range(range_start, range_end, range_step):
                    color_ratio = x / size[0]
                    if x <= black_end:
                        color = (0, 0, 0)
                    else:
                        color_value = int((x - black_end) / (size[0] - black_end) * 255)
                        color = (color_value, color_value, color_value)
                    draw.line([(x, 0), (x, size[1])], fill=color)
            return image.convert('L')
        (crop_size, (left, top, right, bottom)) = crop_data
        crop_image = crop_image.resize(crop_size)
        if sharpen_amount > 0:
            for _ in range(int(sharpen_amount)):
                crop_image = crop_image.filter(ImageFilter.SHARPEN)
        blended_image = Image.new('RGBA', image.size, (0, 0, 0, 255))
        blended_mask = Image.new('L', image.size, 0)
        crop_padded = Image.new('RGBA', image.size, (0, 0, 0, 0))
        blended_image.paste(image, (0, 0))
        crop_padded.paste(crop_image, (left, top))
        crop_mask = Image.new('L', crop_image.size, 0)
        if top > 0:
            gradient_image = ImageOps.flip(lingrad(crop_image.size, 'vertical', blend_amount))
            crop_mask = ImageChops.screen(crop_mask, gradient_image)
        if left > 0:
            gradient_image = ImageOps.mirror(lingrad(crop_image.size, 'horizontal', blend_amount))
            crop_mask = ImageChops.screen(crop_mask, gradient_image)
        if right < image.width:
            gradient_image = lingrad(crop_image.size, 'horizontal', blend_amount)
            crop_mask = ImageChops.screen(crop_mask, gradient_image)
        if bottom < image.height:
            gradient_image = lingrad(crop_image.size, 'vertical', blend_amount)
            crop_mask = ImageChops.screen(crop_mask, gradient_image)
        crop_mask = ImageOps.invert(crop_mask)
        blended_mask.paste(crop_mask, (left, top))
        blended_mask = blended_mask.convert('L')
        blended_image.paste(crop_padded, (0, 0), blended_mask)
        return (ImageOps.invert(blended_image.convert('RGB')).convert('L'), ImageOps.invert(blended_mask.convert('RGB')).convert('L'))
```