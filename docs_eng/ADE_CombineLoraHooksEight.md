# Combine LoRA Hooks [8] 🎭🅐🅓
## Documentation
- Class name: ADE_CombineLoraHooksEight
- Category: Animate Diff 🎭🅐🅓/conditioning/combine lora hooks
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved.git

This node is intended to combine up to eight LoRA links into a single LoRA-linked group. It helps to integrate multiple LoRA-linked changes and allows for more complex and detailed adjustments in model behaviour in the generation task.

## Input types
### Required
### Optional
- lora_hook_A
    - is the first LoRA-linked group that you want to group. It acts as a foundation during the aggregation process, setting the initial conditions for the combined LoRA-linked group.
    - Comfy dtype: LORA_HOOK
    - Python dtype: LoraHookGroup
- lora_hook_B
    - is the second LoRA-linked group that you want to group. The changes it contains expand the capacity and range of modifications of the LoRA-linked group that you want to group.
    - Comfy dtype: LORA_HOOK
    - Python dtype: LoraHookGroup
- lora_hook_C
    - As the third LoRA-link group in the configuration process, additional modifications were made that further enriched the function of the LoRA-linked group after the configuration.
    - Comfy dtype: LORA_HOOK
    - Python dtype: LoraHookGroup
- lora_hook_D
    - The fourth LoRA-linked group, which is meant to be combined, adds a diversity of changes in the LoRA-linked group after the configuration.
    - Comfy dtype: LORA_HOOK
    - Python dtype: LoraHookGroup
- lora_hook_E
    - As the fifth LoRA-linked group in the configuration process, the post-consolidated LoRA-linked group was enhanced by the introduction of more fine adjustments.
    - Comfy dtype: LORA_HOOK
    - Python dtype: LoraHookGroup
- lora_hook_F
    - The sixth LoRA-linked group, which indicated that it was to be combined, contained changes that broadened the scope of the LoRA-linked group after the configuration.
    - Comfy dtype: LORA_HOOK
    - Python dtype: LoraHookGroup
- lora_hook_G
    - As the seventh LoRA-linked group in the configuration process, it added complexity and depth to the post-LoRA-linked group.
    - Comfy dtype: LORA_HOOK
    - Python dtype: LoraHookGroup
- lora_hook_H
    - As the eighth and last group to be combined, the LoRA link group completed the aggregation and maximized the modifications and adjustments in the LoRA link group after the combination.
    - Comfy dtype: LORA_HOOK
    - Python dtype: LoraHookGroup

## Output types
- lora_hook
    - Comfy dtype: LORA_HOOK
    - This group can apply a comprehensive set of modifications to model behaviour.
    - Python dtype: LoraHookGroup

## Usage tips
- Infra type: CPU
- Common nodes: unknown

## Source code
```python
class CombineLoraHookEightOptional:
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
                "lora_hook_E": ("LORA_HOOK",),
                "lora_hook_F": ("LORA_HOOK",),
                "lora_hook_G": ("LORA_HOOK",),
                "lora_hook_H": ("LORA_HOOK",),
            }
        }

    RETURN_TYPES = ("LORA_HOOK",)
    CATEGORY = "Animate Diff 🎭🅐🅓/conditioning/combine lora hooks"
    FUNCTION = "combine_lora_hooks"

    def combine_lora_hooks(self,
                           lora_hook_A: LoraHookGroup=None, lora_hook_B: LoraHookGroup=None,
                           lora_hook_C: LoraHookGroup=None, lora_hook_D: LoraHookGroup=None,
                           lora_hook_E: LoraHookGroup=None, lora_hook_F: LoraHookGroup=None,
                           lora_hook_G: LoraHookGroup=None, lora_hook_H: LoraHookGroup=None):
        candidates = [lora_hook_A, lora_hook_B, lora_hook_C, lora_hook_D,
                      lora_hook_E, lora_hook_F, lora_hook_G, lora_hook_H]
        return (LoraHookGroup.combine_all_lora_hooks(candidates),)