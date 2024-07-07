# Documentation
- Class name: ApplyFooocusInpaint
- Category: inpaint
- Output node: False
- Repo Ref: https://github.com/Acly/comfyui-inpaint-nodes

The node facilitates the image restoration process by applying patches to the given model, focusing on the missing or damaged parts of the data. It enhances the ability of the model to generate consistent and contextually appropriate content in the target area, using potential expression and patch techniques.

# Input types
## Required
- model
    - Model parameters are essential to the image restoration process. They are the basis for applying patches and integrated restoration properties.
    - Comfy dtype: MODEL
    - Python dtype: comfy.model_patcher.ModelPatcher
- patch
    - The patch parameter is essential to the image restoration process, as it contains the specific fixes and settings needed to generate patches that will be applied to the model.
    - Comfy dtype: INPAINT_PATCH
    - Python dtype: Tuple[InpaintHead, dict[str, Tensor]]
- latent
    - Potential parameters are critical to the image restoration process, as they contain coded information used to generate missing area content.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, Any]

# Output types
- MODEL
    - The output is a patch treated model and now contains the elements of repair that are effectively filled with data appropriate to the context with previously missing or damaged parts.
    - Comfy dtype: MODEL
    - Python dtype: comfy.model_patcher.ModelPatcher

# Usage tips
- Infra type: GPU

# Source code
```
class ApplyFooocusInpaint:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'patch': ('INPAINT_PATCH',), 'latent': ('LATENT',)}}
    RETURN_TYPES = ('MODEL',)
    CATEGORY = 'inpaint'
    FUNCTION = 'patch'

    def patch(self, model: ModelPatcher, patch: tuple[InpaintHead, dict[str, Tensor]], latent: dict[str, Any]):
        base_model: BaseModel = model.model
        latent_pixels = base_model.process_latent_in(latent['samples'])
        noise_mask = latent['noise_mask'].round()
        latent_mask = F.max_pool2d(noise_mask, (8, 8)).round().to(latent_pixels)
        (inpaint_head_model, inpaint_lora) = patch
        feed = torch.cat([latent_mask, latent_pixels], dim=1)
        inpaint_head_model.to(device=feed.device, dtype=feed.dtype)
        inpaint_head_feature = inpaint_head_model(feed)

        def input_block_patch(h, transformer_options):
            if transformer_options['block'][1] == 0:
                h = h + inpaint_head_feature.to(h)
            return h
        lora_keys = comfy.lora.model_lora_keys_unet(model.model, {})
        lora_keys.update({x: x for x in base_model.state_dict().keys()})
        loaded_lora = load_fooocus_patch(inpaint_lora, lora_keys)
        m = model.clone()
        m.set_model_input_block_patch(input_block_patch)
        patched = m.add_patches(loaded_lora, 1.0)
        not_patched_count = sum((1 for x in loaded_lora if x not in patched))
        if not_patched_count > 0:
            print(f'[ApplyFooocusInpaint] Failed to patch {not_patched_count} keys')
        inject_patched_calculate_weight()
        return (m,)
```