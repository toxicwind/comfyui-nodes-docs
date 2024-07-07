# Documentation
- Class name: SeargePromptAdapterV2
- Category: UI_PROMPTING
- Output node: False
- Repo Ref: https://github.com/jobunk/SeargeSDXL.git

The node facilitates the construction and retrieval of alert data, enabling the creation of diversified tips for different scenarios by integrating primary, secondary, style tips and their negative counterparts.

# Input types
## Optional
- main_prompt
    - The primary hint is the key element that sets the key context or theme from which the hint is generated. It is essential to guide the direction and content of the output.
    - Comfy dtype: SRG_PROMPT_TEXT
    - Python dtype: str
- secondary_prompt
    - A secondary reminder provides additional information or context for the primary reminder, which enriches the complexity and depth of the content generated.
    - Comfy dtype: SRG_PROMPT_TEXT
    - Python dtype: str
- style_prompt
    - Style tips are used to define the particular tone or manner in which the content should appear, adding a creative layer to the output.
    - Comfy dtype: SRG_PROMPT_TEXT
    - Python dtype: str
- negative_main_prompt
    - The negative key hints balance the main hints by introducing opposing points of view, which enhances the nuance and soundness of the content generated.
    - Comfy dtype: SRG_PROMPT_TEXT
    - Python dtype: str
- negative_secondary_prompt
    - These reminders complement the main negative indications by providing a secondary objection to the possibility of further diversifying the content.
    - Comfy dtype: SRG_PROMPT_TEXT
    - Python dtype: str
- negative_style_prompt
    - Negative style tips introduce an alternative tone or presentation to ensure that outputs include a wider range of style choices.
    - Comfy dtype: SRG_PROMPT_TEXT
    - Python dtype: str
- data
    - The data are the basic input for node operations and may contain earlier reminders or other relevant letters that may affect the generation process.
    - Comfy dtype: SRG_DATA_STREAM
    - Python dtype: Dict[str, Any]

# Output types
- data
    - The output data stream contains structured tips that can be used as input to the follow-up process or for analysis.
    - Comfy dtype: SRG_DATA_STREAM
    - Python dtype: Dict[str, Any]

# Usage tips
- Infra type: CPU

# Source code
```
class SeargePromptAdapterV2:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {}, 'optional': {'data': ('SRG_DATA_STREAM',), 'main_prompt': ('SRG_PROMPT_TEXT',), 'secondary_prompt': ('SRG_PROMPT_TEXT',), 'style_prompt': ('SRG_PROMPT_TEXT',), 'negative_main_prompt': ('SRG_PROMPT_TEXT',), 'negative_secondary_prompt': ('SRG_PROMPT_TEXT',), 'negative_style_prompt': ('SRG_PROMPT_TEXT',)}}
    RETURN_TYPES = ('SRG_DATA_STREAM', 'SRG_DATA_STREAM')
    RETURN_NAMES = ('data', UI.S_PROMPTS)
    FUNCTION = 'get_value'
    CATEGORY = UI.CATEGORY_UI_PROMPTING

    @staticmethod
    def create_dict(main_prompt=None, secondary_prompt=None, style_prompt=None, negative_main_prompt=None, negative_secondary_prompt=None, negative_style_prompt=None):
        return {UI.F_MAIN_PROMPT: main_prompt, UI.F_SECONDARY_PROMPT: secondary_prompt, UI.F_STYLE_PROMPT: style_prompt, UI.F_NEGATIVE_MAIN_PROMPT: negative_main_prompt, UI.F_NEGATIVE_SECONDARY_PROMPT: negative_secondary_prompt, UI.F_NEGATIVE_STYLE_PROMPT: negative_style_prompt}

    def get_value(self, main_prompt=None, secondary_prompt=None, style_prompt=None, negative_main_prompt=None, negative_secondary_prompt=None, negative_style_prompt=None, data=None):
        if data is None:
            data = {}
        data[UI.S_PROMPTS] = self.create_dict(main_prompt, secondary_prompt, style_prompt, negative_main_prompt, negative_secondary_prompt, negative_style_prompt)
        return (data, data[UI.S_PROMPTS])
```