# Documentation
- Class name: CR_PromptListKeyframes
- Category: Comfyroll/Animation/Legacy
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

The CR_PromptListKeyframes node is designed to generate a key frame from the reminder list. It handles the input list, following a specific key frame format, to create a key frame sequence that can be used in animation workflows. This node is essential to automate the key frame creation process to ensure consistency and efficiency in the creation of the animation sequence.

# Input types
## Required
- prompt_list
    - The list of hints is an important input to the node because it contains a hint that will be converted to the key frame. Each hint in the list is part of the key frame through which the node overlaps to generate the final key frame sequence.
    - Comfy dtype: PROMPT_LIST
    - Python dtype: List[Tuple[str, str, str, str, int, int]]
## Optional
- keyframe_format
    - The key frame format parameter determines the structure and style of the key frame generated. Although the node uses the 'Deforum'format by default, this parameter allows flexibility when other formats need to be supported in the future.
    - Comfy dtype: COMBO['Deforum']
    - Python dtype: Literal['Deforum']

# Output types
- keyframe_list
    - The key frame list is the main output of the node, representing the formatted key frame string. This output is used directly for the sequence that defines the animated key frame in the animation software.
    - Comfy dtype: STRING
    - Python dtype: str
- show_help
    - Displays a URL link to a document or help page that links the help output to a node. This is very useful for users seeking more information or guidance on how to use the node effectively.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_PromptListKeyframes:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'prompt_list': ('PROMPT_LIST',), 'keyframe_format': (['Deforum'],)}}
    RETURN_TYPES = ('STRING', 'STRING')
    RETURN_NAMES = ('keyframe_list', 'show_help')
    FUNCTION = 'make_keyframes'
    CATEGORY = icons.get('Comfyroll/Animation/Legacy')

    def make_keyframes(self, prompt_list, keyframe_format):
        keyframe_format = 'Deforum'
        keyframe_list = list()
        i = 0
        for (index, prompt_tuple) in enumerate(prompt_list):
            (prompt, transition_type, transition_speed, transition_profile, keyframe_interval, loops) = prompt_tuple
            if i == 0:
                keyframe_list.extend(['"0": "' + prompt + '",\n'])
                i += keyframe_interval
                continue
            new_keyframe = '"' + str(i) + '": "' + prompt + '",\n'
            keyframe_list.extend([new_keyframe])
            i += keyframe_interval
        keyframes_out = ''.join(keyframe_list)[:-2]
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Prompt-Nodes#cr-prompt-list-keyframes'
        return (keyframes_out, show_help)
```