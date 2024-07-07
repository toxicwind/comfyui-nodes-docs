# Documentation
- Class name: InjectNoiseToLatent
- Category: KJNodes/noise
- Output node: False
- Repo Ref: https://github.com/kijai/ComfyUI-KJNodes.git

InjectNoiseToLatent is designed to simulate the impact of noise on the generation process by introducing noise into potential spatial expressions. It operates by adding to potential samples a noise of specified intensity, which allows selective standardization of results and the application of a mask to control areas affected by noise. This node is essential for addressing the sensitivity of rote experiments on noise and the exploration of models to input disturbances.

# Input types
## Required
- latents
    - The latents parameter is essential because it contains the original potential spatial indication that the noise injection will take place. This is a key input that determines the basic structure of the data to be processed at the node.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]
- strength
    - Strength parameters determine the intensity of noise that is injected into a potential sample. They play an important role in determining the level of disturbance applied to the data, thus affecting the final output.
    - Comfy dtype: FLOAT
    - Python dtype: float
- noise
    - Noise input indicates the noise mode that you want to add to the potential space. It is a key component of the noise injection process and affects the expression of noise in the final output.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]
## Optional
- normalize
    - When the normalize parameter is set to True, potential noise samples will be normalized to ensure that the distribution does not disproportionately tilt after the noise is injected.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- mask
    - The optional mask parameter can be used to specify which areas should be used for noise in potential space. It provides a means of controlling the distribution of noise space.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor
- mix_randn_amount
    - The cross_randn_amount parameter allows the mixing of random noise with existing noise patterns and provides a method for introducing additional variability into noise.
    - Comfy dtype: FLOAT
    - Python dtype: float
- seed
    - The sied parameters provided ensured that randomity during noise generation was re-emerging, which was very useful for consistent experimental results.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- latents
    - Output latents are potential spatial expressions modified by the noise injection process. They are important because they provide the basis for subsequent generation steps.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]

# Usage tips
- Infra type: CPU

# Source code
```
class InjectNoiseToLatent:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'latents': ('LATENT',), 'strength': ('FLOAT', {'default': 0.1, 'min': 0.0, 'max': 200.0, 'step': 0.0001}), 'noise': ('LATENT',), 'normalize': ('BOOLEAN', {'default': False}), 'average': ('BOOLEAN', {'default': False})}, 'optional': {'mask': ('MASK',), 'mix_randn_amount': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1000.0, 'step': 0.001}), 'seed': ('INT', {'default': 123, 'min': 0, 'max': 18446744073709551615, 'step': 1})}}
    RETURN_TYPES = ('LATENT',)
    FUNCTION = 'injectnoise'
    CATEGORY = 'KJNodes/noise'

    def injectnoise(self, latents, strength, noise, normalize, average, mix_randn_amount=0, seed=None, mask=None):
        samples = latents.copy()
        if latents['samples'].shape != noise['samples'].shape:
            raise ValueError('InjectNoiseToLatent: Latent and noise must have the same shape')
        if average:
            noised = (samples['samples'].clone() + noise['samples'].clone()) / 2
        else:
            noised = samples['samples'].clone() + noise['samples'].clone() * strength
        if normalize:
            noised = noised / noised.std()
        if mask is not None:
            mask = torch.nn.functional.interpolate(mask.reshape((-1, 1, mask.shape[-2], mask.shape[-1])), size=(noised.shape[2], noised.shape[3]), mode='bilinear')
            mask = mask.expand((-1, noised.shape[1], -1, -1))
            if mask.shape[0] < noised.shape[0]:
                mask = mask.repeat((noised.shape[0] - 1) // mask.shape[0] + 1, 1, 1, 1)[:noised.shape[0]]
            noised = mask * noised + (1 - mask) * latents['samples']
        if mix_randn_amount > 0:
            if seed is not None:
                torch.manual_seed(seed)
            rand_noise = torch.randn_like(noised)
            noised = ((1 - mix_randn_amount) * noised + mix_randn_amount * rand_noise) / (mix_randn_amount ** 2 + (1 - mix_randn_amount) ** 2) ** 0.5
        samples['samples'] = noised
        return (samples,)
```