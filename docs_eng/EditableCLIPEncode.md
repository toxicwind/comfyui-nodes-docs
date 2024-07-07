# Documentation
- Class name: EditableCLIPEncode
- Category: promptcontrol/old
- Output node: False
- Repo Ref: https://github.com/asagi4/comfyui-prompt-control.git

The node is intended to process the text input and convert it to a structured format available for the CLIP model. It achieves this by parsing the specified filter in the text and converting the structure to a conditional format suitable for the CLIP model.

# Input types
## Required
- clip
    - The "clip" parameter is necessary because it provides the basic model that node will be used to process input. Without this parameter, node cannot perform its intended function.
    - Comfy dtype: CLIP
    - Python dtype: torch.nn.Module
- text
    - The " text " parameter is essential for the node because it contains input data that the node is to be parsed and converted. The quality and format of the " text " directly influences the output of the node.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- filter_tags
    - The " Filter_tags " parameter is used to fine-tune the process of interpreting the input text. It allows the specified labels to be taken into account or ignored by the node during the text processing process.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- CONDITIONING
    - The CONDITONING output represents the processing and structural format of the input text, which is used in conjunction with the CLIP model. It covers the essence of the parsing text and allows for effective interaction with the model.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Dict[str, Any]]

# Usage tips
- Infra type: CPU

# Source code
```
class EditableCLIPEncode:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'clip': ('CLIP',), 'text': ('STRING', {'multiline': True})}, 'optional': {'filter_tags': ('STRING', {'default': ''})}}
    RETURN_TYPES = ('CONDITIONING',)
    CATEGORY = 'promptcontrol/old'
    FUNCTION = 'parse'

    def parse(self, clip, text, filter_tags=''):
        parsed = parse_prompt_schedules(text).with_filters(filter_tags)
        return (control_to_clip_common(clip, parsed),)
```