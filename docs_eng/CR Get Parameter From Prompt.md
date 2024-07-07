# Documentation
- Class name: CR_GetParameterFromPrompt
- Category: Comfyroll/Utils/Other
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

The CR_GetParameterFromPrompt node is designed to extract specific parameters from the given hint string. It searches for the specified search string in the hint and attempts to interpret the subsequent value when it is found. This node is particularly suitable for handling configuration settings or parameters embedded in the text string and provides a flexible way to manage and retrieve information.

# Input types
## Required
- prompt
    - The prompt parameter is a string of text that contains nodes that will search and extract the parameter. It is essential for the operation of the node, as it defines the context and source of the data to be parsed.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- search_string
    - The search_string parameter defines the particular keyword or mode that the node will find in the reminder. It plays a key role in identifying the parameters to be extracted and allows targeted data retrieval.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- prompt
    - Modified hints, the recognized parameters and their values have been removed to allow the output of a clean text that is not searched for parameters.
    - Comfy dtype: STRING
    - Python dtype: str
- text
    - The extraction value associated with the search string may be a string, number or boolean value, depending on the format found in the hint.
    - Comfy dtype: STRING
    - Python dtype: Union[str, int, float, bool]
- float
    - If the value extracted is a value, it is converted to a floating point for further numerical operations or analysis.
    - Comfy dtype: FLOAT
    - Python dtype: float
- boolean
    - The boolean of the extracted value indicates that it provides a direct factual or false explanation based on what was found.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- show_help
    - is the URL link to the node document or help page to provide additional information or guidance to users on how to use the node effectively.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_GetParameterFromPrompt:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'prompt': ('STRING', {'multiline': True, 'default': 'prompt', 'forceInput': True}), 'search_string': ('STRING', {'multiline': False, 'default': '!findme'})}}
    RETURN_TYPES = ('STRING', any_type, 'FLOAT', 'BOOLEAN', 'STRING')
    RETURN_NAMES = ('prompt', 'text', 'float', 'boolean', 'show_help')
    FUNCTION = 'get_string'
    CATEGORY = icons.get('Comfyroll/Utils/Other')

    def get_string(self, prompt, search_string):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Other-Nodes#cr-find-string-in-prompt'
        return_string = ''
        return_value = 0
        return_boolean = False
        return_prompt = prompt
        index = prompt.find(search_string)
        if index != -1:
            if prompt[index + len(search_string)] == '=':
                if prompt[index + len(search_string) + 1] == '"':
                    start_quote = index + len(search_string) + 2
                    end_quote = prompt.find('"', start_quote + 1)
                    if end_quote != -1:
                        return_string = prompt[start_quote:end_quote]
                        print(return_string)
                else:
                    space_index = prompt.find(' ', index + len(search_string))
                    if space_index != -1:
                        return_string = prompt[index + len(search_string):space_index]
                    else:
                        return_string = prompt[index + len(search_string):]
            else:
                return_string = search_string[1:]
        if return_string == '':
            return (return_prompt, return_string, return_value, return_boolean, show_help)
        if return_string.startswith('='):
            return_string = return_string[1:]
        return_boolean = return_string.lower() == 'true'
        try:
            return_value = int(return_string)
        except ValueError:
            try:
                return_value = float(return_string)
            except ValueError:
                return_value = 0
        remove_string = ' ' + search_string + '=' + return_string
        return_prompt = prompt.replace(remove_string, '')
        return (return_prompt, return_string, return_value, return_boolean, show_help)
```