# Documentation
- Class name: CR_SimpleValueScheduler
- Category: Comfyroll/Animation/Schedulers
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_SimpleValueScheduler is a node for the schedule of key frames to manage and plug in values. It plays a key role in smooth transitions and dynamic changes between frames, providing users with a simple and direct way to organize and operate values over time.

# Input types
## Required
- schedule
    - Schedule input is essential to define the key frame values that change over time. It allows different values to be specified on different frames so that nodes can be inserted between them.
    - Comfy dtype: STRING
    - Python dtype: str
- current_frame
    - The Current_frame parameter indicates the current position in the animated time line. It is essential to determine which predefined values are to be applied at any given time.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- INT
    - The INT output provides an integer of the current frame value, which can be used to calculate values in animated water flow lines.
    - Comfy dtype: INT
    - Python dtype: int
- FLOAT
    - The FLOAT output provides an explanation of the floating points of the intended value and applies to more accurate calculations and adjustments during the animation process.
    - Comfy dtype: FLOAT
    - Python dtype: float
- show_help
    - Show_help output provides document links for further guidance and assistance in using CR_SimpleValueScheduler nodes.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_SimpleValueScheduler:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'schedule': ('STRING', {'multiline': True, 'default': 'frame_number, value'}), 'current_frame': ('INT', {'default': 0.0, 'min': 0.0, 'max': 9999.0, 'step': 1.0})}}
    RETURN_TYPES = ('INT', 'FLOAT', 'STRING')
    RETURN_NAMES = ('INT', 'FLOAT', 'show_help')
    FUNCTION = 'simple_schedule'
    CATEGORY = icons.get('Comfyroll/Animation/Schedulers')

    def simple_schedule(self, schedule, current_frame):
        schedule_lines = list()
        if schedule == '':
            print(f'[Warning] CR Simple Value Scheduler. No lines in schedule')
            return ()
        lines = schedule.split('\n')
        for line in lines:
            schedule_lines.extend([('SIMPLE', line)])
        params = keyframe_scheduler(schedule_lines, 'SIMPLE', current_frame)
        if params == '':
            print(f'[Warning] CR Simple Value Scheduler. No schedule found for frame. Simple schedules must start at frame 0.')
        else:
            try:
                int_out = int(params.split('.')[0])
                float_out = float(params)
            except ValueError:
                print(f'[Warning] CR Simple Value Scheduler. Invalid params {params} at frame {current_frame}')
            show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Scheduler-Nodes#cr-simple-value-scheduler'
            return (int_out, float_out, show_help)
```