# Documentation
- Class name: CR_ValueCycler
- Category: Comfyroll/List
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_ValueCycler is an interactive list of string values, which converts each string into a floating point and an integer. It loops through the text values provided in the calendar, repeats the specified number of times, and circulates through the list within the set number of overlaps. This node is particularly suitable for processing the value data in the text format to make it easier to process and analyse in subsequent operations.

# Input types
## Required
- values
    - The `values' parameter is a multi-line string containing numerical data to be processed. It is essential because it is an input data set that overlaps with nodes and is converted to numerical format.
    - Comfy dtype: STRING
    - Python dtype: str
- repeats
    - The `repeats' parameter indicates the number of times that each item in the list will be recycled. It is important because it controls the range of data processing and may affect the output size.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- loops
    - The 'loops' parameter specifies the total number of loops that will occur. It is an optional setting that can be used to further control the operation and output generation of nodes.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- FLOAT
    - The `FLOAT' output provides a list of input text values converted to floating points to facilitate numerical analysis and processing.
    - Comfy dtype: FLOAT
    - Python dtype: List[float]
- INT
    - The `INT' output consists of an integer conversion of input text values, which provides another value format for data processing.
    - Comfy dtype: INT
    - Python dtype: List[int]
- show_text
    - The `show_text' output is a string that provides a link to the node document to help users understand the function and usage of the node.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_ValueCycler:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'values': ('STRING', {'multiline': True, 'default': ''}), 'repeats': ('INT', {'default': 1, 'min': 1, 'max': 99999}), 'loops': ('INT', {'default': 1, 'min': 1, 'max': 99999})}}
    RETURN_TYPES = ('FLOAT', 'INT', 'STRING')
    RETURN_NAMES = ('FLOAT', 'INT', 'show_text')
    OUTPUT_IS_LIST = (True, True, False)
    FUNCTION = 'cycle'
    CATEGORY = icons.get('Comfyroll/List')

    def cycle(self, values, repeats, loops=1):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/List-Nodes#cr-value-cycler'
        lines = values.split('\n')
        float_list_out = []
        int_list_out = []
        for i in range(loops):
            for _ in range(repeats):
                for text_item in lines:
                    if all((char.isdigit() or char == '.' for char in text_item.strip())):
                        float_list_out.append(float(text_item))
                        int_list_out.append(int(float(text_item)))
        return (float_list_out, int_list_out, show_help)
```