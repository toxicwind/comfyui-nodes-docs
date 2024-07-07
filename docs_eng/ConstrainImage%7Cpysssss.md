# Constrain Image 🐍
## Documentation
- Class name: ConstrainImage|pysssss
- Category: image
- Output node: False
- Repo Ref: https://github.com/pythongosssss/ComfyUI-Custom-Scripts

This node is intended to adjust the size of the image to the maximum and minimum size specified, while maintaining the vertical ratio of the image. If the image exceeds the maximum size, it can selectively crop the image.

## Input types
### Required
- images
    - Images that you want to bind. This parameter is vital because it directly affects the core function of the node, i.e. to resize and potentially crop the image to meet the size constraints specified.
    - Comfy dtype: IMAGE
    - Python dtype: List[Image]
- max_width
    - Specifies the maximum width that the image can have after processing. It plays a key role in determining whether and how the image needs to be resized.
    - Comfy dtype: INT
    - Python dtype: int
- max_height
    - Defines the maximum height that the image can have after processing, influencing the resize logic to ensure that the image is suitable for the specified size.
    - Comfy dtype: INT
    - Python dtype: int
- min_width
    - Sets the minimum width that the image should have, ensuring that the image is not adjusted below this width.
    - Comfy dtype: INT
    - Python dtype: int
- min_height
    - Determines the minimum height that the image should have and prevents the image from being adjusted below this altitude.
    - Comfy dtype: INT
    - Python dtype: int
- crop_if_required
    - A sign indicating whether, if the image exceeds the maximum size, the image should be cropped to affect the final output that may change the image's configuration.
    - Comfy dtype: COMBO[STRING]
    - Python dtype: bool

## Output types
- image
    - Comfy dtype: IMAGE
    - Processed images, resize and, if necessary, crop to adapt to the specified constraints.
    - Python dtype: List[Image]

## Usage tips
- Infra type: CPU
- Common nodes: unknown

## Source code
```python
class ConstrainImage:
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
    FUNCTION = "constrain_image"
    CATEGORY = "image"
    OUTPUT_IS_LIST = (True,)

    def constrain_image(self, images, max_width, max_height, min_width, min_height, crop_if_required):
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

        return (results,)