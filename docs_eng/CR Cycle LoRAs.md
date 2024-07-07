# Documentation
- Class name: CR_CycleLoRAs
- Category: Comfyroll/Animation/Legacy
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

The CR_CycleLoRAs node is designed to manage and loop the list of LoRA (low adaptive) parameters of past models and clips, which are used in the specified animated frame. It enhances the diversity and dynamics of the creation of animations through the sequential application of different LoRA adjustments. The node uses the list of LoRA parameters as predefined over time, applying them in a circular manner based on the current frame and frame spacing, thus creating complex and evolving visual effects.

# Input types
## Required
- mode
    - The mode parameter determines the operation of the node. It determines whether the node is in 'Close'state, nothing is done, or 'Order' mode, which circulates through the LoRA parameters. This option significantly influences how the node deals with input and result animation sequences.
    - Comfy dtype: COMBO['Off', 'Sequential']
    - Python dtype: str
- model
    - Model parameters are essential because they represent the core model where the node will operate using the specified LoRA parameters. The adaptation of the model to the LoRA adjustment is key to achieving the desired animation effect.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- clip
    - Cut parameters are essential to provide a visual context where nodes will work with the model. They are used to apply LoRA adjustments with the model to create a coherent animation.
    - Comfy dtype: CLIP
    - Python dtype: torch.Tensor
- lora_list
    - The lora_list parameter is a list of LoRA parameters that will be recycled by nodes. Each element in this list represents a different set of adjustments that can be applied to models and clips, contributing to the diversity of animations.
    - Comfy dtype: LORA_LIST
    - Python dtype: List[Tuple[str, str, float, float]]
## Optional
- frame_interval
    - The frame_interval parameter defines the frequency of nodes to loop through the LoRA parameter. It is essential to control the rhythm and time of the animation sequence.
    - Comfy dtype: INT
    - Python dtype: int
- loops
    - The loops parameter specifies the number of times a node circulates the entire list of LoRA parameters. It affects the duration and repetition of animated effects.
    - Comfy dtype: INT
    - Python dtype: int
- current_frame
    - Current_frame parameters indicate the current position in the animation sequence. It is used to determine which LoRA parameters are applied at any given time.
    - Comfy dtype: INT
    - Python dtype: float

# Output types
- MODEL
    - The output MODEL represents the application of the LoRA-adjusted model based on the current frame and frame spacing. This is the main output, carrying the visual changes anticipated by the animation.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- CLIP
    - The output CLIP is a visual expression adjusted by the LoRA parameter in conjunction with MODEL. It supplements MODEL to provide a complete animation sequence.
    - Comfy dtype: CLIP
    - Python dtype: torch.Tensor
- show_help
    - Show_help output provides a URL link to a document to obtain further help or information about node operations.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_CycleLoRAs:

    @classmethod
    def INPUT_TYPES(s):
        modes = ['Off', 'Sequential']
        return {'required': {'mode': (modes,), 'model': ('MODEL',), 'clip': ('CLIP',), 'lora_list': ('LORA_LIST',), 'frame_interval': ('INT', {'default': 30, 'min': 0, 'max': 999, 'step': 1}), 'loops': ('INT', {'default': 1, 'min': 1, 'max': 1000}), 'current_frame': ('INT', {'default': 0.0, 'min': 0.0, 'max': 9999.0, 'step': 1.0})}}
    RETURN_TYPES = ('MODEL', 'CLIP', 'STRING')
    RETURN_NAMES = ('MODEL', 'CLIP', 'show_help')
    FUNCTION = 'cycle'
    CATEGORY = icons.get('Comfyroll/Animation/Legacy')

    def cycle(self, mode, model, clip, lora_list, frame_interval, loops, current_frame):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Cycler-Nodes#cr-cycle-loras'
        lora_params = list()
        if lora_list:
            for _ in range(loops):
                lora_params.extend(lora_list)
        else:
            return (model, clip, show_help)
        if mode == 'Sequential':
            current_lora_index = current_frame // frame_interval % len(lora_params)
            current_lora_params = lora_params[current_lora_index]
            (lora_alias, lora_name, model_strength, clip_strength) = current_lora_params
            lora_path = folder_paths.get_full_path('loras', lora_name)
            lora = comfy.utils.load_torch_file(lora_path, safe_load=True)
            print(f'[Info] CR_CycleLoRAs: Current LoRA is {lora_name}')
            (model_lora, clip_lora) = comfy.sd.load_lora_for_models(model, clip, lora, model_strength, clip_strength)
            return (model_lora, clip_lora, show_help)
        else:
            return (model, clip, show_help)
```