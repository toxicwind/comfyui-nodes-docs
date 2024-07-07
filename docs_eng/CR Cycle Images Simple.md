# Documentation
- Class name: CR_CycleImagesSimple
- Category: Animation
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

The CR_CycleImagesSimple node is designed to create animated effects by circulating through the list of images in sequence or randomly. It allows for frame spacing, frequency of loops and the current frame to control animated sequences. This node is particularly suitable for generating dynamic visual content from a set of images.

# Input types
## Required
- mode
    - Model parameters determine the sequence of image cycles. It can be set to 'Sequential' to recycle images in a given order, or it can support random patterns in future updates. This setting directly affects animation sequences and user experiences.
    - Comfy dtype: COMBO[str]
    - Python dtype: str
- frame_interval
    - The frame_interval parameter specifies the number of frames between each image change in the animation. It affects the speed of the image cycle and is essential to properly control the animation rhythm.
    - Comfy dtype: INT
    - Python dtype: int
- loops
    - Loops parameters set the number of times animated. It is important to define the duration of animated sequences and can be used to create continuous or limited animations.
    - Comfy dtype: INT
    - Python dtype: int
- current_frame
    - The Current_frame parameter indicates the starting point of the animation. It is essential for synchronizing the animation with other elements or for setting specific points in the animation sequence to start.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- image_1
    - Theimage_1 parameter is the first image that can be included in the animation cycle. It is important because it helps enrich the content and diversity of the animation sequence.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image
- image_list_simple
    - The image_list_simple parameter is the list of images that can be included in the animation loop. It provides flexibility when adding multiple images to the sequence and enhances the overall animation effect.
    - Comfy dtype: IMAGE_LIST_SIMPLE
    - Python dtype: List[PIL.Image.Image]

# Output types
- IMAGE
    - The IMAGE output provides the current image in the animation loop. It is the main visual result of node operations and is essential for displaying animations.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image
- show_help
    - Show_help output provides document URLs to obtain further help and information about node functions.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_CycleImagesSimple:

    @classmethod
    def INPUT_TYPES(s):
        modes = ['Sequential']
        return {'required': {'mode': (modes,), 'frame_interval': ('INT', {'default': 30, 'min': 0, 'max': 999, 'step': 1}), 'loops': ('INT', {'default': 1, 'min': 1, 'max': 1000}), 'current_frame': ('INT', {'default': 0.0, 'min': 0.0, 'max': 9999.0, 'step': 1.0})}, 'optional': {'image_1': ('IMAGE',), 'image_2': ('IMAGE',), 'image_3': ('IMAGE',), 'image_4': ('IMAGE',), 'image_5': ('IMAGE',), 'image_list_simple': ('IMAGE_LIST_SIMPLE',)}}
    RETURN_TYPES = ('IMAGE', 'STRING')
    RETURN_NAMES = ('IMAGE', 'show_help')
    FUNCTION = 'cycle_image'
    CATEGORY = icons.get('Comfyroll/Animation/Legacy')

    def cycle_image(self, mode, frame_interval, loops, current_frame, image_1=None, image_2=None, image_3=None, image_4=None, image_5=None, image_list_simple=None):
        image_params = list()
        image_list = list()
        if image_1 != None:
            (image_list.append(image_1),)
        if image_2 != None:
            (image_list.append(image_2),)
        if image_3 != None:
            (image_list.append(image_3),)
        if image_4 != None:
            (image_list.append(image_4),)
        if image_5 != None:
            (image_list.append(image_5),)
        for _ in range(loops):
            if image_list_simple:
                image_params.extend(image_list_simple)
            image_params.extend(image_list)
        if mode == 'Sequential':
            current_image_index = current_frame // frame_interval % len(image_params)
            print(f'[Debug] CR Cycle Text:{current_image_index}')
            current_image_item = image_params[current_image_index]
            show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Cycler-Nodes#cr-cycle-images-simple'
            return (current_image_item, show_help)
```