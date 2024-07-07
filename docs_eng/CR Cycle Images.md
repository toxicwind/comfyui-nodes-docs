# Documentation
- Class name: CR_CycleImages
- Category: Comfyroll/Animation/Legacy
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

The CR_CycleImages node is designed to loop through the list of images, providing a mechanism for displaying images in the specified frame spacing order. It is particularly suitable for creating animations or slides from a collection of images. This node operates the current image by selecting a list of multiple images based on 'curent_frame' and 'frame_interval' parameters.

# Input types
## Required
- mode
    - Model parameters determine the sequence of image cycles. Only the 'Sequential' mode is currently supported, ensuring that images are displayed in the order in which they appear in the image list.
    - Comfy dtype: STRING
    - Python dtype: str
- image_list
    - The image_list is a collection of images that you want to loop. Each entry in the list should be a group that contains the image aliases and the image object itself.
    - Comfy dtype: IMAGE_LIST
    - Python dtype: List[Tuple[str, Image.Image]]
## Optional
- frame_interval
    - The frame_interval parameter specifies the frame delay between each image display. It is essential to control the speed of animated drawings or slides.
    - Comfy dtype: INT
    - Python dtype: int
- loops
    - The loops parameter determines how many times an image list will be recycled. It allows the duration of animated drawings or slides to be controlled.
    - Comfy dtype: INT
    - Python dtype: int
- current_frame
    - The Current_frame parameter indicates the current position in the loop to determine which image is displayed at any given time.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- IMAGE
    - The IMAGE output provides the current circular image based on input parameters. It is the visual result of node operations and is the core of the node function.
    - Comfy dtype: IMAGE
    - Python dtype: Image.Image
- show_help
    - Show_help output provides a URL linked to the document page to obtain further help or details about the use of nodes.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_CycleImages:

    @classmethod
    def INPUT_TYPES(s):
        modes = ['Sequential']
        return {'required': {'mode': (modes,), 'image_list': ('IMAGE_LIST',), 'frame_interval': ('INT', {'default': 30, 'min': 0, 'max': 999, 'step': 1}), 'loops': ('INT', {'default': 1, 'min': 1, 'max': 1000}), 'current_frame': ('INT', {'default': 0.0, 'min': 0.0, 'max': 9999.0, 'step': 1.0})}}
    RETURN_TYPES = ('IMAGE', 'STRING')
    RETURN_NAMES = ('IMAGE', 'show_help')
    FUNCTION = 'cycle'
    CATEGORY = icons.get('Comfyroll/Animation/Legacy')

    def cycle(self, mode, image_list, frame_interval, loops, current_frame):
        image_params = list()
        if image_list:
            for _ in range(loops):
                image_params.extend(image_list)
        if mode == 'Sequential':
            current_image_index = current_frame // frame_interval % len(image_params)
            print(f'[Debug] CR Cycle Image:{current_image_index}')
            current_image_params = image_params[current_image_index]
            (image_alias, current_image_item) = current_image_params
            show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Cycler-Nodes#cr-cycle-images'
            return (current_image_item, show_help)
```