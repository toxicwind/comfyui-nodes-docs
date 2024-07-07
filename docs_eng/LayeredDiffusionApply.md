# Documentation
- Class name: LayeredDiffusionFG
- Category: layer_diffuse
- Output node: False
- Repo Ref: https://github.com/huchenlei/ComfyUI-layerdiffuse.git

The LayeredDiffusionFG class is designed to enhance image-generation tasks by applying a layered diffusion process to effectively generate prospects with a transparent background. The node is integrated with various models to achieve the desired effect, focusing on seamless layers to produce high-quality visual output.

# Input types
## Required
- model
    - Model parameters are essential for the LayeredDiffusionFG node, as it defines the bottom structure and parameters used in the diffusion process. It determines the quality and characteristics of the images generated.
    - Comfy dtype: MODEL
    - Python dtype: comfy.model_base.BaseModel
- config
    - The configuration parameter is essential to specify the configuration string corresponding to the selected model. It ensures that the right settings are applied in the diffusion process to influence the final output.
    - Comfy dtype: STRING
    - Python dtype: str
- weight
    - The weight parameter influences the intensity of the diffusion effect on the image. It is a key factor in the trade-off between the details of the control outlook and the transparency of the context.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- output
    - The output of the LayeredDiffusionFG node is a modified model that has been patched to the diffusion layer. The model is ready to produce images with the desired foreground and transparent background characteristics.
    - Comfy dtype: MODEL
    - Python dtype: comfy.model_base.BaseModel

# Usage tips
- Infra type: GPU

# Source code
```
class LayeredDiffusionFG:
    """Generate foreground with transparent background."""

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'config': ([c.config_string for c in s.MODELS],), 'weight': ('FLOAT', {'default': 1.0, 'min': -1, 'max': 3, 'step': 0.05})}}
    RETURN_TYPES = ('MODEL',)
    FUNCTION = 'apply_layered_diffusion'
    CATEGORY = 'layer_diffuse'
    MODELS = (LayeredDiffusionBase(model_file_name='layer_xl_transparent_attn.safetensors', model_url='https://huggingface.co/LayerDiffusion/layerdiffusion-v1/resolve/main/layer_xl_transparent_attn.safetensors', sd_version=StableDiffusionVersion.SDXL, injection_method=LayerMethod.ATTN), LayeredDiffusionBase(model_file_name='layer_xl_transparent_conv.safetensors', model_url='https://huggingface.co/LayerDiffusion/layerdiffusion-v1/resolve/main/layer_xl_transparent_conv.safetensors', sd_version=StableDiffusionVersion.SDXL, injection_method=LayerMethod.CONV), LayeredDiffusionBase(model_file_name='layer_sd15_transparent_attn.safetensors', model_url='https://huggingface.co/LayerDiffusion/layerdiffusion-v1/resolve/main/layer_sd15_transparent_attn.safetensors', sd_version=StableDiffusionVersion.SD1x, injection_method=LayerMethod.ATTN, attn_sharing=True))

    def apply_layered_diffusion(self, model: ModelPatcher, config: str, weight: float):
        ld_model = [m for m in self.MODELS if m.config_string == config][0]
        assert get_model_sd_version(model) == ld_model.sd_version
        if ld_model.attn_sharing:
            return ld_model.apply_layered_diffusion_attn_sharing(model)
        else:
            return ld_model.apply_layered_diffusion(model, weight)
```