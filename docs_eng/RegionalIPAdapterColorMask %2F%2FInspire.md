# Documentation
- Class name: RegionalIPAdapterColorMask
- Category: InspirePack/Regional
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Inspire-Pack.git

The RegionalIPAdapterColorMask node is designed to apply colour masks to images, which can be used to concentrate the generation process in a particular area of interest. Using the power of the IPAdapter model, it is conditional on generation according to the provided mask, enhances control over visual output, and ensures closer compliance with the designated colour area.

# Input types
## Required
- color_mask
    - The color_mask parameter is essential, and it defines the image that will be used to generate the mask. The image is processed to create a binary mask that will be used to generate and ensure that the specified colour area is emphasized in the output.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- mask_color
    - The mask_color parameter is essential for determining the specific colour used to create the mask. It is a string that represents the RGB formatted colour value and is used to identify and isolate the target colour range within the image.
    - Comfy dtype: STRING
    - Python dtype: str
- image
    - The image parameter is the input image processed by the node. It is a canvas with a colour mask, the contents of which will be influenced by the mask to achieve the desired visual effect.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- weight
    - Weight parameters adjust the impact of the mask. Higher weights mean that the impact of the mask is more pronounced, while lower weights reduce its effects and allow for a more subtle integration of the coloured areas into the final output.
    - Comfy dtype: FLOAT
    - Python dtype: float
- noise
    - The noise parameter introduces a certain amount of randomity in the generation process. By adjusting this parameter, the user can control the level of change and unpredictability in the result image, adding creativity and diversity to the output.
    - Comfy dtype: FLOAT
    - Python dtype: float
- weight_type
    - Weight_type parameters allow users to choose how to apply the weight to the mask. Different weight types can change the way the mask affects the generation and provide a range of creative control options to achieve the desired aesthetics.
    - Comfy dtype: COMBO
    - Python dtype: str
- start_at
    - The start_at parameter defines the starting point for the effect of the mask. It helps to control the gradual introduction of the mask effect and allows for a more detailed and controlled application of the colour mask in the final output.
    - Comfy dtype: FLOAT
    - Python dtype: float
- end_at
    - The end_at parameter sets the mask to the point where the impact reaches its peak. It works with the start_at parameter to create a smooth transition of mask effect throughout the generation process.
    - Comfy dtype: FLOAT
    - Python dtype: float
- unfold_batch
    - The unfold_batch parameter determines whether the batch dimension should be extended during the application of the mask. This is very useful for some types of generation, and individual elements in the batch need a unique mask application.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
## Optional
- faceid_v2
    - Faceid_v2 parameters enable advanced facial detection and recognition systems that can fine-tune mask applications and focus more accurately on facial features in images.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- weight_v2
    - The weight_v2 parameter is the extra weight control of the Facaid_v2 characteristic, which allows fine-tuning of facial mask applications to achieve more precise and detailed facial characteristics.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- REGIONAL_IPADAPTER
    - Regional_ipadapter output is a conditional model adjusted to your input mask and colour. It is prepared to be used during subsequent generation, and the mask's effects are incorporated to guide the creation of the desired visual elements.
    - Comfy dtype: REGIONAL_IPADAPTER
    - Python dtype: object
- MASK
    - The MASK output is a binary mask created from the input color_mask and mask_color. This mask can be used for further processing or as a reference for the image range to which the colour mask is directed.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class RegionalIPAdapterColorMask:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'color_mask': ('IMAGE',), 'mask_color': ('STRING', {'multiline': False, 'default': '#FFFFFF'}), 'image': ('IMAGE',), 'weight': ('FLOAT', {'default': 0.7, 'min': -1, 'max': 3, 'step': 0.05}), 'noise': ('FLOAT', {'default': 0.5, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'weight_type': (['original', 'linear', 'channel penalty'],), 'start_at': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1.0, 'step': 0.001}), 'end_at': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.001}), 'unfold_batch': ('BOOLEAN', {'default': False})}, 'optional': {'faceid_v2': ('BOOLEAN', {'default': False}), 'weight_v2': ('FLOAT', {'default': 1.0, 'min': -1, 'max': 3, 'step': 0.05})}}
    RETURN_TYPES = ('REGIONAL_IPADAPTER', 'MASK')
    FUNCTION = 'doit'
    CATEGORY = 'InspirePack/Regional'

    def doit(self, color_mask, mask_color, image, weight, noise, weight_type, start_at=0.0, end_at=1.0, unfold_batch=False, faceid_v2=False, weight_v2=False):
        mask = color_to_mask(color_mask, mask_color)
        cond = IPAdapterConditioning(mask, weight, weight_type, noise=noise, image=image, start_at=start_at, end_at=end_at, unfold_batch=unfold_batch, faceid_v2=faceid_v2, weight_v2=weight_v2)
        return (cond, mask)
```