# Documentation
- Class name: PCPromptFromSchedule
- Category: promptcontrol
- Output node: False
- Repo Ref: https://github.com/asagi4/comfyui-prompt-control.git

The node is intended to extract and apply a reminder from a predefined schedule according to the specified time point to ensure that the reminder generated is relevant and timely in the context.

# Input types
## Required
- prompt_schedule
    - The reminder schedule is a key input that outlines the structure and content of the hint over time. This is essential for the correct function of the node and for producing meaningful output.
    - Comfy dtype: PROMPT_SCHEDULE
    - Python dtype: <class 'lark.prompt_schedule.PromptSchedule'>
- at
    - The 'at'parameter specifies precisely the point of time from which the hint is drawn from the schedule. It directly affects the hint of the selection and its relevance.
    - Comfy dtype: FLOAT
    - Python dtype: float
## Optional
- tags
    - The 'tags' parameter allows a schedule of filter hints based on a particular label, which allows the output to be fine-tuned to a particular theme or category.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- prompt
    - Output 'prompt' is a reminder selected from the schedule at a specified time and serves as a basis for further processing or analysis.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class PCPromptFromSchedule:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'prompt_schedule': ('PROMPT_SCHEDULE',), 'at': ('FLOAT', {'min': 0.0, 'max': 1.0, 'step': 0.01})}, 'optional': {'tags': ('STRING', {'default': ''})}}
    RETURN_TYPES = ('STRING',)
    CATEGORY = 'promptcontrol'
    FUNCTION = 'apply'

    def apply(self, prompt_schedule, at, tags=''):
        p = prompt_schedule.with_filters(tags, start=at, end=at).parsed_prompt[-1][1]
        log.info('Prompt at %s:\n%s', at, p['prompt'])
        log.info('LoRAs: %s', p['loras'])
        return (p['prompt'],)
```