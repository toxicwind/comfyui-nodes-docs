# Documentation
- Class name: SeargeVAELoader
- Category: Searge/_deprecated_/Files
- Output node: False
- Repo Ref: https://github.com/jobunk/SeargeSDXL.git

The node is designed to easily load the VAE (distributive encoder) model, providing a simplified interface to access and use these machine learning models in the workflow. It abstractes the complexity of model retrieval and ensures that the VAE model can be integrated into the system seamlessly without detailed knowledge of the storage and loading mechanisms at the bottom.

# Input types
## Required
- vae_name
    - The `vae_name' parameter is essential to specify the only identifier for the VAE model to be loaded. It is used correctly as a key to locate and retrieve the corresponding model from the storage system to ensure the accuracy and efficiency of the expected VAE model load.
    - Comfy dtype: COMBO['VAE_NAME']
    - Python dtype: str

# Output types
- VAE
    - The output VAE represents the loaded variable coder model, which can then be used for various tasks, such as data generation, feature extraction, etc.. It is a sign of the success of the model loading process and is essential for further operation in the workflow.
    - Comfy dtype: VAE
    - Python dtype: nodes.VAE

# Usage tips
- Infra type: CPU

# Source code
```
class SeargeVAELoader:

    def __init__(self):
        self.vae_loader = nodes.VAELoader()

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'vae_name': ('VAE_NAME',)}}
    RETURN_TYPES = ('VAE',)
    FUNCTION = 'load_vae'
    CATEGORY = 'Searge/_deprecated_/Files'

    def load_vae(self, vae_name):
        return self.vae_loader.load_vae(vae_name)
```