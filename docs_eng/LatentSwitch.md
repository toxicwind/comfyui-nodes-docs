# Documentation
- Class name: GeneralSwitch
- Category: ImpactPack/Util
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The GeneralSwitch node is designed to manage the data stream based on the selection of the index. It determines the activity input by assessing the options provided by the index and then leads the corresponding input route to the output. The node plays a key role in the decision-making process in the workflow, allowing conditional branches to be made on the basis of user-defined criteria.

# Input types
## Required
- select
    - The " singlect " parameter is essential for determining the input to be processed by the node. It specifies the index that should be considered as an input to the activity. The function of the node depends to a large extent on this parameter to carry out its decision-making tasks.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- sel_mode
    - The " sel_mode " parameter determines whether the selection is made on the basis of a hint or an execution context. This affects how the node interprets the selection and, in turn, the execution process of the node.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- input1
    - The "input1" parameter is provided as an optional input to the node. Its function is to provide additional flexibility in node data processing capacity, allowing for more diversified processing of input scenarios.
    - Comfy dtype: ANY
    - Python dtype: Any
- unique_id
    - The “unique_id” parameter is used to identify nodes in the workflow. It plays a crucial role in the ability of the node to refer to its own location and context in the larger system.
    - Comfy dtype: UNIQUE_ID
    - Python dtype: str
- extra_pnginfo
    - The " extra_pnginfo " parameter contains additional information that may be required for the normal operation of the node. It provides details of the particular context in which the node can be enhanced.
    - Comfy dtype: EXTRA_PNGINFO
    - Python dtype: Dict[str, Any]

# Output types
- selected_value
    - The "selected_value" output represents the input value selected by the node on the basis of the provided options index. It is a key output because it carries data processing that will be further processed or used downstream in the workflow.
    - Comfy dtype: ANY
    - Python dtype: Any
- selected_label
    - The "selected_label" output provides labels associated with the selected input. This is very useful for providing human-readable identifiers for the selected data and enhances the interpretability of node output.
    - Comfy dtype: STRING
    - Python dtype: str
- selected_index
    - The " selected_index " output indicates the index that is selected for input. It is used as a record of the decision-making process for the recording nodes and can be used in workflows to track or record purposes.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class GeneralSwitch:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'select': ('INT', {'default': 1, 'min': 1, 'max': 999999, 'step': 1}), 'sel_mode': ('BOOLEAN', {'default': True, 'label_on': 'select_on_prompt', 'label_off': 'select_on_execution', 'forceInput': False})}, 'optional': {'input1': (any_typ,)}, 'hidden': {'unique_id': 'UNIQUE_ID', 'extra_pnginfo': 'EXTRA_PNGINFO'}}
    RETURN_TYPES = (any_typ, 'STRING', 'INT')
    RETURN_NAMES = ('selected_value', 'selected_label', 'selected_index')
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Util'

    def doit(self, *args, **kwargs):
        selected_index = int(kwargs['select'])
        input_name = f'input{selected_index}'
        selected_label = input_name
        node_id = kwargs['unique_id']
        nodelist = kwargs['extra_pnginfo']['workflow']['nodes']
        for node in nodelist:
            if str(node['id']) == node_id:
                inputs = node['inputs']
                for slot in inputs:
                    if slot['name'] == input_name and 'label' in slot:
                        selected_label = slot['label']
                break
        if input_name in kwargs:
            return (kwargs[input_name], selected_label, selected_index)
        else:
            print(f'ImpactSwitch: invalid select index (ignored)')
            return (None, '', selected_index)
```