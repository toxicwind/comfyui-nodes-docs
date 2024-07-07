# Documentation
- Class name: ApplyStableSRUpscaler
- Category: image/upscaling
- Output node: False
- Repo Ref: https://github.com/Arthurzhangsheng/Comfyui-StableSR.git

The node uses the power of the StableSR model to improve the resolution of the input image while maintaining its visual integrity. It focuses on the application of advanced up-sampling techniques to produce high-quality, detailed images without compromising the original content.

# Input types
## Required
- model
    - Model parameters are essential because they define the infrastructure and functions that nodes will operate. For up-sampling, having an effective model is key to ensuring the correct application of StableSR technology.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- stablesr_model
    - The stablesr_model parameter is essential because it specifies the path of the StableSR model checkpoint, which contains the pre-training weights required for the sampling process. Without a correct and accessible model path, node cannot perform its intended function.
    - Comfy dtype: COMBO[folder_paths.get_filename_list('stablesr')]
    - Python dtype: str
## Optional
- latent_image
    - When providing latent_image parameters, the node is allowed to incorporate additional information into the sampling process. This can improve the output by considering the potential features of the input, which may lead to better visual outcomes.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor

# Output types
- model_sr
    - The output model model_sr is the result of the application of sampling techniques on StableSR to input models. It represents an enhanced version of the original model, with a higher resolution and detail, for further use or analysis.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module

# Usage tips
- Infra type: GPU

# Source code
```
class ApplyStableSRUpscaler:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'stablesr_model': (folder_paths.get_filename_list('stablesr'),)}, 'optional': {'latent_image': ('LATENT',)}}
    RETURN_TYPES = ('MODEL',)
    FUNCTION = 'apply_stable_sr_upscaler'
    CATEGORY = 'image/upscaling'

    def apply_stable_sr_upscaler(self, model, stablesr_model, latent_image=None):
        stablesr_model_path = folder_paths.get_full_path('stablesr', stablesr_model)
        if not os.path.isfile(stablesr_model_path):
            raise Exception(f'[StableSR] Invalid StableSR model reference')
        upscaler = StableSR(stablesr_model_path, dtype=comfy.model_management.unet_dtype(), device='cpu')
        if latent_image != None:
            latent_image = model.model.process_latent_in(latent_image['samples'])
            upscaler.set_latent_image(latent_image)
        else:
            upscaler.set_auto_set_latent(True)
        model_sr = model.clone()
        model_sr.set_model_unet_function_wrapper(upscaler)
        return (model_sr,)
```