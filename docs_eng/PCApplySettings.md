# Documentation
- Class name: PCApplySettings
- Category: promptcontrol
- Output node: False
- Repo Ref: https://github.com/asagi4/comfyui-prompt-control.git

The 'apply' method of the PCApplySettings node is designed to modify and enhance the function of the tip plan by applying a set of settings. It plays a key role in the behaviour of custom tips in the system, allowing customized responses and interactions based on user-defined parameters.

# Input types
## Required
- prompt_schedule
    - The parameter 'prompt_schedule' is essential to define the structure and time of the hint. It determines how and when the hint is transmitted in the system and significantly affects the overall user experience and interactive processes.
    - Comfy dtype: PromptSchedule
    - Python dtype: PromptSchedule
- settings
    - Parameters'settings' are essential to customizing the action of the tipping plan. It allows users to adjust various aspects, such as filters, start time and default values, to meet specific needs or preferences.
    - Comfy dtype: SCHEDULE_SETTINGS
    - Python dtype: Dict[str, Any]

# Output types
- modified_prompt_schedule
    - Output'modified_prompt_schedule' reflects the application-based update tips plan. It represents a new configuration that will guide the subsequent transmission and interaction of tips in the system.
    - Comfy dtype: PromptSchedule
    - Python dtype: PromptSchedule

# Usage tips
- Infra type: CPU

# Source code
```
class PCApplySettings:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'prompt_schedule': ('PROMPT_SCHEDULE',), 'settings': ('SCHEDULE_SETTINGS',)}}
    RETURN_TYPES = ('PROMPT_SCHEDULE',)
    CATEGORY = 'promptcontrol'
    FUNCTION = 'apply'

    def apply(self, prompt_schedule, settings):
        return (prompt_schedule.with_filters(defaults=settings),)
```