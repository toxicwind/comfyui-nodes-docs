# Documentation
- Class name: CR_RandomWeightLoRA
- Category: Comfyroll/LoRA
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_RandomWeightLoRA node is designed to allocate random weights to the dynamics of the LoRA (low-adaptation) layer in neural network models. It provides a mechanism for introducing variability and customization into model performance by adjusting the effects of a particular LoRA layer. The node operates by generating the only Hashi value for a given set of parameters, and then uses the Hashi value to determine whether new random weights should be assigned. This ensures that the model's output remains somewhat unpredictable while adapting to different input conditions.

# Input types
## Required
- stride
    - A range parameter is essential to determine the length of a node operation. It affects the frequency of node processing input data and can significantly influence the efficiency and results of node execution.
    - Comfy dtype: INT
    - Python dtype: int
- force_randomize_after_stride
    - This parameter indicates whether nodes should be forced to randomize weights after a certain number of steps. It is important to control randomity and ensure that nodes do not fall into predictable patterns.
    - Comfy dtype: COMBO['Off', 'On']
    - Python dtype: str
- lora_name
    - The LoRA name parameter specifies which low-adaptation layer will be targeted. This option is critical because it determines the specific layer where the weight will be randomized.
    - Comfy dtype: STRING
    - Python dtype: str
- switch
    - Switch parameters play a key role in the function of the node by controlling whether the randomization process is activated.
    - Comfy dtype: COMBO['Off', 'On']
    - Python dtype: str
- weight_min
    - The weight_min parameter sets a lower limit for random weights that can be assigned to the LoRA layer. It is essential to define the range of node operations and influences the variability of node output.
    - Comfy dtype: FLOAT
    - Python dtype: float
- weight_max
    - The weight_max parameter sets a ceiling on the range of random weights. It is used in conjunction with weight_min to ensure that the assigned weight falls within the specified area, thereby controlling the behaviour of nodes.
    - Comfy dtype: FLOAT
    - Python dtype: float
- clip_weight
    - The clip_weight parameter is used to cut the assigned weights or limit them to a given value. It ensures that the weight does not exceed the predefined threshold, which is essential for maintaining the stability of node operations.
    - Comfy dtype: FLOAT
    - Python dtype: float
## Optional
- lora_stack
    - The optional lora_stack parameter allows the inclusion of additional LoRA layers in node processing. It provides a method of extending node capacity and customizing its behaviour according to the specific requirements of the task at hand.
    - Comfy dtype: LORA_STACK
    - Python dtype: List[Tuple[str, float, float]]

# Output types
- lora_stack
    - The lora_stack output parameter represents a modified list of LoRA layers with assigned weights after node execution. It is important because it conveys the final output of the node, reflecting the customization applied to the model.
    - Comfy dtype: LORA_STACK
    - Python dtype: List[Tuple[str, float, float]]

# Usage tips
- Infra type: GPU

# Source code
```
class CR_RandomWeightLoRA:

    @classmethod
    def INPUT_TYPES(cls):
        loras = ['None'] + folder_paths.get_filename_list('loras')
        return {'required': {'stride': ('INT', {'default': 1, 'min': 1, 'max': 1000}), 'force_randomize_after_stride': (['Off', 'On'],), 'lora_name': (loras,), 'switch': (['Off', 'On'],), 'weight_min': ('FLOAT', {'default': 0.0, 'min': -10.0, 'max': 10.0, 'step': 0.01}), 'weight_max': ('FLOAT', {'default': 1.0, 'min': -10.0, 'max': 10.0, 'step': 0.01}), 'clip_weight': ('FLOAT', {'default': 1.0, 'min': -10.0, 'max': 10.0, 'step': 0.01})}, 'optional': {'lora_stack': ('LORA_STACK',)}}
    RETURN_TYPES = ('LORA_STACK',)
    FUNCTION = 'random_weight_lora'
    CATEGORY = icons.get('Comfyroll/LoRA')
    LastWeightMap = {}
    StridesMap = {}
    LastHashMap = {}

    @staticmethod
    def getIdHash(lora_name: str, force_randomize_after_stride, stride, weight_min, weight_max, clip_weight) -> int:
        fl_str = f'{lora_name}_{force_randomize_after_stride}_{stride}_{weight_min:.2f}_{weight_max:.2f}_{clip_weight:.2f}'
        return hashlib.sha256(fl_str.encode('utf-8')).hexdigest()

    @classmethod
    def IS_CHANGED(cls, stride, force_randomize_after_stride, lora_name, switch, weight_min, weight_max, clip_weight, lora_stack=None):
        id_hash = CR_RandomWeightLoRA.getIdHash(lora_name, force_randomize_after_stride, stride, weight_min, weight_max, clip_weight)
        if switch == 'Off':
            return id_hash + '_Off'
        if lora_name == 'None':
            return id_hash
        if id_hash not in CR_RandomWeightLoRA.StridesMap:
            CR_RandomWeightLoRA.StridesMap[id_hash] = 0
        CR_RandomWeightLoRA.StridesMap[id_hash] += 1
        if stride > 1 and CR_RandomWeightLoRA.StridesMap[id_hash] < stride and (id_hash in CR_RandomWeightLoRA.LastHashMap):
            return CR_RandomWeightLoRA.LastHashMap[id_hash]
        else:
            CR_RandomWeightLoRA.StridesMap[id_hash] = 0
        last_weight = CR_RandomWeightLoRA.LastWeightMap.get(id_hash, None)
        weight = uniform(weight_min, weight_max)
        if last_weight is not None:
            while weight == last_weight:
                weight = uniform(weight_min, weight_max)
        CR_RandomWeightLoRA.LastWeightMap[id_hash] = weight
        hash_str = f'{id_hash}_{weight:.3f}'
        CR_RandomWeightLoRA.LastHashMap[id_hash] = hash_str
        return hash_str

    def random_weight_lora(self, stride, force_randomize_after_stride, lora_name, switch, weight_min, weight_max, clip_weight, lora_stack=None):
        id_hash = CR_RandomWeightLoRA.getIdHash(lora_name, force_randomize_after_stride, stride, weight_min, weight_max, clip_weight)
        lora_list = list()
        if lora_stack is not None:
            lora_list.extend([l for l in lora_stack if l[0] != 'None'])
        weight = CR_RandomWeightLoRA.LastWeightMap.get(id_hash, 0.0)
        if lora_name != 'None' and switch == 'On':
            (lora_list.extend([(lora_name, weight, clip_weight)]),)
        return (lora_list,)
```