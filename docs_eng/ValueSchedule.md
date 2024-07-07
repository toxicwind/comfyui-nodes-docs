# Documentation
- Class name: ValueSchedule
- Category: FizzNodes 📅🅕🅝/ScheduleNodes
- Output node: False
- Repo Ref: https://github.com/FizzleDorf/ComfyUI_FizzNodes

The ValueSchedule node is designed to animate and insert values according to the given key frame text. It selects the key frame values by parsing the text input, and then inserts values between these key frames to create a smooth value transition on the specified number of frames.

# Input types
## Required
- text
    - The `text' parameter is a string that contains a definition of the key frame used for animating values. It is essential for the operation of the node, as it directly affects the output animation sequence.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- max_frames
    - The `max_frames' parameter specifies the total number of frames that animated events occur. It is essential to determine the range of values to be inserted.
    - Comfy dtype: INT
    - Python dtype: int
- current_frame
    - The `current_frame' parameter indicates the current position in the animation sequence. It is important for calculating the plug value of the current status of the animation.
    - Comfy dtype: INT
    - Python dtype: int
- print_output
    - When set to True, the 'print_output' parameter allows printing the current frame and its plug-in to the console. This is very useful for debugging.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- value
    - The 'value'output represents the plug-in value of the current frame. This is the main output of the node and is essential for the continuation of animation or further processing.
    - Comfy dtype: FLOAT
    - Python dtype: float
- frame_number
    - The 'frame_number'output provides an index of the current frame in the animation sequence. It can be used to track the progress of the animation.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class ValueSchedule:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'text': ('STRING', {'multiline': True, 'default': defaultValue}), 'max_frames': ('INT', {'default': 120.0, 'min': 1.0, 'max': 999999.0, 'step': 1.0}), 'current_frame': ('INT', {'default': 0.0, 'min': 0.0, 'max': 999999.0, 'step': 1.0}), 'print_output': ('BOOLEAN', {'default': False})}}
    RETURN_TYPES = ('FLOAT', 'INT')
    FUNCTION = 'animate'
    CATEGORY = 'FizzNodes 📅🅕🅝/ScheduleNodes'

    def animate(self, text, max_frames, current_frame, print_output):
        current_frame = current_frame % max_frames
        t = get_inbetweens(parse_key_frames(text, max_frames), max_frames)
        if print_output is True:
            print('ValueSchedule: ', current_frame, '\n', 'current_frame: ', current_frame)
        return (t[current_frame], int(t[current_frame]))
```