# Documentation
- Class name: WAS_DebugThis
- Category: debug
- Output node: True
- Repo Ref: https://github.com/WASasquatch/WAS_Extras

The `debug' method in the `WAS_DebugThis' node serves as an essential tool for developers to check and understand the structure and content of input data. It provides clear and concise input print output that helps to identify any unusual or unexpected behavior. At the development stage, this method is particularly useful for debug purposes, ensuring that input is in line with the desired format and contributing to the overall quality assurance of the system.

# Input types
## Required
- input
    - In the `debug' method, the `input' parameter is essential because it is the data to be checked and printed. It can be any type that allows for the debugging of a wide range of data. The ability of the method to process various data types is essential for its usefulness in the debug scenario, as it can provide insight into complex objects and data structures.
    - Comfy dtype: wildcard
    - Python dtype: Any

# Output types
- None
    - The `debug' method does not return any value. The main function is to print the input data and their properties (if the input is an object). This allows the developer to check the input without changing the process or the status of the input data.
    - Comfy dtype: None
    - Python dtype: NoneType

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_DebugThis:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'input': (wildcard, {})}}
    RETURN_TYPES = ()
    OUTPUT_NODE = True
    FUNCTION = 'debug'
    CATEGORY = 'debug'

    def debug(self, input):
        print('Debug:')
        print(input)
        if isinstance(input, object) and (not isinstance(input, (str, int, float, bool, list, dict, tuple))):
            print('Objects directory listing:')
            pprint(dir(input), indent=4)
        return ()
```