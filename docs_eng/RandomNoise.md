# Documentation
- Class name: RandomNoise
- Category: Noise Generation
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The Randomnoise node is designed to generate random noise patterns that can be used as a source of randomity in various production models. It serves as the basic component for creating synthetic data, ensuring diversity and unpredictability in the generation of samples.

# Input types
## Required
- noise_seed
    - The noise_seed parameter is essential for the Randomnoise node, as it determines the initial state of generating random noise. This ensures that the generated noise patterns are recreated, which is essential for the generation of consistent results in different operations of the model.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- noise
    - The output of the Randomnoise node is a volume containing noise generated. This is very important because it forms the basis for further treatment in the production model, affecting the diversity and quality of the final output.
    - Comfy dtype: TENSOR
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class RandomNoise(DisableNoise):

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'noise_seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615})}}

    def get_noise(self, noise_seed):
        return (Noise_RandomNoise(noise_seed),)
```