# Documentation
- Class name: SEGSPaste
- Category: ImpactPack/Detailer
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The SEGSPaste node is designed to integrate the fragments in the split image into the given image and enhance the visual detail of the image. It ensures seamless and detailed results by matching and mixing the segments with the specified plume and alpha values.

# Input types
## Required
- image
    - Enter the image, which will be pasted to the image. It serves as the basis for the whole operation, and the segment will be aligned and mixed with the image.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- segs
    - Contains split data on the segments that you want to paste to the image. Each segment is essential to the detail enhancement process and contributes to the final visual output.
    - Comfy dtype: SEGS
    - Python dtype: List[SEG]
## Optional
- feather
    - The plume parameter controls the softness of the edges when pasting the fragments. It is an important factor in the natural mixing of the fragments and the images.
    - Comfy dtype: INT
    - Python dtype: int
- alpha
    - The alpha parameter adjusts the opacity of the paste fragments to allow control of the visibility and mixing strength with the bottom image.
    - Comfy dtype: INT
    - Python dtype: int
- ref_image_opt
    - An optional reference image provides an additional context for pasting the segments. It can be used to match the light or colour of the segments with the reference images.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Output types
- result
    - The output is an enhanced image, and the fragments from the split drawings are seamlessly integrated. It represents the final visual result of the process of detail enhancement.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class SEGSPaste:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'segs': ('SEGS',), 'feather': ('INT', {'default': 5, 'min': 0, 'max': 100, 'step': 1}), 'alpha': ('INT', {'default': 255, 'min': 0, 'max': 255, 'step': 1})}, 'optional': {'ref_image_opt': ('IMAGE',)}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Detailer'

    @staticmethod
    def doit(image, segs, feather, alpha=255, ref_image_opt=None):
        segs = core.segs_scale_match(segs, image.shape)
        result = None
        for (i, single_image) in enumerate(image):
            image_i = single_image.unsqueeze(0).clone()
            for seg in segs[1]:
                ref_image = None
                if ref_image_opt is None and seg.cropped_image is not None:
                    cropped_image = seg.cropped_image
                    if isinstance(cropped_image, np.ndarray):
                        cropped_image = torch.from_numpy(cropped_image)
                    ref_image = cropped_image[i].unsqueeze(0)
                elif ref_image_opt is not None:
                    ref_tensor = ref_image_opt[i].unsqueeze(0)
                    ref_image = crop_image(ref_tensor, seg.crop_region)
                if ref_image is not None:
                    if seg.cropped_mask.ndim == 3 and len(seg.cropped_mask) == len(image):
                        mask = seg.cropped_mask[i]
                    elif seg.cropped_mask.ndim == 3 and len(seg.cropped_mask) > 1:
                        print(f'[Impact Pack] WARN: SEGSPaste - The number of the mask batch({len(seg.cropped_mask)}) and the image batch({len(image)}) are different. Combine the mask frames and apply.')
                        combined_mask = (seg.cropped_mask[0] * 255).to(torch.uint8)
                        for frame_mask in seg.cropped_mask[1:]:
                            combined_mask |= (frame_mask * 255).to(torch.uint8)
                        combined_mask = (combined_mask / 255.0).to(torch.float32)
                        mask = utils.to_binary_mask(combined_mask, 0.1)
                    else:
                        mask = seg.cropped_mask
                    mask = tensor_gaussian_blur_mask(mask, feather) * (alpha / 255)
                    (x, y, *_) = seg.crop_region
                    mask.cpu()
                    image_i.cpu()
                    ref_image.cpu()
                    tensor_paste(image_i, ref_image, (x, y), mask)
            if result is None:
                result = image_i
            else:
                result = torch.concat((result, image_i), dim=0)
        return (result,)
```