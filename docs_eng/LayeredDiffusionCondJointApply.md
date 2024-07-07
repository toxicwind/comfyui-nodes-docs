# Documentation
- Class name: LayeredDiffusionCondJoint
- Category: layer_diffuse
- Output node: False
- Repo Ref: https://github.com/huchenlei/ComfyUI-layerdiffuse.git

The LayeredDiffusionCondJoint node is designed to integrate vision and background elements seamlessly into a mix of images. It does so through the application of stratification diffusion techniques, which allow for the generation of composite images that maintain the different features of the future and background components. This node is particularly relevant in applications where visual consistency and a realistic mix of different image elements are essential.

# Input types
## Required
- model
    - Model parameters are essential to the operation of nodes because they define the basic model used to generate a mixed image. The selection of models directly affects the quality and style of the image.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- image
    - Image input is essential because it provides visual content that will be processed by nodes and mixed with other elements. The quality and resolution of the input image significantly influences the final output.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- config
    - Configure the string parameters is important because it specifies the settings and options that will guide the diffusion process. It determines how the node mixes prospects and background elements.
    - Comfy dtype: str
    - Python dtype: str
- cond
    - Conditional input, when provided, allows for additional control of the diffusion process to enable nodes to generate images that are more appropriate to specific conditions or styles.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[List[torch.Tensor]]
- blended_cond
    - Mixed condition input is used to further refine the hybrid process and to ensure that the final image meets the aesthetic and thematic requirements required.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[List[torch.Tensor]]

# Output types
- model
    - The output model is the result of the diffusion process and represents a mixed image of the combined outlook and background elements specified according to the input parameters.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module

# Usage tips
- Infra type: GPU

# Source code
```
class LayeredDiffusionCondJoint:
    """Generate fg/bg + blended given fg/bg.
    - FG => Blended + BG
    - BG => Blended + FG
    """

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'image': ('IMAGE',), 'config': ([c.config_string for c in s.MODELS],)}, 'optional': {'cond': ('CONDITIONING',), 'blended_cond': ('CONDITIONING',)}}
    RETURN_TYPES = ('MODEL',)
    FUNCTION = 'apply_layered_diffusion'
    CATEGORY = 'layer_diffuse'
    MODELS = (LayeredDiffusionBase(model_file_name='layer_sd15_fg2bg.safetensors', model_url='https://huggingface.co/LayerDiffusion/layerdiffusion-v1/resolve/main/layer_sd15_fg2bg.safetensors', sd_version=StableDiffusionVersion.SD1x, attn_sharing=True, frames=2, cond_type=LayerType.FG), LayeredDiffusionBase(model_file_name='layer_sd15_bg2fg.safetensors', model_url='https://huggingface.co/LayerDiffusion/layerdiffusion-v1/resolve/main/layer_sd15_bg2fg.safetensors', sd_version=StableDiffusionVersion.SD1x, attn_sharing=True, frames=2, cond_type=LayerType.BG))

    def apply_layered_diffusion(self, model: ModelPatcher, image, config: str, cond: Optional[List[List[torch.TensorType]]]=None, blended_cond: Optional[List[List[torch.TensorType]]]=None):
        ld_model = [m for m in self.MODELS if m.config_string == config][0]
        assert get_model_sd_version(model) == ld_model.sd_version
        assert ld_model.attn_sharing
        work_model = ld_model.apply_layered_diffusion_attn_sharing(model, control_img=image.movedim(-1, 1))[0]
        work_model.model_options.setdefault('transformer_options', {})
        work_model.model_options['transformer_options']['cond_overwrite'] = [cond[0][0] if cond is not None else None for cond in (cond, blended_cond)]
        return (work_model,)
```