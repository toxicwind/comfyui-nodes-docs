# Documentation
- Class name: WAS_Bounded_Image_Blend
- Category: WAS Suite/Image/Bound
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

Method `bounded_image_blend'is designed to mix source images seamlessly into the target image and to limit them to a specific boundary. By applying mix factors and optional feather effects, it creates smooth transitions between images, ensuring visual consistency.

# Input types
## Required
- target
    - Target image, where the source image will be mixed. As a background to the hybrid operation, it is essential to determine the final appearance of the synthetic image.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- target_bounds
    - Defines the coordinates of the areas in which the internal image of the target image will be mixed. These boundaries are essential for the specified area of interest.
    - Comfy dtype: IMAGE_BOUNDS
    - Python dtype: Tuple[int, int, int, int]
- source
    - is the image that will be commingled to the target. It is the main visual element that will be merged into the target image and within the specified boundary.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
## Optional
- blend_factor
    - A floating point value is used to determine the degree of mixing between source and target images. It affects the transparency of source images within the mixing area.
    - Comfy dtype: FLOAT
    - Python dtype: float
- feathering
    - To create smooth transitions, the higher values will lead to a more gradual mix.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- result_image
    - Outputs an image that represents the mix of source and target images within the specified boundary.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Bounded_Image_Blend:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        return {'required': {'target': ('IMAGE',), 'target_bounds': ('IMAGE_BOUNDS',), 'source': ('IMAGE',), 'blend_factor': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0}), 'feathering': ('INT', {'default': 16, 'min': 0, 'max': 18446744073709551615})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'bounded_image_blend'
    CATEGORY = 'WAS Suite/Image/Bound'

    def bounded_image_blend(self, target, target_bounds, source, blend_factor, feathering):
        target = target.unsqueeze(0) if target.dim() == 3 else target
        source = source.unsqueeze(0) if source.dim() == 3 else source
        tgt_len = 1 if len(target) != len(source) else len(source)
        bounds_len = 1 if len(target_bounds) != len(source) else len(source)
        tgt_arr = [tensor2pil(tgt) for tgt in target[:tgt_len]]
        src_arr = [tensor2pil(src) for src in source]
        result_tensors = []
        for idx in range(len(src_arr)):
            src = src_arr[idx]
            if tgt_len == 1 and idx == 0 or tgt_len > 1:
                tgt = tgt_arr[idx]
            if bounds_len == 1 and idx == 0 or bounds_len > 1:
                (rmin, rmax, cmin, cmax) = target_bounds[idx]
                (height, width) = (rmax - rmin + 1, cmax - cmin + 1)
                if feathering > 0:
                    inner_mask = Image.new('L', (width - 2 * feathering, height - 2 * feathering), 255)
                    inner_mask = ImageOps.expand(inner_mask, border=feathering, fill=0)
                    inner_mask = inner_mask.filter(ImageFilter.GaussianBlur(radius=feathering))
                else:
                    inner_mask = Image.new('L', (width, height), 255)
                inner_mask = inner_mask.point(lambda p: p * blend_factor)
                tgt_mask = Image.new('L', tgt.size, 0)
                tgt_mask.paste(inner_mask, (cmin, rmin))
            src_resized = src.resize((width, height), Image.Resampling.LANCZOS)
            src_positioned = Image.new(tgt.mode, tgt.size)
            src_positioned.paste(src_resized, (cmin, rmin))
            result = Image.composite(src_positioned, tgt, tgt_mask)
            result_tensors.append(pil2tensor(result))
        return (torch.cat(result_tensors, dim=0),)
```