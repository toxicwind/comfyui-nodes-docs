# Documentation
- Class name: KSamplerSeq
- Category: sampling
- Output node: False
- Repo Ref: https://github.com/WASasquatch/WAS_Extras

The KSamplerSeq node is designed to perform sequential sampling using various seed patterns and condition sequences. It manages the generation of potential samples, with the ability to rotate between positive and negative condition sequences, insert potential samples, and control noise processes. The node ensures a coherent and controlled sampling workflow that can be fine-tuned according to specific creative or analytical purposes.

# Input types
## Required
- model
    - Model parameters are essential for KSamplerSeq nodes, as they define the generation models to be used for sampling. The selection of models significantly influences the quality and style of the samples.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- seed
    - Seed parameters are essential for initializing the random number generation process, ensuring repeatability in sampling operations. It sets a starting point for the seed sequence that is generated.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- seed_mode_seq
    - Seed_mode_seq parameters determine how the seed values in the sample sequence are updated and allow for different sampling strategies such as incremental, diminishing, random selection or fixed seeds.
    - Comfy dtype: COMBO['increment', 'decrement', 'random', 'fixed']
    - Python dtype: str
- alternate_values
    - The alternate_values parameter allows rotation between different seed states during the sampling process, adding variability to the samples generated.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- steps
    - The Steps parameters specify the number of steps to be taken during the sampling process, which directly affects the resolution and details of the generation of the sample.
    - Comfy dtype: INT
    - Python dtype: int
- cfg
    - The cfg parameter, which represents the configuration value, is used to control the authenticity of the sampling process and to balance the details of the generation of the sample with the noise.
    - Comfy dtype: FLOAT
    - Python dtype: float
- sampler_name
    - The sampler_name parameter selects the specific sampling method to be used from among the available samplers to influence the overall behaviour and characteristics of the sampling process.
    - Comfy dtype: comfy.samplers.KSampler.SAMPLERS
    - Python dtype: str
- scheduler
    - Scheduler parameters define noise reduction strategies during sampling, which may affect the smoothness and consistency in the generation of samples.
    - Comfy dtype: comfy.samplers.KSampler.SCHEDULERS
    - Python dtype: str
- sequence_loop_count
    - The factor_loop_count parameter sets the number of turns of sampling sequences and allows multiple samples to be generated in a single operation.
    - Comfy dtype: INT
    - Python dtype: int
- positive_seq
    - The positionive_seq parameter provides a range of positive-condition values that guide the sampling process towards the desired results.
    - Comfy dtype: CONDITIONING_SEQ
    - Python dtype: List[Tuple[int, torch.Tensor, Dict[str, torch.Tensor]]]
- negative_seq
    - Negative_seq parameters provide a range of negative conditionality values that help improve the sampling process by preventing undesirable results.
    - Comfy dtype: CONDITIONING_SEQ
    - Python dtype: List[Tuple[int, torch.Tensor, Dict[str, torch.Tensor]]]
- use_conditioning_slerp
    - The use_convention_slerp parameter enabled the spherical linear plug-in (SLRP) to mix the conditional values, which could lead to a smoother transition between sample states.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- cond_slerp_strength
    - Cond_slerp_strength parameters control the strength of the SLRP operation at the mix conditions value, affecting the range of interstate plugs.
    - Comfy dtype: FLOAT
    - Python dtype: float
- latent_image
    - The latent_image parameter indicates the initial potential state used as the starting point of the sampling process, affecting the direction and characteristics of the sample generation.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]
- use_latent_interpolation
    - The use_latent_interpolation parameter switch application potential plug-in value is between the generation of the sample, which can result in a more consistent sample sequence.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- latent_interpolation_mode
    - The latent_interpolation_mode parameter selects the potential plug-in method to be used, which defines how successive samples are mixed together.
    - Comfy dtype: COMBO['Blend', 'Slerp', 'Cosine Interp']
    - Python dtype: str
- latent_interp_strength
    - The latent_interp_strength parameter adjusts the effect of the potential plug value and determines how a sample can smooth its transition to the next sample in the sequence.
    - Comfy dtype: FLOAT
    - Python dtype: float
- denoise_start
    - The denoise_start parameter sets the initial de-noise intensity, which affects the reduction of noise at the beginning of the sampling process.
    - Comfy dtype: FLOAT
    - Python dtype: float
- denoise_seq
    - The denoise_seq parameter controls the noise intensity in the entire sample sequence and allows for a reduction of noise to be fine-tuned over time.
    - Comfy dtype: FLOAT
    - Python dtype: float
- unsample_latents
    - When unsample_lates parameters are enabled, trigger the process of generating the potential status of the unsampled state, which can introduce more diversity into the sample output.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- samples
    - The samples parameters encapsulate the potential samples generated during the sampling process.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class KSamplerSeq:

    def __init__(self):
        self.previous_seed = None
        self.current_seed = None

    def initialize_seeds(self, initial_seed):
        self.previous_seed = initial_seed
        self.current_seed = initial_seed

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615}), 'seed_mode_seq': (['increment', 'decrement', 'random', 'fixed'],), 'alternate_values': ('BOOLEAN', {'default': True}), 'steps': ('INT', {'default': 20, 'min': 1, 'max': 10000}), 'cfg': ('FLOAT', {'default': 8.0, 'min': 0.0, 'max': 100.0, 'step': 0.5, 'round': 0.01}), 'sampler_name': (comfy.samplers.KSampler.SAMPLERS,), 'scheduler': (comfy.samplers.KSampler.SCHEDULERS,), 'sequence_loop_count': ('INT', {'default': 20, 'min': 1, 'max': 1024, 'step': 1}), 'positive_seq': ('CONDITIONING_SEQ',), 'negative_seq': ('CONDITIONING_SEQ',), 'use_conditioning_slerp': ('BOOLEAN', {'default': False}), 'cond_slerp_strength': ('FLOAT', {'default': 0.5, 'min': 0.0, 'max': 1.0, 'step': 0.001}), 'latent_image': ('LATENT',), 'use_latent_interpolation': ('BOOLEAN', {'default': False}), 'latent_interpolation_mode': (['Blend', 'Slerp', 'Cosine Interp'],), 'latent_interp_strength': ('FLOAT', {'default': 0.5, 'min': 0.0, 'max': 1.0, 'step': 0.001}), 'denoise_start': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'denoise_seq': ('FLOAT', {'default': 0.5, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'unsample_latents': ('BOOLEAN', {'default': False})}}
    RETURN_TYPES = ('LATENT',)
    FUNCTION = 'sample'
    CATEGORY = 'sampling'

    def update_seed(self, seed, seed_mode):
        if seed_mode == 'increment':
            return seed + 1
        elif seed_mode == 'decrement':
            return seed - 1
        elif seed_mode == 'random':
            return random.randint(0, 18446744073709551615)
        elif seed_mode == 'fixed':
            return seed

    def hash_tensor(self, tensor):
        tensor = tensor.cpu().contiguous()
        return hashlib.sha256(tensor.numpy().tobytes()).hexdigest()

    def update_conditioning(self, conditioning_seq, loop_count, last_conditioning):
        matching_conditioning = None
        for (idx, conditioning, *_) in conditioning_seq:
            if int(idx) == loop_count:
                matching_conditioning = conditioning
                break
        return matching_conditioning if matching_conditioning else last_conditioning if last_conditioning else None

    def update_alternate_seed(self, loop_count):
        if loop_count % 3 == 0:
            if self.previous_seed is None:
                self.previous_seed = self.current_seed
            else:
                (self.previous_seed, self.current_seed) = (self.current_seed, self.previous_seed + 1 if loop_count // 2 % 2 == 0 else self.previous_seed - 1)
        return self.current_seed

    def alternate_denoise(self, current_denoise):
        return 0.95 if current_denoise == 0.75 else 0.75

    def sample(self, model, seed, seed_mode_seq, alternate_values, steps, cfg, sampler_name, scheduler, sequence_loop_count, positive_seq, negative_seq, cond_slerp_strength, latent_image, use_latent_interpolation, latent_interpolation_mode, latent_interp_strength, denoise_start=1.0, denoise_seq=0.5, use_conditioning_slerp=False, unsample_latents=False, alternate_mode=False):
        positive_seq = positive_seq
        negative_seq = negative_seq
        results = []
        positive_conditioning = None
        negative_conditioning = None
        self.initialize_seeds(seed)
        for loop_count in range(sequence_loop_count):
            if alternate_values and loop_count % 2 == 0:
                seq_seed = self.update_alternate_seed(seed) if seed_mode_seq != 'fixed' else seed
            else:
                seq_seed = seed if loop_count <= 0 else self.update_seed(seq_seed, seed_mode_seq)
            print(f'Loop count: {loop_count}, Seed: {seq_seed}')
            last_positive_conditioning = positive_conditioning[0] if positive_conditioning else None
            last_negative_conditioning = negative_conditioning[0] if negative_conditioning else None
            positive_conditioning = self.update_conditioning(positive_seq, loop_count, last_positive_conditioning)
            negative_conditioning = self.update_conditioning(negative_seq, loop_count, last_negative_conditioning)
            if use_conditioning_slerp and (last_positive_conditioning and last_negative_conditioning):
                a = last_positive_conditioning[0].clone()
                b = positive_conditioning[0].clone()
                na = last_negative_conditioning[0].clone()
                nb = negative_conditioning[0].clone()
                pa = last_positive_conditioning[1]['pooled_output'].clone()
                pb = positive_conditioning[1]['pooled_output'].clone()
                npa = last_negative_conditioning[1]['pooled_output'].clone()
                npb = negative_conditioning[1]['pooled_output'].clone()
                pos_cond = slerp(cond_slerp_strength, a, b)
                pos_pooled = slerp(cond_slerp_strength, pa, pb)
                neg_cond = slerp(cond_slerp_strength, na, nb)
                neg_pooled = slerp(cond_slerp_strength, npa, npb)
                positive_conditioning = [pos_cond, {'pooled_output': pos_pooled}]
                negative_conditioning = [neg_cond, {'pooled_output': neg_pooled}]
            positive_conditioning = [positive_conditioning]
            negative_conditioning = [negative_conditioning]
            if positive_conditioning is not None or negative_conditioning is not None:
                end_at_step = steps
                if results is not None and len(results) > 0:
                    latent_input = {'samples': results[-1]}
                    denoise = denoise_seq
                    start_at_step = round((1 - denoise) * steps)
                    end_at_step = steps
                else:
                    latent_input = latent_image
                    denoise = denoise_start
                if unsample_latents and loop_count > 0:
                    force_full_denoise = False if loop_count > 0 or loop_count <= steps - 1 else True
                    disable_noise = False
                    unsampled_latent = unsample(model=model, seed=seq_seed, cfg=cfg, sampler_name=sampler_name, steps=steps, end_at_step=end_at_step, scheduler=scheduler, normalize=False, positive=positive_conditioning, negative=negative_conditioning, latent_image=latent_input)[0]
                    sample = nodes.common_ksampler(model, seq_seed, steps, cfg, sampler_name, scheduler, positive_conditioning, negative_conditioning, unsampled_latent, denoise=denoise, disable_noise=disable_noise, start_step=start_at_step, last_step=end_at_step, force_full_denoise=force_full_denoise)[0]['samples']
                else:
                    sample = nodes.common_ksampler(model, seq_seed, steps, cfg, sampler_name, scheduler, positive_conditioning, negative_conditioning, latent_input, denoise=denoise)[0]['samples']
                if use_latent_interpolation and results and (loop_count > 0):
                    if latent_interpolation_mode == 'Blend':
                        sample = blend_latents(latent_interp_strength, results[-1], sample)
                    elif latent_interpolation_mode == 'Slerp':
                        sample = slerp_latents(latent_interp_strength, results[-1], sample)
                    elif latent_interpolation_mode == 'Cosine Interp':
                        sample = cosine_interp_latents(latent_interp_strength, results[-1], sample)
                    else:
                        sample = sample
                results.append(sample)
        results = torch.cat(results, dim=0)
        results = {'samples': results}
        return (results,)
```