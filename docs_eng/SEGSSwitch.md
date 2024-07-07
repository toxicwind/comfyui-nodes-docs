# Documentation
- Class name: GeneralSwitch
- Category: ImpactPack/Util
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The GeneralSwitch node is designed to manage and route data according to the selected index. It selects an input based on the index provided and retrieves the corresponding labels from the node information of the workflow. The node plays a key role in the decision-making process in the workflow, allowing for the execution of the condition path.

# Input types
## Required
- select
    - The parameter'select' is essential to determine which input will be processed by the node. It directs the node to identify the selection index for the correct input for further action in the workflow.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- sel_mode
    - Parameter'sel_mode' allows the user to specify whether the selection should be based on a hint or an execution context. This affects how the node interprets and responds to input and affects the overall behaviour of the workflow.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- input1
    - The parameter 'input1' is provided as an optional input to nodes. Its function is to provide additional flexibility to process various types of data and to enhance the adaptability of nodes in different workstream scenarios.
    - Comfy dtype: ANY
    - Python dtype: Any
- unique_id
    - The parameter 'unique_id' is used for a particular node in the internal identification workflow. It plays a vital role in the ability of the node to quote its input and configuration settings.
    - Comfy dtype: UNIQUE_ID
    - Python dtype: str
- extra_pnginfo
    - The parameter 'extra_pnginfo' contains additional information about the visual expression of the node in the workflow. It helps to define the look of the node and provides relevant contextual information.
    - Comfy dtype: EXTRA_PNGINFO
    - Python dtype: Dict[str, Any]

# Output types
- selected_value
    - Output'selected_value' represents data selected on the basis of input index selection. It is a key component of node operations, as it determines the data to be passed on to subsequent processing.
    - Comfy dtype: ANY
    - Python dtype: Any
- selected_label
    - Output'selected_label' provides labels associated with the selected input. This is useful for providing context or additional information about the data being processed.
    - Comfy dtype: STRING
    - Python dtype: str
- selected_index
    - Output the'selected_index' instruction is used to select the index that you want to enter. It can be used as a reference for tracking selection in the workflow.
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