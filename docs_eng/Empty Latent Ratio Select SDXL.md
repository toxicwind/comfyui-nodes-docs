# Documentation
- Class name: EmptyLatentRatioSelector
- Category: Mikey/Latent
- Output node: False
- Repo Ref: https://github.com/bash-j/mikey_nodes

The EmptyLatentRadioSelector node is designed to generate potential expressions for a given set of scale dimensions. It plays a key role in the initial stages of potential space operations, providing a structured starting point for further processing. The node ensures that potential space is properly initialized and provides a basis for follow-up action.

# Input types
## Required
- ratio_selected
    - The `ratio_selected' parameter is essential for determining the specific scale size to be used for potential creation. It determines the dimensions of potential space and is an essential aspect of node operations that directly influences the output structure.
    - Comfy dtype: str
    - Python dtype: str
## Optional
- batch_size
    - The `batch_size' parameter allows you to specify the number of potential samples to be generated in a single operation. It is an optional parameter that can be adjusted according to the specific requirements of the calculation resource and the task at hand.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- samples
    - The `samples' output parameter represents the potential expression that is generated. It is a volume and contains information on potential space, which is essential for follow-up and analysis in the system.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class EmptyLatentRatioSelector:

    @classmethod
    def INPUT_TYPES(s):
        (s.ratio_sizes, s.ratio_dict) = read_ratios()
        return {'required': {'ratio_selected': (s.ratio_sizes,), 'batch_size': ('INT', {'default': 1, 'min': 1, 'max': 64})}}
    RETURN_TYPES = ('LATENT',)
    FUNCTION = 'generate'
    CATEGORY = 'Mikey/Latent'

    def generate(self, ratio_selected, batch_size=1):
        width = self.ratio_dict[ratio_selected]['width']
        height = self.ratio_dict[ratio_selected]['height']
        latent = torch.zeros([batch_size, 4, height // 8, width // 8])
        return ({'samples': latent},)
```