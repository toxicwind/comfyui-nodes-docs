# Documentation
- Class name: GaussianBlurMaskInSEGS
- Category: ImpactPack/Util
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

Gaussian Blur Mask InSEGS nodes apply Gaussian blurs to the mask parts of each segment of the SEG object list. This operation increases the smoothness of the mask edges, which may be useful for some images that require more diffuse masks to split tasks.

# Input types
## Required
- segs
    - The segs parameter is the list of SEG objects that the node will process. Each SEG object contains image data, masks and other relevant information that is essential for node operations.
    - Comfy dtype: SEGS
    - Python dtype: List[SEG]
- kernel_size
    - The Kernel_size parameter determines the size of the Gaussian fuzzy core. A larger nuclear size can lead to a more obvious fuzzy effect, which can smooth the edge of the mask more dramatically.
    - Comfy dtype: INT
    - Python dtype: int
- sigma
    - The sigma parameter controls the standard deviation of the Gaussian core and affects the blurry range. Higher sigma values create greater ambiguity, while lower values lead to more moderate effects.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- segs
    - Output segs are original SEG objects whose masks have been modified through Gaussian fuzzy operations. This allows follow-up or analysis of smooth mask data.
    - Comfy dtype: SEGS
    - Python dtype: Tuple[List[SEG], List[SEG]]

# Usage tips
- Infra type: GPU

# Source code
```
class GaussianBlurMaskInSEGS:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'segs': ('SEGS',), 'kernel_size': ('INT', {'default': 10, 'min': 0, 'max': 100, 'step': 1}), 'sigma': ('FLOAT', {'default': 10.0, 'min': 0.1, 'max': 100.0, 'step': 0.1})}}
    RETURN_TYPES = ('SEGS',)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Util'

    def doit(self, segs, kernel_size, sigma):
        new_segs = []
        for seg in segs[1]:
            mask = utils.tensor_gaussian_blur_mask(seg.cropped_mask, kernel_size, sigma)
            mask = torch.squeeze(mask, dim=-1).squeeze(0).numpy()
            seg = SEG(seg.cropped_image, mask, seg.confidence, seg.crop_region, seg.bbox, seg.label, seg.control_net_wrapper)
            new_segs.append(seg)
        return ((segs[0], new_segs),)
```