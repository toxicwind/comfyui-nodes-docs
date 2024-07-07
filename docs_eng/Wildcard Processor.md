# Documentation
- Class name: WildcardProcessor
- Category: Mikey/Text
- Output node: False
- Repo Ref: https://github.com/bash-j/mikey_nodes

The WildcardProcessor node is designed to operate and process text input by replacing wildcards, using a particular mode or value. It enables dynamic text generation based on user-defined criteria by identifying placeholders in input tips and replacing them with corresponding data.

# Input types
## Required
- prompt
    - The `prompt' parameter is the main input of the node as the source text that will be replaced with wildcards. It is essential because it determines the context and content of the node that will be processed and converted.
    - Comfy dtype: STRING
    - Python dtype: str
- seed
    - The `seed' parameter is an integer that is used to initialize the random number generator to ensure the repeatability of the wildcard replacement process. It plays a key role in determining the choice of rows from the wildcard file.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- prompt_
    - The 'prompt_' parameter is an optional dictionary that provides additional context or specific instructions for wildcard replacement. It enhances the customization of node operations by allowing users to customize the replacement process according to their needs.
    - Comfy dtype: PROMPT
    - Python dtype: Dict[str, Any]
- extra_pnginfo
    - The `extra_pnginfo' parameter is an optional JSON object with additional information for wildcard replacement. It is used to provide additional data that may affect node processing input tips.
    - Comfy dtype: EXTRA_PNGINFO
    - Python dtype: Union[str, Dict[str, Any]]

# Output types
- processed_prompt
    - 'Processed_prompt' output is the result of node operations in which the wildcards for input tips are replaced by appropriate values. It marks the completion of text processing and is ready for further use or output.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class WildcardProcessor:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'prompt': ('STRING', {'multiline': True, 'placeholder': 'Prompt Text'}), 'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615})}, 'hidden': {'prompt_': 'PROMPT', 'extra_pnginfo': 'EXTRA_PNGINFO'}}
    RETURN_TYPES = ('STRING',)
    FUNCTION = 'process'
    CATEGORY = 'Mikey/Text'

    def process(self, prompt, seed, prompt_=None, extra_pnginfo=None):
        if prompt_ is None:
            prompt_ = {}
        if extra_pnginfo is None:
            extra_pnginfo = {}
        prompt = search_and_replace(prompt, extra_pnginfo, prompt_)
        prompt = find_and_replace_wildcards(prompt, seed)
        return (prompt,)
```