# Documentation
- Class name: CR_PromptText
- Category: Comfyroll/Essential/Core
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

The CR_PromptText node is designed to simplify the process of accessing user input by means of a hint box. It is the basic component of an interactive application and is essential for guiding application behaviour. The main function of the node is to show the user a hint and to return input and a URL for more help, which enhances the user's experience by providing context help.

# Input types
## Required
- prompt
    - The parameter 'prompt' is essential for defining the query or statement that is displayed to the user. It sets the context for the user's input and is essential for the operation of the node, as it directly affects interaction with the user.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- prompt
    - Output parameter 'prompt' represents the user's response to the initial query. It is important because it captures the user's input and can then be further processed by the application.
    - Comfy dtype: STRING
    - Python dtype: str
- show_help
    - The output parameter'show_help' provides a URL linked to the wiki page, on which users can find more information or help with tips. This is particularly useful to guide users to complex or unfamiliar tasks.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_PromptText:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'prompt': ('STRING', {'default': 'prompt', 'multiline': True})}}
    RETURN_TYPES = ('STRING', 'STRING')
    RETURN_NAMES = ('prompt', 'show_help')
    FUNCTION = 'get_value'
    CATEGORY = icons.get('Comfyroll/Essential/Core')

    def get_value(self, prompt):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Core-Nodes#cr-prompt-text'
        return (prompt, show_help)
```