# Documentation
- Class name: StringSelector
- Category: ImpactPack/Util
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

StringSelector node is designed to process and select a specific string from the given input. It can handle multiple lines and provide options to enable or disable multiple lines. The main purpose of this node is to extract a specific string based on the selection criteria and provide a multifunctional string operation within the ImpactPack application package.

# Input types
## Required
- strings
    - The `strings' parameter is the main input of the node and contains string data to be processed. It plays a key role in node operations, as it is the source from which the selected string will be extracted. The multiline option allows for the processing of strings across multiple lines, enhancing the multifunctionality of node processing different string formats.
    - Comfy dtype: STRING
    - Python dtype: str
- select
    - The `select' parameter is used to specify the index of the string or line that you want to select from the input. It is essential to determine which part of the input data will be the output of the node. Select the index to apply to the modelling of the number of lines or elements to ensure that if it exceeds the available options, it will be recycled.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- multiline
    - The `multiline' parameter determines whether the node should treat the input string as a single entity or as a multiline. When enabled, it allows the node to process the string with a line break and selects according to the content in these lines. This parameter significantly affects the behaviour of the node and the outcome of the string selection process.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- selected_string
    - The `seleted_string' output represents a string selected on the basis of input parameters. It is the result of node processing and reflects the result of string operations performed by node. This output is important because it is the final product of node operations.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class StringSelector:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'strings': ('STRING', {'multiline': True}), 'multiline': ('BOOLEAN', {'default': False, 'label_on': 'enabled', 'label_off': 'disabled'}), 'select': ('INT', {'min': 0, 'max': sys.maxsize, 'step': 1, 'default': 0})}}
    RETURN_TYPES = ('STRING',)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Util'

    def doit(self, strings, multiline, select):
        lines = strings.split('\n')
        if multiline:
            result = []
            current_string = ''
            for line in lines:
                if line.startswith('#'):
                    if current_string:
                        result.append(current_string.strip())
                        current_string = ''
                current_string += line + '\n'
            if current_string:
                result.append(current_string.strip())
            if len(result) == 0:
                selected = strings
            else:
                selected = result[select % len(result)]
            if selected.startswith('#'):
                selected = selected[1:]
        elif len(lines) == 0:
            selected = strings
        else:
            selected = lines[select % len(lines)]
        return (selected,)
```