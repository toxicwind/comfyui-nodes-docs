# Documentation
- Class name: FilterSchedule
- Category: promptcontrol
- Output node: False
- Repo Ref: https://github.com/asagi4/comfyui-prompt-control.git

The FilterSchedule class provides a method of fine-tuning and narrowing a set of tips according to specified conditions, improving the accuracy of the selection process and ensuring that the output is consistent with the desired parameters.

# Input types
## Required
- prompt_schedule
    - The prompt_schedule parameter is necessary, defining the basic set of hints to be filtered. It is the starting point for the filtering process and determines the content pool to be refined.
    - Comfy dtype: PROMPT_SCHEDULE
    - Python dtype: <class 'lark.parser.Parser'>
## Optional
- tags
    - The tags parameter is a filter that allows users to specify specific keywords to narrow the hint selection. It plays a critical role in directing output towards a more targeted set of content.
    - Comfy dtype: STRING
    - Python dtype: str
- start
    - Start parameter is used to define the start of the range of the selection hint. It works with the end parameter, limits the selection process, and ensures that only hints within the specified range are considered.
    - Comfy dtype: FLOAT
    - Python dtype: float
- end
    - End parameters are used in conjunction with start parameters, setting a ceiling on the range of hints that you can select. It further refines the output by focusing on specific subsets of content.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- filtered_prompt_schedule
    - Output filtered_prompt_schedule is the result of applying filter conditions to the original tip plan. It represents a refined set of hints that are more in line with the user's preferences.
    - Comfy dtype: PROMPT_SCHEDULE
    - Python dtype: <class 'lark.parser.Parser'>

# Usage tips
- Infra type: CPU

# Source code
```
class FilterSchedule:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'prompt_schedule': ('PROMPT_SCHEDULE',)}, 'optional': {'tags': ('STRING', {'default': ''}), 'start': ('FLOAT', {'min': 0.0, 'max': 1.0, 'default': 0.0, 'step': 0.01}), 'end': ('FLOAT', {'min': 0.0, 'max': 1.0, 'default': 1.0, 'step': 0.01})}}
    RETURN_TYPES = ('PROMPT_SCHEDULE',)
    CATEGORY = 'promptcontrol'
    FUNCTION = 'apply'

    def apply(self, prompt_schedule, tags='', start=0.0, end=1.0):
        p = prompt_schedule.with_filters(tags, start=start, end=end)
        log.debug(f'Filtered {prompt_schedule.parsed_prompt} with: ({tags}, {start}, {end}); the result is %s', p.parsed_prompt)
        return (p,)
```