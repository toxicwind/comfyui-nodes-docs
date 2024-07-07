# Documentation
- Class name: ConstrainImage
- Category: image
- Output node: False
- Repo Ref: https://github.com/esheep/esheep_custom_nodes.git

The node is designed to adjust the size of the image to the specified boundary while maintaining the vertical ratio of the image. It operates by zooming the image to the nearest maximum and minimum dimensions and, if necessary, cropping the image to ensure that it is well suited to defined constraints.

# Input types
## Required
- images
    - The image parameter is necessary because it provides the input image that will be bound. It directly influences the operation of the node by identifying the data that will be processed and converted.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- max_width
    - The maximum width parameter sets a ceiling on the image's post-transformation width. It plays a vital role in ensuring that the image remains within the desired size, thereby maintaining the expected horizontal and vertical ratio.
    - Comfy dtype: INT
    - Python dtype: int
- max_height
    - Similar to the maximum width, the maximum height parameter sets the upper limit of the image height. It is essential to ensure that the vertical dimensions of the image are properly bound during the transformation process.
    - Comfy dtype: INT
    - Python dtype: int
- min_width
    - The minimum width parameter ensures that the image does not shrink below a threshold, which is important to preserve the integrity of the image and prevent it from becoming too small to be effectively viewed or analysed.
    - Comfy dtype: INT
    - Python dtype: int
- min_height
    - The minimum height parameter is used to maintain a baseline of image height and to ensure that the image remains visible and readable even when it is scaled to suit the specified constraints.
    - Comfy dtype: INT
    - Python dtype: int
- crop_if_required
    - If necessary, the crop_if_required parameter is a decision point for determining whether, after scaling, the image should be cropped if it does not meet the specified constraints. This option affects the final result of the image conversion.
    - Comfy dtype: COMBO
    - Python dtype: str

# Output types
- IMAGE
    - The output image is the result of a constraint process that represents the input image that has been adjusted to fit the specified maximum and minimum dimensions while maintaining its vertical ratio.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class ConstrainImage:
    """
    A node that constrains an image to a maximum and minimum size while maintaining aspect ratio.
    """

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'images': ('IMAGE',), 'max_width': ('INT', {'default': 1024, 'min': 0}), 'max_height': ('INT', {'default': 1024, 'min': 0}), 'min_width': ('INT', {'default': 0, 'min': 0}), 'min_height': ('INT', {'default': 0, 'min': 0}), 'crop_if_required': (['yes', 'no'], {'default': 'no'})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'constrain_image'
    CATEGORY = 'image'
    OUTPUT_IS_LIST = (True,)

    def constrain_image(self, images, max_width, max_height, min_width, min_height, crop_if_required):
        crop_if_required = crop_if_required == 'yes'
        results = []
        for image in images:
            i = 255.0 * image.cpu().numpy()
            img = Image.fromarray(np.clip(i, 0, 255).astype(np.uint8)).convert('RGB')
            (current_width, current_height) = img.size
            aspect_ratio = current_width / current_height
            constrained_width = max(min(current_width, min_width), max_width)
            constrained_height = max(min(current_height, min_height), max_height)
            if constrained_width / constrained_height > aspect_ratio:
                constrained_width = max(int(constrained_height * aspect_ratio), min_width)
                if crop_if_required:
                    constrained_height = int(current_height / (current_width / constrained_width))
            else:
                constrained_height = max(int(constrained_width / aspect_ratio), min_height)
                if crop_if_required:
                    constrained_width = int(current_width / (current_height / constrained_height))
            resized_image = img.resize((constrained_width, constrained_height), Image.LANCZOS)
            if crop_if_required and (constrained_width > max_width or constrained_height > max_height):
                left = max((constrained_width - max_width) // 2, 0)
                top = max((constrained_height - max_height) // 2, 0)
                right = min(constrained_width, max_width) + left
                bottom = min(constrained_height, max_height) + top
                resized_image = resized_image.crop((left, top, right, bottom))
            resized_image = np.array(resized_image).astype(np.float32) / 255.0
            resized_image = torch.from_numpy(resized_image)[None,]
            results.append(resized_image)
        return (results,)
```