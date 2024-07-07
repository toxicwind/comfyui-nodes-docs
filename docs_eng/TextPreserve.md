# Documentation
- Class name: TextPreserve
- Category: Mikey/Text
- Output node: True
- Repo Ref: https://github.com/bash-j/mikey_nodes

TextPreserve is designed to process and retain the original text while allowing dynamic content replacement. It does so by identifying placeholders in the text and replacing them with random or specified values, ensuring the integrity of the original message throughout the conversion process.

# Input types
## Required
- text
    - The `text' parameter is the main input of the node and contains the text to be processed. It is essential because it defines the content that will go through the retention and replacement process. This parameter supports multiple lines, allowing complex and expanded text input.
    - Comfy dtype: STRING
    - Python dtype: str
- result_text
    - The'resource_text' parameter is the place where the text is stored after the node is executed. It is essential because it contains the final output of the text after all replacement and retention operations are completed.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- unique_id
    - The `unique_id' parameter is used to identify the single node in the workflow. It is optional, but it may be important to track and manage the state and output of the node in the larger system.
    - Comfy dtype: UNIQUE_ID
    - Python dtype: Union[str, None]
- extra_pnginfo
    - The `extra_pnginfo' parameter provides additional information that can be used to enhance text processing. It is optional and may include metadata or other relevant details that affect how nodes operate.
    - Comfy dtype: EXTRA_PNGINFO
    - Python dtype: Union[str, None]
- prompt
    - The `prompt' parameter is used to provide dynamic tips to guide the text replacement process. It is optional, but can significantly influence the behaviour of the node by introducing context-specific replacements.
    - Comfy dtype: PROMPT
    - Python dtype: Union[str, None]

# Output types
- text
    - The `text' output parameter represents the final processing text after all operations have been completed. It is the supreme expression of the node function and contains the result of the retention and replacement process.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class TextPreserve:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'text': ('STRING', {'multiline': True, 'default': 'Input Text Here', 'dynamicPrompts': False}), 'result_text': ('STRING', {'multiline': True, 'default': 'Result Text Here (will be replaced)'})}, 'hidden': {'unique_id': 'UNIQUE_ID', 'extra_pnginfo': 'EXTRA_PNGINFO', 'prompt': 'PROMPT'}}
    RETURN_TYPES = ('STRING',)
    RETURN_NAMES = ('text',)
    FUNCTION = 'process'
    OUTPUT_NODE = True
    CATEGORY = 'Mikey/Text'

    def process(self, text, result_text, unique_id=None, extra_pnginfo=None, prompt=None):
        random.seed()
        preserve_text = text
        text = search_and_replace(text, extra_pnginfo, prompt)
        wc_re = re.compile('{([^}]+)}')

        def repl(m):
            return random.choice(m.group(1).split('|'))
        for m in wc_re.finditer(text):
            text = text.replace(m.group(0), repl(m))
        prompt.get(str(unique_id))['inputs']['text'] = preserve_text
        for (i, node_dict) in enumerate(extra_pnginfo['workflow']['nodes']):
            if node_dict['id'] == int(unique_id):
                node_dict['widgets_values'] = [preserve_text, text]
                extra_pnginfo['workflow']['nodes'][i] = node_dict
        prompt.get(str(unique_id))['inputs']['result_text'] = text
        return (text,)
```