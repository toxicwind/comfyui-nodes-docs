# Documentation
- Class name: LoraLoaderBlockWeight
- Category: InspirePack/LoraBlockWeight
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Inspire-Pack.git

The node is intended to load and operate block weights from the Lora file and adjust the emphasis on different model layers to the specified parameters to fine-tune the output results.

# Input types
## Required
- model
    - Model parameters are essential because they define the basic architecture that will apply block weights and significantly influence the final output.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- clip
    - Clip input is essential to provide context information that helps adjust the weight of a block to ensure that the output is consistent with the desired context.
    - Comfy dtype: CLIP
    - Python dtype: torch.nn.Module
- category_filter
    - This parameter filters the LoRa files according to their category and allows nodes to focus on specific aspects of the model layer.
    - Comfy dtype: COMBO[lora_dirs]
    - Python dtype: str
- lora_name
    - The lora_name parameter plays a key role in the selection of a specific LoRa file whose block weights will be loaded and operated.
    - Comfy dtype: COMBO[lora_names]
    - Python dtype: str
- strength_model
    - This parameter adjusts the impact of model block weights to allow fine-tuning of output to meet specific requirements.
    - Comfy dtype: FLOAT
    - Python dtype: float
- strength_clip
    - Strength_clip parameters modify the effect of clip context information on block weight adjustments.
    - Comfy dtype: FLOAT
    - Python dtype: float
- inverse
    - By switching this parameter, nodes can reverse the weight of blocks and provide an alternative perspective on model behaviour.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- seed
    - Seed enters the initialized random number generator to ensure that block weight adjustments are recognizable and consistent.
    - Comfy dtype: INT
    - Python dtype: int
- A
    - A parameter is used to define the base values for certain vector calculations and to influence the overall distribution of block weights.
    - Comfy dtype: FLOAT
    - Python dtype: float
- B
    - Similar to A, the B parameter sets another base value for vector calculation, which contributes to the diversity of block weight adjustments.
    - Comfy dtype: FLOAT
    - Python dtype: float
- block_vector
    - Block_vector parameters specify the weight sequence of blocks to be applied, directly impacting the structure and characteristics of the output.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- preset
    - Predefined parameters provide a predefined selection of block weight configurations and simplify the application of common adjustments.
    - Comfy dtype: COMBO[preset]
    - Python dtype: str
- bypass
    - When enabled, this parameter allows node to bypass block weight adjustments and transmit the original model and clip data without change.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- model
    - The output model has been adjusted to reflect the expected modification of structural behaviour based on the load weight.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- clip
    - Output clip data contains block weight adjustments to ensure that context information is consistent with the modified model.
    - Comfy dtype: CLIP
    - Python dtype: torch.nn.Module
- populated_vector
    - This output provides a detailed record of the block weights applied as a reference for the model to modify its structure.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class LoraLoaderBlockWeight:

    def __init__(self):
        self.loaded_lora = None

    @classmethod
    def INPUT_TYPES(s):
        preset = ['Preset']
        preset += load_lbw_preset('lbw-preset.txt')
        preset += load_lbw_preset('lbw-preset.custom.txt')
        preset = [name for name in preset if not name.startswith('@')]
        lora_names = folder_paths.get_filename_list('loras')
        lora_dirs = [os.path.dirname(name) for name in lora_names]
        lora_dirs = ['All'] + list(set(lora_dirs))
        return {'required': {'model': ('MODEL',), 'clip': ('CLIP',), 'category_filter': (lora_dirs,), 'lora_name': (lora_names,), 'strength_model': ('FLOAT', {'default': 1.0, 'min': -10.0, 'max': 10.0, 'step': 0.01}), 'strength_clip': ('FLOAT', {'default': 1.0, 'min': -10.0, 'max': 10.0, 'step': 0.01}), 'inverse': ('BOOLEAN', {'default': False, 'label_on': 'True', 'label_off': 'False'}), 'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615}), 'A': ('FLOAT', {'default': 4.0, 'min': -10.0, 'max': 10.0, 'step': 0.01}), 'B': ('FLOAT', {'default': 1.0, 'min': -10.0, 'max': 10.0, 'step': 0.01}), 'preset': (preset,), 'block_vector': ('STRING', {'multiline': True, 'placeholder': 'block weight vectors', 'default': '1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1', 'pysssss.autocomplete': False}), 'bypass': ('BOOLEAN', {'default': False, 'label_on': 'True', 'label_off': 'False'})}}
    RETURN_TYPES = ('MODEL', 'CLIP', 'STRING')
    RETURN_NAMES = ('model', 'clip', 'populated_vector')
    FUNCTION = 'doit'
    CATEGORY = 'InspirePack/LoraBlockWeight'

    @staticmethod
    def validate(vectors):
        if len(vectors) < 12:
            return False
        for x in vectors:
            if x in ['R', 'r', 'U', 'u', 'A', 'a', 'B', 'b'] or is_numeric_string(x):
                continue
            else:
                subvectors = x.strip().split(' ')
                for y in subvectors:
                    y = y.strip()
                    if y not in ['R', 'r', 'U', 'u', 'A', 'a', 'B', 'b'] and (not is_numeric_string(y)):
                        return False
        return True

    @staticmethod
    def convert_vector_value(A, B, vector_value):

        def simple_vector(x):
            if x in ['U', 'u']:
                ratio = np.random.uniform(-1.5, 1.5)
                ratio = round(ratio, 2)
            elif x in ['R', 'r']:
                ratio = np.random.uniform(0, 3.0)
                ratio = round(ratio, 2)
            elif x == 'A':
                ratio = A
            elif x == 'a':
                ratio = A / 2
            elif x == 'B':
                ratio = B
            elif x == 'b':
                ratio = B / 2
            elif is_numeric_string(x):
                ratio = float(x)
            else:
                ratio = None
            return ratio
        v = simple_vector(vector_value)
        if v is not None:
            ratios = [v]
        else:
            ratios = [simple_vector(x) for x in vector_value.split(' ')]
        return ratios

    @staticmethod
    def norm_value(value):
        if value == 1:
            return 1
        elif value == 0:
            return 0
        else:
            return value

    @staticmethod
    def load_lora_for_models(model, clip, lora, strength_model, strength_clip, inverse, seed, A, B, block_vector):
        key_map = comfy.lora.model_lora_keys_unet(model.model)
        key_map = comfy.lora.model_lora_keys_clip(clip.cond_stage_model, key_map)
        loaded = comfy.lora.load_lora(lora, key_map)
        block_vector = block_vector.split(':')
        if len(block_vector) > 1:
            block_vector = block_vector[1]
        else:
            block_vector = block_vector[0]
        vector = block_vector.split(',')
        vector_i = 1
        if not LoraLoaderBlockWeight.validate(vector):
            preset_dict = load_preset_dict()
            if len(vector) > 0 and vector[0].strip() in preset_dict:
                vector = preset_dict[vector[0].strip()].split(',')
            else:
                raise ValueError(f"[LoraLoaderBlockWeight] invalid block_vector '{block_vector}'")
        last_k_unet_num = None
        new_modelpatcher = model.clone()
        populated_ratio = strength_model

        def parse_unet_num(s):
            if s[1] == '.':
                return int(s[0])
            else:
                return int(s)
        input_blocks = []
        middle_blocks = []
        output_blocks = []
        others = []
        for (k, v) in loaded.items():
            k_unet = k[len('diffusion_model.'):]
            if k_unet.startswith('input_blocks.'):
                k_unet_num = k_unet[len('input_blocks.'):len('input_blocks.') + 2]
                input_blocks.append((k, v, parse_unet_num(k_unet_num), k_unet))
            elif k_unet.startswith('middle_block.'):
                k_unet_num = k_unet[len('middle_block.'):len('middle_block.') + 2]
                middle_blocks.append((k, v, parse_unet_num(k_unet_num), k_unet))
            elif k_unet.startswith('output_blocks.'):
                k_unet_num = k_unet[len('output_blocks.'):len('output_blocks.') + 2]
                output_blocks.append((k, v, parse_unet_num(k_unet_num), k_unet))
            else:
                others.append((k, v, k_unet))
        input_blocks = sorted(input_blocks, key=lambda x: x[2])
        middle_blocks = sorted(middle_blocks, key=lambda x: x[2])
        output_blocks = sorted(output_blocks, key=lambda x: x[2])
        np.random.seed(seed % 2 ** 31)
        populated_vector_list = []
        ratios = []
        for (k, v, k_unet_num, k_unet) in input_blocks + middle_blocks + output_blocks:
            if last_k_unet_num != k_unet_num and len(vector) > vector_i:
                ratios = LoraLoaderBlockWeight.convert_vector_value(A, B, vector[vector_i].strip())
                ratio = ratios.pop(0)
                if inverse:
                    populated_ratio = 1 - ratio
                else:
                    populated_ratio = ratio
                populated_vector_list.append(LoraLoaderBlockWeight.norm_value(populated_ratio))
                vector_i += 1
            else:
                if len(ratios) > 0:
                    ratio = ratios.pop(0)
                if inverse:
                    populated_ratio = 1 - ratio
                else:
                    populated_ratio = ratio
            last_k_unet_num = k_unet_num
            new_modelpatcher.add_patches({k: v}, strength_model * populated_ratio)
        ratios = LoraLoaderBlockWeight.convert_vector_value(A, B, vector[0].strip())
        ratio = ratios.pop(0)
        if inverse:
            populated_ratio = 1 - ratio
        populated_vector_list.insert(0, LoraLoaderBlockWeight.norm_value(populated_ratio))
        for (k, v, k_unet) in others:
            new_modelpatcher.add_patches({k: v}, strength_model * populated_ratio)
        new_clip = clip.clone()
        new_clip.add_patches(loaded, strength_clip)
        populated_vector = ','.join(map(str, populated_vector_list))
        return (new_modelpatcher, new_clip, populated_vector)

    def doit(self, model, clip, lora_name, strength_model, strength_clip, inverse, seed, A, B, preset, block_vector, bypass=False, category_filter=None):
        if strength_model == 0 and strength_clip == 0 or bypass:
            return (model, clip, '')
        lora_path = folder_paths.get_full_path('loras', lora_name)
        lora = None
        if self.loaded_lora is not None:
            if self.loaded_lora[0] == lora_path:
                lora = self.loaded_lora[1]
            else:
                temp = self.loaded_lora
                self.loaded_lora = None
                del temp
        if lora is None:
            lora = comfy.utils.load_torch_file(lora_path, safe_load=True)
            self.loaded_lora = (lora_path, lora)
        (model_lora, clip_lora, populated_vector) = LoraLoaderBlockWeight.load_lora_for_models(model, clip, lora, strength_model, strength_clip, inverse, seed, A, B, block_vector)
        return (model_lora, clip_lora, populated_vector)
```