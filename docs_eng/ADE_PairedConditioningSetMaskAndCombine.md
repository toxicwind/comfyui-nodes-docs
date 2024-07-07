# Set Props and Combine Conds 🎭🅐🅓
## Documentation
- Class name: ADE_PairedConditioningSetMaskAndCombine
- Category: Animate Diff 🎭🅐🅓/conditioning
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved.git

This node is dedicated to the advanced operation of paired condition data for the generation of models, with particular attention to the application and combination of mask and condition layer applications. It enhances or modifys existing conditions by applying masking, intensity adjustment and integration of new condition elements, thereby more precisely controlling the generation process.

## Input types
### Required
- positive
    - Original positive condition data to be enhanced or modified.
    - Comfy dtype: CONDITIONING
    - Python dtype: torch.Tensor
- negative
    - Original negative condition data to be enhanced or modified.
    - Comfy dtype: CONDITIONING
    - Python dtype: torch.Tensor
- positive_ADD
    - Additional positive condition data to be combined with the original condition.
    - Comfy dtype: CONDITIONING
    - Python dtype: torch.Tensor
- negative_ADD
    - Additional negative condition data to be combined with the original condition.
    - Comfy dtype: CONDITIONING
    - Python dtype: torch.Tensor
- strength
    - Defines the parameters for mask or condition changes strength.
    - Comfy dtype: FLOAT
    - Python dtype: float
- set_cond_area
    - Specifies the area where the mask or modification applies to the condition.
    - Comfy dtype: COMBO[STRING]
    - Python dtype: str

### Optional
- opt_mask
    - An optional mask can be applied to conditional data for selective modification.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor
- opt_lora_hook
    - An optional parameter that allows Lora to be linked to condition data to provide additional conversion or control layers.
    - Comfy dtype: LORA_HOOK
    - Python dtype: LoraHookGroup
- opt_timesteps
    - Optional time-step conditions allow for timing adjustments.
    - Comfy dtype: TIMESTEPS_COND
    - Python dtype: TimestepsCond

## Output types
- positive
    - Comfy dtype: CONDITIONING
    - Application of enhanced or modified positive condition data using mask, strength adjustment, combined with additional conditions.
    - Python dtype: torch.Tensor
- negative
    - Comfy dtype: CONDITIONING
    - Application of enhanced or modified negative condition data using mask, strength adjustment, combined with additional conditions.
    - Python dtype: torch.Tensor

## Usage tips
- Infra type: CPU
- Common nodes: unknown

## Source code
```python
class PairedConditioningSetMaskAndCombineHooked:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "positive": ("CONDITIONING",),
                "negative": ("CONDITIONING",),
                "positive_ADD": ("CONDITIONING",),
                "negative_ADD": ("CONDITIONING",),
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
    FUNCTION = "append_and_combine"

    def append_and_combine(self, positive, negative, positive_ADD, negative_ADD,
                           strength: float, set_cond_area: str,
                           opt_mask: Tensor=None, opt_lora_hook: LoraHookGroup=None, opt_timesteps: TimestepsCond=None):
        final_positive, final_negative = set_mask_and_combine_conds(conds=[positive, negative], new_conds=[positive_ADD, negative_ADD],
                                                                    strength=strength, set_cond_area=set_cond_area,
                                                                    opt_mask=opt_mask, opt_lora_hook=opt_lora_hook, opt_timesteps=opt_timesteps)
        return (final_positive, final_negative,)