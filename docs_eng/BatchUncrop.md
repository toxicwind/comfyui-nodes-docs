# Documentation
- Class name: BatchUncrop
- Category: KJNodes/masking
- Output node: False
- Repo Ref: https://github.com/kijai/ComfyUI-KJNodes.git

BatchUncrop node is designed to restore the clipped image to its original size and shape. It smartises the cutting process by resizing and mixing the crop area with the original image, taking into account border mixing and zoom factors to ensure seamless integration. This node plays a key role in the data enhancement workflow, with the original context of the image being critical for downstream tasks.

# Input types
## Required
- original_images
    - The original_images parameter is essential because it preserves reference to the image before the crop. This is essential for the node to accurately restore the post-cut image to its original state. This input directly affects the outcome of the cancellation process.
    - Comfy dtype: IMAGE
    - Python dtype: List[Image.Image]
- cropped_images
    - Cropped_images enter the image that represents the one that has been cropped and needs to be restored. It is a key component of the MatchUncrop node, as it provides the source material to cancel the crop operation.
    - Comfy dtype: IMAGE
    - Python dtype: List[Image.Image]
- bboxes
    - The bboxes parameter defines the areas that are cut out in the original image. It is important for nodes to correctly identify and restore these areas during the uncut process.
    - Comfy dtype: BBOX
    - Python dtype: List[Tuple[int, int, int, int]]
## Optional
- border_blending
    - border_blending parameters control the mix effect of the crop and the original image border during the uncuting process. It is important for smooth transition between images.
    - Comfy dtype: FLOAT
    - Python dtype: float
- crop_rescale
    - Crop_rescale adjusts the scale of the crop area before it is pasted back to the original image. It affects the ultimate size of the crop area.
    - Comfy dtype: FLOAT
    - Python dtype: float
- border_top
    - The border_top parameter determines whether to add a border to the top of the image during the uncut process. It helps to restore the image's overall appearance.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- border_bottom
    - The border_bottom parameter specifies whether you should include borders at the bottom of the image when you cancel the crop. It affects the image's ultimate visual effects.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- border_left
    - border_left parameters control whether to add a border to the left side of the image during the uncuting. It is part of the node customizing image border function.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- border_right
    - border_right parameters indicate whether the border should be added to the right side of the image while the crop is being cancelled. This is essential to maintain the aesthetic integrity of the image.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- uncropped_images
    - The uncropped_images output contains the final image after the clipping process is cancelled. It represents the image recovered and the original context remains unchanged for further use or analysis.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class BatchUncrop:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'original_images': ('IMAGE',), 'cropped_images': ('IMAGE',), 'bboxes': ('BBOX',), 'border_blending': ('FLOAT', {'default': 0.25, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'crop_rescale': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 10.0, 'step': 0.01}), 'border_top': ('BOOLEAN', {'default': True}), 'border_bottom': ('BOOLEAN', {'default': True}), 'border_left': ('BOOLEAN', {'default': True}), 'border_right': ('BOOLEAN', {'default': True})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'uncrop'
    CATEGORY = 'KJNodes/masking'

    def uncrop(self, original_images, cropped_images, bboxes, border_blending, crop_rescale, border_top, border_bottom, border_left, border_right):

        def inset_border(image, border_width, border_color, border_top, border_bottom, border_left, border_right):
            draw = ImageDraw.Draw(image)
            (width, height) = image.size
            if border_top:
                draw.rectangle((0, 0, width, border_width), fill=border_color)
            if border_bottom:
                draw.rectangle((0, height - border_width, width, height), fill=border_color)
            if border_left:
                draw.rectangle((0, 0, border_width, height), fill=border_color)
            if border_right:
                draw.rectangle((width - border_width, 0, width, height), fill=border_color)
            return image
        if len(original_images) != len(cropped_images):
            raise ValueError(f'The number of original_images ({len(original_images)}) and cropped_images ({len(cropped_images)}) should be the same')
        if len(bboxes) > len(original_images):
            print(f'Warning: Dropping excess bounding boxes. Expected {len(original_images)}, but got {len(bboxes)}')
            bboxes = bboxes[:len(original_images)]
        elif len(bboxes) < len(original_images):
            raise ValueError('There should be at least as many bboxes as there are original and cropped images')
        input_images = tensor2pil(original_images)
        crop_imgs = tensor2pil(cropped_images)
        out_images = []
        for i in range(len(input_images)):
            img = input_images[i]
            crop = crop_imgs[i]
            bbox = bboxes[i]
            (bb_x, bb_y, bb_width, bb_height) = bbox
            paste_region = bbox_to_region((bb_x, bb_y, bb_width, bb_height), img.size)
            scale_x = crop_rescale
            scale_y = crop_rescale
            paste_region = (round(paste_region[0] * scale_x), round(paste_region[1] * scale_y), round(paste_region[2] * scale_x), round(paste_region[3] * scale_y))
            crop = crop.resize((round(paste_region[2] - paste_region[0]), round(paste_region[3] - paste_region[1])))
            crop_img = crop.convert('RGB')
            if border_blending > 1.0:
                border_blending = 1.0
            elif border_blending < 0.0:
                border_blending = 0.0
            blend_ratio = max(crop_img.size) / 2 * float(border_blending)
            blend = img.convert('RGBA')
            mask = Image.new('L', img.size, 0)
            mask_block = Image.new('L', (paste_region[2] - paste_region[0], paste_region[3] - paste_region[1]), 255)
            mask_block = inset_border(mask_block, round(blend_ratio / 2), 0, border_top, border_bottom, border_left, border_right)
            mask.paste(mask_block, paste_region)
            blend.paste(crop_img, paste_region)
            mask = mask.filter(ImageFilter.BoxBlur(radius=blend_ratio / 4))
            mask = mask.filter(ImageFilter.GaussianBlur(radius=blend_ratio / 4))
            blend.putalpha(mask)
            img = Image.alpha_composite(img.convert('RGBA'), blend)
            out_images.append(img.convert('RGB'))
        return (pil2tensor(out_images),)
```