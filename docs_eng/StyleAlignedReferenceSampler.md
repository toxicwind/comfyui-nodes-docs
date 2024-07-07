# Documentation
- Class name: StyleAlignedReferenceSampler
- Category: style_aligned
- Output node: False
- Repo Ref: https://github.com/brianfitzgerald/style_aligned_comfy

The StyleAlignedReferenceSampler class aims to promote potential spatial sampling for style alignment and to ensure that the content generated follows a particular style reference. It combines attention mechanisms and normative techniques to refine output and provides a detailed method for creating style alignment in models.

# Input types
## Required
- model
    - Model parameters are essential because they define the basic structure and parameters of the production model to be used for style alignment sampling. They are the basis for style alignment and sampling process construction.
    - Comfy dtype: MODEL
    - Python dtype: ModelPatcher
- share_norm
    - The share_norm parameter determines how the normative layer is shared between different layers or groups in the model, which has a significant impact on the style alignment process by controlling the flow of information.
    - Comfy dtype: SHARE_NORM_OPTIONS
    - Python dtype: str
- share_attn
    - Share_attn parameters determine the strategy for sharing attention mechanisms in the model, which is essential to align content generation with desired styles by influencing the weight of attention.
    - Comfy dtype: SHARE_ATTN_OPTIONS
    - Python dtype: str
- scale
    - The impact of the scale parameter adjustment style reference on the generation of the sample allows fine-tuned style alignment to achieve the desired aesthetic results.
    - Comfy dtype: FLOAT
    - Python dtype: float
- batch_size
    - Match_size determines the number of samples to be processed simultaneously, which affects the efficiency and speed of the style alignment sampling process.
    - Comfy dtype: INT
    - Python dtype: int
- noise_seed
    - Noise_seed is used to generate noise vectors during sampling to ensure that symmetrical samples can be replicated consistently.
    - Comfy dtype: INT
    - Python dtype: int
- cfg
    - The cfg parameter influences the configuration of the sampling process, in particular how the model responds to condition input, which is essential for achieving accurate style alignment.
    - Comfy dtype: FLOAT
    - Python dtype: float
- positive
    - Positive condition input is essential to guide the model towards desired style features as a reference for the style alignment process.
    - Comfy dtype: CONDITIONING
    - Python dtype: T
- negative
    - Negative condition input helps refine model output by specifying undesired features to be avoided and improves the accuracy of style alignment.
    - Comfy dtype: CONDITIONING
    - Python dtype: T
- ref_positive
    - The ref_positive condition input provides an additional style reference layer to further ensure that the samples generated are closely matched to the target style.
    - Comfy dtype: CONDITIONING
    - Python dtype: T
- sampler
    - Sampler parameters define sampling strategies, which are critical to the diversity and quality of style-tailored output.
    - Comfy dtype: SAMPLER
    - Python dtype: T
- sigmas
    - The sigmas parameters are used to control the noise level applied during the sampling process and directly affect the smoothness and consistency of the style alignment samples.
    - Comfy dtype: SIGMAS
    - Python dtype: T
- ref_latents
    - Ref_lates provide a set of potential indications for style alignment to ensure that the output sample follows the desired style details.
    - Comfy dtype: STEP_LATENTS
    - Python dtype: T

# Output types
- output
    - The output parameter contains a potential sample of style alignment generated by the model, which is the main result of the sampling process and can be further processed or analysed.
    - Comfy dtype: LATENT
    - Python dtype: dict
- denoised_output
    - The denoised_output parameters provide a potential refined sample that has been processed to reduce noise and enhance clarity and provide a clearer indication of the target style.
    - Comfy dtype: LATENT
    - Python dtype: dict

# Usage tips
- Infra type: GPU

# Source code
```
class StyleAlignedReferenceSampler:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'model': ('MODEL',), 'share_norm': (SHARE_NORM_OPTIONS,), 'share_attn': (SHARE_ATTN_OPTIONS,), 'scale': ('FLOAT', {'default': 1, 'min': 0, 'max': 2.0, 'step': 0.01}), 'batch_size': ('INT', {'default': 2, 'min': 1, 'max': 8, 'step': 1}), 'noise_seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615}), 'cfg': ('FLOAT', {'default': 8.0, 'min': 0.0, 'max': 100.0, 'step': 0.1, 'round': 0.01}), 'positive': ('CONDITIONING',), 'negative': ('CONDITIONING',), 'ref_positive': ('CONDITIONING',), 'sampler': ('SAMPLER',), 'sigmas': ('SIGMAS',), 'ref_latents': ('STEP_LATENTS',)}}
    RETURN_TYPES = ('LATENT', 'LATENT')
    RETURN_NAMES = ('output', 'denoised_output')
    FUNCTION = 'patch'
    CATEGORY = 'style_aligned'

    def patch(self, model: ModelPatcher, share_norm: str, share_attn: str, scale: float, batch_size: int, noise_seed: int, cfg: float, positive: T, negative: T, ref_positive: T, sampler: T, sigmas: T, ref_latents: T) -> 'tuple[dict, dict]':
        m = model.clone()
        args = StyleAlignedArgs(share_attn)
        style_latent_tensor = ref_latents[0].unsqueeze(0)
        (height, width) = style_latent_tensor.shape[-2:]
        latent_t = torch.zeros([batch_size, 4, height, width], device=ref_latents.device)
        latent = {'samples': latent_t}
        noise = comfy.sample.prepare_noise(latent_t, noise_seed)
        latent_t = torch.cat((style_latent_tensor, latent_t), dim=0)
        ref_noise = torch.zeros_like(noise[0]).unsqueeze(0)
        noise = torch.cat((ref_noise, noise), dim=0)
        x0_output = {}
        preview_callback = latent_preview.prepare_callback(m, sigmas.shape[-1] - 1, x0_output)

        def callback(step: int, x0: T, x: T, steps: int):
            preview_callback(step, x0, x, steps)
            if step + 1 < steps:
                x[0] = ref_latents[step + 1]
                x0[0] = ref_latents[step + 1]
        share_group_norm = share_norm in ['group', 'both']
        share_layer_norm = share_norm in ['layer', 'both']
        register_shared_norm(m, share_group_norm, share_layer_norm)
        m.set_model_attn1_patch(SharedAttentionProcessor(args, scale))
        batched_condition = []
        for (i, condition) in enumerate(positive):
            additional = condition[1].copy()
            batch_with_reference = torch.cat([ref_positive[i][0], condition[0].repeat([batch_size] + [1] * len(condition[0].shape[1:]))], dim=0)
            if 'pooled_output' in additional and 'pooled_output' in ref_positive[i][1]:
                pooled_output = torch.cat([ref_positive[i][1]['pooled_output'], additional['pooled_output'].repeat([batch_size] + [1] * len(additional['pooled_output'].shape[1:]))], dim=0)
                additional['pooled_output'] = pooled_output
            if 'control' in additional:
                if 'control' in ref_positive[i][1]:
                    control_hint = torch.cat([ref_positive[i][1]['control'].cond_hint_original, additional['control'].cond_hint_original.repeat([batch_size] + [1] * len(additional['control'].cond_hint_original.shape[1:]))], dim=0)
                    cloned_controlnet = additional['control'].copy()
                    cloned_controlnet.set_cond_hint(control_hint, strength=additional['control'].strength, timestep_percent_range=additional['control'].timestep_percent_range)
                    additional['control'] = cloned_controlnet
                else:
                    control_hint = torch.cat([torch.zeros_like(additional['control'].cond_hint_original), additional['control'].cond_hint_original.repeat([batch_size] + [1] * len(additional['control'].cond_hint_original.shape[1:]))], dim=0)
                    cloned_controlnet = additional['control'].copy()
                    cloned_controlnet.set_cond_hint(control_hint, strength=additional['control'].strength, timestep_percent_range=additional['control'].timestep_percent_range)
                    additional['control'] = cloned_controlnet
            batched_condition.append([batch_with_reference, additional])
        disable_pbar = not comfy.utils.PROGRESS_BAR_ENABLED
        samples = comfy.sample.sample_custom(m, noise, cfg, sampler, sigmas, batched_condition, negative, latent_t, callback=callback, disable_pbar=disable_pbar, seed=noise_seed)
        samples = samples[1:]
        out = latent.copy()
        out['samples'] = samples
        if 'x0' in x0_output:
            out_denoised = latent.copy()
            x0 = x0_output['x0'][1:]
            out_denoised['samples'] = m.model.process_latent_out(x0.cpu())
        else:
            out_denoised = out
        return (out, out_denoised)
```