# Documentation
- Class name: LatentFromBatch
- Category: latent/batch
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The LatentFromBatch method is designed to extract potential samples of a given length from a given batch, starting with a specific batch index. It ensures that samples and masks taken are correctly indexed and cloned, if they exist, in order to preserve their integrity.

# Input types
## Required
- samples
    - The'samples' parameter is essential because it preserves the potential expression of the batch from which you want to extract it. It directly influences the output of nodes by identifying the source of the potential data.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]
## Optional
- batch_index
    - The 'batch_index' parameter defines the starting point for extracting potential data from the sample. It is important because it determines the particular segment of the batch that will be used in subsequent operations.
    - Comfy dtype: INT
    - Python dtype: int
- length
    - The 'length' parameter specifies the number of samples to be taken from the batch. It plays an important role in determining the output size and the range of potential data to be processed.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- latent_samples
    - The 'latet_samples' output contains potential indications based on the batch index and length parameters provided. It is important because it represents the core data that are further used in the workflow.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class LatentFromBatch:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'samples': ('LATENT',), 'batch_index': ('INT', {'default': 0, 'min': 0, 'max': 63}), 'length': ('INT', {'default': 1, 'min': 1, 'max': 64})}}
    RETURN_TYPES = ('LATENT',)
    FUNCTION = 'frombatch'
    CATEGORY = 'latent/batch'

    def frombatch(self, samples, batch_index, length):
        s = samples.copy()
        s_in = samples['samples']
        batch_index = min(s_in.shape[0] - 1, batch_index)
        length = min(s_in.shape[0] - batch_index, length)
        s['samples'] = s_in[batch_index:batch_index + length].clone()
        if 'noise_mask' in samples:
            masks = samples['noise_mask']
            if masks.shape[0] == 1:
                s['noise_mask'] = masks.clone()
            else:
                if masks.shape[0] < s_in.shape[0]:
                    masks = masks.repeat(math.ceil(s_in.shape[0] / masks.shape[0]), 1, 1, 1)[:s_in.shape[0]]
                s['noise_mask'] = masks[batch_index:batch_index + length].clone()
        if 'batch_index' not in s:
            s['batch_index'] = [x for x in range(batch_index, batch_index + length)]
        else:
            s['batch_index'] = samples['batch_index'][batch_index:batch_index + length]
        return (s,)
```