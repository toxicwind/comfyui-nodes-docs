# Documentation
- Class name: TwoSamplersForMask
- Category: ImpactPack/Sampler
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The node coordinates the sampling process by integrating two different sampling mechanisms, allowing for the generation of potential indications that meet specific mask criteria. It enhances the ability of models to focus on relevant characteristics and inhibit unwanted information, thus achieving more controlled and targeted sampling results.

# Input types
## Required
- latent_image
    - The potential image is an input expression of the infrastructure and characteristics needed to carry the sampling process. It is essential because it forms the basis for node operations and affects the quality and characteristics of the final output.
    - Comfy dtype: LATENT
    - Python dtype: dict
- base_sampler
    - The basic sampler is an important component that provides the basic sampling capability. It is responsible for the initial generation of potential images and for laying the foundation for further refinement and operation of the mask sampler.
    - Comfy dtype: KSAMPLER
    - Python dtype: KSamplerWrapper or KSamplerAdvancedWrapper
- mask_sampler
    - The mask sampler plays a key role in applying a given mask standard to a potential image. It refines the sampling process by focusing on the required features and containing unrelated ones, thus shaping the final output according to the predefined mask.
    - Comfy dtype: KSAMPLER
    - Python dtype: KSamplerWrapper or KSamplerAdvancedWrapper
- mask
    - The mask parameter is a binary expression that determines which areas of potential images should be retained or discarded. It is an integral part of node operations, as it guides the mask sampler to determine which features should be taken into account and which ones should be ignored.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Output types
- latent_image
    - The output of a potential image is a refined expression that combines the results of the base and mask sampler. It contains the required features according to the mask and suppresses unrelated features as the final input for subsequent model operations.
    - Comfy dtype: LATENT
    - Python dtype: dict

# Usage tips
- Infra type: GPU

# Source code
```
class TwoSamplersForMask:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'latent_image': ('LATENT',), 'base_sampler': ('KSAMPLER',), 'mask_sampler': ('KSAMPLER',), 'mask': ('MASK',)}}
    RETURN_TYPES = ('LATENT',)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Sampler'

    def doit(self, latent_image, base_sampler, mask_sampler, mask):
        inv_mask = torch.where(mask != 1.0, torch.tensor(1.0), torch.tensor(0.0))
        latent_image['noise_mask'] = inv_mask
        new_latent_image = base_sampler.sample(latent_image)
        new_latent_image['noise_mask'] = mask
        new_latent_image = mask_sampler.sample(new_latent_image)
        del new_latent_image['noise_mask']
        return (new_latent_image,)
```