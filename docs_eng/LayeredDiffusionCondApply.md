# Documentation
- Class name: LayeredDiffusionCond
- Category: layer_diffuse
- Output node: False
- Repo Ref: https://github.com/huchenlei/ComfyUI-layerdiffuse.git

The LayeredDiffusionCond node is designed to enter a mixed image from the perspective or background. It uses the power of the diffusion model to create a seamless mix under the conditions provided to enhance the visual consistency and detail of the output.

# Input types
## Required
- model
    - Model parameters are essential because it defines the basic diffusion model used to generate a mixed image. It directly affects the performance of nodes and the quality of the output image.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- cond
    - Cond parameters represent the conditions that guide the diffusion process towards a given result. Proper selection is essential to achieve the required image features.
    - Comfy dtype: CONDITIONING
    - Python dtype: Dict[str, torch.Tensor]
- uncond
    - Uncond parameters are entered as additional conditions that can be used to influence the diffusion process and allow for more refined control of the final image.
    - Comfy dtype: CONDITIONING
    - Python dtype: Dict[str, torch.Tensor]
- latent
    - The latent parameter saves the potential representation of the image, which is the input of the diffusion model. It plays a key role in determining the initial state of the generation process.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
- config
    - The config parameter specifies the configuration of the diffusion model. It is important to align the behaviour of the model with the required production features.
    - Comfy dtype: STR
    - Python dtype: str
- weight
    - Weight parameters are adjusted to apply to the impact of the patches of the model. It provides a method of fine-tuning the balance between original and modified image features.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- blended_model
    - The blended_model output represents a modified diffusion model that has been enhanced by the stratification process. It is important because it contains the combined effects of input conditions.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- blended_cond
    - The blended_cond output is the result of the application of condition information after layer diffusion. It reflects the state of renewal of the image generation process.
    - Comfy dtype: CONDITIONING
    - Python dtype: Dict[str, torch.Tensor]
- blended_uncond
    - The blended_uncond output corresponds to the additional condition information processed through the diffusion model. It contributes to the fineness of the final image.
    - Comfy dtype: CONDITIONING
    - Python dtype: Dict[str, torch.Tensor]

# Usage tips
- Infra type: GPU

# Source code
```
class LayeredDiffusionCond:
    """Generate foreground + background given background / foreground.
    - FG => Blended
    - BG => Blended
    """

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'cond': ('CONDITIONING',), 'uncond': ('CONDITIONING',), 'latent': ('LATENT',), 'config': ([c.config_string for c in s.MODELS],), 'weight': ('FLOAT', {'default': 1.0, 'min': -1, 'max': 3, 'step': 0.05})}}
    RETURN_TYPES = ('MODEL', 'CONDITIONING', 'CONDITIONING')
    FUNCTION = 'apply_layered_diffusion'
    CATEGORY = 'layer_diffuse'
    MODELS = (LayeredDiffusionBase(model_file_name='layer_xl_fg2ble.safetensors', model_url='https://huggingface.co/LayerDiffusion/layerdiffusion-v1/resolve/main/layer_xl_fg2ble.safetensors', sd_version=StableDiffusionVersion.SDXL, cond_type=LayerType.FG), LayeredDiffusionBase(model_file_name='layer_xl_bg2ble.safetensors', model_url='https://huggingface.co/LayerDiffusion/layerdiffusion-v1/resolve/main/layer_xl_bg2ble.safetensors', sd_version=StableDiffusionVersion.SDXL, cond_type=LayerType.BG))

    def apply_layered_diffusion(self, model: ModelPatcher, cond, uncond, latent, config: str, weight: float):
        ld_model = [m for m in self.MODELS if m.config_string == config][0]
        assert get_model_sd_version(model) == ld_model.sd_version
        c_concat = model.model.latent_format.process_in(latent['samples'])
        return ld_model.apply_layered_diffusion(model, weight) + ld_model.apply_c_concat(cond, uncond, c_concat)
```