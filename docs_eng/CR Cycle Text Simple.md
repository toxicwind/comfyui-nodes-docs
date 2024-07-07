# Documentation
- Class name: CR_CycleTextSimple
- Category: Comfyroll/Animation/Legacy
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_CycleTextSimple is a node designed for a list of sequential loop text strings. It can handle multiple text inputes and loops according to the specified frame spacing and frequency. This node is particularly suitable for creating dynamic text animations in the Comfy UI environment.

# Input types
## Required
- mode
    - The mode parameter determines the circular order of the text string. It is essential to define the order and mode of the text animation.
    - Comfy dtype: COMBO[str]
    - Python dtype: str
- frame_interval
    - Frame spacing determines the speed of the text string loop and affects the speed of the animation.
    - Comfy dtype: int
    - Python dtype: int
- loops
    - The number of times a loop parameter specifies the number of times a text string will be looped, which affects the duration of the animation.
    - Comfy dtype: int
    - Python dtype: int
- current_frame
    - The current frame indicates the current position in the animation sequence to determine which text string to display.
    - Comfy dtype: int
    - Python dtype: int
## Optional
- text_1
    - Text_1 is an optional input for the first text string in the list. It provides a diversified text content for loops.
    - Comfy dtype: str
    - Python dtype: str
- text_list_simple
    - Text_list_simple is an optional parameter that allows for simplified input of more than one text string, simplifying the process of adding text content.
    - Comfy dtype: TEXT_LIST_SIMPLE
    - Python dtype: List[str]

# Output types
- current_text_item
    - The current text item represents the text string that is currently being displayed as part of the text loop animation.
    - Comfy dtype: str
    - Python dtype: str
- show_help
    - Show_help output provides a URL link to the document for further help and information about the use of nodes.
    - Comfy dtype: str
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_CycleTextSimple:

    @classmethod
    def INPUT_TYPES(s):
        modes = ['Sequential']
        return {'required': {'mode': (modes,), 'frame_interval': ('INT', {'default': 30, 'min': 0, 'max': 999, 'step': 1}), 'loops': ('INT', {'default': 1, 'min': 1, 'max': 1000}), 'current_frame': ('INT', {'default': 0.0, 'min': 0.0, 'max': 9999.0, 'step': 1.0})}, 'optional': {'text_1': ('STRING', {'multiline': False, 'default': ''}), 'text_2': ('STRING', {'multiline': False, 'default': ''}), 'text_3': ('STRING', {'multiline': False, 'default': ''}), 'text_4': ('STRING', {'multiline': False, 'default': ''}), 'text_5': ('STRING', {'multiline': False, 'default': ''}), 'text_list_simple': ('TEXT_LIST_SIMPLE',)}}
    RETURN_TYPES = ('STRING', 'STRING')
    RETURN_NAMES = ('STRING', 'show_help')
    FUNCTION = 'cycle_text'
    CATEGORY = icons.get('Comfyroll/Animation/Legacy')

    def cycle_text(self, mode, frame_interval, loops, current_frame, text_1, text_2, text_3, text_4, text_5, text_list_simple=None):
        text_params = list()
        text_list = list()
        if text_1 != '':
            text_list.append(text_1)
        if text_2 != '':
            text_list.append(text_2)
        if text_3 != '':
            text_list.append(text_3)
        if text_4 != '':
            text_list.append(text_4)
        if text_5 != '':
            text_list.append(text_5)
        for _ in range(loops):
            if text_list_simple:
                text_params.extend(text_list_simple)
            text_params.extend(text_list)
        if mode == 'Sequential':
            current_text_index = current_frame // frame_interval % len(text_params)
            current_text_item = text_params[current_text_index]
            show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Cycler-Nodes#cr-cycle-text-simple'
            return (current_text_item, show_help)
```