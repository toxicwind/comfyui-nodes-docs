# Documentation
- Class name: LayeredDiffusionDiff
- Category: layer_diffuse
- Output node: False
- Repo Ref: https://github.com/huchenlei/ComfyUI-layerdiffuse.git

The LayeredDiiffusionDiff node is designed to separate futures and background elements from the mixed image. It does so by applying the diffusion process, which allows models to distinguish and extract futures or backgrounds according to the conditions provided. This node is essential for tasks that require the operation or isolation of specific image components without affecting other visual elements.

# Input types
## Required
- model
    - Model parameters are essential for the operation of nodes, as they define the bottom model that will be used to apply the diffusion process. It is through this model that nodes interact with image data to separate prospects and background.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- cond
    - The cond parameter is a condition input to guide the diffusion process to extract the image components required. It plays a key role in determining the results of the separation process.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Tuple[str, Dict[str, torch.Tensor]}}
- uncond
    - The uncond parameter provides unconditional input, complements the diffusion process and ensures that the model is capable of generating the required image components without specific preconditions.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Tuple[str, Dict[str, torch.Tensor]}}
- blended_latent
    - The blended_latet parameter represents the potential expression of a mixed image from which node attempts to extract a future or background. This is a key input into the diffusion process.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]
- latent
    - The potential representation of the latent parameter for the preservation of the image will be used in conjunction with the mixed potential expression to guide the diffusion process.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]
- config
    - The config parameter specifies the configuration of the diffusion model and ensures that nodes are operated according to the predefined model specifications.
    - Comfy dtype: STRING
    - Python dtype: str
- weight
    - The weight parameter allows fine-tuning of the impact of the diffusion process on image separation. It provides a means of adjusting the intensity of the application.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- model
    - Model output represents a modified version of the input model after application of the diffusion process. Depending on the diffusion configuration, it contains a separated perspective or background.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- cond
    - Cond output provides updated information on the conditions for changes made in the diffusion process.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Tuple[str, Dict[str, torch.Tensor]}}
- uncond
    - The uncond output reflects updated and unconditional input processed through the proliferation mechanism.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Tuple[str, Dict[str, torch.Tensor]}}

# Usage tips
- Infra type: GPU

# Source code
```
class LayeredDiffusionDiff:
    """Extract FG/BG from blended image.
    - Blended + FG => BG
    - Blended + BG => FG
    """

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'cond': ('CONDITIONING',), 'uncond': ('CONDITIONING',), 'blended_latent': ('LATENT',), 'latent': ('LATENT',), 'config': ([c.config_string for c in s.MODELS],), 'weight': ('FLOAT', {'default': 1.0, 'min': -1, 'max': 3, 'step': 0.05})}}
    RETURN_TYPES = ('MODEL', 'CONDITIONING', 'CONDITIONING')
    FUNCTION = 'apply_layered_diffusion'
    CATEGORY = 'layer_diffuse'
    MODELS = (LayeredDiffusionBase(model_file_name='layer_xl_fgble2bg.safetensors', model_url='https://huggingface.co/LayerDiffusion/layerdiffusion-v1/resolve/main/layer_xl_fgble2bg.safetensors', sd_version=StableDiffusionVersion.SDXL, cond_type=LayerType.FG), LayeredDiffusionBase(model_file_name='layer_xl_bgble2fg.safetensors', model_url='https://huggingface.co/LayerDiffusion/layerdiffusion-v1/resolve/main/layer_xl_bgble2fg.safetensors', sd_version=StableDiffusionVersion.SDXL, cond_type=LayerType.BG))

    def apply_layered_diffusion(self, model: ModelPatcher, cond, uncond, blended_latent, latent, config: str, weight: float):
        ld_model = [m for m in self.MODELS if m.config_string == config][0]
        assert get_model_sd_version(model) == ld_model.sd_version
        c_concat = model.model.latent_format.process_in(torch.cat([latent['samples'], blended_latent['samples']], dim=1))
        return ld_model.apply_layered_diffusion(model, weight) + ld_model.apply_c_concat(cond, uncond, c_concat)
```