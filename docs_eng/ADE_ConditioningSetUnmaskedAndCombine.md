# Set Unmasked Cond 🎭🅐🅓
## Documentation
- Class name: ADE_ConditioningSetUnmaskedAndCombine
- Category: Animate Diff 🎭🅐🅓/conditioning/single cond ops
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved.git

This node is dedicated to the advanced condition data operation of the model, with particular attention to removing masks and combining different conditions input sets. It enhances or modifys the generation process by applying complex conditions conversions.

## Input types
### Required
- cond
    - The main condition input as the basis for the conversion. It plays a key role in determining the initial state or context of the generation process.
    - Comfy dtype: CONDITIONING
    - Python dtype: list
- cond_DEFAULT
    - Enter the additional condition that you want to combine with the main condition input. This input usually represents the default or supplemental information that changes or enhances the underlying condition.
    - Comfy dtype: CONDITIONING
    - Python dtype: list

### Optional
- opt_lora_hook
    - An optional parameter allowing the application of Lora linkages to condition input and providing further customization and control mechanisms for the conditionality process.
    - Comfy dtype: LORA_HOOK
    - Python dtype: LoraHookGroup

## Output types
- conditioning
    - Comfy dtype: CONDITIONING
    - Combining and removing the result of the condition input provided by the mask represents the condition state used to generate modifications or enhancements of the model.
    - Python dtype: list

## Usage tips
- Infra type: CPU
- Common nodes: unknown

## Source code
```python
class ConditioningSetUnmaskedAndCombineHooked:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "cond": ("CONDITIONING",),
                "cond_DEFAULT": ("CONDITIONING",),
            },
            "optional": {
                "opt_lora_hook": ("LORA_HOOK",),
            }
        }
    
    RETURN_TYPES = ("CONDITIONING",)
    CATEGORY = "Animate Diff 🎭🅐🅓/conditioning/single cond ops"
    FUNCTION = "append_and_combine"

    def append_and_combine(self, cond, cond_DEFAULT,
                           opt_lora_hook: LoraHookGroup=None):
        (final_conditioning,) = set_unmasked_and_combine_conds(conds=[cond], new_conds=[cond_DEFAULT],
                                                                        opt_lora_hook=opt_lora_hook)
        return (final_conditioning,)