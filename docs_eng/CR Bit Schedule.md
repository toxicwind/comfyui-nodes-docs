# Documentation
- Class name: CR_BitSchedule
- Category: Comfyroll/Animation/Schedule
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_BitSchedule node is designed to generate a schedule based on binary string input that specifies the number of intervals and loops. It handles binary strings to create a series of scheduled events, which is particularly useful for animation and timing in the project.

# Input types
## Required
- binary_string
    - Binary string is the binary number (0 and 1) sequence used by nodes to create the schedule. Each bit in the string corresponds to an event in the schedule, which is repeated according to the number of loops specified.
    - Comfy dtype: STRING
    - Python dtype: str
- interval
    - The spacing parameter determines the spacing between the intended events in the sequence. It is an integer value that directly affects the timeline time.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- loops
    - Cycle parameters specify how many times a timetable should be repeated. It is an optional integer that allows the duration of the custom timetable.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- SCHEDULE
    - The output schedule is a string that represents the sequence of intended events based on input binary strings, intervals and loops. It is used for further processing or displaying within the application.
    - Comfy dtype: STRING
    - Python dtype: str
- show_text
    - Show_text output provides a URL for help documents that provide additional information and guidance on how to use node-generated schedules.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_BitSchedule:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'binary_string': ('STRING', {'multiline': True, 'default': ''}), 'interval': ('INT', {'default': 1, 'min': 1, 'max': 99999}), 'loops': ('INT', {'default': 1, 'min': 1, 'max': 99999})}}
    RETURN_TYPES = ('STRING', 'STRING')
    RETURN_NAMES = ('SCHEDULE', 'show_text')
    FUNCTION = 'bit_schedule'
    CATEGORY = icons.get('Comfyroll/Animation/Schedule')

    def bit_schedule(self, binary_string, interval, loops=1):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Schedule-Nodes#cr-bit-schedule'
        schedule = []
        binary_string = binary_string.replace(' ', '').replace('\n', '')
        '\n        for i in range(len(binary_string) * loops):\n            index = i % len(binary_string)  # Use modulo to ensure the index continues in a single sequence\n            bit = int(binary_string[index])\n            schedule.append(f"{i},{bit}")\n        '
        for i in range(len(binary_string) * loops):
            schedule_index = i * interval
            bit_index = i % len(binary_string)
            bit = int(binary_string[bit_index])
            schedule.append(f'{schedule_index},{bit}')
        schedule_out = '\n'.join(schedule)
        return (schedule_out, show_help)
```