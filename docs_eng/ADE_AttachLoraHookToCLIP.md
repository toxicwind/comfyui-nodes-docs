# Set CLIP LoRA Hook 🎭🅐🅓
## Documentation
- Class name: ADE_AttachLoraHookToCLIP
- Category: Animate Diff 🎭🅐🅓/conditioning
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved.git

This node is intended to attach LoRA to the CLIP model and to enhance its functionality by integrating additional layers or modifications. It serves as a custom point for the CLIP model, allowing custom adjustments to influence the behaviour or output of the model.

## Input types
### Required
- clip
    - The CLIP model is attached to the LoRA-linked model. This parameter is essential because it determines the underlying model that will be modified.
    - Comfy dtype: CLIP
    - Python dtype: CLIP
- lora_hook
    - The LoRA link attached to the CLIP model. This link represents the modification or enhancement to be applied and plays a key role in custom modelling functions.
    - Comfy dtype: LORA_HOOK
    - Python dtype: LoraHookGroup

## Output types
- hook_CLIP
    - Comfy dtype: CLIP
    - The modified CLAIP model, which is attached to the LoRA link, represents an enhanced version of the original model.
    - Python dtype: CLIPWithHooks

## Usage tips
- Infra type: CPU
- Common nodes: unknown

## Source code
```python
class SetClipLoraHook:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "clip": ("CLIP",),
                "lora_hook": ("LORA_HOOK",),
            }
        }
    
    RETURN_TYPES = ("CLIP",)
    RETURN_NAMES = ("hook_CLIP",)
    CATEGORY = "Animate Diff 🎭🅐🅓/conditioning"
    FUNCTION = "apply_lora_hook"

    def apply_lora_hook(self, clip: CLIP, lora_hook: LoraHookGroup):
        new_clip = CLIPWithHooks(clip)
        new_clip.set_desired_hooks(lora_hooks=lora_hook)
        return (new_clip, )