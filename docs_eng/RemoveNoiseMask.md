# Documentation
- Class name: RemoveNoiseMask
- Category: ImpactPack/Util
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The node aims to process and optimize data by removing unwanted noise from the input sample, ensuring that subsequent analysis or processing steps are based on cleaner and more reliable information.

# Input types
## Required
- samples
    - The samples parameter is the key input to the node because it contains the data to be processed. The function of the node is to identify and remove noise from these samples in order to improve the quality of the data.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]

# Output types
- res
    - The "res" output is the result of node operations and contains a sample after noise. It represents refined data that can be used for further processing or analysis.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]

# Usage tips
- Infra type: CPU

# Source code
```
class RemoveNoiseMask:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'samples': ('LATENT',)}}
    RETURN_TYPES = ('LATENT',)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Util'

    def doit(self, samples):
        res = {key: value for (key, value) in samples.items() if key != 'noise_mask'}
        return (res,)
```