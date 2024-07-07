# Set Props on Cond 🎭🅐🅓
## Documentation
- Class name: ADE_ConditioningSetMask
- Category: Animate Diff 🎭🅐🅓/conditioning/single cond ops
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved.git

This node is intended to apply the mask to conditional data and to adjust the area and intensity of the condition according to the specified parameter. It makes it possible to modify the dynamic changes in the condition input to better match the intended result, such as to focus on or exclude a particular area of the data.

## Input types
### Required
- cond_ADD
    - The condition data that you want to add to or modify. This parameter is essential for introducing a new context or content within the existing conditionality framework.
    - Comfy dtype: CONDITIONING
    - Python dtype: Tensor
- strength
    - Define the intensity of the influence of the mask on condition data and allow for fine-tuning of the effects of the changes.
    - Comfy dtype: FLOAT
    - Python dtype: float
- set_cond_area
    - The determination of whether the mask effect should be applied to the boundary of the default area or the mask provides flexibility for positioning in a given area.
    - Comfy dtype: COMBO[STRING]
    - Python dtype: str

### Optional
- opt_mask
    - An optional mask specifying the condition data range to be modified to provide additional control over the effect of the condition.
    - Comfy dtype: MASK
    - Python dtype: Tensor
- opt_lora_hook
    - An optional parameter allows the application of Lora to conditions and further customization of the conditions process.
    - Comfy dtype: LORA_HOOK
    - Python dtype: LoraHookGroup
- opt_timesteps
    - Optional time-step conditions allowing time adjustments of condition data.
    - Comfy dtype: TIMESTEPS_COND
    - Python dtype: TimestepsCond

## Output types
- conditioning
    - Comfy dtype: CONDITIONING
    - The modified condition data reflect the application mask and adjustments, including any additional condition data added.
    - Python dtype: Tensor

## Usage tips
- Infra type: CPU
- Common nodes: unknown

## Source code
```python
class ConditioningSetMaskHooked:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "cond_ADD": ("CONDITIONING",),
                "strength": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 10.0, "step": 0.01}),
                "set_cond_area": (COND_CONST._LIST_COND_AREA,),
            },
            "optional": {
                "opt_mask": ("MASK", ),
                "opt_lora_hook": ("LORA_HOOK",),
                "opt_timesteps": ("TIMESTEPS_COND",)
            }
        }

    RETURN_TYPES = ("CONDITIONING",)
    CATEGORY = "Animate Diff 🎭🅐🅓/conditioning/single cond ops"
    FUNCTION = "append_and_hook"

    def append_and_hook(self, cond_ADD,
                        strength: float, set_cond_area: str,
                        opt_mask: Tensor=None, opt_lora_hook: LoraHookGroup=None, opt_timesteps: TimestepsCond=None):
        (final_conditioning,) = set_mask_conds(conds=[cond_ADD],
                                               strength=strength, set_cond_area=set_cond_area,
                                               opt_mask=opt_mask, opt_lora_hook=opt_lora_hook, opt_timesteps=opt_timesteps)
        return (final_conditioning,) 