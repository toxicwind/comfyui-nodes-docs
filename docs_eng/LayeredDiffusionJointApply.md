# Documentation
- Class name: LayeredDiffusionJoint
- Category: layer_diffuse
- Output node: False
- Repo Ref: https://github.com/huchenlei/ComfyUI-layerdiffuse.git

The LayeredDiffusionJoint node is designed to carry out a single batch of reasoning and generate futures, background and mixed images. It can process complex image generation tasks by applying layered diffusion techniques, allowing for the creation of images with complex details and layered effects. This node is particularly suitable for applications that require the simultaneous generation of multiple image components, simplifying processes and increasing the overall efficiency of image synthesis workflows.

# Input types
## Required
- model
    - Model parameters are essential for the operation of nodes, as they define the bottom model that will be used to diffuse the process. This is a key component that directly affects the execution of nodes and the quality of the images generated.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- config
    - Configures a string is a necessary parameter that specifies the settings for a layered diffusion process. It plays a key role in determining how the node applies diffusion technology to generate the required image.
    - Comfy dtype: str
    - Python dtype: str
- fg_cond
    - Foreground parameters are optional and are used to provide specific guidance for the future part of the image generation. It allows fine-tuning of the diffusion process to meet the specific requirements of the image outlook.
    - Comfy dtype: CONDITIONING
    - Python dtype: Optional[List[List[torch.Tensor]]]
- bg_cond
    - Background condition parameters are optional to guide the creation of the image background. It enables nodes to create a background consistent with the visual effects required.
    - Comfy dtype: CONDITIONING
    - Python dtype: Optional[List[List[torch.Tensor]]]
- blended_cond
    - Mixed condition parameters are optional and are used to define the hybrid properties that generate the image. It helps to achieve a harmonious mix of future and background elements within the image.
    - Comfy dtype: CONDITIONING
    - Python dtype: Optional[List[List[torch.Tensor]]]

# Output types
- model
    - The output model represents a patch version of the input model, which now has a layered diffusion capability. The model is ready to produce images with layered effects, providing a higher degree of control and customization of the image synthesis process.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module

# Usage tips
- Infra type: GPU

# Source code
```
class LayeredDiffusionJoint:
    """Generate FG + BG + Blended in one inference batch. Batch size = 3N."""

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'config': ([c.config_string for c in s.MODELS],)}, 'optional': {'fg_cond': ('CONDITIONING',), 'bg_cond': ('CONDITIONING',), 'blended_cond': ('CONDITIONING',)}}
    RETURN_TYPES = ('MODEL',)
    FUNCTION = 'apply_layered_diffusion'
    CATEGORY = 'layer_diffuse'
    MODELS = (LayeredDiffusionBase(model_file_name='layer_sd15_joint.safetensors', model_url='https://huggingface.co/LayerDiffusion/layerdiffusion-v1/resolve/main/layer_sd15_joint.safetensors', sd_version=StableDiffusionVersion.SD1x, attn_sharing=True, frames=3),)

    def apply_layered_diffusion(self, model: ModelPatcher, config: str, fg_cond: Optional[List[List[torch.TensorType]]]=None, bg_cond: Optional[List[List[torch.TensorType]]]=None, blended_cond: Optional[List[List[torch.TensorType]]]=None):
        ld_model = [m for m in self.MODELS if m.config_string == config][0]
        assert get_model_sd_version(model) == ld_model.sd_version
        assert ld_model.attn_sharing
        work_model = ld_model.apply_layered_diffusion_attn_sharing(model)[0]
        work_model.model_options.setdefault('transformer_options', {})
        work_model.model_options['transformer_options']['cond_overwrite'] = [cond[0][0] if cond is not None else None for cond in (fg_cond, bg_cond, blended_cond)]
        return (work_model,)
```