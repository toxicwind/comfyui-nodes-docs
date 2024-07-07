# Documentation
- Class name: ScheduleToModel
- Category: promptcontrol
- Output node: False
- Repo Ref: https://github.com/asagi4/comfyui-prompt-control.git

The ScheduleToModel node 'apply' method is designed to adjust the structure of the model based on the dynamic timetable provided. It allows seamless integration of different model configurations in the specified steps and enhances the ability of the model to generate a response that matches the context of each step.

# Input types
## Required
- model
    - Model parameters are essential because they represent the neural network that will be modified according to the reminder schedule. They are the basis for node operations and their structure directly influences the results of the sampling process.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- prompt_schedule
    - The prompt_schedule parameter defines the model adjustment sequence that will occur during each step of the sampling process. It is essential to guide the operation of nodes and to determine the specific changes to be applied for each step.
    - Comfy dtype: PROMPT_SCHEDULE
    - Python dtype: Dict[str, Any]

# Output types
- model
    - The output'model' is a modified neural network that is scheduled to be adjusted by the indicative schedule. It covers the results of node operations and reflects the dynamic changes applied during the sampling process.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module

# Usage tips
- Infra type: GPU

# Source code
```
class ScheduleToModel:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'prompt_schedule': ('PROMPT_SCHEDULE',)}}
    RETURN_TYPES = ('MODEL',)
    CATEGORY = 'promptcontrol'
    FUNCTION = 'apply'

    def apply(self, model, prompt_schedule):
        return (schedule_lora_common(model, prompt_schedule),)
```