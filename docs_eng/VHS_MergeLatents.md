# Documentation
- Class name: MergeLatents
- Category: Video Helper Suite 🎥🅥🅗🅢/latent
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite.git

The MergeLatents node is designed to combine two sets of potential expressions into a single coherent structure. It is intelligently applying the specified integration strategy to ensure that the potential dimensions of the two sets match, one of which may be scaled to match the other. The node plays a key role in consolidating information from different sources into a uniform format that can be further processed or analysed.

# Input types
## Required
- latents_A
    - The parameter'latents_A' represents the first group of potential indications that you want to merge. It is essential because it constitutes half of the input required for the integration process. The dimensions and characteristics of these potential expressions significantly affect the function of the nodes.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]
- latents_B
    - The parameter'latents_B' contains a second group of potential indications for consolidation. It is as important as 'latents_A' and, together with 'latents_A', constitutes a complete input for node operations. The validity of nodes for consolidation depends on the compatibility and alignment of 'latents_A' and 'latents_B'.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]
- merge_strategy
    - The parameter'merge_strategy' indicates how to merge potential expressions. It is essential to determine the adjustment size and alignment process that the nodes will follow in order to combine potential expressions into a harmonious structure.
    - Comfy dtype: str
    - Python dtype: str
- scale_method
    - The parameter'scale_method' specifies the method to scale the potential expressions during the consolidation process. It is important because it affects the quality and resolution of the potential expressions after the merger.
    - Comfy dtype: str
    - Python dtype: str
- crop
    - The parameter'crop' defines how potential expressions should be trimmed during the consolidation process, if necessary. It plays a crucial role in maintaining the integrity of potential expressions after consolidation.
    - Comfy dtype: str
    - Python dtype: str

# Output types
- LATENT
    - Output 'LATENT' contains the potential sign of consolidation. It is the main result of node operations and is valuable for follow-up or analysis.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]
- count
    - Output 'count' provides the number of potential indications after consolidation. It helps to understand the scope of the merger operation and can be used for further processing.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class MergeLatents:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'latents_A': ('LATENT',), 'latents_B': ('LATENT',), 'merge_strategy': (MergeStrategies.list_all,), 'scale_method': (ScaleMethods.list_all,), 'crop': (CropMethods.list_all,)}}
    CATEGORY = 'Video Helper Suite 🎥🅥🅗🅢/latent'
    RETURN_TYPES = ('LATENT', 'INT')
    RETURN_NAMES = ('LATENT', 'count')
    FUNCTION = 'merge'

    def merge(self, latents_A: dict, latents_B: dict, merge_strategy: str, scale_method: str, crop: str):
        latents = []
        latents_A = latents_A.copy()['samples']
        latents_B = latents_B.copy()['samples']
        if latents_A.shape[3] != latents_B.shape[3] or latents_A.shape[2] != latents_B.shape[2]:
            A_size = latents_A.shape[3] * latents_A.shape[2]
            B_size = latents_B.shape[3] * latents_B.shape[2]
            use_A_as_template = True
            if merge_strategy == MergeStrategies.MATCH_A:
                pass
            elif merge_strategy == MergeStrategies.MATCH_B:
                use_A_as_template = False
            elif merge_strategy in (MergeStrategies.MATCH_SMALLER, MergeStrategies.MATCH_LARGER):
                if A_size <= B_size:
                    use_A_as_template = True if merge_strategy == MergeStrategies.MATCH_SMALLER else False
            if use_A_as_template:
                latents_B = comfy.utils.common_upscale(latents_B, latents_A.shape[3], latents_A.shape[2], scale_method, crop)
            else:
                latents_A = comfy.utils.common_upscale(latents_A, latents_B.shape[3], latents_B.shape[2], scale_method, crop)
        latents.append(latents_A)
        latents.append(latents_B)
        merged = {'samples': torch.cat(latents, dim=0)}
        return (merged, len(merged['samples']))
```