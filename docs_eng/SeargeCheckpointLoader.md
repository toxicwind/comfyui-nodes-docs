# Documentation
- Class name: SeargeCheckpointLoader
- Category: Searge/_deprecated_/Files
- Output node: False
- Repo Ref: https://github.com/jobunk/SeargeSDXL.git

The node is intended to retrieve and load previously saved model inspection points, thus enabling the continued training or evaluation of models from a given point in time.

# Input types
## Required
- ckpt_name
    - The name of the check point is essential to identify the specific model state that you want to load. It directly influences the operation of the node by determining which point you want to visit.
    - Comfy dtype: CHECKPOINT_NAME
    - Python dtype: str

# Output types
- MODEL
    - The output model represents the state of the model when preserving the site and allows for further training or evaluation.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- CLIP
    - If a CLIP component exists, the loaded model will be provided with additional context and functionality to enhance its functionality.
    - Comfy dtype: CLIP
    - Python dtype: Any
- VAE
    - If there is a VAE component, it represents the variable coder associated with the check point, making it productive.
    - Comfy dtype: VAE
    - Python dtype: torch.nn.Module

# Usage tips
- Infra type: CPU

# Source code
```
class SeargeCheckpointLoader:

    def __init__(self):
        self.chkp_loader = nodes.CheckpointLoaderSimple()

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'ckpt_name': ('CHECKPOINT_NAME',)}}
    RETURN_TYPES = ('MODEL', 'CLIP', 'VAE')
    FUNCTION = 'load_checkpoint'
    CATEGORY = 'Searge/_deprecated_/Files'

    def load_checkpoint(self, ckpt_name):
        return self.chkp_loader.load_checkpoint(ckpt_name)
```