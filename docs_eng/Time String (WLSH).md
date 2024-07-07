# Documentation
- Class name: WLSH_Time_String
- Category: WLSH Nodes/text
- Output node: False
- Repo Ref: https://github.com/wallish77/wlsh_nodes

The WLSH_Time_String node is designed to generate a time stamp string based on the time format provided. It captures the current date and time and formats it according to the specified style, providing a multifunctional way of accessing time information in human readable form.

# Input types
## Required
- style
    - The'style'parameter determines the format of the output time stamp string. It is vital because it determines the way the date and time are expressed and affects the readability and usefulness of the resulting string.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- time_format
    - The 'time_format'parameter represents the formatted time stamp string for node output. It is important because it is the main result of node operations, and the current date and time are sealed in the specified format.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class WLSH_Time_String:
    time_format = ['%Y%m%d%H%M%S', '%Y%m%d%H%M', '%Y%m%d', '%Y-%m-%d-%H%M%S', '%Y-%m-%d-%H%M', '%Y-%m-%d']

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'style': (s.time_format,)}}
    RETURN_TYPES = ('STRING',)
    RETURN_NAMES = ('time_format',)
    FUNCTION = 'get_time'
    CATEGORY = 'WLSH Nodes/text'

    def get_time(self, style):
        now = datetime.now()
        timestamp = now.strftime(style)
        return (timestamp,)
```