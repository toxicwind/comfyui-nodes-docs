# Documentation
- Class name: IPAdapterUnifiedLoaderCommunity
- Category: ipadapter/loaders
- Output node: False
- Repo Ref: https://github.com/cubiq/ComfyUI_IPAdapter_plus.git

The IPAdapterUnied LoaderCommunity node aims to simplify the loading and management of models and presets in the IPAdapter framework. It provides a unified interface to access different model configurations to ensure compatibility and ease of use in different applications.

# Input types
## Required
- model
    - The `model' parameter is essential for the operation of the node because it specifies the model to be loaded. It directly affects the execution of the node because it determines the configuration of the particular model to be used.
    - Comfy dtype: MODEL
    - Python dtype: str
## Optional
- preset
    - The `preset' parameter allows the selection of a specific preset configuration from the predefined list, which can significantly influence the function of the node and the output of the result.
    - Comfy dtype: COMBO['Composition']
    - Python dtype: str
- ipadapter
    - The optional `ipadapter'parameter is used to specify the specific IPAdapter to be used by the node. It contains elements that enhance the adaptability of the node to different IPAdapter configurations.
    - Comfy dtype: IPADAPTER
    - Python dtype: str

# Output types

# Usage tips
- Infra type: CPU

# Source code
```
class IPAdapterUnifiedLoaderCommunity(IPAdapterUnifiedLoader):

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'preset': (['Composition'],)}, 'optional': {'ipadapter': ('IPADAPTER',)}}
    CATEGORY = 'ipadapter/loaders'
```