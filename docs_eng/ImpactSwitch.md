# Documentation
- Class name: GeneralSwitch
- Category: ImpactPack/Util
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The GeneralSwitch node is designed to manage the flow of data in the stream by selecting the input of a particular index. It operates by assessing the index provided and determining the corresponding input for processing. The node plays a key role in the decision-making process in the system to ensure that the correct data is directed to follow-up operations.

# Input types
## Required
- select
    - The'select' parameter is essential because it determines the input to be processed by the node. As a decision-making factor, it allows nodes to identify and select the appropriate input from the available options.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- sel_mode
    - The'sel_mode'parameter is used to determine whether the selection is based on a reminder or an implementation context. It provides flexibility in the manner in which nodes are interpreted and responded to the selection criteria.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- input1
    - The 'input1'parameter is an optional input that can be provided to nodes. It allows for more flexible data types to be processed and increases the adaptability of nodes in various workflows.
    - Comfy dtype: ANY
    - Python dtype: Any
- unique_id
    - The 'unique_id'parameter is a hidden field that helps to identify a particular node in the workflow. It is important for internal tracking and ensures that node operations are correctly associated with its position in the workflow.
    - Comfy dtype: UNIQUE_ID
    - Python dtype: str
- extra_pnginfo
    - The 'extra_pnginfo'parameter contains additional information relevant to node operations, such as detailed workflow information. It is used internally to facilitate interaction between nodes and the wider system.
    - Comfy dtype: EXTRA_PNGINFO
    - Python dtype: Dict[str, Any]

# Output types
- selected_value
    - The'selected_value' output represents the data selected by the node based on the index provided. This is a key output because it determines the flow of data to the following node in the workflow.
    - Comfy dtype: ANY
    - Python dtype: Any
- selected_label
    - The'selected_label' output provides labels associated with the selected input. This is very useful for debugging and providing context for node decision-making processes.
    - Comfy dtype: STRING
    - Python dtype: str
- selected_index
    - The'selected_index' output instruction is used to select the index to be entered. The record of the decision it makes as a node may be important for audit and tracking purposes.
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