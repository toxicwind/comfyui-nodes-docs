# Documentation
- Class name: EmptyLatentRatioCustom
- Category: Mikey/Latent
- Output node: False
- Repo Ref: https://github.com/bash-j/mikey_nodes

The EmptyLatentRadioCustom node is designed to generate potential expressions for a given set of dimensions and batch sizes. It determines the appropriate potential size based on a predefined ratio or user-defined ratio intelligence to ensure that the potential space for output is best suited to further process or generate the task.

# Input types
## Required
- width
    - A width parameter is essential to define the horizontal dimensions of the input space. It directly affects the calculation of potential size, which is essential for the output of nodes.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - Altitude parameters specify the vertical dimensions of the input space. It works with the width parameters to determine the potential size, which is a key element of the node function.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- batch_size
    - A batch size parameter allows the user to specify the number of samples to be processed once. This is an optional parameter that can affect the efficiency of node execution.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- samples
    - Sample output provides a potential indication of generation. It is important because it provides the basis for follow-up operations or analysis in the workflow.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class EmptyLatentRatioCustom:

    @classmethod
    def INPUT_TYPES(s):
        (s.ratio_sizes, s.ratio_dict) = read_ratios()
        return {'required': {'width': ('INT', {'default': 1024, 'min': 1, 'max': 8192, 'step': 1}), 'height': ('INT', {'default': 1024, 'min': 1, 'max': 8192, 'step': 1}), 'batch_size': ('INT', {'default': 1, 'min': 1, 'max': 64})}}
    RETURN_TYPES = ('LATENT',)
    FUNCTION = 'generate'
    CATEGORY = 'Mikey/Latent'

    def generate(self, width, height, batch_size=1):
        if width == 1 and height == 1 or width == height:
            (w, h) = (1024, 1024)
        if f'{width}:{height}' in self.ratio_dict:
            (w, h) = self.ratio_dict[f'{width}:{height}']
        else:
            (w, h) = find_latent_size(width, height)
        latent = torch.zeros([batch_size, 4, h // 8, w // 8])
        return ({'samples': latent},)
```