# Documentation
- Class name: GaussianBlurMask
- Category: ImpactPack/Util
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

GaussianBlurMask nodes apply Gaussian blurry to input masks, soften their edges and reduce noise. It is designed to enhance the visual quality of masks by smoothing the contour and making them suitable for further processing or display.

# Input types
## Required
- mask
    - Enter the mask is the key parameter for the node, which determines the contents of the image that will be blurred. The size and format of the mask directly influences the way Gaussian fuzzy applications are applied and the ultimate effect on the image.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor or np.ndarray
## Optional
- kernel_size
    - The nuclear size parameter determines the extent of the Gaussian fuzzy effect. It controls the size of the area to calculate the blurry. The larger the value, the clearer the fuzzy effect.
    - Comfy dtype: INT
    - Python dtype: int
- sigma
    - The sigma parameter defines the standard deviation of the Gaussian core, which determines the degree of ambiguity. Higher sigma values lead to stronger fuzzy effects, while lower values lead to more subtle ambiguity.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- blurred_mask
    - The output is a blurry version of the mask, which has been made smoother by Gaussian fuzzy treatment. This output is essential for applications that require fine shades on the edges of the mask.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class GaussianBlurMask:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'mask': ('MASK',), 'kernel_size': ('INT', {'default': 10, 'min': 0, 'max': 100, 'step': 1}), 'sigma': ('FLOAT', {'default': 10.0, 'min': 0.1, 'max': 100.0, 'step': 0.1})}}
    RETURN_TYPES = ('MASK',)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Util'

    def doit(self, mask, kernel_size, sigma):
        mask = make_3d_mask(mask)
        mask = torch.unsqueeze(mask, dim=-1)
        mask = utils.tensor_gaussian_blur_mask(mask, kernel_size, sigma)
        mask = torch.squeeze(mask, dim=-1)
        return (mask,)
```