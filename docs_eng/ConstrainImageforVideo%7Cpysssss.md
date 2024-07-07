# Constrain Image for Video 🐍
## Documentation
- Class name: ConstrainImageforVideo|pysssss
- Category: image
- Output node: False
- Repo Ref: https://github.com/pythongosssss/ComfyUI-Custom-Scripts

This node is intended to adjust the size of the image to the maximum and minimum size specified, while maintaining the vertical ratio. It provides the option of tailoring the image to meet size constraints if necessary.

## Input types
### Required
- images
    - Images to be processed. They will be adjusted to fit the specified dimensions, while maintaining their vertical ratio.
    - Comfy dtype: IMAGE
    - Python dtype: List[torch.Tensor]
- max_width
    - The maximum width allowed for the image. The width of the image above this value will be adjusted for this width.
    - Comfy dtype: INT
    - Python dtype: int
- max_height
    - The image allows maximum height. Images above this value are adjusted for this height.
    - Comfy dtype: INT
    - Python dtype: int
- min_width
    - The minimum width allowed for the image. Images with a width less than this value will be adjusted for this width.
    - Comfy dtype: INT
    - Python dtype: int
- min_height
    - The minimum altitude allowed for the image. Images with a height less than this value will be adjusted for this height.
    - Comfy dtype: INT
    - Python dtype: int
- crop_if_required
    - Whether to tailor the image when the size is not enough to meet the size constraints.
    - Comfy dtype: COMBO[STRING]
    - Python dtype: bool

## Output types
- IMAGE
    - Comfy dtype: IMAGE
    - Processed images, resize and, if necessary, crop to adjust to the size constraints specified.
    - Python dtype: List[torch.Tensor]

## Usage tips
- Infra type: GPU
- Common nodes: unknown

## Source code
```python
class ConstrainImageforVideo:
    """
    A node that constrains an image to a maximum and minimum size while maintaining aspect ratio.
    """

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "images": ("IMAGE",),
                "max_width": ("INT", {"default": 1024, "min": 0}),
                "max_height": ("INT", {"default": 1024, "min": 0}),
                "min_width": ("INT", {"default": 0, "min": 0}),
                "min_height": ("INT", {"default": 0, "min": 0}),
                "crop_if_required": (["yes", "no"], {"default": "no"}),
            },
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("IMAGE",)
    FUNCTION = "constrain_image_for_video"
    CATEGORY = "image"

    def constrain_image_for_video(self, images, max_width, max_height, min_width, min_height, crop_if_required):
        crop_if_required = crop_if_required == "yes"
        results = []
        for image in images:
            i = 255. * image.cpu().numpy()
            img = Image.fromarray(np.clip(i, 0, 255).astype(np.uint8)).convert("RGB")

            current_width, current_height = img.size
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
            all_images = torch.cat(results, dim=0)

        return (all_images, all_images.size(0),)