# Documentation
- Class name: LoraSyntaxProcessor
- Category: Mikey/Lora
- Output node: False
- Repo Ref: https://github.com/bash-j/mikey_nodes

The LoraSyntaxProcessor node is designed to process text input through a series of syntax conversions. It replaces the placeholder with a random value, searches and replaces the specific mode with the corresponding data in the hint provided, and loads the external LoRA model to enhance the capability of the underlying model. The node plays a key role in text output that is dynamic and contextually sensitive based on input parameters.

# Input types
## Required
- model
    - Model parameters are essential for the operation of nodes, as they represent baseline models that will be enhanced or used. It influences the node implementation by identifying models that will undergo any subsequent conversion or treatment.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- clip
    - The clip parameter is the key component of text processing, especially when processing visual and multi-module data. It is used to align text with visual performance and can influence node output by influencing the context of text processing.
    - Comfy dtype: CLIP
    - Python dtype: CLIP model or related object
- text
    - Text parameters are the main input of the node, which contains the original text that will be processed in grammar. It is the basis for node operations, as the entire conversion process revolves around this input.
    - Comfy dtype: STRING
    - Python dtype: str
- seed
    - The Seed parameter is used to initialize the random number generator to ensure repeatable results when a random value is generated in the text. It plays an important role in maintaining the consistency of node output.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- extra_pnginfo
    - Extra_pnginfo parameters provide additional context or metadata that can be used for custom text processing. It can influence the implementation of nodes by providing additional information that may be relevant for some conversions.
    - Comfy dtype: EXTRA_PNGINFO
    - Python dtype: dict or str
- prompt
    - The prompt parameter is used to guide text processing and, by providing nodes, is used to replace the specific command or data of the model in the text. It influences node implementation by determining the specific conversions that will be applied to the input text.
    - Comfy dtype: PROMPT
    - Python dtype: dict or str

# Output types
- model
    - The model output represents a model that may be enhanced by the application of any conversion or loading of an additional LoRA model. It marks the completion of node processing and is essential for the follow-up task that relies on the updated model.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- clip
    - The clip output is a process or enhanced version of the input. It may have been modified according to the conversion applied at the node. It is important for the task of updating visual expressions that need to be aligned with the processed text.
    - Comfy dtype: CLIP
    - Python dtype: CLIP model or related object
- text
    - Text output is the final processed text after all syntax conversions have been applied. It is the direct result of node operations and is essential for any downstream task that requires text information.
    - Comfy dtype: STRING
    - Python dtype: str
- unprocessed_text
    - Unprocessed text output provides raw text input to remove any LoRA-related grammar. It is useful for scenarios where the original text is required to be compared or further analysed together with the processed text.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class LoraSyntaxProcessor:

    def __init__(self):
        self.loaded_lora = None

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'clip': ('CLIP',), 'text': ('STRING', {'multiline': True, 'default': '<lora:filename:weight>'}), 'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615})}, 'hidden': {'extra_pnginfo': 'EXTRA_PNGINFO', 'prompt': 'PROMPT'}}
    RETURN_TYPES = ('MODEL', 'CLIP', 'STRING', 'STRING')
    RETURN_NAMES = ('model', 'clip', 'text', 'unprocessed_text')
    FUNCTION = 'process'
    CATEGORY = 'Mikey/Lora'

    def process(self, model, clip, text, seed, extra_pnginfo=None, prompt=None):
        text = process_random_syntax(text, seed)
        text = search_and_replace(text, extra_pnginfo, prompt)
        lora_re = '<lora:(.*?)(?::(.*?))?>'
        lora_prompts = re.findall(lora_re, text)
        stripped_text = text
        clip_lora = clip
        if len(lora_prompts) > 0:
            for lora_prompt in lora_prompts:
                lora_filename = lora_prompt[0]
                if '.safetensors' not in lora_filename:
                    lora_filename += '.safetensors'
                try:
                    lora_multiplier = float(lora_prompt[1]) if lora_prompt[1] != '' else 1.0
                except:
                    lora_multiplier = 1.0
                (model, clip) = load_lora(model, clip, lora_filename, lora_multiplier, lora_multiplier)
        stripped_text = re.sub(lora_re, '', stripped_text)
        return (model, clip, stripped_text, text)
```