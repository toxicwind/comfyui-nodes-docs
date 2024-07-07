# Documentation
- Class name: CR_RandomLoRAStack
- Category: Comfyroll/LoRA
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_RandomLoRAStack is designed to randomly stack the LoRA (low-adaptation) module onto the base model. It deals intelligently with the selection and application of the LoRA module based on assigned weights, opportunities and exclusivity, ensuring diversity and controlled enhancement of model capabilities.

# Input types
## Required
- exclusive_mode
    - The exclusive mode decides whether to apply only one LoRA at a time. When set to 'On', it enforces mutuality and ensures that node operations are non-redundant and focused.
    - Comfy dtype: COMBO['Off', 'On']
    - Python dtype: str
- stride
    - Step defines the interval between node re-evaluation of LoRA stacks. It is essential to control the frequency of LoRA applications, thus affecting the overall performance of nodes.
    - Comfy dtype: INT
    - Python dtype: int
- force_randomize_after_stride
    - When this parameter is enabled, the node randomizes the LoRA selection after a certain number of steps, adding unpredictable elements to the operation of the node.
    - Comfy dtype: COMBO['Off', 'On']
    - Python dtype: str
- lora_name_1
    - Consider the first LoRA module to stack. Its selection can significantly change the function of the node, introduce new features or modify existing ones.
    - Comfy dtype: STRING
    - Python dtype: str
- chance_1
    - The probability of applying the first LoRA module. It plays a key role in the randomity of node operations, allowing a degree of controllability.
    - Comfy dtype: FLOAT
    - Python dtype: float
- model_weight_1
    - The weight assigned to the first LoRA module affects the extent to which it affects the final output of the node. It is a key factor in the behaviour of the microregulating point.
    - Comfy dtype: FLOAT
    - Python dtype: float
- clip_weight_1
    - The cutting weight of the first LoRA module can help control the intensity of LoRA's influence on node output.
    - Comfy dtype: FLOAT
    - Python dtype: float
- switch_1
    - Determines whether the first LoRA module is a activated switch. It is a simple and efficient method for switching the content of the LoRA module in node operations.
    - Comfy dtype: COMBO['Off', 'On']
    - Python dtype: str
## Optional
- lora_name_2
    - A second LoRA module for stacking could be considered, providing additional options for enhancing the capacity of nodes.
    - Comfy dtype: STRING
    - Python dtype: str
- chance_2
    - The probability associated with the second LoRA module further contributes to random behaviour at nodes.
    - Comfy dtype: FLOAT
    - Python dtype: float
- model_weight_2
    - The weight of the second LoRA module allows for fine control of its contribution to node output.
    - Comfy dtype: FLOAT
    - Python dtype: float
- clip_weight_2
    - The editing weight of the second LoRA module provides a mechanism for adjusting its impact on node results.
    - Comfy dtype: FLOAT
    - Python dtype: float
- switch_2
    - The switch of the second LoRA module allows flexibility to control its activation during nodes.
    - Comfy dtype: COMBO['Off', 'On']
    - Python dtype: str
- lora_name_3
    - The stacked third LoRA module option provides further diversity of potential functions of nodes.
    - Comfy dtype: STRING
    - Python dtype: str
- chance_3
    - The probability of the third LoRA module adds another layer of randomity to the operation of nodes.
    - Comfy dtype: FLOAT
    - Python dtype: float
- model_weight_3
    - The weight assigned to the third LoRA module affects its effect on node output in stacking.
    - Comfy dtype: FLOAT
    - Python dtype: float
- clip_weight_3
    - The cut weight of the third LoRA module allows fine particle size control of its impact on the final outcome of the node.
    - Comfy dtype: FLOAT
    - Python dtype: float
- switch_3
    - The third LoRA module switch provides options that contain or exclude it in node operations.
    - Comfy dtype: COMBO['Off', 'On']
    - Python dtype: str
- lora_stack
    - This allows customization and preset LoRA stacking before further randomization.
    - Comfy dtype: LORA_STACK
    - Python dtype: List[Tuple[str, float, float]]

# Output types
- lora_stack
    - Output is a randomly selected and weighted LoRA module stack based on input parameters. This stack plays a key role in modifying the behavior of the underlying model based on node configuration.
    - Comfy dtype: LORA_STACK
    - Python dtype: List[Tuple[str, float, float]]

# Usage tips
- Infra type: CPU

# Source code
```
class CR_RandomLoRAStack:

    @classmethod
    def INPUT_TYPES(cls):
        loras = ['None'] + folder_paths.get_filename_list('loras')
        return {'required': {'exclusive_mode': (['Off', 'On'],), 'stride': ('INT', {'default': 1, 'min': 1, 'max': 1000}), 'force_randomize_after_stride': (['Off', 'On'],), 'lora_name_1': (loras,), 'switch_1': (['Off', 'On'],), 'chance_1': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'model_weight_1': ('FLOAT', {'default': 1.0, 'min': -10.0, 'max': 10.0, 'step': 0.01}), 'clip_weight_1': ('FLOAT', {'default': 1.0, 'min': -10.0, 'max': 10.0, 'step': 0.01}), 'lora_name_2': (loras,), 'switch_2': (['Off', 'On'],), 'chance_2': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'model_weight_2': ('FLOAT', {'default': 1.0, 'min': -10.0, 'max': 10.0, 'step': 0.01}), 'clip_weight_2': ('FLOAT', {'default': 1.0, 'min': -10.0, 'max': 10.0, 'step': 0.01}), 'lora_name_3': (loras,), 'switch_3': (['Off', 'On'],), 'chance_3': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'model_weight_3': ('FLOAT', {'default': 1.0, 'min': -10.0, 'max': 10.0, 'step': 0.01}), 'clip_weight_3': ('FLOAT', {'default': 1.0, 'min': -10.0, 'max': 10.0, 'step': 0.01})}, 'optional': {'lora_stack': ('LORA_STACK',)}}
    RETURN_TYPES = ('LORA_STACK',)
    FUNCTION = 'random_lora_stacker'
    CATEGORY = icons.get('Comfyroll/LoRA')
    UsedLorasMap = {}
    StridesMap = {}
    LastHashMap = {}

    @staticmethod
    def getIdHash(lora_name_1: str, lora_name_2: str, lora_name_3: str) -> int:
        id_set = set([lora_name_1, lora_name_2, lora_name_3])
        id_hash = hash(frozenset(id_set))
        return id_hash

    @staticmethod
    def deduplicateLoraNames(lora_name_1: str, lora_name_2: str, lora_name_3: str):
        is_same_1 = False
        is_same_2 = False
        is_same_3 = False
        if lora_name_1 == lora_name_2:
            is_same_1 = True
            is_same_2 = True
        if lora_name_1 == lora_name_3:
            is_same_1 = True
            is_same_3 = True
        if lora_name_2 == lora_name_3:
            is_same_2 = True
            is_same_3 = True
        if is_same_1:
            lora_name_1 = lora_name_1 + 'CR_RandomLoRAStack_1'
        if is_same_2:
            lora_name_2 = lora_name_2 + 'CR_RandomLoRAStack_2'
        if is_same_3:
            lora_name_3 = lora_name_3 + 'CR_RandomLoRAStack_3'
        return (lora_name_1, lora_name_2, lora_name_3)

    @staticmethod
    def cleanLoraName(lora_name) -> str:
        if 'CR_RandomLoRAStack_1' in lora_name:
            lora_name = lora_name.replace('CR_RandomLoRAStack_1', '')
        elif 'CR_RandomLoRAStack_2' in lora_name:
            lora_name = lora_name.replace('CR_RandomLoRAStack_2', '')
        elif 'CR_RandomLoRAStack_3' in lora_name:
            lora_name = lora_name.replace('CR_RandomLoRAStack_3', '')
        return lora_name

    @classmethod
    def IS_CHANGED(cls, exclusive_mode, stride, force_randomize_after_stride, lora_name_1, model_weight_1, clip_weight_1, switch_1, chance_1, lora_name_2, model_weight_2, clip_weight_2, switch_2, chance_2, lora_name_3, model_weight_3, clip_weight_3, switch_3, chance_3, lora_stack=None):
        lora_set = set()
        (lora_name_1, lora_name_2, lora_name_3) = CR_RandomLoRAStack.deduplicateLoraNames(lora_name_1, lora_name_2, lora_name_3)
        id_hash = CR_RandomLoRAStack.getIdHash(lora_name_1, lora_name_2, lora_name_3)
        if id_hash not in CR_RandomLoRAStack.StridesMap:
            CR_RandomLoRAStack.StridesMap[id_hash] = 0
        CR_RandomLoRAStack.StridesMap[id_hash] += 1
        if stride > 1 and CR_RandomLoRAStack.StridesMap[id_hash] < stride and (id_hash in CR_RandomLoRAStack.LastHashMap):
            return CR_RandomLoRAStack.LastHashMap[id_hash]
        else:
            CR_RandomLoRAStack.StridesMap[id_hash] = 0
        total_on = 0
        if lora_name_1 != 'None' and switch_1 == 'On' and (chance_1 > 0.0):
            total_on += 1
        if lora_name_2 != 'None' and switch_2 == 'On' and (chance_2 > 0.0):
            total_on += 1
        if lora_name_3 != 'None' and switch_3 == 'On' and (chance_3 > 0.0):
            total_on += 1

        def perform_randomization() -> set:
            _lora_set = set()
            rand_1 = random()
            rand_2 = random()
            rand_3 = random()
            apply_1 = True if rand_1 <= chance_1 and switch_1 == 'On' else False
            apply_2 = True if rand_2 <= chance_2 and switch_2 == 'On' else False
            apply_3 = True if rand_3 <= chance_3 and switch_3 == 'On' else False
            num_to_apply = sum([apply_1, apply_2, apply_3])
            if exclusive_mode == 'On' and num_to_apply > 1:
                rand_dict = {}
                if apply_1:
                    rand_dict[1] = rand_1
                if apply_2:
                    rand_dict[2] = rand_2
                if apply_3:
                    rand_dict[3] = rand_3
                sorted_rands = sorted(rand_dict.keys(), key=lambda k: rand_dict[k])
                if sorted_rands[0] == 1:
                    apply_2 = False
                    apply_3 = False
                elif sorted_rands[0] == 2:
                    apply_1 = False
                    apply_3 = False
                elif sorted_rands[0] == 3:
                    apply_1 = False
                    apply_2 = False
            if lora_name_1 != 'None' and switch_1 == 'On' and apply_1:
                _lora_set.add(lora_name_1)
            if lora_name_2 != 'None' and switch_2 == 'On' and apply_2:
                _lora_set.add(lora_name_2)
            if lora_name_3 != 'None' and switch_3 == 'On' and apply_3:
                _lora_set.add(lora_name_3)
            return _lora_set
        last_lora_set = CR_RandomLoRAStack.UsedLorasMap.get(id_hash, set())
        lora_set = perform_randomization()
        if force_randomize_after_stride == 'On' and len(last_lora_set) > 0 and (total_on > 1):
            while lora_set == last_lora_set:
                lora_set = perform_randomization()
        CR_RandomLoRAStack.UsedLorasMap[id_hash] = lora_set
        hash_str = str(hash(frozenset(lora_set)))
        CR_RandomLoRAStack.LastHashMap[id_hash] = hash_str
        return hash_str

    def random_lora_stacker(self, exclusive_mode, stride, force_randomize_after_stride, lora_name_1, model_weight_1, clip_weight_1, switch_1, chance_1, lora_name_2, model_weight_2, clip_weight_2, switch_2, chance_2, lora_name_3, model_weight_3, clip_weight_3, switch_3, chance_3, lora_stack=None):
        lora_list = list()
        if lora_stack is not None:
            lora_list.extend([l for l in lora_stack if l[0] != 'None'])
        (lora_name_1, lora_name_2, lora_name_3) = CR_RandomLoRAStack.deduplicateLoraNames(lora_name_1, lora_name_2, lora_name_3)
        id_hash = CR_RandomLoRAStack.getIdHash(lora_name_1, lora_name_2, lora_name_3)
        used_loras = CR_RandomLoRAStack.UsedLorasMap.get(id_hash, set())
        if lora_name_1 != 'None' and switch_1 == 'On' and (lora_name_1 in used_loras):
            (lora_list.extend([(CR_RandomLoRAStack.cleanLoraName(lora_name_1), model_weight_1, clip_weight_1)]),)
        if lora_name_2 != 'None' and switch_2 == 'On' and (lora_name_2 in used_loras):
            (lora_list.extend([(CR_RandomLoRAStack.cleanLoraName(lora_name_2), model_weight_2, clip_weight_2)]),)
        if lora_name_3 != 'None' and switch_3 == 'On' and (lora_name_3 in used_loras):
            (lora_list.extend([(CR_RandomLoRAStack.cleanLoraName(lora_name_3), model_weight_3, clip_weight_3)]),)
        return (lora_list,)
```