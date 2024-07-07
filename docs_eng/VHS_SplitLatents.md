# Documentation
- Class name: SplitLatents
- Category: Video Helper Suite 🎥🅥🅗🅢/latent
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite.git

SplitLatents is designed to divide a given set of potential variables into two different groups according to the specified index. It plays a key role in managing and organizing potential data, allowing for more sophisticated control and operation of potential video-related information.

# Input types
## Required
- latents
    - The 'latents' parameter is a dictionary containing'samples', representing the potential variables to be divided. It is essential for the operation of nodes, because it determines the data to be divided.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]
## Optional
- split_index
    - The'split_index' parameter defines the location where the potential variable will be split. It is important because it determines the number of samples assigned to each group.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- LATENT_A
    - The first output, 'LATENT_A', contains the potential variables of the first group after the split operation. It is valuable because it represents part of the original potential data.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]
- A_count
    - The 'A_count' output represents the number of potential variables in the first group. It is important because it provides a quantitative measure of splits.
    - Comfy dtype: INT
    - Python dtype: int
- LATENT_B
    - The 'LATENT_B' output contains the potential variables of the second group after the split operation. It is important because it represents the remainder of the original potential data.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]
- B_count
    - The 'B_count' output represents the number of potential variables in the second group. It is important because it complements 'A_count' and provides a measure of the completeness of the split.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class SplitLatents:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'latents': ('LATENT',), 'split_index': ('INT', {'default': 0, 'step': 1, 'min': BIGMIN, 'max': BIGMAX})}}
    CATEGORY = 'Video Helper Suite 🎥🅥🅗🅢/latent'
    RETURN_TYPES = ('LATENT', 'INT', 'LATENT', 'INT')
    RETURN_NAMES = ('LATENT_A', 'A_count', 'LATENT_B', 'B_count')
    FUNCTION = 'split_latents'

    def split_latents(self, latents: dict, split_index: int):
        latents = latents.copy()
        group_a = latents['samples'][:split_index]
        group_b = latents['samples'][split_index:]
        group_a_latent = {'samples': group_a}
        group_b_latent = {'samples': group_b}
        return (group_a_latent, group_a.size(0), group_b_latent, group_b.size(0))
```