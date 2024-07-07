# Documentation
- Class name: ZipPrompt
- Category: InspirePack/Prompt
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Inspire-Pack.git

The ZipPrompt node efficiently combines both positive and negative tips into a single compressed entity, which enhances the multifunctional nature of data processing in creative tasks. It emphasizes the role of the node in simplifying the integration of hints, without going into specific realization details.

# Input types
## Required
- positive
    - The `positive' parameter is necessary to provide positive content to node operations and is a key element in creating compressed tips.
    - Comfy dtype: STRING
    - Python dtype: str
- negative
    - The `negative' parameter plays a crucial role in providing comparative content, which is essential for compressing the comprehensiveness of the hint.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- name_opt
    - While the `name_opt' parameter is optional, it can be used to add a personalized layer to the compressed hint by defining output.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- zipped_prompt
    - The output `zipped_prompt' represents a combination of both positive and negative input and is enclosed in a compact and structured format for further use.
    - Comfy dtype: ZIPPED_PROMPT
    - Python dtype: Tuple[str, str, str]

# Usage tips
- Infra type: CPU

# Source code
```
class ZipPrompt:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'positive': ('STRING', {'forceInput': True, 'multiline': True}), 'negative': ('STRING', {'forceInput': True, 'multiline': True})}, 'optional': {'name_opt': ('STRING', {'forceInput': True, 'multiline': False})}}
    RETURN_TYPES = ('ZIPPED_PROMPT',)
    FUNCTION = 'doit'
    CATEGORY = 'InspirePack/Prompt'

    def doit(self, positive, negative, name_opt=''):
        return ((positive, negative, name_opt),)
```