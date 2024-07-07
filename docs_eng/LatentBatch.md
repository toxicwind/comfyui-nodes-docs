# Documentation
- Class name: LatentBatch
- Category: latent/batch
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The `batch'method of the LatentBatch class is designed to combine two groups of potential samples into one batch in an efficient manner. Before connecting, it ensures that the dimensions of the samples from both groups are compatible and then adds batch indexes accordingly. This method is essential when preparing data for further processing in machine learning workflows.

# Input types
## Required
- samples1
    - The parameter'samples1' represents the first potential sample for batch processing. It plays a key role in determining the final shape and structure of a group of batches, especially with regard to the dimensions of potential space.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]
- samples2
    - The parameter'samples2' represents a second group of potential samples for batch processing. It is essential for the method to compare and match the dimensions of'samples1' to create a consistent data batch.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]

# Output types
- samples_out
    - The parameter'samples_out' is the output of the batch process, containing a combination of potential samples from'samples1' and'samples2'. It's important because it represents data ready for downstream missions.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]

# Usage tips
- Infra type: CPU

# Source code
```
class LatentBatch:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'samples1': ('LATENT',), 'samples2': ('LATENT',)}}
    RETURN_TYPES = ('LATENT',)
    FUNCTION = 'batch'
    CATEGORY = 'latent/batch'

    def batch(self, samples1, samples2):
        samples_out = samples1.copy()
        s1 = samples1['samples']
        s2 = samples2['samples']
        if s1.shape[1:] != s2.shape[1:]:
            s2 = comfy.utils.common_upscale(s2, s1.shape[3], s1.shape[2], 'bilinear', 'center')
        s = torch.cat((s1, s2), dim=0)
        samples_out['samples'] = s
        samples_out['batch_index'] = samples1.get('batch_index', [x for x in range(0, s1.shape[0])]) + samples2.get('batch_index', [x for x in range(0, s2.shape[0])])
        return (samples_out,)
```