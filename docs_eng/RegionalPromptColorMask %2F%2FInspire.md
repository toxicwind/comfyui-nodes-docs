# Documentation
- Class name: RegionalPromptColorMask
- Category: InspirePack/Regional
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Inspire-Pack.git

The RegionalPromptColorMask node is designed to generate area tips and masks based on colour input, and then uses these tips and masks to refine the details of a particular area in the image. The node enhances the image by applying the area mask to allow targeted details and clarity improvements within the specified colour area.

# Input types
## Required
- basic_pipe
    - The basic_pipe parameter is essential for the node and carries the necessary components for image processing, including models, clips, VAE and condition information. It is the basis for the process of regional fine-tuning.
    - Comfy dtype: BASIC_PIPE
    - Python dtype: Tuple[model, clip, vae, positive, negative]
- color_mask
    - color_mask input is a key element in the visual context, which is used by nodes to identify the coloured areas that need to be enhanced. It is used to create a mask for processing these particular areas.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- mask_color
    - The mask_color parameter is a string that indicates the colour value of the RGB mask. It is important because it determines which color areas in the image will be targeted for fine-tuning.
    - Comfy dtype: STRING
    - Python dtype: str
- cfg
    - The cfg parameter is a floating point value used to adjust the configuration of the node to affect the intensity and focus of regional detail.
    - Comfy dtype: FLOAT
    - Python dtype: float
- sampler_name
    - The sampler_name input of the sampling method to be used is essential for determining the strategy and efficiency of the regional sampling process.
    - Comfy dtype: SAMPLERS
    - Python dtype: str
- scheduler
    - The Scheduler parameter defines the node movement strategy, which is essential for managing the iterative process and achieving the best results.
    - Comfy dtype: SCHEDULERS
    - Python dtype: str
## Optional
- wildcard_prompt
    - Wildcard_prompt is a dynamic text input that allows for the inclusion of variable elements in the reminder, increasing the flexibility and adaptability of the regionalization process.
    - Comfy dtype: STRING
    - Python dtype: str
- controlnet_in_pipe
    - The controlnet_in_pipe parameter is a boolean symbol used to determine whether to maintain or overwrite the existing control settings in the Basic_pipe, affecting overall control over the fine-tuning of the area.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- sigma_factor
    - Sigma_factor is a floating point value used to adjust noise levels during regional sampling to influence the quality and detail of the final output.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- REGIONAL_PROMPTS
    - The output REGIONAL_PROMPTS is a set of tips for the specified colour area, designed to fine-tune and enhance the image according to the input parameters.
    - Comfy dtype: REGIONAL_PROMPTS
    - Python dtype: Dict[str, Any]
- MASK
    - MASK output is a binary mask generated on the basis of input color_mask and mask_color, which is used to isolate and process specific areas in the image.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class RegionalPromptColorMask:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'basic_pipe': ('BASIC_PIPE',), 'color_mask': ('IMAGE',), 'mask_color': ('STRING', {'multiline': False, 'default': '#FFFFFF'}), 'cfg': ('FLOAT', {'default': 8.0, 'min': 0.0, 'max': 100.0}), 'sampler_name': (comfy.samplers.KSampler.SAMPLERS,), 'scheduler': (comfy.samplers.KSampler.SCHEDULERS,), 'wildcard_prompt': ('STRING', {'multiline': True, 'dynamicPrompts': False, 'placeholder': 'wildcard prompt'}), 'controlnet_in_pipe': ('BOOLEAN', {'default': False, 'label_on': 'Keep', 'label_off': 'Override'}), 'sigma_factor': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 10.0, 'step': 0.01})}}
    RETURN_TYPES = ('REGIONAL_PROMPTS', 'MASK')
    FUNCTION = 'doit'
    CATEGORY = 'InspirePack/Regional'

    def doit(self, basic_pipe, color_mask, mask_color, cfg, sampler_name, scheduler, wildcard_prompt, controlnet_in_pipe=False, sigma_factor=1.0):
        mask = color_to_mask(color_mask, mask_color)
        rp = RegionalPromptSimple().doit(basic_pipe, mask, cfg, sampler_name, scheduler, wildcard_prompt, controlnet_in_pipe, sigma_factor=sigma_factor)[0]
        return (rp, mask)
```