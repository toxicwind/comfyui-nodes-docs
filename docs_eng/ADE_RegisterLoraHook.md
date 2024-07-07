# Register LoRA Hook 🎭🅐🅓
## Documentation
- Class name: ADE_RegisterLoraHook
- Category: Animate Diff 🎭🅐🅓/conditioning/register lora hooks
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved.git

This node is intended to link the registration of LoRA within the AnimatéDiff framework, thereby effecting dynamic modifications in model behaviour to enhance animation and image processing capabilities.

## Input types
### Required
- model
    - The LoRA-linked model is to be used as the basis for dynamic behavioral change.
    - Comfy dtype: MODEL
    - Python dtype: ModelPatcher or ModelPatcherAndInjector
- clip
    - The CLIP model, which may be optionally modified with the main model, allows for synchronisation.
    - Comfy dtype: CLIP
    - Python dtype: CLIP
- lora_name
    - A LoRA-specific identifier to be applied determines the nature of the modification of the behaviour.
    - Comfy dtype: COMBO[STRING]
    - Python dtype: str
- strength_model
    - Defines the intensity of the influence of LoRA on the model and allows for fine control of behavioural changes.
    - Comfy dtype: FLOAT
    - Python dtype: float
- strength_clip
    - Specifies the intensity of the impact of LoRA linkages on the CLIP model, with a view to fine-tuning its behaviour.
    - Comfy dtype: FLOAT
    - Python dtype: float

## Output types
- model
    - Comfy dtype: MODEL
    - An enhanced animation and image processing task is prepared using the LoRA linked model.
    - Python dtype: ModelPatcher or ModelPatcherAndInjector
- clip
    - Comfy dtype: CLIP
    - The optional modified CLIP model is synchronized with the main model to achieve enhancements.
    - Python dtype: CLIP
- lora_hook
    - Comfy dtype: LORA_HOOK
    - The registered LoRA is linked and the specified changes are sealed and prepared for application to the model.
    - Python dtype: LoraHookGroup

## Usage tips
- Infra type: CPU
- Common nodes: unknown

## Source code
```python
class MaskableLoraLoader:
    def __init__(self):
        self.loaded_lora = None

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "model": ("MODEL",),
                "clip": ("CLIP",),
                "lora_name": (folder_paths.get_filename_list("loras"), ),
                "strength_model": ("FLOAT", {"default": 1.0, "min": -20.0, "max": 20.0, "step": 0.01}),
                "strength_clip": ("FLOAT", {"default": 1.0, "min": -20.0, "max": 20.0, "step": 0.01}),
            }
        }
    
    RETURN_TYPES = ("MODEL", "CLIP", "LORA_HOOK")
    CATEGORY = "Animate Diff 🎭🅐🅓/conditioning/register lora hooks"
    FUNCTION = "load_lora"

    def load_lora(self, model: Union[ModelPatcher, ModelPatcherAndInjector], clip: CLIP, lora_name: str, strength_model: float, strength_clip: float):
        if strength_model == 0 and strength_clip == 0:
            return (model, clip)
        
        lora_path = folder_paths.get_full_path("loras", lora_name)
        lora = None
        if self.loaded_lora is not None:
            if self.loaded_lora[0] == lora_path:
                lora = self.loaded_lora[1]
            else:
                temp = self.loaded_lora
                self.loaded_lora = None
                del temp
        
        if lora is None:
            lora = comfy.utils.load_torch_file(lora_path, safe_load=True)
            self.loaded_lora = (lora_path, lora)

        lora_hook = LoraHook(lora_name=lora_name)
        lora_hook_group = LoraHookGroup()
        lora_hook_group.add(lora_hook)
        model_lora, clip_lora = load_hooked_lora_for_models(model=model, clip=clip, lora=lora, lora_hook=lora_hook,
                                                            strength_model=strength_model, strength_clip=strength_clip)
        return (model_lora, clip_lora, lora_hook_group)