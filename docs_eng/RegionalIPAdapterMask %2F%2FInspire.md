# Documentation
- Class name: RegionalIPAdapterMask
- Category: InspirePack/Regional
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Inspire-Pack.git

The RegionalIPAdapterMask node is designed to adapt and process regional image data by applying masking and various conditional parameters. It facilitates the modification of image effects in a given region without changing the entire data set and enhancing control over image conversion and adaptation.

# Input types
## Required
- mask
    - The mask parameter is essential to define the areas in which the node will focus on the image. It determines which parts of the image will be affected by node processing, making targeted modifications and enhancements possible.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor
- image
    - The image parameter is necessary because it provides the basic input for node operations. It is the raw data to be processed by the node, applying regional adaptation and enhancement based on mask and other parameters.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image or torch.Tensor
- weight
    - The weight parameter affects the intensity of the node processing. It adjusts the intensity of the application of the area to the image, allowing for fine-tuning of the output according to the desired effect.
    - Comfy dtype: FLOAT
    - Python dtype: float
- noise
    - Noise is an important parameter that introduces variability in node processing. It adds a degree of randomity to regional adaptation, which helps to create more natural or diversified output changes.
    - Comfy dtype: FLOAT
    - Python dtype: float
- weight_type
    - The weight type parameter determines how the weight is applied to the image. It can be primary, linear or routed, and each method affects the distribution and impact of the weight in the image, thereby changing the end result.
    - Comfy dtype: COMBO
    - Python dtype: str
- start_at
    - Start_at defines the range of node treatments to begin. It is a floating point value that sets the starting point for weight applications and allows controlled transitions in regional adaptation.
    - Comfy dtype: FLOAT
    - Python dtype: float
- end_at
    - End_at marks the end of the range of node treatments. Like start_at, it is a floating point value that sets the end point for weight applications and ensures a smooth and gradual transition to regional adaptation.
    - Comfy dtype: FLOAT
    - Python dtype: float
- unfold_batch
    - Expands batches, which, when enabled, change the way nodes process image data. It improves the efficiency of node operations, especially when processing large batches of images.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
## Optional
- faceid_v2
    - When the faceid_v2 parameter is enabled, the additional facial recognition function is activated within the node. This enhances the ability of the node to process and adapt to a particular facial area in the image.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- weight_v2
    - Weight_v2 is an advanced parameter that allows further customization of weight applications. It provides an additional layer of control to fine-tune the area.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- output
    - The output of the RegionalIPAdapter Mask node is an adapted image, which is treated regionally according to input parameters. The output is ready for further use or analysis, and the regional adaptation and enhancement is fully integrated into the final outcome.
    - Comfy dtype: REGIONAL_IPADAPTER
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class RegionalIPAdapterMask:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'mask': ('MASK',), 'image': ('IMAGE',), 'weight': ('FLOAT', {'default': 0.7, 'min': -1, 'max': 3, 'step': 0.05}), 'noise': ('FLOAT', {'default': 0.5, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'weight_type': (['original', 'linear', 'channel penalty'],), 'start_at': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1.0, 'step': 0.001}), 'end_at': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.001}), 'unfold_batch': ('BOOLEAN', {'default': False})}, 'optional': {'faceid_v2': ('BOOLEAN', {'default': False}), 'weight_v2': ('FLOAT', {'default': 1.0, 'min': -1, 'max': 3, 'step': 0.05})}}
    RETURN_TYPES = ('REGIONAL_IPADAPTER',)
    FUNCTION = 'doit'
    CATEGORY = 'InspirePack/Regional'

    def doit(self, mask, image, weight, noise, weight_type, start_at=0.0, end_at=1.0, unfold_batch=False, faceid_v2=False, weight_v2=False):
        cond = IPAdapterConditioning(mask, weight, weight_type, noise=noise, image=image, start_at=start_at, end_at=end_at, unfold_batch=unfold_batch, faceid_v2=faceid_v2, weight_v2=weight_v2)
        return (cond,)
```