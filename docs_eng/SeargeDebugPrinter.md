# Documentation
- Class name: SeargeDebugPrinter
- Category: DEBUG
- Output node: True
- Repo Ref: https://github.com/jobunk/SeargeSDXL.git

The SeergeDebugPrinter node is designed to provide detailed and formatted output of the data structure to support the debugging process by visualizing the content of the data stream. It emphasizes the structure and relationships within the data, providing clarity in the organization and handling of the information.

# Input types
## Required
- enabled
    - The `enabled' parameter is essential to activate the debugging process. When set to True, it triggers the structure and content of the node output data stream and allows a thorough examination of the data being processed.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
## Optional
- data
    - The 'data'parameter represents the flow of data to be checked and formatted for debugging purposes. It is the core input that determines the content and structure of the output.
    - Comfy dtype: SRG_DATA_STREAM
    - Python dtype: Dict[str, Any]
- prefix
    - The `prefix' parameter is used to add a string at the beginning of each line of output, with an additional emphasis on the readability and organization of the test information. It helps to distinguish the different data points and track the source of the data.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- data
    - The output `data' represents the data stream that was originally entered, and is now accompanied by a detailed and formatted description of its structure and content. This provides a reference for further analysis and validation.
    - Comfy dtype: SRG_DATA_STREAM
    - Python dtype: Dict[str, Any]

# Usage tips
- Infra type: CPU

# Source code
```
class SeargeDebugPrinter:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'enabled': ('BOOLEAN', {'default': True})}, 'optional': {'data': ('SRG_DATA_STREAM',), 'prefix': ('STRING', {'multiline': False, 'default': ''})}}
    RETURN_TYPES = ('SRG_DATA_STREAM',)
    RETURN_NAMES = ('data',)
    FUNCTION = 'output'
    OUTPUT_NODE = True
    CATEGORY = UI.CATEGORY_DEBUG

    def output(self, enabled, data=None, prefix=None):
        if data is None or not enabled:
            return (data,)
        prefix = '' if prefix is None or len(prefix) < 1 else prefix + ': '
        indent_spaces = '· '
        test_data = False
        if test_data:
            data['test_dict'] = {'k1': 1.0, 'k2': 2, 'k3': True}
            data['test_list'] = ['l1', 2.0, 3]
            data['test_tuple'] = (1, 't2', 3.0)

        def print_dict(coll, ind=0, kp='"', pk=True):
            spaces = indent_spaces * ind
            for (k, v) in coll.items():
                print_val(k, v, ind, kp, pk)

        def print_coll(coll, ind=0, kp='', pk=False):
            spaces = indent_spaces * ind
            cl = len(coll)
            for i in range(0, cl):
                v = coll[i]
                print_val(i, v, ind, kp, pk)

        def print_val(k, v, ind=0, kp='"', pk=True):
            spaces = indent_spaces * ind
            key = kp + str(k) + kp + ': ' if pk else ''
            if ind > 10:
                print(prefix + spaces + key + '<max recursion depth>')
                return
            if v is None:
                print(prefix + spaces + key + 'None,')
            elif isinstance(v, int) or isinstance(v, float):
                print(prefix + spaces + key + str(v) + ',')
            elif isinstance(v, str):
                print(prefix + spaces + key + '"' + v + '",')
            elif isinstance(v, dict):
                if k != Names.S_MAGIC_BOX_HIDDEN:
                    print(prefix + spaces + key + '{')
                    print_dict(v, ind + 1, '"', True)
                    print(prefix + spaces + '},')
                else:
                    print(prefix + spaces + key + '{ ... printing skipped ... }')
            elif isinstance(v, list):
                print(prefix + spaces + key + '[')
                print_coll(v, ind + 1, '', True)
                print(prefix + spaces + '],')
            elif isinstance(v, tuple):
                print(prefix + spaces + key + '(')
                print_coll(v, ind + 1, '', False)
                print(prefix + spaces + '),')
            else:
                print(prefix + spaces + key + str(type(v)))
        print(prefix + '===============================================================================')
        if not isinstance(data, dict):
            print(prefix + ' ! invalid data stream !')
        else:
            print(prefix + '* DATA STREAM *')
            print(prefix + '---------------')
            print_val('data', data)
        print(prefix + '===============================================================================')
        return (data,)
```