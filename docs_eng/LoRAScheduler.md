# Documentation
- Class name: LoRAScheduler
- Category: promptcontrol/old
- Output node: False
- Repo Ref: https://github.com/asagi4/comfyui-prompt-control.git

During the reasoning process, the node has modified the behaviour of the model in the light of predefined instructions to dynamically modify the model, increasing its adaptability and controlability without changing the basic structure of the model.

# Input types
## Required
- model
    - Model parameters are essential, and they define the core of node operations. They are machine learning models that will be modified to modify behaviors according to the alert schedule.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- text
    - Text parameters include a reminder schedule, which specifies the changes to be applied to the model. This is essential to guide node implementation of the required conversions.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- model
    - The output model is a modified version of the input model, which now allows for more detailed control and behaviour in the reasoning process, using the alert schedule.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module

# Usage tips
- Infra type: CPU

# Source code
```
class LoRAScheduler:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'text': ('STRING', {'multiline': True})}}
    RETURN_TYPES = ('MODEL',)
    CATEGORY = 'promptcontrol/old'
    FUNCTION = 'apply'

    def apply(self, model, text):
        schedules = parse_prompt_schedules(text)
        return (schedule_lora_common(model, schedules),)
```