# Documentation
- Class name: PromptScheduleNodeFlow
- Category: FizzNodes 📅🅕🅝/ScheduleNodes
- Output node: False
- Repo Ref: https://github.com/FizzleDorf/ComfyUI_FizzNodes

The node is intended to operate and schedule strings according to the given frame number. It allows users to add or modify text content at specified frame intervals, which is essential for the application of the information to be time-structured.

# Input types
## Required
- text
    - The 'text' parameter is essential for defining what is to be added to the agenda. It affects the structure and presentation of information in the specified frame.
    - Comfy dtype: STRING
    - Python dtype: str
- num_frames
    - The `num_frames' parameter indicates the current frame number at the time of the operation. It is essential for calculating the maximum number of new frames after adding or modifying the text.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- in_text
    - The optional `in_text' parameter allows changes to existing text entries in the schedule. It plays an important role in updating the schedule and avoids duplication.
    - Comfy dtype: STRING
    - Python dtype: str
- max_frames
    - The'max_frames' parameter specifies the maximum number of frames that should be added or modified. It directly affects the time slot of the text in the schedule.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- new_max
    - `new_max' output indicates the maximum number of frames updated by adding or modifying text. It marks a new time boundary in the calendar.
    - Comfy dtype: INT
    - Python dtype: int
- new_text
    - `new_text' output is the updated text content of the agenda added or modified. It reflects the changes made to the text on the specified frame.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class PromptScheduleNodeFlow:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'text': ('STRING', {'multiline': True}), 'num_frames': ('INT', {'default': 24.0, 'min': 0.0, 'max': 9999.0, 'step': 1.0})}, 'optional': {'in_text': ('STRING', {'multiline': False}), 'max_frames': ('INT', {'default': 0.0, 'min': 0.0, 'max': 999999.0, 'step': 1.0})}}
    RETURN_TYPES = ('INT', 'STRING')
    FUNCTION = 'addString'
    CATEGORY = 'FizzNodes 📅🅕🅝/ScheduleNodes'

    def addString(self, text, in_text='', max_frames=0, num_frames=0):
        if in_text:
            in_text = in_text.rstrip(',')
        new_max = num_frames + max_frames
        if max_frames == 0:
            new_text = in_text + (', ' if in_text else '') + f'"{max_frames}": "{text}"'
        else:
            new_text = in_text + (', ' if in_text else '') + f'"{new_max}": "{text}"'
        return (new_max, new_text)
```