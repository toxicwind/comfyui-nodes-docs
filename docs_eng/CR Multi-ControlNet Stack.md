# Documentation
- Class name: CR_ControlNetStack
- Category: Comfyroll/ControlNet
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_ControlNetStack is a node used to manage and apply multiple ContractorNet configurations in an sequential manner. It allows users to switch various ControlNet switches, adjust their impact and define the range they should apply. This node is essential to fine-tune the control and direction of the image generation process, ensuring high customization and accuracy.

# Input types
## Optional
- switch_1
    - Switch parameters determine whether the first ControlNet is activated in a warehouse. It plays a key role in controlling the signal stream within the control node and can enable or disable a specific impact layer.
    - Comfy dtype: COMBO['Off', 'On']
    - Python dtype: str
- controlnet_1
    - The contronet_1 parameter specifies the first ControlNet to be used in the warehouse. It is essential to define the control type to be applied and has a significant impact on the results of the image generation process.
    - Comfy dtype: COMBO[<list of controlnet filenames>]
    - Python dtype: str
- controlnet_strength_1
    - The contronet_strength_1 parameter adjusts the intensity of the impact of the first ControlNet. It is a key factor in the balance between the different control layers within the microregulating point.
    - Comfy dtype: FLOAT
    - Python dtype: float
- start_percent_1
    - The start_percent_1 parameter defines the starting percentage of the first controlNet in the image generation process. It is important to control the spatial distribution of the control signal.
    - Comfy dtype: FLOAT
    - Python dtype: float
- end_percent_1
    - The end_percent_1 parameter marks the percentage of the first controlNet impact ending in the image generation process. It is essential to determine the range of control applications.
    - Comfy dtype: FLOAT
    - Python dtype: float
- image_1
    - The image_1 parameter represents the image associated with the first ControlNet. It is essential to provide visual context and guidance for the control mechanism.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image

# Output types
- CONTROLNET_STACK
    - The CONTROLNET_STACK output contains a compiled list of active ContractorNets and their respective settings, which are prepared for application in the image generation process.
    - Comfy dtype: CONTROL_NET_STACK
    - Python dtype: List[Tuple[comfy.controlnet.ControlNet, PIL.Image, float, float, float]]
- show_help
    - Show_help output provides a URL to a document to obtain further guidance on the use of CR_ControlNetStack nodes.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_ControlNetStack:
    controlnets = ['None'] + folder_paths.get_filename_list('controlnet')

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {}, 'optional': {'switch_1': (['Off', 'On'],), 'controlnet_1': (cls.controlnets,), 'controlnet_strength_1': ('FLOAT', {'default': 1.0, 'min': -10.0, 'max': 10.0, 'step': 0.01}), 'start_percent_1': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1.0, 'step': 0.001}), 'end_percent_1': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.001}), 'switch_2': (['Off', 'On'],), 'controlnet_2': (cls.controlnets,), 'controlnet_strength_2': ('FLOAT', {'default': 1.0, 'min': -10.0, 'max': 10.0, 'step': 0.01}), 'start_percent_2': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1.0, 'step': 0.001}), 'end_percent_2': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.001}), 'switch_3': (['Off', 'On'],), 'controlnet_3': (cls.controlnets,), 'controlnet_strength_3': ('FLOAT', {'default': 1.0, 'min': -10.0, 'max': 10.0, 'step': 0.01}), 'start_percent_3': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1.0, 'step': 0.001}), 'end_percent_3': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.001}), 'image_1': ('IMAGE',), 'image_2': ('IMAGE',), 'image_3': ('IMAGE',), 'controlnet_stack': ('CONTROL_NET_STACK',)}}
    RETURN_TYPES = ('CONTROL_NET_STACK', 'STRING')
    RETURN_NAMES = ('CONTROLNET_STACK', 'show_help')
    FUNCTION = 'controlnet_stacker'
    CATEGORY = icons.get('Comfyroll/ControlNet')

    def controlnet_stacker(self, switch_1, controlnet_1, controlnet_strength_1, start_percent_1, end_percent_1, switch_2, controlnet_2, controlnet_strength_2, start_percent_2, end_percent_2, switch_3, controlnet_3, controlnet_strength_3, start_percent_3, end_percent_3, image_1=None, image_2=None, image_3=None, controlnet_stack=None):
        controlnet_list = []
        if controlnet_stack is not None:
            controlnet_list.extend([l for l in controlnet_stack if l[0] != 'None'])
        if controlnet_1 != 'None' and switch_1 == 'On' and (image_1 is not None):
            controlnet_path = folder_paths.get_full_path('controlnet', controlnet_1)
            controlnet_1 = comfy.controlnet.load_controlnet(controlnet_path)
            (controlnet_list.extend([(controlnet_1, image_1, controlnet_strength_1, start_percent_1, end_percent_1)]),)
        if controlnet_2 != 'None' and switch_2 == 'On' and (image_2 is not None):
            controlnet_path = folder_paths.get_full_path('controlnet', controlnet_2)
            controlnet_2 = comfy.controlnet.load_controlnet(controlnet_path)
            (controlnet_list.extend([(controlnet_2, image_2, controlnet_strength_2, start_percent_2, end_percent_2)]),)
        if controlnet_3 != 'None' and switch_3 == 'On' and (image_3 is not None):
            controlnet_path = folder_paths.get_full_path('controlnet', controlnet_3)
            controlnet_3 = comfy.controlnet.load_controlnet(controlnet_path)
            (controlnet_list.extend([(controlnet_3, image_3, controlnet_strength_3, start_percent_3, end_percent_3)]),)
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/ControlNet-Nodes#cr-multi-controlnet-stack'
        return (controlnet_list, show_help)
```