# Documentation
- Class name: CR_ModelList
- Category: Comfyroll/Animation/Legacy
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

The CR_ModelList node is designed to manage and compile a list of models, each of which is linked to a check-point file and an alias. It facilitates the organization and retrieval of a model check point for further processing or animation tasks. This node plays a key role in model management and improves the efficiency of work processes by enabling users to designate multiple check-points and their corresponding aliases.

# Input types
## Required
- ckpt_name1
    - The ckpt_name1 parameter is essential for identifying the first check point file associated with the model. It is a key component of node operations, as it directly affects the selection and organization of model check points in the list.
    - Comfy dtype: STRING
    - Python dtype: str
- alias1
    - Alias1 is an alternative name or identifier for the first check point that allows easier citation and management in the model list. It enhances the function of the node by providing a user-friendly naming agreement for the check point.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- ckpt_name2
    - The ckpt_name2 parameter is optional and can be used to specify a second check point file in the model list. It expands the power of the node by allowing additional check points to be included in the model management process.
    - Comfy dtype: STRING
    - Python dtype: str
- alias2
    - Alias2 is an optional parameter that provides an alternative name for the second check point and enhances the flexibility and user-friendliness of nodes by providing customable naming options for the check point.
    - Comfy dtype: STRING
    - Python dtype: str
- model_list
    - The model_list parameter is optional and allows the user to enter a pre-existing model list. This parameter enhances the adaptability of the node by enabling the external model list to be integrated into the operation of the node.
    - Comfy dtype: MODEL_LIST
    - Python dtype: List[Tuple[str, str]]

# Output types
- MODEL_LIST
    - The MODEL_LIST output parameter represents the list of models compiled, including the relevant checkpoints and aliases. It is an important output because it covers the primary function of node organization and management model check points.
    - Comfy dtype: MODEL_LIST
    - Python dtype: List[Tuple[str, str]]
- show_text
    - Show_text output parameters provide text for the model list, which is very useful for displaying or recording purposes. It reflects the ability of nodes to generate human-readable summaries of model inspection points.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_ModelList:

    @classmethod
    def INPUT_TYPES(cls):
        checkpoint_files = ['None'] + folder_paths.get_filename_list('checkpoints')
        return {'required': {'ckpt_name1': (checkpoint_files,), 'alias1': ('STRING', {'multiline': False, 'default': ''}), 'ckpt_name2': (checkpoint_files,), 'alias2': ('STRING', {'multiline': False, 'default': ''}), 'ckpt_name3': (checkpoint_files,), 'alias3': ('STRING', {'multiline': False, 'default': ''}), 'ckpt_name4': (checkpoint_files,), 'alias4': ('STRING', {'multiline': False, 'default': ''}), 'ckpt_name5': (checkpoint_files,), 'alias5': ('STRING', {'multiline': False, 'default': ''})}, 'optional': {'model_list': ('MODEL_LIST',)}}
    RETURN_TYPES = ('MODEL_LIST', 'STRING')
    RETURN_NAMES = ('MODEL_LIST', 'show_text')
    FUNCTION = 'model_list'
    CATEGORY = icons.get('Comfyroll/Animation/Legacy')

    def model_list(self, ckpt_name1, alias1, ckpt_name2, alias2, ckpt_name3, alias3, ckpt_name4, alias4, ckpt_name5, alias5, model_list=None):
        models = list()
        model_text = list()
        if model_list is not None:
            models.extend([l for l in model_list if l[0] != None])
            model_text += '\n'.join(map(str, model_list)) + '\n'
        if ckpt_name1 != 'None':
            model1_tup = [(alias1, ckpt_name1)]
            (models.extend(model1_tup),)
            model_text += '\n'.join(map(str, model1_tup)) + '\n'
        if ckpt_name2 != 'None':
            model2_tup = [(alias2, ckpt_name2)]
            (models.extend(model2_tup),)
            model_text += '\n'.join(map(str, model2_tup)) + '\n'
        if ckpt_name3 != 'None':
            model3_tup = [(alias3, ckpt_name3)]
            (models.extend(model3_tup),)
            model_text += '\n'.join(map(str, model3_tup)) + '\n'
        if ckpt_name4 != 'None':
            model4_tup = [(alias4, ckpt_name4)]
            (models.extend(model4_tup),)
            model_text += '\n'.join(map(str, model4_tup)) + '\n'
        if ckpt_name5 != 'None':
            model5_tup = [(alias5, ckpt_name5)]
            (models.extend(model5_tup),)
            model_text += '\n'.join(map(str, model5_tup)) + '\n'
        show_text = ''.join(model_text)
        return (models, show_text)
```