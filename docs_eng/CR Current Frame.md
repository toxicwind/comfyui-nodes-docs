# Documentation
- Class name: CR_CurrentFrame
- Category: Comfyroll/Animation/Utils
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_CurrentFrame node is designed to facilitate the recording and display of the current frame index in the control table environment. It provides a tool for developers to track the progress of animation or a series of frames.

# Input types
## Required
- index
    - The `index' parameter represents the current frame index in the animation sequence. It is essential because it determines the frame that is being recorded or monitored.
    - Comfy dtype: INT
    - Python dtype: int
- print_to_console
    - The 'print_to_console' parameter determines whether the current frame index should be printed on the console. It is an important switch to control the output visibility of the node.
    - Comfy dtype: COMBO['Yes', 'No']
    - Python dtype: str

# Output types
- index
    - The `index' output provides a current frame index for node processing, which can be used in animation workflows for further operations or analysis.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class CR_CurrentFrame:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'index': ('INT', {'default': 1, 'min': -10000, 'max': 10000}), 'print_to_console': (['Yes', 'No'],)}}
    RETURN_TYPES = ('INT',)
    RETURN_NAMES = ('index',)
    FUNCTION = 'to_console'
    CATEGORY = icons.get('Comfyroll/Animation/Utils')

    def to_console(self, index, print_to_console):
        if print_to_console == 'Yes':
            print(f'[Info] CR Current Frame:{index}')
        return (index,)
```