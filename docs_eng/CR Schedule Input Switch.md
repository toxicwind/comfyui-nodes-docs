# Documentation
- Class name: Comfyroll_ScheduleInputSwitch
- Category: Comfyroll/Animation/Schedule
- Output node: True
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

Comfyroll_ScheduleInputSwitch is designed to select between two different schedules based on input values. It allows conditions to be performed in workflows so that users can follow the flow according to the input guidance provided. This node plays a key role in organizing complex animations, by setting the timetable to be followed.

# Input types
## Required
- Input
    - The `Input' parameter is essential for determining which timetable will be implemented. It determines the animated process according to its value, which can be between one and two. This parameter is essential for the node decision-making process and directly affects the results of the operation.
    - Comfy dtype: INT
    - Python dtype: int
- schedule1
    - The `schedule1' parameter represents the first schedule that can be selected for the node. It is a key component of the node decision-making process and provides an alternative path to the animation sequence when the input value is 1.
    - Comfy dtype: SCHEDULE
    - Python dtype: Schedule
- schedule2
    - The `schedule2' parameter is the second schedule option available for nodes. When the input value is not 1, it becomes important and guides the next steps of the animation according to this timetable.
    - Comfy dtype: SCHEDULE
    - Python dtype: Schedule

# Output types
- SCHEDULE
    - The `SCHEDULE' output is based on the input-selected schedule provided to the node. It is the core result of the node operation and guides the next steps in the animated workflow.
    - Comfy dtype: SCHEDULE
    - Python dtype: Schedule
- show_help
    - The'show_help' output provides a URL for the wiki page, which provides additional guidance and information on node functions. It is a resource for users seeking to use nodes effectively.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class Comfyroll_ScheduleInputSwitch:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'Input': ('INT', {'default': 1, 'min': 1, 'max': 2}), 'schedule1': ('SCHEDULE',), 'schedule2': ('SCHEDULE',)}}
    RETURN_TYPES = ('SCHEDULE', 'STRING')
    RETURN_NAMES = ('SCHEDULE', 'show_help')
    OUTPUT_NODE = True
    FUNCTION = 'switch'
    CATEGORY = icons.get('Comfyroll/Animation/Schedule')

    def switch(self, Input, schedule1, schedule2):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Schedule-Nodes#cr-schedule-input-switch'
        if Input == 1:
            return (schedule1, show_help)
        else:
            return (schedule2, show_help)
```