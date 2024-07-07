# Documentation
- Class name: CR_SimplePromptListKeyframes
- Category: Comfyroll/Animation/Legacy
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_SimplePromptListKeyframes is a node used to generate a series of frames from the reminder list. It organizes the creation of key frame data through an iterative list of hints and uses the specified time intervals for each key frame. The node handles multiple loops and transitions, allowing custom animation sequences.

# Input types
## Required
- simple_prompt_list
    - The simple_prompt_list parameter is a set of tips to generate the key frame. Each hint in the list corresponds to a key frame in the final output.
    - Comfy dtype: STRING
    - Python dtype: List[str]
## Optional
- keyframe_interval
    - The keyframe_interval parameter defines the time increment between each key frame. It is essential to control the rhythm of the animation sequence and can be adjusted to control the speed of transition.
    - Comfy dtype: INT
    - Python dtype: int
- loops
    - Loops parameters specify the number of times a key frame sequence should be repeated. It is an essential aspect of creating a repeat or circular animation.
    - Comfy dtype: INT
    - Python dtype: int
- transition_type
    - Transition_type parameters determine the style of transition between frames. It affects the visual mobility of animations and can be set as 'Default' or other predefined options.
    - Comfy dtype: COMBO['Default']
    - Python dtype: str
- transition_speed
    - Transition_speed parameters indicate the speed of transition between frames. It can be set as 'Default' or other options to control the speed of transition.
    - Comfy dtype: COMBO['Default']
    - Python dtype: str
- transition_profile
    - Transition_profile parameters set the contours of the transition, which can affect the way the transition is displayed over time. It is set as 'Default' or other contours to achieve different effects.
    - Comfy dtype: COMBO['Default']
    - Python dtype: str
- keyframe_format
    - Keyframe_format parameters specify the presentation format for the key frame. The 'Deforum' option is used to ensure compatibility with certain animation systems.
    - Comfy dtype: COMBO['Deforum']
    - Python dtype: str

# Output types
- keyframe_list
    - Keyframe_list output is a string expression of the key frame generated. Its format can be used directly in the animated system.
    - Comfy dtype: STRING
    - Python dtype: str
- show_help
    - Show_help output provides a document URL link to further assist and understand how to use the node effectively.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_SimplePromptListKeyframes:

    @classmethod
    def INPUT_TYPES(s):
        transition_types = ['Default']
        transition_speeds = ['Default']
        transition_profiles = ['Default']
        return {'required': {'simple_prompt_list': ('SIMPLE_PROMPT_LIST',), 'keyframe_interval': ('INT', {'default': 30, 'min': 0, 'max': 999, 'step': 1}), 'loops': ('INT', {'default': 1, 'min': 1, 'max': 1000}), 'transition_type': (transition_types,), 'transition_speed': (transition_speeds,), 'transition_profile': (transition_profiles,), 'keyframe_format': (['Deforum'],)}}
    RETURN_TYPES = ('STRING', 'STRING')
    RETURN_NAMES = ('keyframe_list', 'show_help')
    FUNCTION = 'make_keyframes'
    CATEGORY = icons.get('Comfyroll/Animation/Legacy')

    def make_keyframes(self, simple_prompt_list, keyframe_interval, loops, transition_type, transition_speed, transition_profile, keyframe_format):
        keyframe_format = 'Deforum'
        keyframe_list = list()
        i = 0
        for j in range(1, loops + 1):
            for (index, prompt) in enumerate(simple_prompt_list):
                if i == 0:
                    keyframe_list.extend(['"0": "' + prompt + '",\n'])
                    i += keyframe_interval
                    continue
                new_keyframe = '"' + str(i) + '": "' + prompt + '",\n'
                keyframe_list.extend([new_keyframe])
                i += keyframe_interval
        keyframes_out = ' '.join(keyframe_list)[:-2]
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Prompt-Nodes#cr-simple-prompt-list-keyframes'
        return (keyframes_out, show_help)
```