# Set Model LoRA Hook 🎭🅐🅓
## Documentation
- Class name: ADE_AttachLoraHookToConditioning
- Category: Animate Diff 🎭🅐🅓/conditioning/single cond ops
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved.git

This node is intended to bind LoRA to conditional data, thereby dynamically modifying model behaviour according to the specified LoRA link. It plays a key role in customization and control during the creation of model conditions, especially in the context of animation and differential rendering.

## Input types
### Required
- conditioning
    - This data determines the behaviour and output of the model, and the additional LoRA links can be dynamically adjusted.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Tuple[Any, Dict[str, Any]]]
- lora_hook
    - The LoRA link, which is attached to the conditional data, makes it possible to modify model parameters at the time of operation, thereby increasing the control and customization of the generation process.
    - Comfy dtype: LORA_HOOK
    - Python dtype: LoraHookGroup

## Output types
- conditioning
    - Comfy dtype: CONDITIONING
    - Modified condition data attached to LoRA links allow for dynamic adjustment of model behaviour.
    - Python dtype: List[Tuple[Any, Dict[str, Any]]]

## Usage tips
- Infra type: CPU
- Common nodes: unknown

## Source code
```python
class SetModelLoraHook:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "conditioning": ("CONDITIONING",),
                "lora_hook": ("LORA_HOOK",),
            }
        }
    
    RETURN_TYPES = ("CONDITIONING",)
    CATEGORY = "Animate Diff 🎭🅐🅓/conditioning/single cond ops"
    FUNCTION = "attach_lora_hook"

    def attach_lora_hook(self, conditioning, lora_hook: LoraHookGroup):
        c = []
        for t in conditioning:
            n = [t[0], t[1].copy()]
            n[1]["lora_hook"] = lora_hook
            c.append(n)
        return (c, )