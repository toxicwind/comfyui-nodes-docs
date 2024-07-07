# Combine LoRA Hooks [2] 🎭🅐🅓
## Documentation
- Class name: ADE_CombineLoraHooks
- Category: Animate Diff 🎭🅐🅓/conditioning/combine lora hooks
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved.git

This node is intended to bring together multiple LoRA-linked groups into a single LoRA-linked group. It helps to combine the various LoRA-linked links to achieve more complex and detailed model conditions by combining the different modifications or enhancements provided by each individual link.

## Input types
### Required
### Optional
- lora_hook_A
    - is the first LoRA-link group to be combined. It plays a key role in the process of aggregation, contributing to its modification or enhancement to the ultimate unified LoRA-link group.
    - Comfy dtype: LORA_HOOK
    - Python dtype: LoraHookGroup
- lora_hook_B
    - is the second LoRA-linked group to be combined. Contributes to its unique modification or enhancement to the unified LoRA-linked group and enriches the overall conditionalities.
    - Comfy dtype: LORA_HOOK
    - Python dtype: LoraHookGroup

## Output types
- lora_hook
    - Comfy dtype: LORA_HOOK
    - The output is a unified LoRA-linked group, which combines changes or enhancements to input the LoRA-linked group. This polymer-linked group contributes to more complex model conditions.
    - Python dtype: LoraHookGroup

## Usage tips
- Infra type: CPU
- Common nodes: unknown

## Source code
```python
class CombineLoraHooks:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
            },
            "optional": {
                "lora_hook_A": ("LORA_HOOK",),
                "lora_hook_B": ("LORA_HOOK",),
            }
        }
    
    RETURN_TYPES = ("LORA_HOOK",)
    CATEGORY = "Animate Diff 🎭🅐🅓/conditioning/combine lora hooks"
    FUNCTION = "combine_lora_hooks"

    def combine_lora_hooks(self, lora_hook_A: LoraHookGroup=None, lora_hook_B: LoraHookGroup=None):
        candidates = [lora_hook_A, lora_hook_B]
        return (LoraHookGroup.combine_all_lora_hooks(candidates),)