# Documentation
- Class name: LatentBatchSeedBehavior
- Category: latent/advanced
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The LatentBatchSeed Behavior node is designed to operate seed behaviour for a potential sample. It allows the seed to be `random' or `fixed', which is essential for some types of model training or analysis of potential space exploration that require consistency or change.

# Input types
## Required
- samples
    - The'samples' parameter is necessary because it contains potential indications that nodes will be dealt with. It is essential for nodes to carry out their operations and has a direct impact on the results, as it determines the potential space for sampling samples.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]
- seed_behavior
    - The'seed_behavior' parameter indicates how the seed of a potential sample will be handled. It is essential for the application of the key factor for the replicability or variability of potential space. The default is set to 'fix', ensuring that results are consistent unless explicitly set to 'random'.
    - Comfy dtype: COMBO['random', 'fixed']
    - Python dtype: Literal['random', 'fixed']

# Output types
- samples_out
    - The'samples_out' parameter indicates that a batch of potentially processed samples has been applied to seed behaviour. It is important because it carries the results of node operations and reflects the impact of seed behaviour on potential space exploration.
    - Comfy dtype: LATENT
    - Python dtype: Tuple[Dict[str, torch.Tensor]]

# Usage tips
- Infra type: CPU

# Source code
```
class LatentBatchSeedBehavior:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'samples': ('LATENT',), 'seed_behavior': (['random', 'fixed'], {'default': 'fixed'})}}
    RETURN_TYPES = ('LATENT',)
    FUNCTION = 'op'
    CATEGORY = 'latent/advanced'

    def op(self, samples, seed_behavior):
        samples_out = samples.copy()
        latent = samples['samples']
        if seed_behavior == 'random':
            if 'batch_index' in samples_out:
                samples_out.pop('batch_index')
        elif seed_behavior == 'fixed':
            batch_number = samples_out.get('batch_index', [0])[0]
            samples_out['batch_index'] = [batch_number] * latent.shape[0]
        return (samples_out,)
```