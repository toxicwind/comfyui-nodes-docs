# Documentation
- Class name: SeargeTextInputV2
- Category: UI_PROMPTING
- Output node: False
- Repo Ref: https://github.com/jobunk/SeargeSDXL.git

The node facilitates the system's collection of text input from users and supports interactive communications within the system. It is designed to ask questions to users and capture their responses as a basic component of user participation and data collection.

# Input types
## Required
- prompt
    - A reminder parameter is essential because it defines the questions or statements to be presented to the user and guides their input. It is the main way in which nodes communicate with the user, affecting the nature and quality of the responses collected.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- prompt_text
    - The output represents the user’s response to the reminder, which is a valuable source of information for further processing or analysis. It is a direct reflection of the user’s input and represents an interactive success.
    - Comfy dtype: SRG_PROMPT_TEXT
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class SeargeTextInputV2:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'prompt': ('STRING', {'default': '', 'multiline': True})}}
    RETURN_TYPES = ('SRG_PROMPT_TEXT',)
    RETURN_NAMES = ('prompt_text',)
    FUNCTION = 'get_value'
    CATEGORY = UI.CATEGORY_UI_PROMPTING

    def get_value(self, prompt):
        return (prompt,)
```