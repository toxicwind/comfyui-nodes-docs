# Documentation
- Class name: CR_LatentBatchSize
- Category: Comfyroll/Essential/Core
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

The CR_LatentBatchSize node is designed to process and manage the volume size of potential expressions. It efficiently handles copying and connecting potential samples to reach the specified volume size and ensures that downstream processes run consistently, regardless of the number of original samples.

# Input types
## Required
- latent
    - The latent parameter is critical because it contains potential indications that the batch process is required. This is the main input of the node, which directly affects the operation of the node and the volume data generated.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]
## Optional
- batch_size
    - The catch_size parameter determines the number of samples in each batch. If not provided, it is an optional input with a default value of 2. This parameter significantly influences the output of the node, as it determines the size of the batch created from the potential sample.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- samples
    - The samples output, which is a potentially linked volume, has been adjusted to match the volume size required. This output is essential to ensure compatibility with follow-up steps that are expected to have specific batch dimensions.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class CR_LatentBatchSize:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'latent': ('LATENT',), 'batch_size': ('INT', {'default': 2, 'min': 1, 'max': 999, 'step': 1})}}
    RETURN_TYPES = ('LATENT',)
    FUNCTION = 'batchsize'
    CATEGORY = icons.get('Comfyroll/Essential/Core')

    def batchsize(self, latent: tg.Sequence[tg.Mapping[tg.Text, torch.Tensor]], batch_size: int):
        samples = latent['samples']
        shape = samples.shape
        sample_list = [samples] + [torch.clone(samples) for _ in range(batch_size - 1)]
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Core-Nodes#cr-latent-batch-size'
        return ({'samples': torch.cat(sample_list)},)
```