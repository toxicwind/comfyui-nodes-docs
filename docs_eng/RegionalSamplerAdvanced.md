# Documentation
- Class name: RegionalSamplerAdvanced
- Category: ImpactPack/Regional
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The RegionalSamplerAdvanced node is designed to perform advanced sampling operations for specific areas of potential images. It allows custom sampling steps, noise additions and restoration of potential status within defined areas, providing a high degree of control over the sampling process for local image generation.

# Input types
## Required
- add_noise
    - The 'add_noise' parameter determines whether to add noise to potential images during the sampling process. This affects the quality and randomity of the images generated and is a key factor in achieving the required visual effect.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- noise_seed
    - The 'noise_seed 'parameter is used to initialize the random number generator that adds noise to ensure the repeatability of the sampling process. Its value directly affects the noise mode in potential images.
    - Comfy dtype: INT
    - Python dtype: int
- steps
    - The'steps' parameter specifies the number of sampling steps to be performed. It is the key determinant of the final image detail and resolution, and more steps usually lead to more refined results.
    - Comfy dtype: INT
    - Python dtype: int
- start_at_step
    - The'start_at_step' parameter defines the steps to begin the sampling process, allows custom sampling time lines and enables users to control the progress of image generation.
    - Comfy dtype: INT
    - Python dtype: int
- end_at_step
    - The 'end_at_step' parameter sets the steps for the end of the sampling process. It is used in conjunction with'start_at_step', defining the range of steps to perform the sampling and influencing the overall duration of the sampling process.
    - Comfy dtype: INT
    - Python dtype: int
- overlap_factor
    - The 'overlap_factor' parameter controls the degree of overlap between the regional masks during the sampling process. It is essential to ensure seamless integration of the sample area and plays an important role in the final picture of the image.
    - Comfy dtype: INT
    - Python dtype: int
- restore_latent
    - The'restore_latet' parameter indicates whether the potential state should be restored after sampling in each region. This helps to maintain image integrity in multiple areas where sampling operations overlap.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- return_with_leftover_noise
    - The'return_with_leftover_noise' parameter determines whether the final potential image after the sampling process retains any residual noise. This is useful for further processing or analysis of noise properties.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- latent_image
    - The 'latent_image' parameter indicates the initial potential state of the image to be sampled. It is the starting point of the sampling process and is essential for generating the final image.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]
- base_sampler
    - The 'base_sampler' parameter defines the basic sampling method to be used for potential images. It is a key component in determining the algorithm for image generation and affects the overall style and quality of the output.
    - Comfy dtype: KSAMPLER_ADVANCED
    - Python dtype: KSamplerAdvancedWrapper
- regional_prompts
    - The'regional_prompts' parameter contains a combination of hints that define the areas of interest in the sampling. Each hint can influence the sampling process within its assigned area, allowing for detailed control of local image features.
    - Comfy dtype: REGIONAL_PROMPTS
    - Python dtype: List[Any]
- additional_mode
    - The 'additional_mode' parameter specifies the recovery mode to be applied during the sampling process. It determines how additional sampling is integrated with basic sampling, affecting the consistency and detail of the final image.
    - Comfy dtype: COMBO['DISABLE', 'ratio additional', 'ratio between']
    - Python dtype: str
- additional_sampler
    - The 'additional_sampler' parameter selects the type of sampler to be used for extra sampling tasks. An important factor in restoring and fine-tuning image details during the sampling process.
    - Comfy dtype: COMBO['AUTO', 'euler', 'heun', 'heunpp2', 'dpm_2', 'dpm_fast', 'dpmpp_2m', 'ddpm']
    - Python dtype: str
- additional_sigma_ratio
    - The 'additional_sigma_ratio' parameter adjusts the sigma scale for extra sampling to allow fine-tuning of noise levels and their impact on the image generation process.
    - Comfy dtype: FLOAT
    - Python dtype: float
## Optional
- unique_id
    - The 'unique_id'parameter is used in the implementation process for the only internal identification node. It plays a key role in tracking and managing the node state to ensure accurate reporting and coordination within the system.
    - Comfy dtype: UNIQUE_ID
    - Python dtype: str

# Output types
- latent_image
    - The 'latent_image' output is a potential image of the final sample after the application of the RegionalSamplerAdvanced node. It covers the results of the advanced sampling process and reflects the custom noise, steps and regional adjustments made during the execution.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]

# Usage tips
- Infra type: GPU

# Source code
```
class RegionalSamplerAdvanced:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'add_noise': ('BOOLEAN', {'default': True, 'label_on': 'enabled', 'label_off': 'disabled'}), 'noise_seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615}), 'steps': ('INT', {'default': 20, 'min': 1, 'max': 10000}), 'start_at_step': ('INT', {'default': 0, 'min': 0, 'max': 10000}), 'end_at_step': ('INT', {'default': 10000, 'min': 0, 'max': 10000}), 'overlap_factor': ('INT', {'default': 10, 'min': 0, 'max': 10000}), 'restore_latent': ('BOOLEAN', {'default': True, 'label_on': 'enabled', 'label_off': 'disabled'}), 'return_with_leftover_noise': ('BOOLEAN', {'default': False, 'label_on': 'enabled', 'label_off': 'disabled'}), 'latent_image': ('LATENT',), 'base_sampler': ('KSAMPLER_ADVANCED',), 'regional_prompts': ('REGIONAL_PROMPTS',), 'additional_mode': (['DISABLE', 'ratio additional', 'ratio between'], {'default': 'ratio between'}), 'additional_sampler': (['AUTO', 'euler', 'heun', 'heunpp2', 'dpm_2', 'dpm_fast', 'dpmpp_2m', 'ddpm'],), 'additional_sigma_ratio': ('FLOAT', {'default': 0.3, 'min': 0.0, 'max': 1.0, 'step': 0.01})}, 'hidden': {'unique_id': 'UNIQUE_ID'}}
    RETURN_TYPES = ('LATENT',)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Regional'

    def doit(self, add_noise, noise_seed, steps, start_at_step, end_at_step, overlap_factor, restore_latent, return_with_leftover_noise, latent_image, base_sampler, regional_prompts, additional_mode, additional_sampler, additional_sigma_ratio, unique_id):
        if restore_latent:
            latent_compositor = nodes.NODE_CLASS_MAPPINGS['LatentCompositeMasked']()
        else:
            latent_compositor = None
        masks = [regional_prompt.mask.numpy() for regional_prompt in regional_prompts]
        masks = [np.ceil(mask).astype(np.int32) for mask in masks]
        combined_mask = torch.from_numpy(np.bitwise_or.reduce(masks))
        inv_mask = torch.where(combined_mask == 0, torch.tensor(1.0), torch.tensor(0.0))
        region_len = len(regional_prompts)
        end_at_step = min(steps, end_at_step)
        total = (end_at_step - start_at_step) * region_len
        new_latent_image = latent_image.copy()
        base_latent_image = None
        region_masks = {}
        for i in range(start_at_step, end_at_step - 1):
            core.update_node_status(unique_id, f'{start_at_step + i}/{end_at_step} steps  |         ', (i - start_at_step) * region_len / total)
            cur_add_noise = True if i == start_at_step and add_noise else False
            new_latent_image['noise_mask'] = inv_mask
            new_latent_image = base_sampler.sample_advanced(cur_add_noise, noise_seed, steps, new_latent_image, i, i + 1, True, recovery_mode=additional_mode, recovery_sampler=additional_sampler, recovery_sigma_ratio=additional_sigma_ratio)
            if restore_latent:
                del new_latent_image['noise_mask']
                base_latent_image = new_latent_image.copy()
            j = 1
            for regional_prompt in regional_prompts:
                if restore_latent:
                    new_latent_image = base_latent_image.copy()
                core.update_node_status(unique_id, f'{start_at_step + i}/{end_at_step} steps  |  {j}/{region_len}', ((i - start_at_step) * region_len + j) / total)
                if j not in region_masks:
                    region_mask = regional_prompt.get_mask_erosion(overlap_factor).squeeze(0).squeeze(0)
                    region_masks[j] = region_mask
                else:
                    region_mask = region_masks[j]
                new_latent_image['noise_mask'] = region_mask
                new_latent_image = regional_prompt.sampler.sample_advanced(False, noise_seed, steps, new_latent_image, i, i + 1, True, recovery_mode=additional_mode, recovery_sampler=additional_sampler, recovery_sigma_ratio=additional_sigma_ratio)
                if restore_latent:
                    del new_latent_image['noise_mask']
                    base_latent_image = latent_compositor.composite(base_latent_image, new_latent_image, 0, 0, False, region_mask)[0]
                    new_latent_image = base_latent_image
                j += 1
        core.update_node_status(unique_id, f'finalize')
        if base_latent_image is not None:
            new_latent_image = base_latent_image
        else:
            base_latent_image = new_latent_image
        new_latent_image['noise_mask'] = inv_mask
        new_latent_image = base_sampler.sample_advanced(False, noise_seed, steps, new_latent_image, end_at_step - 1, end_at_step, return_with_leftover_noise, recovery_mode=additional_mode, recovery_sampler=additional_sampler, recovery_sigma_ratio=additional_sigma_ratio)
        core.update_node_status(unique_id, f'{end_at_step}/{end_at_step} steps', total)
        core.update_node_status(unique_id, '', None)
        if restore_latent:
            new_latent_image = base_latent_image
        if 'noise_mask' in new_latent_image:
            del new_latent_image['noise_mask']
        return (new_latent_image,)
```