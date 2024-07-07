# Documentation
- Class name: RepeatLatentBatch
- Category: latent/batch
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The `repeat' method for RepeatlatentBatch nodes is designed to replicate potential space samples. It accepts a batch of potential samples and an integer, which specifies the number of repeats, and then returns a new batch, in which the sample repeats the number of times specified. This function is essential for expanding data sets or enhancing training data in machine learning applications.

# Input types
## Required
- samples
    - For the Repeat LatentBatch node, the'samples' parameter is a key input because it contains potential indications that need to be repeated. The effectiveness of this method in copying these expressions is directly related to the quality and structure of the input sample.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]
- amount
    - The 'amount' parameter determines how many times each sample in the'samples' input will be repeated. It is a fundamental factor in controlling the size of the output batch and the degree of data enhancement.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- repeated_samples
    - The'repeated_samples' output is based on the specified potential expression batch of 'amount'. It is the main output that is further processed or analysed during the follow-up phase of the workflow.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]

# Usage tips
- Infra type: CPU

# Source code
```
class RepeatLatentBatch:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'samples': ('LATENT',), 'amount': ('INT', {'default': 1, 'min': 1, 'max': 64})}}
    RETURN_TYPES = ('LATENT',)
    FUNCTION = 'repeat'
    CATEGORY = 'latent/batch'

    def repeat(self, samples, amount):
        s = samples.copy()
        s_in = samples['samples']
        s['samples'] = s_in.repeat((amount, 1, 1, 1))
        if 'noise_mask' in samples and samples['noise_mask'].shape[0] > 1:
            masks = samples['noise_mask']
            if masks.shape[0] < s_in.shape[0]:
                masks = masks.repeat(math.ceil(s_in.shape[0] / masks.shape[0]), 1, 1, 1)[:s_in.shape[0]]
            s['noise_mask'] = samples['noise_mask'].repeat((amount, 1, 1, 1))
        if 'batch_index' in s:
            offset = max(s['batch_index']) - min(s['batch_index']) + 1
            s['batch_index'] = s['batch_index'] + [x + i * offset for i in range(1, amount) for x in s['batch_index']]
        return (s,)
```