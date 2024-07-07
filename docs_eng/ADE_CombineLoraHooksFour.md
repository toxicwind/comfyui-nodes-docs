# Combine LoRA Hooks [4] 🎭🅐🅓
## Documentation
- Class name: ADE_CombineLoraHooksFour
- Category: Animate Diff 🎭🅐🅓/conditioning/combine lora hooks
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved.git

This node is intended to bind together and combine up to four LoRAs into a single LoRA-linked group. It helps to integrate multiple LoRA-linked changes and allows for more complex and detailed adjustments to model behaviour in the Animate Diff framework.

## Input types
### Required
### Optional
- lora_hook_A
    - is the first LoRA-linked group that you want to combine. It plays a key role in the process of aggregation and contributes to the overall modification.
    - Comfy dtype: LORA_HOOK
    - Python dtype: LoraHookGroup
- lora_hook_B
    - As a group, the second LoRA connection group. The changes it contains allow for stacking to enhance the adaptiveness of the model.
    - Comfy dtype: LORA_HOOK
    - Python dtype: LoraHookGroup
- lora_hook_C
    - The third LoRA-linked group, which added another layer of customization, further optimized model behaviour.
    - Comfy dtype: LORA_HOOK
    - Python dtype: LoraHookGroup
- lora_hook_D
    - The fourth and last group to be combined, the LoRA Link Group, completed the revision set to enable the model to be fully adjusted.
    - Comfy dtype: LORA_HOOK
    - Python dtype: LoraHookGroup

## Output types
- lora_hook
    - Comfy dtype: LORA_HOOK
    - Combine up to four integrated groups linked to LoRA. This group allows for enhanced and more complex model conditions.
    - Python dtype: LoraHookGroup

## Usage tips
- Infra type: CPU
- Common nodes: unknown

## Source code
```python
class CombineLoraHookFourOptional:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
            },
            "optional": {
                "lora_hook_A": ("LORA_HOOK",),
                "lora_hook_B": ("LORA_HOOK",),
                "lora_hook_C": ("LORA_HOOK",),
                "lora_hook_D": ("LORA_HOOK",),
            }
        }

    RETURN_TYPES = ("LORA_HOOK",)
    CATEGORY = "Animate Diff 🎭🅐🅓/conditioning/combine lora hooks"
    FUNCTION = "combine_lora_hooks"

    def combine_lora_hooks(self,
                           lora_hook_A: LoraHookGroup=None, lora_hook_B: LoraHookGroup=None,
                           lora_hook_C: LoraHookGroup=None, lora_hook_D: LoraHookGroup=None,):
        candidates = [lora_hook_A, lora_hook_B, lora_hook_C, lora_hook_D]