# Documentation
- Class name: SelectEveryNthLatent
- Category: Video Helper Suite 🎥🅥🅗🅢/latent
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite.git

The node is used to screen a range of potential indications that each n element is retained according to the interval specified by the user. It is intended to reduce the dimensions of the data while retaining key information, which is essential for the follow-up steps in the video analysis or generation of the task.

# Input types
## Required
- latents
    - The potential input represents a series of compressed video frames or other visual data that need to be processed. This parameter is essential because it forms the basis for node operations and determines the data to be filtered and then used in the downstream task.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
- select_every_nth
    - This parameter determines the spacing of potential expressions from the input sequence. It is a key factor in determining the output density and node to calculate efficiency, as it directly affects the number of elements to be processed.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- LATENT
    - Output contains a compressed potential expression sequence for each n element that is retained from the input. The filtered data can be used to further analyse or generate a lower-resolution video, while maintaining critical visual information.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
- count
    - This output instruction retains the number of potential expressions after the selection process. It provides a measure to understand the reduction in the dimensions of the data and can be used to adjust subsequent processing steps.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class SelectEveryNthLatent:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'latents': ('LATENT',), 'select_every_nth': ('INT', {'default': 1, 'min': 1, 'max': BIGMAX, 'step': 1})}}
    CATEGORY = 'Video Helper Suite 🎥🅥🅗🅢/latent'
    RETURN_TYPES = ('LATENT', 'INT')
    RETURN_NAMES = ('LATENT', 'count')
    FUNCTION = 'select_latents'

    def select_latents(self, latents: dict, select_every_nth: int):
        sub_latents = latents.copy()['samples'][0::select_every_nth]
        return ({'samples': sub_latents}, sub_latents.size(0))
```