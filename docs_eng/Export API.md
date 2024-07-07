# Documentation
- Class name: WAS_Export_API
- Category: WAS Suite/Debug
- Output node: True
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Export_API node facilitates the export of alert data in a structured and orderly manner, ensuring that outputs are stored with appropriate naming protocols and file paths for retrieval and further analysis.

# Input types
## Required
- save_prompt_api
    - This parameter controls whether API should keep the reminder data. This is important to maintain the record of the hints used in the workflow, which is essential for the purposes of debugging and review.
    - Comfy dtype: COMBO[[['true', 'true']]]
    - Python dtype: str
- output_path
    - The output path is essential because it defines the directory that will save the hint data. This ensures the organization of the data and facilitates future reference.
    - Comfy dtype: STRING
    - Python dtype: str
- filename_prefix
    - The filename prefix is used to provide a consistent starting point for naming export files. It helps to classify and identify files more efficiently in the output directory.
    - Comfy dtype: STRING
    - Python dtype: str
- filename_delimiter
    - The separator is a key element that separates the filename prefix from the digital counter and ensures that the exported document has a systematic and orderly naming protocol.
    - Comfy dtype: STRING
    - Python dtype: str
- filename_number_padding
    - Numerical parameters determine the format of the digital counter, ensuring that the filenames are aligned and can be sorted in chronological or numerical order.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- parse_text_tokens
    - When this feature is enabled, it resolves and replaces the tags in the text of the reminder with the corresponding values, which are essential for customizing and personalizing the exported data.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- ui
    - The form of the JSON expression, which provides a formatted reminder data, is essential to ensure that the exported information is structured and machine-readable.
    - Comfy dtype: COMBO[[{'string': 'Prompt JSON'}]]
    - Python dtype: Dict[str, str]

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Export_API:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'save_prompt_api': (['true', 'true'],), 'output_path': ('STRING', {'default': './ComfyUI/output/', 'multiline': False}), 'filename_prefix': ('STRING', {'default': 'ComfyUI_Prompt'}), 'filename_delimiter': ('STRING', {'default': '_'}), 'filename_number_padding': ('INT', {'default': 4, 'min': 2, 'max': 9, 'step': 1}), 'parse_text_tokens': ('BOOLEAN', {'default': False})}, 'hidden': {'prompt': 'PROMPT'}}
    OUTPUT_NODE = True
    RETURN_TYPES = ()
    FUNCTION = 'export_api'
    CATEGORY = 'WAS Suite/Debug'

    def export_api(self, output_path=None, filename_prefix='ComfyUI', filename_number_padding=4, filename_delimiter='_', prompt=None, save_prompt_api='true', parse_text_tokens=False):
        delimiter = filename_delimiter
        number_padding = filename_number_padding if filename_number_padding > 1 else 4
        tokens = TextTokens()
        if output_path in [None, '', 'none', '.']:
            output_path = comfy_paths.output_directory
        else:
            output_path = tokens.parseTokens(output_path)
        pattern = f'{re.escape(filename_prefix)}{re.escape(filename_delimiter)}(\\d{{{number_padding}}})'
        existing_counters = [int(re.search(pattern, filename).group(1)) for filename in os.listdir(output_path) if re.match(pattern, filename)]
        existing_counters.sort(reverse=True)
        if existing_counters:
            counter = existing_counters[0] + 1
        else:
            counter = 1
        file = f'{filename_prefix}{filename_delimiter}{counter:0{number_padding}}.json'
        output_file = os.path.abspath(os.path.join(output_path, file))
        if prompt:
            if parse_text_tokens:
                prompt = self.parse_prompt(prompt, tokens, keys_to_parse)
            prompt_json = json.dumps(prompt, indent=4)
            cstr('Prompt API JSON').msg.print()
            print(prompt_json)
            if save_prompt_api == 'true':
                with open(output_file, 'w') as f:
                    f.write(prompt_json)
                cstr(f'Output file path: {output_file}').msg.print()
        return {'ui': {'string': prompt_json}}

    def parse_prompt(self, obj, tokens, keys_to_parse):
        if isinstance(obj, dict):
            return {key: self.parse_prompt(value, tokens, keys_to_parse) if key in keys_to_parse else value for (key, value) in obj.items()}
        elif isinstance(obj, list):
            return [self.parse_prompt(element, tokens, keys_to_parse) for element in obj]
        elif isinstance(obj, str):
            return tokens.parseTokens(obj)
        else:
            return obj
```