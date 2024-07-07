# Documentation
- Class name: ImpactConditionalBranchSelMode
- Category: ImpactPack/Logic
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The 'doit' method of the ImpactConditional BranchSelMode node serves as a condition switch in the workflow. It evaluates the 'cond' input to determine whether to return 'tt_value' or 'ff_value', thus guiding the process according to the conditions.

# Input types
## Required
- cond
    - The parameter 'cond' is a boolean value, which determines the path of the node's execution. It's vital because it directly impacts back 'tt_value' or 'ff_value', thus influencing downstream operations.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
## Optional
- sel_mode
    - The parameter'sel_mode' should indicate whether the node should be selected on the basis of a reminder or an execution. It is important because it can change the node's behaviour without changing the conditions and provide flexibility in the decision-making process.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- tt_value
    - When the condition is true, 'tt_value' is the value returned. Its importance is to define the outcome of the node for the determination of the situation, which is essential for the next steps in the workflow.
    - Comfy dtype: any_typ
    - Python dtype: Any
- ff_value
    - When the condition is false, 'ff_value' is the value returned. It is important because it sets out the output of nodes for denial, which may be crucial for the continuity and logic of the follow-up process.
    - Comfy dtype: any_typ
    - Python dtype: Any

# Output types
- result
    - 'Result' output represents the result of the execution of the condition. If the condition is true, it is 'tt_value'; if the condition is false, it is 'ff_value', providing key data for subsequent operations.
    - Comfy dtype: any_typ
    - Python dtype: Any

# Usage tips
- Infra type: CPU

# Source code
```
class ImpactConditionalBranchSelMode:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'cond': ('BOOLEAN',), 'sel_mode': ('BOOLEAN', {'default': True, 'label_on': 'select_on_prompt', 'label_off': 'select_on_execution'})}, 'optional': {'tt_value': (any_typ,), 'ff_value': (any_typ,)}}
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Logic'
    RETURN_TYPES = (any_typ,)

    def doit(self, cond, sel_mode, tt_value=None, ff_value=None):
        print(f'tt={tt_value is None}\nff={ff_value is None}')
        if cond:
            return (tt_value,)
        else:
            return (ff_value,)
```