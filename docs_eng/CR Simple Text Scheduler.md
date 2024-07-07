# Documentation
- Class name: CR_SimpleTextScheduler
- Category: Comfyroll/Animation/Schedulers
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_SimpleTextScheduler is a node for managing and scheduling text output based on the current frame in the predefined key frame collection and animation sequence. This node provides a simple interface for users to enter a timetable and retrieve the corresponding text for the given frame to ensure seamless integration of dynamic text elements in the animation.

# Input types
## Required
- schedule
    - The schedule parameter is a string that contains information on the text scheduler's key frame. It is essential to define the order of text changes in the entire animation. Multiline attributes allow a more complex time schedule definition that can be entered across multiple lines.
    - Comfy dtype: STRING
    - Python dtype: str
- current_frame
    - The Current_frame parameter indicates the current position in the animation sequence. It is essential to determine which text in the schedule should be displayed at any given time. Integer types ensure accurate frame tracking.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- text_out
    - Text_out parameters represent the text shown in the current frame plan. This is the main output of the node and provides dynamic text content consistent with animation progress.
    - Comfy dtype: STRING
    - Python dtype: str
- show_help
    - Show_help parameters provide a document URL link for further help. It is particularly useful for more users who need to use node or trouble resolution information.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_SimpleTextScheduler:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'schedule': ('STRING', {'multiline': True, 'default': 'frame_number, text'}), 'current_frame': ('INT', {'default': 0.0, 'min': 0.0, 'max': 9999.0, 'step': 1.0})}}
    RETURN_TYPES = ('STRING', 'STRING')
    RETURN_NAMES = ('STRING', 'show_help')
    FUNCTION = 'simple_schedule'
    CATEGORY = icons.get('Comfyroll/Animation/Schedulers')

    def simple_schedule(self, schedule, current_frame):
        schedule_lines = list()
        if schedule == '':
            print(f'[Warning] CR Simple Text Scheduler. No lines in schedule')
            return ()
        lines = schedule.split('\n')
        for line in lines:
            schedule_lines.extend([('SIMPLE', line)])
        params = keyframe_scheduler(schedule_lines, 'SIMPLE', current_frame)
        if params == '':
            print(f'[Warning] CR Simple Text Scheduler. No schedule found for frame. Simple schedules must start at frame 0.')
        else:
            try:
                text_out = str(params)
            except ValueError:
                print(f'[Warning] CR Simple Text Scheduler. Invalid params {params} at frame {current_frame}')
            show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Scheduler-Nodes#cr-simple-text-scheduler'
            return (text_out, show_help)
```