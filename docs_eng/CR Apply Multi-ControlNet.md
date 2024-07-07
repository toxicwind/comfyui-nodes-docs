# Documentation
- Class name: CR_ApplyControlNetStack
- Category: Comfyroll/ControlNet
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_ApplyControlNetStack is designed to apply a series of ContractorNet to a pair of basic images to enhance the control of the generation process. It manages the integration of multiple ContractorNets according to user-defined parameters and ensures fine particle size control of the final output.

# Input types
## Required
- base_positive
    - The base_positive parameter is a key input that represents a positive condition image. It is used as a reference to guide the use of ContractorNet and significantly influence the direction and quality of the output generated.
    - Comfy dtype: CONDITIONING
    - Python dtype: torch.Tensor
- base_negative
    - Base_negative parameters, as negative conditional images, help to refine the process by comparing them with base_positive images. It plays a vital role in guiding output away from undesirable features.
    - Comfy dtype: CONDITIONING
    - Python dtype: torch.Tensor
- switch
    - The switch parameter is a switch that determines whether to activate the KontrolNet stack application. It is essential to enable or disable the impact of ContractorNet on the generation process.
    - Comfy dtype: COMBO['Off', 'On']
    - Python dtype: str
## Optional
- controlnet_stack
    - The controlnet_stack parameter is an optional input that allows predefined ContractorNet pools to be applied to base images, once available. Each ConradNet in the stack contributes to overall conditionality and enhances the specificity and accuracy of the generation.
    - Comfy dtype: CONTROL_NET_STACK
    - Python dtype: List[Tuple[str, torch.Tensor, float, float, float]]

# Output types
- base_pos
    - Base_pos output is a positive condition image modified after application of the ContractorNet stack. It contains the collective effects of the ContractorNet for all applications and represents a fine guide to the generation process.
    - Comfy dtype: CONDITIONING
    - Python dtype: torch.Tensor
- base_neg
    - Base_neg output corresponds to a negative condition image modified during the application of the ContractorNet stack. It acts as a tool in shaping the final output by guiding it to avoid undesirable properties.
    - Comfy dtype: CONDITIONING
    - Python dtype: torch.Tensor
- show_help
    - Show_help output provides a URL linked to the CR_ApplyControlNetStack node for more help and guidance. This is a useful resource for users seeking more information about node functions and usages.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: GPU

# Source code
```
class CR_ApplyControlNetStack:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'base_positive': ('CONDITIONING',), 'base_negative': ('CONDITIONING',), 'switch': (['Off', 'On'],), 'controlnet_stack': ('CONTROL_NET_STACK',)}}
    RETURN_TYPES = ('CONDITIONING', 'CONDITIONING', 'STRING')
    RETURN_NAMES = ('base_pos', 'base_neg', 'show_help')
    FUNCTION = 'apply_controlnet_stack'
    CATEGORY = icons.get('Comfyroll/ControlNet')

    def apply_controlnet_stack(self, base_positive, base_negative, switch, controlnet_stack=None):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/ControlNet-Nodes#cr-apply-multi-controlnet-stack'
        if switch == 'Off':
            return (base_positive, base_negative, show_help)
        if controlnet_stack is not None:
            for controlnet_tuple in controlnet_stack:
                (controlnet_name, image, strength, start_percent, end_percent) = controlnet_tuple
                if type(controlnet_name) == str:
                    controlnet_path = folder_paths.get_full_path('controlnet', controlnet_name)
                    controlnet = comfy.sd.load_controlnet(controlnet_path)
                else:
                    controlnet = controlnet_name
                controlnet_conditioning = ControlNetApplyAdvanced().apply_controlnet(base_positive, base_negative, controlnet, image, strength, start_percent, end_percent)
                (base_positive, base_negative) = (controlnet_conditioning[0], controlnet_conditioning[1])
        return (base_positive, base_negative, show_help)
```