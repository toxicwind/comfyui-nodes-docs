# Documentation
- Class name: BatchCropFromMask
- Category: KJNodes/masking
- Output node: False
- Repo Ref: https://github.com/kijai/ComfyUI-KJNodes.git

The MatchCropFromMask node is designed to process a collection of images and their matching masks in order to generate cropped images. It identifies the areas of interest in the images based on the mask, and uses cropping to focus on them. The node also smooths the size and centre of the boundary box to enhance consistency in the different image cropping processes in the batch.

# Input types
## Required
- original_images
    - The orginal_images parameter is essential because it represents a batch of images that will be processed by nodes. This node will be used to combine the images with the available mask to determine the area to be cropped.
    - Comfy dtype: IMAGE
    - Python dtype: List[torch.Tensor]
- masks
    - The masks parameter defines the binary mask that corresponds to the area of interest in the original image. These masks are essential for identifying which parts of the image should be retained after the node is marked.
    - Comfy dtype: MASK
    - Python dtype: List[torch.Tensor]
## Optional
- crop_size_mult
    - The crop_size_mult parameter allows the size of the crop area to be adjusted by multiplying this factor to the size of the boundary box. It provides flexibility in controlling the scope of the crop operation.
    - Comfy dtype: FLOAT
    - Python dtype: float
- bbox_smooth_alpha
    - The bbox_smooth_alpha parameter controls the smoothness of the border frame size between successive images in the batch. It helps to keep the size of the crop consistent, which is important for batch processing.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- original_images
    - The original_images output contains the original image batch that is entered into the node, unaltered and exists in its original form.
    - Comfy dtype: IMAGE
    - Python dtype: List[torch.Tensor]
- cropped_images
    - Cropped_images output provides a batch of images that are cropped according to the area identified by the corresponding mask.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- bboxes
    - The bboxes output includes the boundary box used to determine the area of each image in the batch.
    - Comfy dtype: BBOX
    - Python dtype: List[Tuple[int, int, int, int]]
- width
    - Width output indicates the width of the boundary box that is smooth and multiply processed, indicating the horizontal range of the area to be cropped.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - The header output corresponds to the height of the boundary box that is smooth and multiply processed, indicating the vertical range of the area to be cropped.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class BatchCropFromMask:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'original_images': ('IMAGE',), 'masks': ('MASK',), 'crop_size_mult': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 10.0, 'step': 0.001}), 'bbox_smooth_alpha': ('FLOAT', {'default': 0.5, 'min': 0.0, 'max': 1.0, 'step': 0.01})}}
    RETURN_TYPES = ('IMAGE', 'IMAGE', 'BBOX', 'INT', 'INT')
    RETURN_NAMES = ('original_images', 'cropped_images', 'bboxes', 'width', 'height')
    FUNCTION = 'crop'
    CATEGORY = 'KJNodes/masking'

    def smooth_bbox_size(self, prev_bbox_size, curr_bbox_size, alpha):
        if alpha == 0:
            return prev_bbox_size
        return round(alpha * curr_bbox_size + (1 - alpha) * prev_bbox_size)

    def smooth_center(self, prev_center, curr_center, alpha=0.5):
        if alpha == 0:
            return prev_center
        return (round(alpha * curr_center[0] + (1 - alpha) * prev_center[0]), round(alpha * curr_center[1] + (1 - alpha) * prev_center[1]))

    def crop(self, masks, original_images, crop_size_mult, bbox_smooth_alpha):
        bounding_boxes = []
        cropped_images = []
        self.max_bbox_width = 0
        self.max_bbox_height = 0
        curr_max_bbox_width = 0
        curr_max_bbox_height = 0
        for mask in masks:
            _mask = tensor2pil(mask)[0]
            non_zero_indices = np.nonzero(np.array(_mask))
            (min_x, max_x) = (np.min(non_zero_indices[1]), np.max(non_zero_indices[1]))
            (min_y, max_y) = (np.min(non_zero_indices[0]), np.max(non_zero_indices[0]))
            width = max_x - min_x
            height = max_y - min_y
            curr_max_bbox_width = max(curr_max_bbox_width, width)
            curr_max_bbox_height = max(curr_max_bbox_height, height)
        self.max_bbox_width = self.smooth_bbox_size(self.max_bbox_width, curr_max_bbox_width, bbox_smooth_alpha)
        self.max_bbox_height = self.smooth_bbox_size(self.max_bbox_height, curr_max_bbox_height, bbox_smooth_alpha)
        self.max_bbox_width = round(self.max_bbox_width * crop_size_mult)
        self.max_bbox_height = round(self.max_bbox_height * crop_size_mult)
        bbox_aspect_ratio = self.max_bbox_width / self.max_bbox_height
        for (i, (mask, img)) in enumerate(zip(masks, original_images)):
            _mask = tensor2pil(mask)[0]
            non_zero_indices = np.nonzero(np.array(_mask))
            (min_x, max_x) = (np.min(non_zero_indices[1]), np.max(non_zero_indices[1]))
            (min_y, max_y) = (np.min(non_zero_indices[0]), np.max(non_zero_indices[0]))
            center_x = np.mean(non_zero_indices[1])
            center_y = np.mean(non_zero_indices[0])
            curr_center = (round(center_x), round(center_y))
            if not hasattr(self, 'prev_center'):
                self.prev_center = curr_center
            if i > 0:
                center = self.smooth_center(self.prev_center, curr_center, bbox_smooth_alpha)
            else:
                center = curr_center
            self.prev_center = center
            half_box_width = round(self.max_bbox_width / 2)
            half_box_height = round(self.max_bbox_height / 2)
            min_x = max(0, center[0] - half_box_width)
            max_x = min(img.shape[1], center[0] + half_box_width)
            min_y = max(0, center[1] - half_box_height)
            max_y = min(img.shape[0], center[1] + half_box_height)
            bounding_boxes.append((min_x, min_y, max_x - min_x, max_y - min_y))
            cropped_img = img[min_y:max_y, min_x:max_x, :]
            new_height = min(cropped_img.shape[0], self.max_bbox_height)
            new_width = round(new_height * bbox_aspect_ratio)
            resize_transform = Resize((new_height, new_width))
            resized_img = resize_transform(cropped_img.permute(2, 0, 1))
            crop_transform = CenterCrop((self.max_bbox_height, self.max_bbox_width))
            cropped_resized_img = crop_transform(resized_img)
            cropped_images.append(cropped_resized_img.permute(1, 2, 0))
        cropped_out = torch.stack(cropped_images, dim=0)
        return (original_images, cropped_out, bounding_boxes, self.max_bbox_width, self.max_bbox_height)
```