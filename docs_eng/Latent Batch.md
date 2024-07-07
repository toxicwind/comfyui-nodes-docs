# Documentation
- Class name: WAS_Latent_Batch
- Category: WAS Suite/Latent
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

WAS_Latent_Batch nodes are designed to combine multiple potential volumes to ensure that they have the same dimensions. It plays a key role in managing and organizing potential spatial indications, making it possible to process potential data efficiently in various applications.

# Input types
## Optional
- latent_a
    - The parameter 'latent_a' is an optional input that represents a potential volume. It is important for the proper operation of the node, as it helps the potentially expressed batch processing. The presence of the parameter affects the ability of the node to process and generate a consistent potential batch.
    - Comfy dtype: LATENT
    - Python dtype: Union[torch.Tensor, None]
- latent_b
    - The parameter 'latent_b' functions similar to 'latent_a', allowing for another potential mass to be included in the batch. It enhances the ability of nodes to handle multiple potential vectors, which is essential for comprehensive potential space analysis.
    - Comfy dtype: LATENT
    - Python dtype: Union[torch.Tensor, None]
- latent_c
    - The parameter 'latet_c' is another optional potential mass that can be contained in a batch. Its inclusion provides additional flexibility for nodes to adapt to different potential structures, which is essential for complex potential space operations.
    - Comfy dtype: LATENT
    - Python dtype: Union[torch.Tensor, None]
- latent_d
    - The parameter'latet_d' provides further flexibility for nodes to deal with more potential loads in the batch. It is particularly useful when it needs to deal with more potential expressions together.
    - Comfy dtype: LATENT
    - Python dtype: Union[torch.Tensor, None]

# Output types
- latent
    - The output 'latet' is a batch load that integrates all the potential loads entered into a single structure. It is important because it allows flowline processing and analysis of the potential expressions of the combination.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Latent_Batch:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {}, 'optional': {'latent_a': ('LATENT',), 'latent_b': ('LATENT',), 'latent_c': ('LATENT',), 'latent_d': ('LATENT',)}}
    RETURN_TYPES = ('LATENT',)
    RETURN_NAMES = ('latent',)
    FUNCTION = 'latent_batch'
    CATEGORY = 'WAS Suite/Latent'

    def _check_latent_dimensions(self, tensors, names):
        dimensions = [tensor['samples'].shape for tensor in tensors]
        if len(set(dimensions)) > 1:
            mismatched_indices = [i for (i, dim) in enumerate(dimensions) if dim[1] != dimensions[0][1]]
            mismatched_latents = [names[i] for i in mismatched_indices]
            if mismatched_latents:
                raise ValueError(f'WAS latent Batch Warning: Input latent dimensions do not match for latents: {mismatched_latents}')

    def latent_batch(self, **kwargs):
        batched_tensors = [kwargs[key] for key in kwargs if kwargs[key] is not None]
        latent_names = [key for key in kwargs if kwargs[key] is not None]
        if not batched_tensors:
            raise ValueError('At least one input latent must be provided.')
        self._check_latent_dimensions(batched_tensors, latent_names)
        samples_out = {}
        samples_out['samples'] = torch.cat([tensor['samples'] for tensor in batched_tensors], dim=0)
        samples_out['batch_index'] = []
        for tensor in batched_tensors:
            cindex = tensor.get('batch_index', list(range(tensor['samples'].shape[0])))
            samples_out['batch_index'] += cindex
        return (samples_out,)
```