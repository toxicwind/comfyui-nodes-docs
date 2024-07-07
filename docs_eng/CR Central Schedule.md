# Documentation
- Class name: CR_CentralSchedule
- Category: Animation/Schedule
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

The node creates and manages complex animation schedules by integrating multiple types of input, including text, tips and models, to generate consistent and dynamic time lines for animation execution.

# Input types
## Required
- schedule_1
    - The main schedule text outlines the sequence of the animation actions. It is the core of the node operation, as it provides the basis for the construction of the schedule.
    - Comfy dtype: STRING
    - Python dtype: str
- schedule_type1
    - Specifies the type of schedule, influences how nodes interpret and process input text and influences the overall structure and execution of the animation schedule.
    - Comfy dtype: COMBO
    - Python dtype: str
- schedule_format
    - A decision on the presentation of the final timetable will affect the readability and availability of the animation schedule for further processing or review.
    - Comfy dtype: COMBO
    - Python dtype: str
## Optional
- schedule_alias1
    - The alias of the first schedule can be used for reference or marking purposes to improve the readability and organization of the animation schedule.
    - Comfy dtype: STRING
    - Python dtype: str
- schedule_2
    - Additional schedule text to supplement the main schedule, allowing for more complex animation sequences and action layers.
    - Comfy dtype: STRING
    - Python dtype: str
- schedule_type2
    - To define the type of the second schedule, guide node processing and integrate it with the main schedule to form a comprehensive animation plan.
    - Comfy dtype: COMBO
    - Python dtype: str
- schedule_alias2
    - The alias of the second schedule helps to identify and manage multiple schedules within the animated time line.
    - Comfy dtype: STRING
    - Python dtype: str
- schedule_3
    - The third schedule text further expands the animation sequence to allow nodes to handle complex animations with multiple layers and complex time.
    - Comfy dtype: STRING
    - Python dtype: str
- schedule_type3
    - Indicate the type of the third schedule to help nodes organize and implement additional animation layers within the overall schedule.
    - Comfy dtype: COMBO
    - Python dtype: str
- schedule_alias3
    - The third, alias, provides clarity and easy management of complex animation sequences involving multiple schedules.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- SCHEDULE
    - A timetable for the compilation and formatting of animations to cover the sequence of actions and times in a structured format for the execution of animation systems.
    - Comfy dtype: SCHEDULE
    - Python dtype: Tuple[str, List[Tuple[str, str]]]
- show_text
    - The human readable expression of the animation schedule provides a clear overview of sequences and details for review and reference.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_CentralSchedule:

    @classmethod
    def INPUT_TYPES(cls):
        schedule_types = ['Value', 'Text', 'Prompt', 'Prompt Weight', 'Model', 'LoRA', 'ControlNet', 'Style', 'Upscale', 'Camera', 'Job']
        return {'required': {'schedule_1': ('STRING', {'multiline': True, 'default': 'schedule'}), 'schedule_type1': (schedule_types,), 'schedule_alias1': ('STRING', {'multiline': False, 'default': ''}), 'schedule_2': ('STRING', {'multiline': True, 'default': 'schedule'}), 'schedule_type2': (schedule_types,), 'schedule_alias2': ('STRING', {'multiline': False, 'default': ''}), 'schedule_3': ('STRING', {'multiline': True, 'default': 'schedule'}), 'schedule_type3': (schedule_types,), 'schedule_alias3': ('STRING', {'multiline': False, 'default': ''}), 'schedule_format': (['CR', 'Deforum'],)}, 'optional': {'schedule': ('SCHEDULE',)}}
    RETURN_TYPES = ('SCHEDULE', 'STRING')
    RETURN_NAMES = ('SCHEDULE', 'show_text')
    FUNCTION = 'build_schedule'
    CATEGORY = icons.get('Comfyroll/Animation/Schedule')

    def build_schedule(self, schedule_1, schedule_type1, schedule_alias1, schedule_2, schedule_type2, schedule_alias2, schedule_3, schedule_type3, schedule_alias3, schedule_format, schedule=None):
        schedules = list()
        schedule_text = list()
        if schedule is not None:
            schedules.extend([l for l in schedule])
            (schedule_text.extend([l for l in schedule]),)
        if schedule_1 != '' and schedule_alias1 != '':
            lines = schedule_1.split('\n')
            for line in lines:
                (schedules.extend([(schedule_alias1, line)]),)
            (schedule_text.extend([schedule_alias1 + ',' + schedule_1 + '\n']),)
        if schedule_2 != '' and schedule_alias2 != '':
            lines = schedule_2.split('\n')
            for line in lines:
                (schedules.extend([(schedule_alias2, line)]),)
            (schedule_text.extend([schedule_alias2 + ',' + schedule_2 + '\n']),)
        if schedule_3 != '' and schedule_alias3 != '':
            lines = schedule_3.split('\n')
            for line in lines:
                (schedules.extend([(schedule_alias3, line)]),)
            (schedule_text.extend([schedule_alias3 + ',' + schedule_3 + '\n']),)
        show_text = ''.join(schedule_text)
        return (schedules, show_text)
```