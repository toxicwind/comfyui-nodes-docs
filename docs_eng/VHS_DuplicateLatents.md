# Documentation
- Class name: DuplicateLatents
- Category: Video Helper Suite 🎥🅥🅗🅢/latent
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite.git

The DuplicateLatents node is designed to replicate the potential indications of input, effectively increasing their numbers through the specified factors. Its function is to increase the size of potential spatially operated data sets without changing the integrity of the raw data, thereby enhancing their usefulness in various applications, such as training or data enhancement.

# Input types
## Required
- latents
    - The `latents' parameter is a dictionary containing Tensor objects, representing potential spatial data. It is the key to node operations because it is the main input to be copied. The copying process depends on the quality and structure of this input, which directly influences the output of the node and its subsequent use in downstream tasks.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]
## Optional
- multiply_by
    - The'multiply_by' parameter determines the multiples of potential indications that will be copied. It plays an important role in the implementation of the node because it directly affects the amount of output data. This parameter allows fine-tuning of the size of the dataset, which is necessary for the application of a given number of potential samples.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- LATENT
    - Output 'LATENT' is a dictionary that contains potential spatial data for replication. It is important because it represents processed data that expands according to the specified multiplier factor. This output is ready for further analysis or input as other nodes that need to increase the number of potential samples.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]
- count
    - The ‘count’ output represents the total number of potential samples following the replication process. This is an important information that shows the extent to which the data are magnified. This measure can be used to make informed decisions about the next steps in the data processing or model training workflow.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class DuplicateLatents:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'latents': ('LATENT',), 'multiply_by': ('INT', {'default': 1, 'min': 1, 'max': BIGMAX, 'step': 1})}}
    CATEGORY = 'Video Helper Suite 🎥🅥🅗🅢/latent'
    RETURN_TYPES = ('LATENT', 'INT')
    RETURN_NAMES = ('LATENT', 'count')
    FUNCTION = 'duplicate_input'

    def duplicate_input(self, latents: dict[str, Tensor], multiply_by: int):
        new_latents = latents.copy()
        full_latents = []
        for n in range(0, multiply_by):
            full_latents.append(new_latents['samples'])
        new_latents['samples'] = torch.cat(full_latents, dim=0)
        return (new_latents, new_latents['samples'].size(0))
```