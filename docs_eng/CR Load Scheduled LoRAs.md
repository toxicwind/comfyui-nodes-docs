# Documentation
- Class name: CR_LoadScheduledLoRAs
- Category: Comfyroll/Animation/Schedulers
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_LoadScheduledLoRAs is a node for managing and applying the planned LoRAs (low adaptation) to models and clips. It allows users to specify operating models, including banning the function, loading default LoRAs or following a custom plan. This node selects the appropriate LoRA according to the current frame dynamics, ensuring that models and clips are enhanced or modified according to the user's plan.

# Input types
## Required
- mode
    - The mode parameter determines how the node handles the load of LoRA. It can be set to close, load the default LoRA or load according to the plan.
    - Comfy dtype: COMBO
    - Python dtype: str
- model
    - Models that need to be addressed.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- clip
    - Need to deal with clip.
    - Comfy dtype: CLIP
    - Python dtype: torch.Tensor
- current_frame
    - The current frame number is used to determine which LoRA is loaded according to the plan.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- schedule_alias
    - Plan aliases for quick selection of a predefined set of LoRA loading plans.
    - Comfy dtype: STRING
    - Python dtype: str
- default_lora
    - When no LoRA is specified for the current frame, the default LoRA name will be used.
    - Comfy dtype: STRING
    - Python dtype: str
- strength_model
    - The strength factor of the model is used to adjust the impact of LoRA on the model.
    - Comfy dtype: FLOAT
    - Python dtype: float
- strength_clip
    - The strength factor for clip is used to adjust the impact of LoRA on clip.
    - Comfy dtype: FLOAT
    - Python dtype: float
- schedule_format
    - The format of the plan determines how to interpret and apply the LoRA loading plan.
    - Comfy dtype: COMBO
    - Python dtype: str
- lora_list
    - An optional list of LoRAs provides a range of LoRA options for planning options.
    - Comfy dtype: LORA_LIST
    - Python dtype: List[str]
- schedule
    - The custom LoRA loading plan specifies in detail the LoRA and its parameters that each frame should load.
    - Comfy dtype: SCHEDULE
    - Python dtype: List[Tuple[str, str]]

# Output types
- MODEL
    - The treated model may have been applied to LoRA.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- CLIP
    - After processing clip, it's probably already applied to LoRA.
    - Comfy dtype: CLIP
    - Python dtype: torch.Tensor
- show_help
    - Links to help documents to provide users with more information on how to use the node.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_LoadScheduledLoRAs:

    @classmethod
    def INPUT_TYPES(s):
        modes = ['Off', 'Load default LoRA', 'Schedule']
        return {'required': {'mode': (modes,), 'model': ('MODEL',), 'clip': ('CLIP',), 'current_frame': ('INT', {'default': 0.0, 'min': 0.0, 'max': 9999.0, 'step': 1.0}), 'schedule_alias': ('STRING', {'default': '', 'multiline': False}), 'default_lora': (folder_paths.get_filename_list('loras'),), 'strength_model': ('FLOAT', {'default': 1.0, 'min': -10.0, 'max': 10.0, 'step': 0.01}), 'strength_clip': ('FLOAT', {'default': 1.0, 'min': -10.0, 'max': 10.0, 'step': 0.01}), 'schedule_format': (['CR', 'Deforum'],)}, 'optional': {'lora_list': ('LORA_LIST',), 'schedule': ('SCHEDULE',)}}
    RETURN_TYPES = ('MODEL', 'CLIP', 'STRING')
    RETURN_NAMES = ('MODEL', 'CLIP', 'show_help')
    FUNCTION = 'schedule'
    CATEGORY = icons.get('Comfyroll/Animation/Schedulers')

    def schedule(self, mode, model, clip, current_frame, schedule_alias, default_lora, strength_model, strength_clip, schedule_format, lora_list=None, schedule=None):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Scheduler-Nodes#cr-load-scheduled-loras'
        if mode == 'Off':
            print(f'[Info] CR Load Scheduled LoRAs. Disabled.')
            return (model, clip, show_help)
        if mode == 'Load default LoRA':
            if default_lora == None:
                return (model, clip, show_help)
            if strength_model == 0 and strength_clip == 0:
                return (model, clip, show_help)
            (model, clip) = LoraLoader().load_lora(model, clip, default_lora, strength_model, strength_clip)
            print(f'[Info] CR Load Scheduled LoRAs. Loading default LoRA {lora_name}.')
            return (model, clip, show_help)
        params = keyframe_scheduler(schedule, schedule_alias, current_frame)
        if params == '':
            print(f'[Warning] CR Load Scheduled LoRAs. No LoRA specified in schedule for frame {current_frame}. Using default lora.')
            if default_lora != None:
                (model, clip) = LoraLoader().load_lora(model, clip, default_lora, strength_model, strength_clip)
            return (model, clip, show_help)
        else:
            parts = params.split(',')
            if len(parts) == 3:
                s_lora_alias = parts[0].strip()
                s_strength_model = float(parts[1].strip())
                s_strength_clip = float(parts[1].strip())
            else:
                print(f'[Warning] CR Simple Value Scheduler. Skipped invalid line: {line}')
                return ()
        for (l_lora_alias, l_lora_name, l_strength_model, l_strength_clip) in lora_list:
            print(l_lora_alias, l_lora_name, l_strength_model, l_strength_clip)
            if l_lora_alias == s_lora_alias:
                print(f'[Info] CR Load Scheduled LoRAs. LoRA alias match found for {s_lora_alias}')
                lora_name = l_lora_name
                break
        if lora_name == '':
            print(f'[Info] CR Load Scheduled LoRAs. No LoRA alias match found for {s_lora_alias}. Frame {current_frame}.')
            return ()
        else:
            print(f'[Info] CR Load Scheduled LoRAs. LoRA {lora_name}')
        (model, clip) = LoraLoader().load_lora(model, clip, lora_name, s_strength_model, s_strength_clip)
        print(f'[Debug] CR Load Scheduled LoRAs. Loading new LoRA {lora_name}')
        return (model, clip, show_help)
```