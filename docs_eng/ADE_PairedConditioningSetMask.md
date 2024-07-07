# Set Props on Conds 🎭🅐🅓
## Documentation
- Class name: ADE_PairedConditioningSetMask
- Category: Animate Diff 🎭🅐🅓/conditioning
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved.git

ADE_PairedConditioningSetMask node is designed to apply a mask and condition adjustment to a pair of conditions. It fine-tunes the condition process by using additional parameters such as strength, setting the condition area and optional elements such as mask, Lora connection and time-step conditions, with the aim of increasing or modifying the properties of the content generated in accordance with the specified adjustment.

## Input types
### Required
- positive_ADD
    - Specifies the positive condition input that you want to adjust. It plays a key role in defining the attributes or characteristics that you want to enhance or modify in the creation of the content.
    - Comfy dtype: CONDITIONING
    - Python dtype: CONDITIONING
- negative_ADD
    - Specifies the negative condition input to be adjusted. It is essential to define properties or characteristics that are to be weakened or changed in a manner that is contrary to positive conditions.
    - Comfy dtype: CONDITIONING
    - Python dtype: CONDITIONING
- strength
    - Determines the strength of the adjustment. A higher value indicates a stronger impact on the condition input.
    - Comfy dtype: FLOAT
    - Python dtype: float
- set_cond_area
    - Defines the range in which the conditions affected by the adjustment are entered. It allows for targeted changes in the conditions input.
    - Comfy dtype: COMBO[STRING]
    - Python dtype: COND_CONST._LIST_COND_AREA

### Optional
- opt_mask
    - An optional mask that can be applied to condition input for more precise adjustments.
    - Comfy dtype: MASK
    - Python dtype: Tensor
- opt_lora_hook
    - An optional Lora link can be applied to conditionalities conversion.
    - Comfy dtype: LORA_HOOK
    - Python dtype: LoraHookGroup
- opt_timesteps
    - Optional time-step conditions allow time adjustments to be made to the condition input.
    - Comfy dtype: TIMESTEPS_COND
    - Python dtype: TimestepsCond

## Output types
- positive
    - Comfy dtype: CONDITIONING
    - Applys the specified positive condition output.
    - Python dtype: CONDITIONING
- negative
    - Comfy dtype: CONDITIONING
    - Applys the specified negative condition output.
    - Python dtype: CONDITIONING

## Usage tips
- Infra type: CPU
- Common nodes: unknown

## Source code
```python
class PairedConditioningSetMaskHooked:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "positive_ADD": ("CONDITIONING", ),
                "negative_ADD": ("CONDITIONING", ),
                "strength": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 10.0, "step": 0.01}),
                "set_cond_area": (COND_CONST._LIST_COND_AREA,),
            },
            "optional": {
                "opt_mask": ("MASK", ),
                "opt_lora_hook": ("LORA_HOOK",),
                "opt_timesteps": ("TIMESTEPS_COND",)
            }
        }

    RETURN_TYPES = ("CONDITIONING", "CONDITIONING")
    RETURN_NAMES = ("positive", "negative")
    CATEGORY = "Animate Diff 🎭🅐🅓/conditioning"
    FUNCTION = "append_and_hook"

    def append_and_hook(self, positive_ADD, negative_ADD,
                        strength: float, set_cond_area: str,
                        opt_mask: Tensor=None, opt_lora_hook: LoraHookGroup=None, opt_timesteps: TimestepsCond=None):
        final_positive, final_negative = set_mask_conds(conds=[positive_ADD, negative_ADD],
                                                        strength=strength, set_cond_area=set_cond_area,
                                                        opt_mask=opt_mask, opt_lora_hook=opt_lora_hook, opt_timesteps=opt_timesteps)
        return (final_positive, final_negative)