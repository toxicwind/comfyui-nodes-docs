# Documentation
- Class name: PromptToSchedule
- Category: promptcontrol
- Output node: False
- Repo Ref: https://github.com/asagi4/comfyui-prompt-control.git

The `parse' method for PromptToSchedule nodes is designed to interpret texttips and convert them into structured timetable formats. This method is essential to manage and organize consistent schedules that can be further processed or implemented in the system. It captures the complexity of the analysis in abstract terms and focuses on converting the original text into available formats.

# Input types
## Required
- text
    - The 'text' parameter is essential for the 'parse' method because it means that you need to interpret the original text input into the structured timetable. It is the main input and determines the outcome of the operation of the nodes and the process of parsing.
    - Comfy dtype: STRING
    - Python dtype: str
- settings
    - The'settings' parameter is an optional configuration for the 'parse' method, which is used to customize the resolution behaviour. It allows micromediation processes to be subject to specific requirements or constraints.
    - Comfy dtype: DICT
    - Python dtype: Dict[str, Any]

# Output types
- PROMPT_SCHEDULE
    - The output of the 'parse' method is 'PROMPT_SCHEDULE', which is a structured expression of the input text. This output is important because it provides the basis for any subsequent operation or analysis that depends on the parsing schedule.
    - Comfy dtype: PROMPT_SCHEDULE
    - Python dtype: PromptSchedule

# Usage tips
- Infra type: CPU

# Source code
```
class PromptToSchedule:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'text': ('STRING', {'multiline': True})}}
    RETURN_TYPES = ('PROMPT_SCHEDULE',)
    CATEGORY = 'promptcontrol'
    FUNCTION = 'parse'

    def parse(self, text, settings=None):
        schedules = parse_prompt_schedules(text)
        return (schedules,)
```