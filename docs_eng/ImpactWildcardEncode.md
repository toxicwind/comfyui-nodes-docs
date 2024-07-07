# Documentation
- Class name: ImpactWildcardEncode
- Category: ImpactPack/Prompt
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The "Impact Wildcard Encode " node is designed to integrate and operate text data with models and clips. It handles text containing wildcards and uses advanced techniques such as LoRA for text modification. This node is central to applications that are essential for dynamic text generation and model reconciliation.

# Input types
## Required
- model
    - The “model” parameter is essential for the operation of the node because it defines the model to be used for text processing. This is a basic component that directly affects the ability of the node to generate and operate text data.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- clip
    - The "clip" parameter is necessary because it represents multimedia clips that will be processed with the text. It plays an important role in how the node integrates text and multimedia content.
    - Comfy dtype: CLIP
    - Python dtype: torch.Tensor
- wildcard_text
    - The " wildcard_text " parameter allows the inclusion of placeholders in the text, which can be filled according to context dynamics. This is a key feature for applications that require flexible text input.
    - Comfy dtype: STRING
    - Python dtype: str
- populated_text
    - The 'populated_text' parameter is the location of the actual text to be processed. It is important because it is the main input for text operations and directly affects output.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- mode
    - The “mode” parameter determines whether the text will be filled or fixed. This is an important switch that changes the behaviour of the node based on the desired outcome.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- Select to add LoRA
    - The "Select to add LoRA" parameter allows the addition of LoRA to the text, which significantly enhances the performance and adaptability of the text in the context of the model.
    - Comfy dtype: COMBO[Select the LoRA to add to the text]
    - Python dtype: str
- Select to add Wildcard
    - The "Select to add Wildcard" parameter is used to introduce wildcards into the text and provides a dynamic text insertion and modification mechanism.
    - Comfy dtype: COMBO[Select the Wildcard to add to the text]
    - Python dtype: str
- seed
    - “Seed” parameters are important to ensure the repeatability of node operations, especially when processing random processes.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- model
    - The “model” output represents an updated model for processing text and editing, which can be further used or analysed.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- clip
    - The "clip" output is a processed multimedia clip that is integrated with the text data set.
    - Comfy dtype: CLIP
    - Python dtype: torch.Tensor
- conditioning
    - The “conventioning” output provides contextual information derived from text and clippings that can be used to guide further modelling operations.
    - Comfy dtype: CONDITIONING
    - Python dtype: Dict[str, torch.Tensor]
- populated_text
    - The "populated_text" output is the final text after all processing steps, reflecting dynamic changes made during node implementation.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class ImpactWildcardEncode:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'clip': ('CLIP',), 'wildcard_text': ('STRING', {'multiline': True, 'dynamicPrompts': False}), 'populated_text': ('STRING', {'multiline': True, 'dynamicPrompts': False}), 'mode': ('BOOLEAN', {'default': True, 'label_on': 'Populate', 'label_off': 'Fixed'}), 'Select to add LoRA': (['Select the LoRA to add to the text'] + folder_paths.get_filename_list('loras'),), 'Select to add Wildcard': (['Select the Wildcard to add to the text'],), 'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615})}}
    CATEGORY = 'ImpactPack/Prompt'
    RETURN_TYPES = ('MODEL', 'CLIP', 'CONDITIONING', 'STRING')
    RETURN_NAMES = ('model', 'clip', 'conditioning', 'populated_text')
    FUNCTION = 'doit'

    @staticmethod
    def process_with_loras(**kwargs):
        return impact.wildcards.process_with_loras(**kwargs)

    @staticmethod
    def get_wildcard_list():
        return impact.wildcards.get_wildcard_list()

    def doit(self, *args, **kwargs):
        populated = kwargs['populated_text']
        (model, clip, conditioning) = impact.wildcards.process_with_loras(populated, kwargs['model'], kwargs['clip'])
        return (model, clip, conditioning, populated)
```