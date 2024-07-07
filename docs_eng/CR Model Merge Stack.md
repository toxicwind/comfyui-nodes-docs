# Documentation
- Class name: CR_ModelMergeStack
- Category: Comfyroll/Model Merge
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

The CR_ModelMergeStack node is designed to merge multiple model check points into a single stack. It allows users to switch to include each check point and adjusts the contribution ratio of the models and clip components to provide a flexible approach to combining different models based on specific needs.

# Input types
## Required
- switch_1
    - The switch_1 parameter decides whether to include the first check point in a model store. It plays a key role in the operation of the node by enabling or disableing the integration of a particular check point.
    - Comfy dtype: COMBO['Off', 'On']
    - Python dtype: str
- ckpt_name1
    - ckpt_name1 parameters specify the name of the first check-point file that you want to potentially contain in the template. This is essential for identifying the particular model that you want to merge.
    - Comfy dtype: STRING
    - Python dtype: str
- model_ratio1
    - The model_ratio1 parameter adjusts the contribution weight of the model component of the first check point in the compound. It is important to fine-tune the impact of each model in the final output.
    - Comfy dtype: FLOAT
    - Python dtype: float
- clip_ratio1
    - The clip_ratio1 parameter sets the contribution weight of the editing component of the first check point. It is important to balance the overall impact of the editing guide in the consolidation matrix.
    - Comfy dtype: FLOAT
    - Python dtype: float
- switch_2
    - The switch_2 parameter controls whether the second check point is included in the model pad. Similar to switch_1, it is essential to select which checkpoints are integrated into the final stack.
    - Comfy dtype: COMBO['Off', 'On']
    - Python dtype: str
- ckpt_name2
    - ckpt_name2 parameter identification may be included in a second checkpoint file in a model warehouse. It is a key factor in determining the model to be merged.
    - Comfy dtype: STRING
    - Python dtype: str
- model_ratio2
    - Model_ratio2 parameters modify the weight of the model component in the warehouse for the second check point. It influences the salient features of the model in the combined output.
    - Comfy dtype: FLOAT
    - Python dtype: float
- clip_ratio2
    - The clip_ratio2 parameter defines the weight of the editing component of the second check point, affecting the extent to which the editing guidance is taken into account in the merged model stack.
    - Comfy dtype: FLOAT
    - Python dtype: float
- switch_3
    - The switch_3 parameter decides whether to include the third check point in the model store. It is another key switch that controls the final stacking.
    - Comfy dtype: COMBO['Off', 'On']
    - Python dtype: str
- ckpt_name3
    - ckpt_name3 parameters specify a third checkpoint file that may be part of a model warehouse. It is essential to include a particular model in the consolidation process.
    - Comfy dtype: STRING
    - Python dtype: str
- model_ratio3
    - It is important for the overall balance of model contributions.
    - Comfy dtype: FLOAT
    - Python dtype: float
- clip_ratio3
    - The clip_ratio3 parameter sets the impact level of the editing component of the third check point in the back. It is important for the final mix of editing instructions in the merged model.
    - Comfy dtype: FLOAT
    - Python dtype: float
## Optional
- model_stack
    - The optional model_stack parameter allows the user to provide a list of initial models to be merged. It is useful for building on the existing matrix.
    - Comfy dtype: MODEL_STACK
    - Python dtype: List[Tuple[str, float, float]]

# Output types
- MODEL_STACK
    - The MODEL_STACK output contains a list of consolidated model checkpoints with their respective ratios. It is the main result of node operations and represents a consolidated model pad.
    - Comfy dtype: MODEL_STACK
    - Python dtype: List[Tuple[str, float, float]]
- show_help
    - Show_help output provides a URL link to the document for more help. It guides the user to external resources for more information about node functions.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_ModelMergeStack:

    @classmethod
    def INPUT_TYPES(cls):
        checkpoint_files = ['None'] + folder_paths.get_filename_list('checkpoints')
        return {'required': {'switch_1': (['Off', 'On'],), 'ckpt_name1': (checkpoint_files,), 'model_ratio1': ('FLOAT', {'default': 1.0, 'min': -100.0, 'max': 100.0, 'step': 0.01}), 'clip_ratio1': ('FLOAT', {'default': 1.0, 'min': -100.0, 'max': 100.0, 'step': 0.01}), 'switch_2': (['Off', 'On'],), 'ckpt_name2': (checkpoint_files,), 'model_ratio2': ('FLOAT', {'default': 1.0, 'min': -100.0, 'max': 100.0, 'step': 0.01}), 'clip_ratio2': ('FLOAT', {'default': 1.0, 'min': -100.0, 'max': 100.0, 'step': 0.01}), 'switch_3': (['Off', 'On'],), 'ckpt_name3': (checkpoint_files,), 'model_ratio3': ('FLOAT', {'default': 1.0, 'min': -100.0, 'max': 100.0, 'step': 0.01}), 'clip_ratio3': ('FLOAT', {'default': 1.0, 'min': -100.0, 'max': 100.0, 'step': 0.01})}, 'optional': {'model_stack': ('MODEL_STACK',)}}
    RETURN_TYPES = ('MODEL_STACK', 'STRING')
    RETURN_NAMES = ('MODEL_STACK', 'show_help')
    FUNCTION = 'list_checkpoints'
    CATEGORY = icons.get('Comfyroll/Model Merge')

    def list_checkpoints(self, switch_1, ckpt_name1, model_ratio1, clip_ratio1, switch_2, ckpt_name2, model_ratio2, clip_ratio2, switch_3, ckpt_name3, model_ratio3, clip_ratio3, model_stack=None):
        model_list = list()
        if model_stack is not None:
            model_list.extend([l for l in model_stack if l[0] != 'None'])
        if ckpt_name1 != 'None' and switch_1 == 'On':
            (model_list.extend([(ckpt_name1, model_ratio1, clip_ratio1)]),)
        if ckpt_name2 != 'None' and switch_2 == 'On':
            (model_list.extend([(ckpt_name2, model_ratio2, clip_ratio2)]),)
        if ckpt_name3 != 'None' and switch_3 == 'On':
            (model_list.extend([(ckpt_name3, model_ratio3, clip_ratio3)]),)
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Model-Merge-Nodes#cr-model-stack'
        return (model_list, show_help)
```