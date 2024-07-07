# Documentation
- Class name: CR_CycleModels
- Category: Comfyroll/Animation/Legacy
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_CycleModels nodes are designed to manage and circular the list of browsing models according to specified parameters (e.g. mode, frame spacing and frequency of loops). It provides the function of selecting and processing models sequentially, or is based on a predefined list, making them multifunctional tools in the animation workflow that requires model conversion.

# Input types
## Required
- mode
    - Model parameters determine the behaviour of the model cycle. It can be set as 'Off' or 'Sequential' and affect how nodes travel through the model list.
    - Comfy dtype: COMBO[string]
    - Python dtype: str
- model
    - Model parameters represent the initial model used in the animation sequence. It is essential for setting the baseline for subsequent model conversion.
    - Comfy dtype: MODEL
    - Python dtype: Any
- clip
    - Cut parameters are used to save references to specific clips in animated drawings and can be operated or replaced during model loops.
    - Comfy dtype: CLIP
    - Python dtype: Any
- frame_interval
    - The frame_interval parameter specifies the spacing of the model cycle in the animation. It is a key factor in controlling the rhythm of model conversion.
    - Comfy dtype: INT
    - Python dtype: int
- loops
    - The loops parameter defines the number of times the model list should loop. It is essential to control the duration of the animation sequence.
    - Comfy dtype: INT
    - Python dtype: int
- current_frame
    - Current_frame parameters indicate the current frame in the animation sequence. It is used to determine which model to use at any given time.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- model_list
    - The model_list parameter is a list of models, and nodes can loop through these models. It provides flexibility in defining the model sequences used in animations.
    - Comfy dtype: MODEL_LIST
    - Python dtype: List[Any]

# Output types
- MODEL
    - Output MODEL represents the current model used in the animation sequence after circulation through the model list.
    - Comfy dtype: MODEL
    - Python dtype: Any
- CLIP
    - Output CLIP is the current clip associated with the animation after the conversion of the processing model.
    - Comfy dtype: CLIP
    - Python dtype: Any
- VAE
    - The VAE output provided a variable coder configuration for the selected model, which could be used for further processing or analysis.
    - Comfy dtype: VAE
    - Python dtype: Any
- show_help
    - Show_help output means a URL link to a node document that provides additional information and guidance on its use.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_CycleModels:

    @classmethod
    def INPUT_TYPES(s):
        modes = ['Off', 'Sequential']
        return {'required': {'mode': (modes,), 'model': ('MODEL',), 'clip': ('CLIP',), 'model_list': ('MODEL_LIST',), 'frame_interval': ('INT', {'default': 30, 'min': 0, 'max': 999, 'step': 1}), 'loops': ('INT', {'default': 1, 'min': 1, 'max': 1000}), 'current_frame': ('INT', {'default': 0.0, 'min': 0.0, 'max': 9999.0, 'step': 1.0})}}
    RETURN_TYPES = ('MODEL', 'CLIP', 'VAE', 'STRING')
    RETURN_NAMES = ('MODEL', 'CLIP', 'VAE', 'show_help')
    FUNCTION = 'cycle_models'
    CATEGORY = icons.get('Comfyroll/Animation/Legacy')

    def cycle_models(self, mode, model, clip, model_list, frame_interval, loops, current_frame):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Cycler-Nodes#cr-cycle-models'
        model_params = list()
        if model_list:
            for _ in range(loops):
                model_params.extend(model_list)
        if mode == 'Off':
            return (model, clip, show_help)
        elif mode == 'Sequential':
            if current_frame == 0:
                return (model, clip, show_help)
            else:
                current_model_index = current_frame // frame_interval % len(model_params)
                current_model_params = model_params[current_model_index]
                (model_alias, ckpt_name) = current_model_params
                print(f'[Info] CR Cycle Models: Current model is {ckpt_name}')
                ckpt_path = folder_paths.get_full_path('checkpoints', ckpt_name)
                out = comfy.sd.load_checkpoint_guess_config(ckpt_path, output_vae=True, output_clip=True, embedding_directory=folder_paths.get_folder_paths('embeddings'))
                return (out, show_help)
```