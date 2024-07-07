# Documentation
- Class name: loraStackLoader
- Category: EasyUse/Loaders
- Output node: False
- Repo Ref: https://github.com/yolain/ComfyUI-Easy-Use.git

The LoraStack Loader node is designed to simplify the loading and configuration of Lora stacks, which is essential for fine-tuning and improving the performance of neural network models. It simplifys the complexity of managing multiple Lora layers by providing a structured way of designating names, intensity and other relevant parameters.

# Input types
## Required
- toggle
    - The toggle parameter is essential to determine whether the node should carry out its loading process. When set to True, the node will perform the loading of the specified Lora stack; otherwise, it will return without any operation.
    - Comfy dtype: BOOL
    - Python dtype: bool
- mode
    - The mode parameter determines the complexity of the Lora stack configuration. It allows users to select simple or advanced settings that affect the interpretation and application of subsequent parameters.
    - Comfy dtype: STR
    - Python dtype: str
- num_loras
    - Num_loras parameters specify the number of Lora layers that you want to load. It determines how many Lora configurations of direct impact nodes will be handled.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- optional_lora_stack
    - General_lora_stack parameters provide a way to provide nodes with existing Lora stacks. This is very useful for expanding or modifying already configured stacks without starting from scratch.
    - Comfy dtype: LORA_STACK
    - Python dtype: List[Tuple[str, float, float]]
- lora_{i}_name
    - The lora_iname parameter allows the user to specify the name of the Lora layer at the location {i}. This is important for identifying and loading the correct Lora configuration.
    - Comfy dtype: STR
    - Python dtype: str
- lora_{i}_strength
    - The strength of the Lora layer at the location of the {i}_strength parameter. This is the key factor for the weight of the influence of the Lora layer in the model.
    - Comfy dtype: FLOAT
    - Python dtype: float
- lora_{i}_model_strength
    - The lora_(i)_model_strength parameter applies in advanced mode, setting the Lora layer at the position {i} specific to the strength of the model. It is used to fine-tune the influence of Lora on model output.
    - Comfy dtype: FLOAT
    - Python dtype: float
- lora_{i}_clip_strength
    - The lora_clip_strength parameter is also used in advanced mode, which determines the intensity of interaction between the Lora layer and the CLIP model at the location {i]. This is essential for controlling the integration of text-based guidance in model processing.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- lora_stack
    - The lora_stack output is a collection of Lora configurations processed by nodes. It represents the final Lora layer stack that is prepared to be applied to the neural network model.
    - Comfy dtype: LORA_STACK
    - Python dtype: List[Tuple[str, float, float]]

# Usage tips
- Infra type: CPU

# Source code
```
class loraStackLoader:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        max_lora_num = 10
        inputs = {'required': {'toggle': ([True, False],), 'mode': (['simple', 'advanced'],), 'num_loras': ('INT', {'default': 1, 'min': 0, 'max': max_lora_num})}, 'optional': {'optional_lora_stack': ('LORA_STACK',)}}
        for i in range(1, max_lora_num + 1):
            inputs['optional'][f'lora_{i}_name'] = (['None'] + folder_paths.get_filename_list('loras'), {'default': 'None'})
            inputs['optional'][f'lora_{i}_strength'] = ('FLOAT', {'default': 1.0, 'min': -10.0, 'max': 10.0, 'step': 0.01})
            inputs['optional'][f'lora_{i}_model_strength'] = ('FLOAT', {'default': 1.0, 'min': -10.0, 'max': 10.0, 'step': 0.01})
            inputs['optional'][f'lora_{i}_clip_strength'] = ('FLOAT', {'default': 1.0, 'min': -10.0, 'max': 10.0, 'step': 0.01})
        return inputs
    RETURN_TYPES = ('LORA_STACK',)
    RETURN_NAMES = ('lora_stack',)
    FUNCTION = 'stack'
    CATEGORY = 'EasyUse/Loaders'

    def stack(self, toggle, mode, num_loras, lora_stack=None, **kwargs):
        if toggle in [False, None, 'False'] or not kwargs:
            return (None,)
        loras = []
        if lora_stack is not None:
            loras.extend([l for l in lora_stack if l[0] != 'None'])
        for i in range(1, num_loras + 1):
            lora_name = kwargs.get(f'lora_{i}_name')
            if not lora_name or lora_name == 'None':
                continue
            if mode == 'simple':
                lora_strength = float(kwargs.get(f'lora_{i}_strength'))
                loras.append((lora_name, lora_strength, lora_strength))
            elif mode == 'advanced':
                model_strength = float(kwargs.get(f'lora_{i}_model_strength'))
                clip_strength = float(kwargs.get(f'lora_{i}_clip_strength'))
                loras.append((lora_name, model_strength, clip_strength))
        return (loras,)
```