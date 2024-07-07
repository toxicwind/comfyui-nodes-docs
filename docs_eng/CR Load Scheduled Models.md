# Documentation
- Class name: CR_LoadScheduledModels
- Category: Comfyroll/Animation/Schedulers
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_LoadScheduledModels nodes are designed to manage the loading of models according to a predefined timetable. It allows the selection of default models or the loading of different models in the specified frame dynamics, increasing the flexibility and adaptability of models in various scenarios.

# Input types
## Required
- mode
    - Model parameters determine whether to load the default model or to select the model according to the timetable. It is essential for the operation of the node, as it determines the loading behaviour of the model.
    - Comfy dtype: COMBO[string]
    - Python dtype: str
- current_frame
    - The current frame parameter specifies the current frame in the animation or sequence, which is essential for determining the model to be loaded according to the timetable.
    - Comfy dtype: INT
    - Python dtype: int
- default_model
    - The default model parameter sets the back-up model that is used when the current frame does not schedule a specific model.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- schedule_alias
    - Schedule alias parameters provide identifiers for a given schedule within the node, which influences how the node interprets and applies the schedule to load the model.
    - Comfy dtype: STRING
    - Python dtype: str
- schedule_format
    - Timetable format parameters define the structure and format of the nodes used to load the schedule in the model.
    - Comfy dtype: COMBO[string]
    - Python dtype: str
- model_list
    - Model list parameters include a list of models with their respective aliases, which are used to match and load models according to schedule aliases.
    - Comfy dtype: MODEL_LIST
    - Python dtype: List[Tuple[str, str]]
- schedule
    - Timetable parameters represent the actual schedule of models to be loaded in a given frame and guide the operation of nodes.
    - Comfy dtype: SCHEDULE
    - Python dtype: str

# Output types
- MODEL
    - MODEL output provides a model for loading based on schedule or default settings, which is the core of the node function.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- CLIP
    - The CLIP output is linked to the contextual image processing model, which complements the main model's function in understanding and generating images.
    - Comfy dtype: CLIP
    - Python dtype: torch.nn.Module
- VAE
    - The VAE output represents a variable from the encoder component, which is critical to the ability of the model to generate new data points.
    - Comfy dtype: VAE
    - Python dtype: torch.nn.Module
- show_help
    - Show_help output provides a document URL to provide further help and guidance when using nodes.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_LoadScheduledModels:

    @classmethod
    def INPUT_TYPES(s):
        modes = ['Load default Model', 'Schedule']
        return {'required': {'mode': (modes,), 'current_frame': ('INT', {'default': 0.0, 'min': 0.0, 'max': 9999.0, 'step': 1.0}), 'schedule_alias': ('STRING', {'default': '', 'multiline': False}), 'default_model': (folder_paths.get_filename_list('checkpoints'),), 'schedule_format': (['CR', 'Deforum'],)}, 'optional': {'model_list': ('MODEL_LIST',), 'schedule': ('SCHEDULE',)}}
    RETURN_TYPES = ('MODEL', 'CLIP', 'VAE', 'STRING')
    RETURN_NAMES = ('MODEL', 'CLIP', 'VAE', 'show_help')
    FUNCTION = 'schedule'
    CATEGORY = icons.get('Comfyroll/Animation/Schedulers')

    def schedule(self, mode, current_frame, schedule_alias, default_model, schedule_format, model_list=None, schedule=None):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Scheduler-Nodes#cr-load-scheduled-models'
        if mode == 'Load default Model':
            ckpt_path = folder_paths.get_full_path('checkpoints', default_model)
            out = comfy.sd.load_checkpoint_guess_config(ckpt_path, output_vae=True, output_clip=True, embedding_directory=folder_paths.get_folder_paths('embeddings'))
            print(f'[Debug] CR Load Scheduled Models. Loading default model.')
            return (out[:3], show_help)
        params = keyframe_scheduler(schedule, schedule_alias, current_frame)
        if params == '':
            print(f'[Warning] CR Load Scheduled Models. No model specified in schedule for frame {current_frame}. Using default model.')
            ckpt_path = folder_paths.get_full_path('checkpoints', default_model)
            out = comfy.sd.load_checkpoint_guess_config(ckpt_path, output_vae=True, output_clip=True, embedding_directory=folder_paths.get_folder_paths('embeddings'))
            return (out[:3], show_help)
        else:
            try:
                model_alias = str(params)
            except ValueError:
                print(f'[Warning] CR Load Scheduled Models. Invalid params: {params}')
                return ()
        for (ckpt_alias, ckpt_name) in model_list:
            if ckpt_alias == model_alias:
                model_name = ckpt_name
                break
        if model_name == '':
            print(f'[Info] CR Load Scheduled Models. No model alias match found for {model_alias}. Frame {current_frame} will produce an error.')
            return ()
        else:
            print(f'[Info] CR Load Scheduled Models. Model alias {model_alias} matched to {model_name}')
        ckpt_path = folder_paths.get_full_path('checkpoints', model_name)
        out = comfy.sd.load_checkpoint_guess_config(ckpt_path, output_vae=True, output_clip=True, embedding_directory=folder_paths.get_folder_paths('embeddings'))
        print(f'[Info] CR Load Scheduled Models. Loading new checkpoint model {model_name}')
        return (out[:3], show_help)
```