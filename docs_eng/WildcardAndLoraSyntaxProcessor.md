# Documentation
- Class name: WildcardAndLoraSyntaxProcessor
- Category: Mikey/Lora
- Output node: False
- Repo Ref: https://github.com/bash-j/mikey_nodes

The Wildcard And Lora SyntaxProcessor node is designed to process and process complex text input by replacing wildcards and Lora syntax with specific values or documents. It enhances the flexibility and customization of text-processing workflows by enabling dynamic content generation based on predefined models and external documents.

# Input types
## Required
- model
    - Model parameters are essential for the operation of nodes, as they represent the core models to be processed. This is a necessary input that directly affects the ability of nodes to function properly.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- clip
    - The clip parameter is a necessary input that works in conjunction with model parameters. It plays an important role in the implementation of nodes by providing additional context or data that the model may require.
    - Comfy dtype: CLIP
    - Python dtype: CLIP model instance
- text
    - The text parameter is the key input for the node because it contains the original text to be processed. It contains the special syntax used for wildcards and Lora references, which are explained and replaced accordingly.
    - Comfy dtype: STRING
    - Python dtype: str
- seed
    - Seed parameters are important for the randomization process of nodes. It ensures that random elements in the text are generated in a recognizable manner, which is essential for achieving consistent results between different operations.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- extra_pnginfo
    - Extra_pnginfo parameters, while optional, can provide additional information for further customizing node behaviour. It can include metadata or other relevant data to enhance node processing capacity.
    - Comfy dtype: EXTRA_PNGINFO
    - Python dtype: str or dict
- prompt
    - A reminder parameter is an optional input that can guide node processing by providing a specific command or context. When processing complex text input, it can be used to influence node decision-making.
    - Comfy dtype: PROMPT
    - Python dtype: str or dict

# Output types
- model
    - The node model output represents the processed model, which has been updated or modified according to the operation of the node. It marks the completion of node text processing and is ready for further use or analysis.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- clip
    - The clip output is a processing version of the input application, reflecting any changes made during the node execution. This is an important result that may be used in the follow-up phase of the workflow.
    - Comfy dtype: CLIP
    - Python dtype: CLIP model instance
- text
    - Text output is the final processing text after all wildcards and Lora syntax have been replaced. It represents the main output of the node and is the result of the node core function.
    - Comfy dtype: STRING
    - Python dtype: str
- unprocessed_text
    - The unprocessed text output provides the original text input for the node, without any changes to the node operation. It is used as a reference for comparison or further analysis.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class WildcardAndLoraSyntaxProcessor:

    def __init__(self):
        self.loaded_lora = None

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'clip': ('CLIP',), 'text': ('STRING', {'multiline': True, 'default': '<lora:filename:weight>'}), 'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615})}, 'hidden': {'extra_pnginfo': 'EXTRA_PNGINFO', 'prompt': 'PROMPT'}}
    RETURN_TYPES = ('MODEL', 'CLIP', 'STRING', 'STRING')
    RETURN_NAMES = ('model', 'clip', 'text', 'unprocessed_text')
    FUNCTION = 'process'
    CATEGORY = 'Mikey/Lora'

    def extract_and_load_loras(self, text, model, clip):
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
        return (model, clip, stripped_text)

    def process(self, model, clip, text, seed, extra_pnginfo=None, prompt=None):
        text = search_and_replace(text, extra_pnginfo, prompt)
        text = process_random_syntax(text, seed)
        text_ = find_and_replace_wildcards(text, seed, True)
        if len(text_) != len(text):
            seed = random.randint(0, 1000000)
        else:
            seed = 1
        (model, clip, stripped_text) = self.extract_and_load_loras(text_, model, clip)
        stripped_text = find_and_replace_wildcards(stripped_text, seed, True)
        return (model, clip, stripped_text, text_)
```