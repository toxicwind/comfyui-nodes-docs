# Documentation
- Class name: LoraBlockInfo
- Category: InspirePack/LoraBlockWeight
- Output node: True
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Inspire-Pack.git

The node class covers the process of extracting and organizing information from the Lora model, which is a key component of understanding the structure and functions of the model. It provides a comprehensive overview of the different types of blocks in the model, such as input blocks, intermediate blocks, output blocks and text blocks, and their respective numbers and connections. This advanced function helps to analyse and optimize the structure of the model.

# Input types
## Required
- model
    - Model parameters are essential because they provide the basis for node implementation analysis.
    - Comfy dtype: MODEL
    - Python dtype: Any
- clip
    - The clip parameter is essential for refining the block information of the model. It helps to map the key accurately and enhances the overall extraction process.
    - Comfy dtype: CLIP
    - Python dtype: Any
- lora_name
    - The lora_name parameter specifies the Lora model to be analysed. It is a key input that guides node to the correct data source for block extraction.
    - Comfy dtype: STRING
    - Python dtype: str
- unique_id
    - The unique_id parameter is essential for tracking node implementation. It ensures that each node is uniquely identified and allows accurate feedback and error processing.
    - Comfy dtype: UNIQUE_ID
    - Python dtype: str
## Optional
- block_info
    - The Block_info parameter, as a text input provided by the user, can provide additional context or specification for the piece extraction process. It complements the automatic analysis with human insight.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types

# Usage tips
- Infra type: CPU

# Source code
```
class LoraBlockInfo:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'clip': ('CLIP',), 'lora_name': (folder_paths.get_filename_list('loras'),), 'block_info': ('STRING', {'multiline': True})}, 'hidden': {'unique_id': 'UNIQUE_ID'}}
    CATEGORY = 'InspirePack/LoraBlockWeight'
    OUTPUT_NODE = True
    RETURN_TYPES = ()
    FUNCTION = 'doit'

    @staticmethod
    def extract_info(model, clip, lora):
        key_map = comfy.lora.model_lora_keys_unet(model.model)
        key_map = comfy.lora.model_lora_keys_clip(clip.cond_stage_model, key_map)
        loaded = comfy.lora.load_lora(lora, key_map)

        def parse_unet_num(s):
            if s[1] == '.':
                return int(s[0])
            else:
                return int(s)
        input_block_count = set()
        input_blocks = []
        input_blocks_map = {}
        middle_block_count = set()
        middle_blocks = []
        middle_blocks_map = {}
        output_block_count = set()
        output_blocks = []
        output_blocks_map = {}
        text_block_count = set()
        text_blocks = []
        text_blocks_map = {}
        others = []
        for (k, v) in loaded.items():
            k_unet = k[len('diffusion_model.'):]
            if k_unet.startswith('input_blocks.'):
                k_unet_num = k_unet[len('input_blocks.'):len('input_blocks.') + 2]
                k_unet_int = parse_unet_num(k_unet_num)
                input_block_count.add(k_unet_int)
                input_blocks.append(k_unet)
                if k_unet_int in input_blocks_map:
                    input_blocks_map[k_unet_int].append(k_unet)
                else:
                    input_blocks_map[k_unet_int] = [k_unet]
            elif k_unet.startswith('middle_block.'):
                k_unet_num = k_unet[len('middle_block.'):len('middle_block.') + 2]
                k_unet_int = parse_unet_num(k_unet_num)
                middle_block_count.add(k_unet_int)
                middle_blocks.append(k_unet)
                if k_unet_int in middle_blocks_map:
                    middle_blocks_map[k_unet_int].append(k_unet)
                else:
                    middle_blocks_map[k_unet_int] = [k_unet]
            elif k_unet.startswith('output_blocks.'):
                k_unet_num = k_unet[len('output_blocks.'):len('output_blocks.') + 2]
                k_unet_int = parse_unet_num(k_unet_num)
                output_block_count.add(k_unet_int)
                output_blocks.append(k_unet)
                if k_unet_int in output_blocks_map:
                    output_blocks_map[k_unet_int].append(k_unet)
                else:
                    output_blocks_map[k_unet_int] = [k_unet]
            elif k_unet.startswith('_model.encoder.layers.'):
                k_unet_num = k_unet[len('_model.encoder.layers.'):len('_model.encoder.layers.') + 2]
                k_unet_int = parse_unet_num(k_unet_num)
                text_block_count.add(k_unet_int)
                text_blocks.append(k_unet)
                if k_unet_int in text_blocks_map:
                    text_blocks_map[k_unet_int].append(k_unet)
                else:
                    text_blocks_map[k_unet_int] = [k_unet]
            else:
                others.append(k_unet)
        text = ''
        input_blocks = sorted(input_blocks)
        middle_blocks = sorted(middle_blocks)
        output_blocks = sorted(output_blocks)
        others = sorted(others)
        text += f'\n-------[Input blocks] ({len(input_block_count)}, Subs={len(input_blocks)})-------\n'
        input_keys = sorted(input_blocks_map.keys())
        for x in input_keys:
            text += f' IN{x}: {len(input_blocks_map[x])}\n'
        text += f'\n-------[Middle blocks] ({len(middle_block_count)}, Subs={len(middle_blocks)})-------\n'
        middle_keys = sorted(middle_blocks_map.keys())
        for x in middle_keys:
            text += f' MID{x}: {len(middle_blocks_map[x])}\n'
        text += f'\n-------[Output blocks] ({len(output_block_count)}, Subs={len(output_blocks)})-------\n'
        output_keys = sorted(output_blocks_map.keys())
        for x in output_keys:
            text += f' OUT{x}: {len(output_blocks_map[x])}\n'
        text += f'\n-------[Text blocks] ({len(text_block_count)}, Subs={len(text_blocks)})-------\n'
        text_keys = sorted(text_blocks_map.keys())
        for x in text_keys:
            text += f' CLIP{x}: {len(text_blocks_map[x])}\n'
        text += f'\n-------[Base blocks] ({len(others)})-------\n'
        for x in others:
            text += f' {x}\n'
        return text

    def doit(self, model, clip, lora_name, block_info, unique_id):
        lora_path = folder_paths.get_full_path('loras', lora_name)
        lora = comfy.utils.load_torch_file(lora_path, safe_load=True)
        text = LoraBlockInfo.extract_info(model, clip, lora)
        PromptServer.instance.send_sync('inspire-node-feedback', {'node_id': unique_id, 'widget_name': 'block_info', 'type': 'text', 'data': text})
        return {}
```