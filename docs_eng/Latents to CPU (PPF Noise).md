# Documentation
- Class name: PPFNLatentToCPU
- Category: Power Noise Suite/Latent/Util
- Output node: False
- Repo Ref: https://github.com/WASasquatch/PowerNoiseSuite

The node facilitates the transfer of potential data to the CPU environment, and ensures that the calculation of the CPUs with direct access can be carried out efficiently. It is essential to manage the computing resources and data flow within the system.

# Input types
## Required
- latents
    - The latents parameter is essential because it preserves the data that need to be transferred to the CPU. It directly affects the operation of nodes and relies on the follow-up processing of CPU-based calculations.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]

# Output types
- latents
    - Output latents represent data that can now be used on CPUs and are prepared to be used in a variety of computing tasks that require CPU processing capacity.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]

# Usage tips
- Infra type: CPU

# Source code
```
class PPFNLatentToCPU:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'latents': ('LATENT',)}}
    RETURN_TYPES = ('LATENT',)
    RETURN_NAMES = ('latents',)
    FUNCTION = 'latent_to_cpu'
    CATEGORY = 'Power Noise Suite/Latent/Util'

    def latent_to_cpu(self, latents):
        return ({'samples': latents['samples'].to(device='cpu')},)
```