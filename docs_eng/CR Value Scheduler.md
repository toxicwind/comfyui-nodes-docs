# Documentation
- Class name: CR_ValueScheduler
- Category: Animation/Schedulers
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_ValueScheduler is a node used to manage value scheduling in animated workflows. It allows for the selection of default values or the application of planned values based on the current frame. This node provides a flexible way to handle different value allocation patterns and ensures that animation parameters are correctly set according to the given plan or default settings.

# Input types
## Required
- mode
    - The mode parameter determines whether the node should use the default or planned value. It is essential to define the mode of operation of the scheduler and influences the distribution of the values in the animation.
    - Comfy dtype: COMBO['Default Value', 'Schedule']
    - Python dtype: str
- current_frame
    - The current frame parameter specifies the current frame in the animated timeline. It is essential for nodes to determine the correct value to be applied from the plan or to use the default value when the current frame has no planned value.
    - Comfy dtype: INT
    - Python dtype: int
- default_value
    - The default value parameter setting node will be used when the mode is set as the " default value " or when the current frame has no available planned value. It plays an important role in ensuring that the animation has a consistent starting point or reserve value.
    - Comfy dtype: FLOAT
    - Python dtype: float
## Optional
- schedule_alias
    - The plan alias parameter is used to quote a particular plan in the animation. When the node runs in the Plan mode, it is important because it helps to identify which frames and parameters should be considered for value allocation.
    - Comfy dtype: STRING
    - Python dtype: str
- schedule_format
    - The plan format parameter defines the node that will explain the plan format. It is important to ensure that the node correctly understands and processes the planned data, which may be in different formats.
    - Comfy dtype: COMBO['CR', 'Deforum']
    - Python dtype: str
- schedule
    - The plan parameter provides the actual plan data that will be used to determine the current frame value. When the node is in the Plan mode, it is important because it directly affects the assigned value.
    - Comfy dtype: SCHEDULE
    - Python dtype: Schedule

# Output types
- int_out
    - The int_out parameter represents the integer value of the node output, which can be the result of the application of the plan or the default value. It is important for animated parameters that require the integer value.
    - Comfy dtype: INT
    - Python dtype: int
- float_out
    - The float_out parameter represents the floating point value of the node output, or the result of the application of the planned or default value. It is critical for animated parameters that require float accuracy.
    - Comfy dtype: FLOAT
    - Python dtype: float
- show_help
    - Show_help parameters provide a URL link to the node document that can be used to further guide or understand how to use the node effectively.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_ValueScheduler:

    @classmethod
    def INPUT_TYPES(s):
        modes = ['Default Value', 'Schedule']
        return {'required': {'mode': (modes,), 'current_frame': ('INT', {'default': 0.0, 'min': 0.0, 'max': 9999.0, 'step': 1.0}), 'schedule_alias': ('STRING', {'default': '', 'multiline': False}), 'default_value': ('FLOAT', {'default': 1.0, 'min': -9999.0, 'max': 9999.0, 'step': 0.01}), 'schedule_format': (['CR', 'Deforum'],)}, 'optional': {'schedule': ('SCHEDULE',)}}
    RETURN_TYPES = ('INT', 'FLOAT', 'STRING')
    RETURN_NAMES = ('INT', 'FLOAT', 'show_help')
    FUNCTION = 'schedule'
    CATEGORY = icons.get('Comfyroll/Animation/Schedulers')

    def schedule(self, mode, current_frame, schedule_alias, default_value, schedule_format, schedule=None):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Scheduler-Nodes#cr-value-scheduler'
        if mode == 'Default Value':
            print(f'[Info] CR Value Scheduler: Scheduler {schedule_alias} is disabled')
            (int_out, float_out) = (int(default_value), float(default_value))
            return (int_out, float_out, show_help)
        params = keyframe_scheduler(schedule, schedule_alias, current_frame)
        if params == '':
            if current_frame == 0:
                print(f'[Warning] CR Value Scheduler. No frame 0 found in schedule. Starting with default value at frame 0')
            (int_out, float_out) = (int(default_value), float(default_value))
        else:
            try:
                value = float(params)
                (int_out, float_out) = (int(value), float(value))
            except ValueError:
                print(f'[Warning] CR Value Scheduler. Invalid params: {params}')
                return ()
        return (int_out, float_out, show_help)
```