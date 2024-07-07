# Documentation
- Class name: CR_LoRAStack
- Category: Comfyroll/LoRA
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

The CR_LoRAStack node is designed to manage and assemble multiple LoRA (low-adaptation) layers into a single warehouse. It allows users to switch the content of each LoRA layer, set model weights and edit the weights to fine-tune the contribution of each layer to the final output. The function of the node is concentrated in stacking the LoRA layer to enhance model performance without significantly increasing costing.

# Input types
## Required
- switch_1
    - Switch parameters determine whether or not to include the first LoRA layer in the pad. It is essential to control the final composition of the LoRA stack.
    - Comfy dtype: COMBO['Off', 'On']
    - Python dtype: str
- lora_name_1
    - The lora_name_1 parameter specifies the name of the first LoRA layer that may be contained in the stack. It plays an important role in identifying a particular LoRA layer during the stacking process.
    - Comfy dtype: STRING
    - Python dtype: str
- model_weight_1
    - Model_weight_1 parameter adjusts the impact of the first LoRA layer on the final output. It is essential to fine-tune the contribution of each layer.
    - Comfy dtype: FLOAT
    - Python dtype: float
- clip_weight_1
    - The clip_weight_1 parameter is used to edit or limit the weight of the first LoRA layer in order to prevent its over-absorption of the final output.
    - Comfy dtype: FLOAT
    - Python dtype: float
- switch_2
    - The second LoRA layer switch parameters determine whether they are contained in the shed. It plays a key role in determining the final structure of LoRA.
    - Comfy dtype: COMBO['Off', 'On']
    - Python dtype: str
- lora_name_2
    - The lora_name_2 parameter specifies the name of the second LoRA layer to be considered for addition to the warehouse. It is a key factor in identifying the LoRA layer.
    - Comfy dtype: STRING
    - Python dtype: str
- model_weight_2
    - Model_weight_2 parameters modify the impact of the second LoRA layer on the final result. It is indispensable for calibrating the contribution of the layer.
    - Comfy dtype: FLOAT
    - Python dtype: float
- clip_weight_2
    - The clip_weight_2 parameter is responsible for editing the weight of the second LoRA layer in order to maintain the balance of the final output.
    - Comfy dtype: FLOAT
    - Python dtype: float
- switch_3
    - The third LoRA layer switch parameters control its presence in the stack. It is a key element in the formation of LoRA.
    - Comfy dtype: COMBO['Off', 'On']
    - Python dtype: str
- lora_name_3
    - The lora_name_3 parameter identification may be contained in the third LoRA layer in the warehouse. It is essential for the selection process of the LoRA layer.
    - Comfy dtype: STRING
    - Python dtype: str
- model_weight_3
    - The model_weight_3 parameter influences the impact of the third LoRA layer on the final result. It is essential to adjust the impact of the layer.
    - Comfy dtype: FLOAT
    - Python dtype: float
- clip_weight_3
    - The weight of the third LoRA layer of the clip_weight_3 parameter clip to ensure that it does not disproportionately affect the output of the final warehouse.
    - Comfy dtype: FLOAT
    - Python dtype: float
## Optional
- lora_stack
    - The lora_stack parameter allows the existing layer to be prefilled with LoRA. It applies to the continuation of work from the previous state.
    - Comfy dtype: LORA_STACK
    - Python dtype: List[Tuple[str, float, float]]

# Output types
- LORA_STACK
    - LORA_STACK output is a meta-list that shows the stacked LoRA layer and its corresponding weights and editing values. This is the main result of the node operation.
    - Comfy dtype: LORA_STACK
    - Python dtype: List[Tuple[str, float, float]]
- show_help
    - Show_help output provides a URL link to a document to get more help and information about the use of nodes.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_LoRAStack:

    @classmethod
    def INPUT_TYPES(cls):
        loras = ['None'] + folder_paths.get_filename_list('loras')
        return {'required': {'switch_1': (['Off', 'On'],), 'lora_name_1': (loras,), 'model_weight_1': ('FLOAT', {'default': 1.0, 'min': -10.0, 'max': 10.0, 'step': 0.01}), 'clip_weight_1': ('FLOAT', {'default': 1.0, 'min': -10.0, 'max': 10.0, 'step': 0.01}), 'switch_2': (['Off', 'On'],), 'lora_name_2': (loras,), 'model_weight_2': ('FLOAT', {'default': 1.0, 'min': -10.0, 'max': 10.0, 'step': 0.01}), 'clip_weight_2': ('FLOAT', {'default': 1.0, 'min': -10.0, 'max': 10.0, 'step': 0.01}), 'switch_3': (['Off', 'On'],), 'lora_name_3': (loras,), 'model_weight_3': ('FLOAT', {'default': 1.0, 'min': -10.0, 'max': 10.0, 'step': 0.01}), 'clip_weight_3': ('FLOAT', {'default': 1.0, 'min': -10.0, 'max': 10.0, 'step': 0.01})}, 'optional': {'lora_stack': ('LORA_STACK',)}}
    RETURN_TYPES = ('LORA_STACK', 'STRING')
    RETURN_NAMES = ('LORA_STACK', 'show_help')
    FUNCTION = 'lora_stacker'
    CATEGORY = icons.get('Comfyroll/LoRA')

    def lora_stacker(self, lora_name_1, model_weight_1, clip_weight_1, switch_1, lora_name_2, model_weight_2, clip_weight_2, switch_2, lora_name_3, model_weight_3, clip_weight_3, switch_3, lora_stack=None):
        lora_list = list()
        if lora_stack is not None:
            lora_list.extend([l for l in lora_stack if l[0] != 'None'])
        if lora_name_1 != 'None' and switch_1 == 'On':
            (lora_list.extend([(lora_name_1, model_weight_1, clip_weight_1)]),)
        if lora_name_2 != 'None' and switch_2 == 'On':
            (lora_list.extend([(lora_name_2, model_weight_2, clip_weight_2)]),)
        if lora_name_3 != 'None' and switch_3 == 'On':
            (lora_list.extend([(lora_name_3, model_weight_3, clip_weight_3)]),)
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/LoRA-Nodes#cr-lora-stack'
        return (lora_list, show_help)
```