# Set Props and Combine Cond 🎭🅐🅓
## Documentation
- Class name: ADE_ConditioningSetMaskAndCombine
- Category: Animate Diff 🎭🅐🅓/conditioning/single cond ops
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved.git

This node is dedicated to the advanced condition data operation for the generation of the model, with particular attention to the application and combination of the mask and condition layer. It enhances or modifys existing conditions by applying the mask, strength adjustment and integration of new condition data, thus allowing for more accurate control of the generation process.

## Input types
### Required
- cond
    - The raw condition data that you want to enhance or modify. It serves as the basis for the application of the conditionality layer and the mask, directly influences the final output.
    - Comfy dtype: CONDITIONING
    - Python dtype: CustomType[CONDITIONING]
- cond_ADD
    - The attached data that you want to combine with the original conditions. This layer should be applied to existing conditions, allowing for the introduction of new features or modifications.
    - Comfy dtype: CONDITIONING
    - Python dtype: CustomType[CONDITIONING]
- strength
    - A metric value determines the strength of the mask to be applied to the condition. It controls the extent to which conditions are attached and the mask affects the original data.
    - Comfy dtype: FLOAT
    - Python dtype: float
- set_cond_area
    - Specifies the area to be modified in the condition data without reference to a particular type.
    - Comfy dtype: COMBO[STRING]
    - Python dtype: str

### Optional
- opt_mask
    - An optional mask can be applied to condition data. It allows selective enhancement or modification of a particular area of the condition.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor
- opt_lora_hook
    - An optional LornookGroup can be applied to further operating condition data. It provides additional flexibility to modify conditions.
    - Comfy dtype: LORA_HOOK
    - Python dtype: LoraHookGroup
- opt_timesteps
    - optional time steps for condition operations. This parameter allows changes to be applied at specific points in the generation process.
    - Comfy dtype: TIMESTEPS_COND
    - Python dtype: TimestepsCond

## Output types
- conditioning
    - Comfy dtype: CONDITIONING
    - Apply conditions-based, enhanced or modified data that are attached, masked and adjusted.
    - Python dtype: CustomType[CONDITIONING]

## Usage tips
- Infra type: CPU
- Common nodes: unknown

## Source code
```python
class ConditioningSetMaskAndCombineHooked:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "cond": ("CONDITIONING",),
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
    FUNCTION = "append_and_combine"

    def append_and_combine(self, conditioning, conditioning_ADD,
                           strength: float, set_cond_area: str,
                           opt_mask: Tensor=None, opt_lora_hook: LoraHookGroup=None, opt_timesteps: TimestepsCond=None):
        (final_conditioning,) = set_mask_and_combine_conds(conds=[conditioning], new_conds=[conditioning_ADD],
                                                                    strength=strength, set_cond_area=set_cond_area,
                                                                    opt_mask=opt_mask, opt_lora_hook=opt_lora_hook, opt_timesteps=opt_timesteps)
        return (final_conditioning,)