# Documentation
- Class name: MakeCircularVAE
- Category: latent
- Output node: False
- Repo Ref: https://github.com/spinagon/ComfyUI-seamless-tiling

The `run'method at MakeCircurarVAE node is designed to modify the variable-to-codifier (VAE) model in order to achieve circular filling of the volume layer. This adjustment allows the model to process data with cyclical boundary conditions, which is particularly useful for data with inherent circular symmetry. Node may be based on the provision of a flat configuration, applying the cycle fill to two dimensions (x) and (y) or selectively to one dimension.

# Input types
## Required
- vae
    - The 'vae' parameter is a modified variable-based encoder model. It is the core component of the node operation, as it determines the model that will be subject to loop fill conversion.
    - Comfy dtype: VAE
    - Python dtype: torch.nn.Module
- tiling
    - The 'tiling' parameter determines how to apply the loop fill to the volume layers of the VAE model. It controls whether the fill should be applied to two dimensions, or only one dimension, which is essential to the ability of the model to process cyclical data.
    - Comfy dtype: COMBO['enable', 'x_only', 'y_only', 'disable']
    - Python dtype: str
- copy_vae
    - The 'copy_vae' parameter determines whether to directly modify the original VAE model or first create a copy of the model. This option affects the extent of memory use and changes made to the model.
    - Comfy dtype: COMBO['Make a copy', 'Modify in place']
    - Python dtype: str

# Output types
- VAE
    - The output of the node is a modified or copied variable-based encoder model, with a volume layer that has been used for loop filling, which enhances its ability to process recyclable symmetric data.
    - Comfy dtype: VAE
    - Python dtype: torch.nn.Module

# Usage tips
- Infra type: GPU

# Source code
```
class MakeCircularVAE:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'vae': ('VAE',), 'tiling': (['enable', 'x_only', 'y_only', 'disable'],), 'copy_vae': (['Make a copy', 'Modify in place'],)}}
    RETURN_TYPES = ('VAE',)
    FUNCTION = 'run'
    CATEGORY = 'latent'

    def run(self, vae, tiling, copy_vae):
        if copy_vae == 'Modify in place':
            vae_copy = vae
        else:
            vae_copy = copy.deepcopy(vae)
        if tiling == 'enable':
            make_circular_asymm(vae_copy.first_stage_model, True, True)
        elif tiling == 'x_only':
            make_circular_asymm(vae_copy.first_stage_model, True, False)
        elif tiling == 'y_only':
            make_circular_asymm(vae_copy.first_stage_model, False, True)
        else:
            make_circular_asymm(vae_copy.first_stage_model, False, False)
        return (vae_copy,)
```