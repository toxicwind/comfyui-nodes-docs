# Set Unmasked Conds 🎭🅐🅓
## Documentation
- Class name: ADE_PairedConditioningSetUnmaskedAndCombine
- Category: Animate Diff 🎭🅐🅓/conditioning
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved.git

This node is designed to process and assemble pairs of condition inputs, applying decoupled masks and optional LoRA-link conversions. It focuses on integrating default or baseline conditions with current conditions, preparing for further processing or generation of tasks, thereby increasing flexibility and control over the conditionality process.

## Input types
### Required
- positive
    - Enter the current positive condition that you want to combine with your default counterpart.
    - Comfy dtype: CONDITIONING
    - Python dtype: Dict[str, Any]
- negative
    - Enter the current negative condition that you want to combine with your default counterpart.
    - Comfy dtype: CONDITIONING
    - Python dtype: Dict[str, Any]
- positive_DEFAULT
    - The default that you want to combine with the current positive condition is entered.
    - Comfy dtype: CONDITIONING
    - Python dtype: Dict[str, Any]
- negative_DEFAULT
    - The default negative condition that you want to combine with the current negative condition.
    - Comfy dtype: CONDITIONING
    - Python dtype: Dict[str, Any]

### Optional
- opt_lora_hook
    - An optional LoRA link is used to convert conditions before they are combined.
    - Comfy dtype: LORA_HOOK
    - Python dtype: Optional[LoraHookGroup]

## Output types
- positive
    - Comfy dtype: CONDITIONING
    - The group that integrates the current and default input is being exported to the condition.
    - Python dtype: Dict[str, Any]
- negative
    - Comfy dtype: CONDITIONING
    - Outputs the group negative condition after the current and default input.
    - Python dtype: Dict[str, Any]

## Usage tips
- Infra type: CPU
- Common nodes: unknown

## Source code
```python
class PairedConditioningSetUnmaskedAndCombineHooked:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "positive": ("CONDITIONING",),
                "negative": ("CONDITIONING",),
                "positive_DEFAULT": ("CONDITIONING",),
                "negative_DEFAULT": ("CONDITIONING",),
            },
            "optional": {
                "opt_lora_hook": ("LORA_HOOK",),
            }
        }
    
    RETURN_TYPES = ("CONDITIONING", "CONDITIONING")
    RETURN_NAMES = ("positive", "negative")
    CATEGORY = "Animate Diff 🎭🅐🅓/conditioning"
    FUNCTION = "append_and_combine"

    def append_and_combine(self, positive, negative, positive_DEFAULT, negative_DEFAULT,
                           opt_lora_hook: LoraHookGroup=None):
        final_positive, final_negative = set_unmasked_and_combine_conds(conds=[positive, negative], new_conds=[positive_DEFAULT, negative_DEFAULT],
                                                                        opt_lora_hook=opt_lora_hook)
        return (final_positive, final_negative,)