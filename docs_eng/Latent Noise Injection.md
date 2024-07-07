# Documentation
- Class name: WAS_Latent_Noise
- Category: WAS Suite/Latent/Generate
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The "inject_noise" method is designed to introduce random noise into a group of potential samples and to increase the diversity of output generated. This method is essential for the application of random changes that need to be introduced in potential spaces to simulate the distribution of data in the real world.

# Input types
## Required
- samples
    - The samples parameter is a key input that represents the potential spatial vector that will inject noise. It is the key to node execution because it determines the basis on which random changes will be applied.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]
## Optional
- noise_std
    - The 'noise_std'parameter determines the standard difference of noise to be added to the sample. This is an optional parameter that allows users to control the randomity of introducing potential space.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- samples
    - The output “samples” is a potential spatial vector that injects noise. This output is important because it forms the basis for follow-up or generation steps in the workflow.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Latent_Noise:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'samples': ('LATENT',), 'noise_std': ('FLOAT', {'default': 0.1, 'min': 0.0, 'max': 1.0, 'step': 0.01})}}
    RETURN_TYPES = ('LATENT',)
    FUNCTION = 'inject_noise'
    CATEGORY = 'WAS Suite/Latent/Generate'

    def inject_noise(self, samples, noise_std):
        s = samples.copy()
        noise = torch.randn_like(s['samples']) * noise_std
        s['samples'] = s['samples'] + noise
        return (s,)
```