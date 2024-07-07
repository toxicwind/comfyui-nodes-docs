# Documentation
- Class name: RegionalIPAdapterEncodedColorMask
- Category: InspirePack/Regional
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Inspire-Pack.git

The node applies the colour mask to the image and encodes it for use in the IPAdapter model. It allows precision control over the application of the mask so that users can focus on the particular area of the image and condition the process during its generation.

# Input types
## Required
- color_mask
    - Enter the image that will be used as a colour mask. This image is the basis for regional conditionality during the process.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- mask_color
    - to define the colour value of the mask. This parameter is important because it determines which parts of the input image will be highlighted or ignored during the conditionality process.
    - Comfy dtype: STRING
    - Python dtype: str
- embeds
    - Embedding vectors add additional context to the model and enhance the conditionality process. These embedded vectors are essential for shaping the final output according to the style of input tips and expectations.
    - Comfy dtype: EMBEDS
    - Python dtype: List[torch.Tensor]
- weight
    - The weight parameter adjustment mask has an effect on the generation. Higher weights lead to stricter adherence to the mask, while lower weights allow for more change.
    - Comfy dtype: FLOAT
    - Python dtype: float
- weight_type
    - This parameter determines the type of weight application, which can significantly change the conditionality effect. It allows for different strategies on how the mask affects the generation of content.
    - Comfy dtype: COMBO
    - Python dtype: str
- start_at
    - It controls the initial impact strength of the mask on the generation process.
    - Comfy dtype: FLOAT
    - Python dtype: float
- end_at
    - The end point of the mask effect is also ranged from 0.0 to 1.0. It determines how the mask's impact on the generation process will gradually diminish until the end.
    - Comfy dtype: FLOAT
    - Python dtype: float
## Optional
- unfold_batch
    - When this option is enabled, the batch application mask is allowed, which is useful for processing multiple images on a single basis.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- REGIONAL_IPADAPTER
    - The output is a regionally conditional IPAdapter object that can be used for subsequent generation steps with coded mask information to guide the model.
    - Comfy dtype: REGIONAL_IPADAPTER
    - Python dtype: IPAdapterConditioning
- MASK
    - A masked image that has been processed and is prepared for use in the generation process. It is a key component for achieving the desired regional effect.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class RegionalIPAdapterEncodedColorMask:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'color_mask': ('IMAGE',), 'mask_color': ('STRING', {'multiline': False, 'default': '#FFFFFF'}), 'embeds': ('EMBEDS',), 'weight': ('FLOAT', {'default': 0.7, 'min': -1, 'max': 3, 'step': 0.05}), 'weight_type': (['original', 'linear', 'channel penalty'],), 'start_at': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1.0, 'step': 0.001}), 'end_at': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.001}), 'unfold_batch': ('BOOLEAN', {'default': False})}}
    RETURN_TYPES = ('REGIONAL_IPADAPTER', 'MASK')
    FUNCTION = 'doit'
    CATEGORY = 'InspirePack/Regional'

    def doit(self, color_mask, mask_color, embeds, weight, weight_type, start_at=0.0, end_at=1.0, unfold_batch=False):
        mask = color_to_mask(color_mask, mask_color)
        cond = IPAdapterConditioning(mask, weight, weight_type, embeds=embeds, start_at=start_at, end_at=end_at, unfold_batch=unfold_batch)
        return (cond, mask)
```