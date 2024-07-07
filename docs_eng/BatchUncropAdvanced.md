# Documentation
- Class name: BatchUncropAdvanced
- Category: KJNodes/masking
- Output node: False
- Repo Ref: https://github.com/kijai/ComfyUI-KJNodes.git

The CatchUncropAdvanced node is intended to restore the original image to its original state by using boundary frame coordinates and masks to precisely put the clipped image back into the context of the original image. It considers border mixing and zoom factors in order to achieve natural appearances and ensure seamless integration of the cutting parts with the original image.

# Input types
## Required
- original_images
    - The original image is the base canvas, and the cropped image is reinserted. They are essential for maintaining the overall context and structure of the final output.
    - Comfy dtype: IMAGE
    - Python dtype: List[Image.Image]
- cropped_images
    - needs to be restored to the original image. These images carry changes or focusses that will be reintegrated into the original context.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- cropped_masks
    - The mask corresponding to the crop image defines the area of interest that will be reintegrated back into the original image.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor
- combined_crop_mask
    - An optional combination mask could be used as a substitute for a separate crop mask to achieve a unified integration of the crop area.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor
- bboxes
    - The boundary box provides the coordinates of the cropped area in the original image, which is essential for accurate placement.
    - Comfy dtype: BBOX
    - Python dtype: List[Tuple[int, int, int, int]]
- border_blending
    - A floating point value is used to determine the border mixing intensity between the original image and the crop image in order to achieve smooth transition.
    - Comfy dtype: FLOAT
    - Python dtype: float
- crop_rescale
    - Scale factors applied before cropping the image to resize and reinserting the original image.
    - Comfy dtype: FLOAT
    - Python dtype: float
- use_combined_mask
    - A boolean sign indicates whether to use a combination mask instead of a separate crop mask in the uncut operation.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- use_square_mask
    - A Boolean flag, set up and used a square mask instead of the original mask shape during the mixing process.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
## Optional
- combined_bounding_box
    - An optional parameter provides a predefined boundary box with a combination mask that covers each boundary box.
    - Comfy dtype: BBOX
    - Python dtype: Tuple[int, int, int, int]=None

# Output types
- output_images
    - The output of the CatchUncropAdvanced node is the original image, the area of which has been returned to its original position and the image has been restored seamlessly.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class BatchUncropAdvanced:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'original_images': ('IMAGE',), 'cropped_images': ('IMAGE',), 'cropped_masks': ('MASK',), 'combined_crop_mask': ('MASK',), 'bboxes': ('BBOX',), 'border_blending': ('FLOAT', {'default': 0.25, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'crop_rescale': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 10.0, 'step': 0.01}), 'use_combined_mask': ('BOOLEAN', {'default': False}), 'use_square_mask': ('BOOLEAN', {'default': True})}, 'optional': {'combined_bounding_box': ('BBOX', {'default': None})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'uncrop'
    CATEGORY = 'KJNodes/masking'

    def uncrop(self, original_images, cropped_images, cropped_masks, combined_crop_mask, bboxes, border_blending, crop_rescale, use_combined_mask, use_square_mask, combined_bounding_box=None):

        def inset_border(image, border_width=20, border_color=0):
            (width, height) = image.size
            bordered_image = Image.new(image.mode, (width, height), border_color)
            bordered_image.paste(image, (0, 0))
            draw = ImageDraw.Draw(bordered_image)
            draw.rectangle((0, 0, width - 1, height - 1), outline=border_color, width=border_width)
            return bordered_image
        if len(original_images) != len(cropped_images):
            raise ValueError(f'The number of original_images ({len(original_images)}) and cropped_images ({len(cropped_images)}) should be the same')
        if len(bboxes) > len(original_images):
            print(f'Warning: Dropping excess bounding boxes. Expected {len(original_images)}, but got {len(bboxes)}')
            bboxes = bboxes[:len(original_images)]
        elif len(bboxes) < len(original_images):
            raise ValueError('There should be at least as many bboxes as there are original and cropped images')
        crop_imgs = tensor2pil(cropped_images)
        input_images = tensor2pil(original_images)
        out_images = []
        for i in range(len(input_images)):
            img = input_images[i]
            crop = crop_imgs[i]
            bbox = bboxes[i]
            if use_combined_mask:
                (bb_x, bb_y, bb_width, bb_height) = combined_bounding_box[0]
                paste_region = bbox_to_region((bb_x, bb_y, bb_width, bb_height), img.size)
                mask = combined_crop_mask[i]
            else:
                (bb_x, bb_y, bb_width, bb_height) = bbox
                paste_region = bbox_to_region((bb_x, bb_y, bb_width, bb_height), img.size)
                mask = cropped_masks[i]
            scale_x = scale_y = crop_rescale
            paste_region = (round(paste_region[0] * scale_x), round(paste_region[1] * scale_y), round(paste_region[2] * scale_x), round(paste_region[3] * scale_y))
            crop = crop.resize((round(paste_region[2] - paste_region[0]), round(paste_region[3] - paste_region[1])))
            crop_img = crop.convert('RGB')
            if border_blending > 1.0:
                border_blending = 1.0
            elif border_blending < 0.0:
                border_blending = 0.0
            blend_ratio = max(crop_img.size) / 2 * float(border_blending)
            blend = img.convert('RGBA')
            if use_square_mask:
                mask = Image.new('L', img.size, 0)
                mask_block = Image.new('L', (paste_region[2] - paste_region[0], paste_region[3] - paste_region[1]), 255)
                mask_block = inset_border(mask_block, round(blend_ratio / 2), 0)
                mask.paste(mask_block, paste_region)
            else:
                original_mask = tensor2pil(mask)[0]
                original_mask = original_mask.resize((paste_region[2] - paste_region[0], paste_region[3] - paste_region[1]))
                mask = Image.new('L', img.size, 0)
                mask.paste(original_mask, paste_region)
            mask = mask.filter(ImageFilter.BoxBlur(radius=blend_ratio / 4))
            mask = mask.filter(ImageFilter.GaussianBlur(radius=blend_ratio / 4))
            blend.paste(crop_img, paste_region)
            blend.putalpha(mask)
            img = Image.alpha_composite(img.convert('RGBA'), blend)
            out_images.append(img.convert('RGB'))
        return (pil2tensor(out_images),)
```