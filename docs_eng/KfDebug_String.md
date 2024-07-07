# Documentation
- Class name: KfDebug_String
- Category: Debugging
- Output node: True
- Repo Ref: https://github.com/dmarx/ComfyUI-Keyframed

The node is intended to facilitate the examination and analysis of string data in the workflow. It enables users to view and verify the content and structure of string at different stages and to ensure the accuracy and completeness of text information being processed.

# Input types
## Required
- input_string
    - The input_string parameter is essential for this node because it carries text data that needs to be checked. It is a key component because the primary function of the node revolves around analysing and displaying the contents of the string.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- output_string
    - Output_string represents the result of the node operation, which is usually the same as input_string, but may be modified or annotated according to the debugging process. It is important because it provides the text data that is eventually checked.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class KfDebug_String(KfDebug_Passthrough):
    RETURN_TYPES = ('STRING',)
```