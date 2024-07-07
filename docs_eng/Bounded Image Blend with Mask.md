# Documentation
- Class name: WAS_Bounded_Image_Blend_With_Mask
- Category: WAS Suite/Image/Bound
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The method 'bounded_image_blend_with_mask' is designed to control the mixing process using a mask that mixes the source and target images within the specified boundary. It uses the mix factor intelligently to determine the extent of the mixing and is optional, using the plume effect to smooth the transition between images.

# Input types
## Required
- target
    - The target image is the image where the source image is to be mixed. It is essential for the final output as the basis for the whole hybrid operation.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- target_mask
    - Defines the mask of the area where a mixture occurs in the target image. It plays a key role in determining which parts of the target image are affected by the source image.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor
- target_bounds
    - Specifies the boundary that will occur as a result of mixing within the target image. It is essential to limit the effect of mixing to a given area.
    - Comfy dtype: IMAGE_BOUNDS
    - Python dtype: Tuple[int, int, int, int]
- source
    - Images will be commingled to the target. Their visual content and properties significantly influence the outcome of the mixing process.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
## Optional
- blend_factor
    - Controls the factor of the mixing strength between source and target images. It allows fine-tuning of the mixing effect to achieve the required visual effect.
    - Comfy dtype: FLOAT
    - Python dtype: float
- feathering
    - The plume applied to the mask, which smooths the edges of the mixed area in order to achieve a more natural transition. It improves the aesthetic quality of the mixed images.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- result_image
    - Generates the image after the mixing process, reflecting a combination of visual elements of the source and target images at the specified boundary and mask.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Bounded_Image_Blend_With_Mask:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        return {'required': {'target': ('IMAGE',), 'target_mask': ('MASK',), 'target_bounds': ('IMAGE_BOUNDS',), 'source': ('IMAGE',), 'blend_factor': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0}), 'feathering': ('INT', {'default': 16, 'min': 0, 'max': 18446744073709551615})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'bounded_image_blend_with_mask'
    CATEGORY = 'WAS Suite/Image/Bound'

    def bounded_image_blend_with_mask(self, target, target_mask, target_bounds, source, blend_factor, feathering):
        target = target.unsqueeze(0) if target.dim() == 3 else target
        source = source.unsqueeze(0) if source.dim() == 3 else source
        target_mask = target_mask.unsqueeze(0) if target_mask.dim() == 2 else target_mask
        tgt_mask_len = 1 if len(target_mask) != len(source) else len(source)
        tgt_len = 1 if len(target) != len(source) else len(source)
        bounds_len = 1 if len(target_bounds) != len(source) else len(source)
        tgt_arr = [tensor2pil(tgt) for tgt in target[:tgt_len]]
        src_arr = [tensor2pil(src) for src in source]
        tgt_mask_arr = []
        for m_idx in range(tgt_mask_len):
            np_array = np.clip(target_mask[m_idx].cpu().numpy().squeeze() * 255.0, 0, 255)
            tgt_mask_arr.append(Image.fromarray(np_array.astype(np.uint8), mode='L'))
        result_tensors = []
        for idx in range(len(src_arr)):
            src = src_arr[idx]
            if tgt_len == 1 and idx == 0 or tgt_len > 1:
                tgt = tgt_arr[idx]
            if bounds_len == 1 and idx == 0 or bounds_len > 1:
                (rmin, rmax, cmin, cmax) = target_bounds[idx]
                (height, width) = (rmax - rmin + 1, cmax - cmin + 1)
            if tgt_mask_len == 1 and idx == 0 or tgt_mask_len > 1:
                tgt_mask = tgt_mask_arr[idx]
            if tgt_mask_len == 1 and bounds_len == 1 and (idx == 0) or (tgt_mask_len > 1 or bounds_len > 1):
                if tgt_mask.size != tgt.size:
                    mask_extended_canvas = Image.new('L', tgt.size, 0)
                    mask_extended_canvas.paste(tgt_mask, (cmin, rmin))
                    tgt_mask = mask_extended_canvas
                if feathering > 0:
                    tgt_mask = tgt_mask.filter(ImageFilter.GaussianBlur(radius=feathering))
                tgt_mask = tgt_mask.point(lambda p: p * blend_factor)
            src_resized = src.resize((width, height), Image.Resampling.LANCZOS)
            src_positioned = Image.new(tgt.mode, tgt.size)
            src_positioned.paste(src_resized, (cmin, rmin))
            result = Image.composite(src_positioned, tgt, tgt_mask)
            result_tensors.append(pil2tensor(result))
        return (torch.cat(result_tensors, dim=0),)
```