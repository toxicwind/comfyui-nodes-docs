# Documentation
- Class name: CR_SimpleSchedule
- Category: Comfyroll/Animation/Schedule
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_SimpleSchedule is a node for managing and organizing schedules for various tasks in animated workflows. It processes input schedules, categorizes them by type and formats them for use in different contexts, ensuring a flow-based approach to scheduling in Comfyroll.

# Input types
## Required
- schedule
    - The `schedule' parameter is essential for defining the contents of the timetable. It should be a string with multiple lines, each of which represents a different schedule item. This input is a core function that drives nodes by providing raw data that will be processed and formatted.
    - Comfy dtype: STRING
    - Python dtype: str
- schedule_type
    - The `schedule_type' parameter determines the category of the schedule item. It is a key component because it determines the interpretation and use of the schedule in the system. Each type may be a different treatment mechanism or a processing logic.
    - Comfy dtype: COMBO['Value', 'Text', 'Prompt', 'Prompt Weight', 'Model', 'LoRA', 'ControlNet', 'Style', 'Upscale', 'Camera', 'Job']
    - Python dtype: str
## Optional
- schedule_alias
    - The `schedule_alias' parameter provides an alternative name or identifier for the schedule, which is very useful for citing or organizing the schedule in a larger workflow. Although not necessary, it adds a degree of flexibility to the movement control process.
    - Comfy dtype: STRING
    - Python dtype: str
- schedule_format
    - The `schedule_format' parameter specifies the desired output format for the schedule. It allows users to choose between different formatting styles, which is essential for compatibility with the various systems or for user preferences.
    - Comfy dtype: COMBO['CR', 'Deforum']
    - Python dtype: str

# Output types
- SCHEDULE
    - The `SCHEDULE' output is a list of components, each containing a schedule alias and the corresponding line of the input schedule. This output represents a processed and formatted schedule that can be used by downstream applications or systems.
    - Comfy dtype: LIST[Tuple[str, str]]
    - Python dtype: List[Tuple[str, str]]
- show_help
    - The'show_help' output provides a URL link to the document to get more help. This is very useful for more users who need information on how to use nodes or their functionality.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_SimpleSchedule:

    @classmethod
    def INPUT_TYPES(s):
        schedule_types = ['Value', 'Text', 'Prompt', 'Prompt Weight', 'Model', 'LoRA', 'ControlNet', 'Style', 'Upscale', 'Camera', 'Job']
        return {'required': {'schedule': ('STRING', {'multiline': True, 'default': 'frame_number, item_alias, [attr_value1, attr_value2]'}), 'schedule_type': (schedule_types,), 'schedule_alias': ('STRING', {'default': '', 'multiline': False}), 'schedule_format': (['CR', 'Deforum'],)}}
    RETURN_TYPES = ('SCHEDULE', 'STRING')
    RETURN_NAMES = ('SCHEDULE', 'show_help')
    FUNCTION = 'send_schedule'
    CATEGORY = icons.get('Comfyroll/Animation/Schedule')

    def send_schedule(self, schedule, schedule_type, schedule_alias, schedule_format):
        schedule_lines = list()
        if schedule != '' and schedule_alias != '':
            lines = schedule.split('\n')
            for line in lines:
                if not line.strip():
                    print(f'[Warning] CR Simple Schedule. Skipped blank line: {line}')
                    continue
                schedule_lines.extend([(schedule_alias, line)])
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Schedule-Nodes#cr-simple-schedule'
        return (schedule_lines, show_help)
```