# Register Model as LoRA Hook 🎭🅐🅓
## Documentation
- Class name: ADE_RegisterModelAsLoraHook
- Category: Animate Diff 🎭🅐🅓/conditioning/register lora hooks
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved.git

This node is intended to link the model to LoRA in the AnimateDiff framework, thereby achieving dynamic modification and control of model behaviour during generation. It allows enhanced customization and fine-tuning of model output according to specific conditions or input through the integration of LoRA (low adaptation) technologies and models.

## Input types
### Required
- model
    - This indicates the target model parameters to which LoRA linkages will be applied. It is essential to define the scope and context of LoRA adaptation and to influence how model behaviour is modified in the process of generation.
    - Comfy dtype: MODEL
    - Python dtype: Union[ModelPatcher, ModelPatcherAndInjector]
- clip
    - The CLIP models involved in the designation process, if any, provide the context in which LoRA adaptation may be applied in conjunction with the main model.
    - Comfy dtype: CLIP
    - Python dtype: CLIP
- ckpt_name
    - The name of the check point indicating the state of the loaded model is essential for the use of specific pre-training weights or for the configuration of the initialization model.
    - Comfy dtype: COMBO[STRING]
    - Python dtype: str
- strength_model
    - Controls the intensity parameters of the LoRA modifications applied to the model. It allows fine-tuning of the influence of LoRA on model behaviour, thus allowing precise adjustments to the generation process.
    - Comfy dtype: FLOAT
    - Python dtype: float
- strength_clip
    - Similar to Strength_model, this parameter adjusts the intensity of the LoRA modifications, but is particularly specific to the CLIP models involved in the process. It allows for separate control of the adaptation intensity of different frame components.
    - Comfy dtype: FLOAT
    - Python dtype: float

## Output types
- model
    - Comfy dtype: MODEL
    - Apply the LoRA-linked model to reflect the dynamic adaptation specified by input parameters.
    - Python dtype: ModelPatcher
- clip
    - Comfy dtype: CLIP
    - If the CLIP model is involved in the process, the CLIP model, which is linked to LoRA, is used. It directs LoRA to modify the application to the CLIP component.
    - Python dtype: CLIP
- lora_hook
    - Comfy dtype: LORA_HOOK
    - Registered and applied to model and/or CLIP LoRA, where specific adaptations are sealed.
    - Python dtype: LoraHook

## Usage tips
- Infra type: CPU
- Common nodes: unknown

## Source code
```python
class MaskableSDModelLoader:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "model": ("MODEL",),
                "clip": ("CLIP",),
                "ckpt_name": (folder_paths.get_filename_list("checkpoints"), ),
                "strength_model": ("FLOAT", {"default": 1.0, "min": -20.0, "max": 20.0, "step": 0.01}),
                "strength_clip": ("FLOAT", {"default": 1.0, "min": -20.0, "max": 20.0, "step": 0.01}),
            }
        }
    
    RETURN_TYPES = ("MODEL", "CLIP", "LORA_HOOK")
    CATEGORY = "Animate Diff 🎭🅐🅓/conditioning/register lora hooks"
    FUNCTION = "load_model_as_lora"

    def load_model_as_lora(self, model: ModelPatcher, clip: CLIP, ckpt_name: str, strength_model: float, strength_clip: float):
        ckpt_path = folder_paths.get_full_path("checkpoints", ckpt_name)
        out = comfy.sd.load_checkpoint_guess_config(ckpt_path, output_vae=True, output_clip=True, embedding_directory=folder_paths.get_folder_paths("embeddings"))
        model_loaded = out[0]
        clip_loaded = out[1]

        lora_hook = LoraHook(lora_name=ckpt_name)
        lora_hook_group = LoraHookGroup()
        lora_hook_group.add(lora_hook)
        model_lora, clip_lora = load_model_as_hooked_lora_for_models(model=model, clip=clip,
                                                                     model_loaded=model_loaded, clip_loaded=clip_loaded,
                                                                     lora_hook=lora_hook,
                                                                     strength_model=strength_model, strength_clip=strength_clip)
        return (model_lora, clip_lora, lora_hook_group)