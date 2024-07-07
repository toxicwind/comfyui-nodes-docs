# Documentation
- Class name: LatentBatchSplitter
- Category: InspirePack/Util
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Inspire-Pack.git

The node is designed to divide a group of potential expressions into multiple subsets to facilitate diverse applications in data processing and modelling training. It enhances the flexibility of potential space exploration by generating diversified data sets from a single input, which is essential for tasks such as generating diversified outputs or expanding data sets in a controlled manner.

# Input types
## Required
- latent
    - The `latent' parameter is essential because it provides initial potential expressions of batches to be processed by nodes. It is the basis for all follow-up operations, enabling nodes to perform their intended functions, i.e. to split and reorganize data.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]
## Optional
- split_count
    - The `split_count' parameter sets out the number of potential batches to be divided into the required subsets. It plays a key role in determining the particle size of the output and can significantly influence the diversity and distribution of the data sets generated.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- latent
    - The output of `latet' represents potential expressions of reorganization and is now structured into a specified number of subsets. This output is essential for downstream processes that rely on zoning data, such as model training or the generation of diversified content.
    - Comfy dtype: LATENT
    - Python dtype: List[Dict[str, torch.Tensor]]

# Usage tips
- Infra type: CPU

# Source code
```
class LatentBatchSplitter:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'latent': ('LATENT',), 'split_count': ('INT', {'default': 4, 'min': 0, 'max': 50, 'step': 1})}}
    RETURN_TYPES = ByPassTypeTuple(('LATENT',))
    FUNCTION = 'doit'
    CATEGORY = 'InspirePack/Util'

    def doit(self, latent, split_count):
        samples = latent['samples']
        latent_base = latent.copy()
        del latent_base['samples']
        cnt = min(split_count, len(samples))
        res = []
        for single_samples in samples[:cnt]:
            item = latent_base.copy()
            item['samples'] = single_samples.unsqueeze(0)
            res.append(item)
        if split_count >= len(samples):
            lack_cnt = split_count - cnt + 1
            item = latent_base.copy()
            item['samples'] = empty_latent()
            for x in range(0, lack_cnt):
                res.append(item)
        elif cnt < len(samples):
            remained_cnt = len(samples) - cnt
            remained_latent = latent_base.copy()
            remained_latent['samples'] = samples[-remained_cnt:]
            res.append(remained_latent)
        return tuple(res)
```