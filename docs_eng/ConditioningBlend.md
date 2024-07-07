# Documentation
- Class name: WAS_ConditioningBlend
- Category: conditioning
- Output node: False
- Repo Ref: https://github.com/WASasquatch/WAS_Extras

The WAS_ConditioningBlend node is designed to mix the two conditions seamlessly using the specified mix mode and strength to ensure the harmonious integration of the two inputes. This node plays a key role in generating the output of the conditions, by combining the different condition signals and customizing the level of impact.

# Input types
## Required
- conditioning_a
    - The first type of condition input is to be mixed with another condition. It is a key component because it constitutes half of the mixture and significantly affects the final condition output.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Tuple[torch.Tensor, Dict[str, torch.Tensor]]]
- conditioning_b
    - The second condition is entered, adding the first during the mixing process. It is essential because it helps to eventually mix and influences the characteristics of the output of the condition.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Tuple[torch.Tensor, Dict[str, torch.Tensor]]]
- blending_mode
    - The hybrid mode determines how two conditions are combined. It is a key parameter because it determines the algorithm to be used for mixing, thus affecting the nature of the final output.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- blending_strength
    - Mixed strength parameters control the strength of the mixed effect. It is important because it allows fine-tuning of the balance between two conditions in the mixture.
    - Comfy dtype: FLOAT
    - Python dtype: float
- seed
    - Node is used to generate seeds in random numbers. It ensures the recurrence of results through a consistent random state in the execution process.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- conditioning
    - The output of the WAS_ConditioningBlend node is a single mass of conditions, representing a mixture of two input loads. It is important because it is a follow-on node that requires condition data.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Tuple[torch.Tensor, Dict[str, torch.Tensor]]]

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_ConditioningBlend:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'conditioning_a': ('CONDITIONING',), 'conditioning_b': ('CONDITIONING',), 'blending_mode': (list(blending_modes.keys()),), 'blending_strength': ('FLOAT', {'default': 0.5, 'min': -10.0, 'max': 10.0, 'step': 0.001}), 'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615})}}
    RETURN_TYPES = ('CONDITIONING',)
    RETURN_NAMES = ('conditioning',)
    FUNCTION = 'combine'
    CATEGORY = 'conditioning'

    def combine(self, conditioning_a, conditioning_b, blending_mode, blending_strength, seed):
        if seed > 0:
            torch.manual_seed(seed)
        a = conditioning_a[0][0].clone()
        b = conditioning_b[0][0].clone()
        pa = conditioning_a[0][1]['pooled_output'].clone()
        pb = conditioning_b[0][1]['pooled_output'].clone()
        cond = normalize(blending_modes[blending_mode](a, b, 1 - blending_strength))
        pooled = normalize(blending_modes[blending_mode](pa, pb, 1 - blending_strength))
        conditioning = [[cond, {'pooled_output': pooled}]]
        return (conditioning,)
```