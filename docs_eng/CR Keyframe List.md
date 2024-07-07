# Documentation
- Class name: CR_KeyframeList
- Category: Comfyroll/Animation/Prompt
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

The CR_Keyframelist node is designed to manage and process the key frame list, which is the frame sequence that defines the animated time line. It plays a key role in the animation workflow by allowing users to enter key frame data and specify formats for correct interpretation.

# Input types
## Required
- keyframe_list
    - The key frame list is a string that contains the frame sequence that defines the animation. It is essential for the node because it directly affects the animation sequence of the output.
    - Comfy dtype: STRING
    - Python dtype: str
- keyframe_format
    - The key frame format parameter determines how to interpret the key frame list. It is important to ensure that nodes correctly understand and process key frame data.
    - Comfy dtype: COMBO['Deforum', 'CR']
    - Python dtype: str

# Output types
- keyframe_list
    - A list of processed frames has been formatted according to the specified key frame format and is prepared for animated sequences.
    - Comfy dtype: STRING
    - Python dtype: str
- show_help
    - A URL linked to a document page provides additional information and guidance on the use of the key frame list function.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_KeyframeList:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'keyframe_list': ('STRING', {'multiline': True, 'default': 'keyframes'}), 'keyframe_format': (['Deforum', 'CR'],)}}
    RETURN_TYPES = ('STRING', 'STRING')
    RETURN_NAMES = ('keyframe_list', 'show_help')
    FUNCTION = 'keyframelist'
    CATEGORY = icons.get('Comfyroll/Animation/Prompt')

    def keyframelist(self, keyframe_list, keyframe_format):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Prompt-Nodes#cr-keyframe-list'
        return (keyframe_list, show_help)
```