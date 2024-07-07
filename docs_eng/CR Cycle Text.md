# Documentation
- Class name: CR_CycleText
- Category: Comfyroll/Animation/Legacy
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

The CR_CycleText node is designed to loop through the predefined list of text entries at specified intervals, creating animated text series. It runs in a continuous mode, with an iterative text list showing dynamic text. This node is particularly suitable for applications that require text-based animations, such as presentations or interactive displays.

# Input types
## Required
- mode
    - Model parameters determine the circular order of text items. It is essential for determining the order and pattern of text animations.
    - Comfy dtype: COMBO[str]
    - Python dtype: str
- text_list
    - The text_list parameter is a list of text entries that the node will loop through. It is necessary because it defines the animated content.
    - Comfy dtype: TEXT_LIST
    - Python dtype: List[str]
## Optional
- frame_interval
    - The frame_interval parameter specifies the time interval between each text change in the animation. It affects the speed of the text cycle.
    - Comfy dtype: INT
    - Python dtype: int
- loops
    - The loops parameter determines the number of times the text list will be looped. It controls the duration of the animation sequence.
    - Comfy dtype: INT
    - Python dtype: int
- current_frame
    - The Current_frame parameter indicates the current position in the text animation. It is used to track the animation's progress.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- STRING
    - The STRING output provides the current text item in the list of text in circulation.
    - Comfy dtype: STRING
    - Python dtype: str
- show_help
    - Show_help output provides a link to a document to obtain further help or detailed information about node operations.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_CycleText:

    @classmethod
    def INPUT_TYPES(s):
        modes = ['Sequential']
        return {'required': {'mode': (modes,), 'text_list': ('TEXT_LIST',), 'frame_interval': ('INT', {'default': 30, 'min': 0, 'max': 999, 'step': 1}), 'loops': ('INT', {'default': 1, 'min': 1, 'max': 1000}), 'current_frame': ('INT', {'default': 0.0, 'min': 0.0, 'max': 9999.0, 'step': 1.0})}}
    RETURN_TYPES = ('STRING', 'STRING')
    RETURN_NAMES = ('STRING', 'show_help')
    FUNCTION = 'cycle_text'
    CATEGORY = icons.get('Comfyroll/Animation/Legacy')

    def cycle_text(self, mode, text_list, frame_interval, loops, current_frame):
        text_params = list()
        if text_list:
            for _ in range(loops):
                text_params.extend(text_list)
        if mode == 'Sequential':
            current_text_index = current_frame // frame_interval % len(text_params)
            current_text_params = text_params[current_text_index]
            print(f'[Debug] CR Cycle Text:{current_text_params}')
            (text_alias, current_text_item) = current_text_params
            show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Cycler-Nodes#cr-cycle-text'
            return (current_text_item, show_help)
```