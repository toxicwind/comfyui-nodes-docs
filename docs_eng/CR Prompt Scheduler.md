# Documentation
- Class name: CR_PromptScheduler
- Category: Comfyroll/Animation/Schedulers
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_PromptScheduler is a node for managing and scheduling tips according to a key frame or predefined schedule. It allows users to set default hints, insert between value tips, and custom scheduling formats to meet various needs. The function of the node is centred on providing a seamless way to process dynamic tips for animation or other time-based applications.

# Input types
## Required
- mode
    - The mode determines the mode of movement to be used at the node. It determines whether to apply the default hint, follow the key frame list or achieve a more complex schedule.
    - Comfy dtype: COMBO['Default Prompt', 'Keyframe List', 'Schedule']
    - Python dtype: str
- current_frame
    - The current frame is the reference point for the scheduler to determine which hints to apply. It is essential for the implementation of the node, as it directly affects the selection of hints according to the timetable provided.
    - Comfy dtype: INT
    - Python dtype: int
- default_prompt
    - Default reminder is used as a backup text when no specific hint is scheduled in the current frame. It ensures that even in the absence of a defined timetable, there is always a useful hint.
    - Comfy dtype: STRING
    - Python dtype: str
- schedule_format
    - The schedule format specifies the structure for entering the schedule data. It is important because it informs node how to interpret and process the schedule information provided by the user.
    - Comfy dtype: COMBO['CR', 'Deforum']
    - Python dtype: str
- interpolate_prompt
    - Plug-in tips determine whether nodes should be inserted between hints in order to achieve a smoother transition. This enhances the flow of animations or applications using tips.
    - Comfy dtype: COMBO['Yes', 'No']
    - Python dtype: str
## Optional
- keyframe_list
    - The key frame list provides a multi-line input to define the key frame and its association. When the mode is set to the key frame list, it is essential to create a hint for a particular frame.
    - Comfy dtype: STRING
    - Python dtype: str
- prepend_text
    - The pretext allows users to add custom text before the hint. This is very useful for including additional context or information next to the main hint.
    - Comfy dtype: STRING
    - Python dtype: str
- append_text
    - Additional text allows a custom text to be added after the hint. It provides flexibility to expand the hint to include more detailed information, or to end the hint with a specific end.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- current_prompt
    - The current reminder is a reminder to assess the current active state based on the scheduler. It is an output that is used directly in an application or animation.
    - Comfy dtype: STRING
    - Python dtype: str
- next_prompt
    - The next reminder indicates that the next frame will be active. This is very useful for previewing or preparing changes in the reminder sequence.
    - Comfy dtype: STRING
    - Python dtype: str
- weight
    - The weight is a floating point value that represents the transition progress between the hints. When the plug-in hint is set to " Yes ", it is particularly relevant, indicating the extent of the plug-in.
    - Comfy dtype: FLOAT
    - Python dtype: float
- show_help
    - Displays the URL link to the document or help page that helps you provide the node. It is a quick reference for users seeking more information or help about the node.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_PromptScheduler:

    @classmethod
    def INPUT_TYPES(s):
        modes = ['Default Prompt', 'Keyframe List', 'Schedule']
        return {'required': {'mode': (modes,), 'current_frame': ('INT', {'default': 0.0, 'min': 0.0, 'max': 9999.0, 'step': 1.0}), 'default_prompt': ('STRING', {'multiline': False, 'default': 'default prompt'}), 'schedule_format': (['CR', 'Deforum'],), 'interpolate_prompt': (['Yes', 'No'],)}, 'optional': {'schedule': ('SCHEDULE',), 'schedule_alias': ('STRING', {'default prompt': '', 'multiline': False}), 'keyframe_list': ('STRING', {'multiline': True, 'default': 'keyframe list'}), 'prepend_text': ('STRING', {'multiline': True, 'default': 'prepend text'}), 'append_text': ('STRING', {'multiline': True, 'default': 'append text'})}}
    RETURN_TYPES = ('STRING', 'STRING', 'FLOAT', 'STRING')
    RETURN_NAMES = ('current_prompt', 'next_prompt', 'weight', 'show_help')
    FUNCTION = 'schedule'
    CATEGORY = icons.get('Comfyroll/Animation/Schedulers')

    def schedule(self, mode, prepend_text, append_text, current_frame, schedule_alias, default_prompt, schedule_format, interpolate_prompt, keyframe_list='', schedule=None):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Scheduler-Nodes#cr-prompt-scheduler'
        schedule_lines = list()
        if mode == 'Default Prompt':
            print(f'[Info] CR Prompt Scheduler: Scheduler {schedule_alias} is disabled')
            return (default_prompt, default_prompt, 1.0, show_help)
        if mode == 'Keyframe List':
            if keyframe_list == '':
                print(f'[Error] CR Prompt Scheduler: No keyframe list found.')
                return ()
            else:
                lines = keyframe_list.split('\n')
                for line in lines:
                    if schedule_format == 'Deforum':
                        line = line.replace(':', ',')
                        line = line.rstrip(',')
                        line = line.lstrip()
                    if not line.strip():
                        print(f'[Warning] CR Simple Prompt Scheduler. Skipped blank line at line {i}')
                        continue
                    schedule_lines.extend([(schedule_alias, line)])
                schedule = schedule_lines
        if mode == 'Schedule':
            if schedule is None:
                print(f'[Error] CR Prompt Scheduler: No schedule found.')
                return ()
            if schedule_format == 'Deforum':
                for item in schedule:
                    (alias, line) = item
                    line = line.replace(':', ',')
                    line = line.rstrip(',')
                    schedule_lines.extend([(schedule_alias, line)])
                schedule = schedule_lines
        (current_prompt, next_prompt, current_keyframe, next_keyframe) = prompt_scheduler(schedule, schedule_alias, current_frame)
        if current_prompt == '':
            print(f'[Warning] CR Simple Prompt Scheduler. No prompt found for frame. Schedules should start at frame 0.')
        else:
            try:
                current_prompt_out = prepend_text + ', ' + str(current_prompt) + ', ' + append_text
                next_prompt_out = prepend_text + ', ' + str(next_prompt) + ', ' + append_text
                from_index = int(current_keyframe)
                to_index = int(next_keyframe)
            except ValueError:
                print(f'[Warning] CR Simple Text Scheduler. Invalid keyframe at frame {current_frame}')
        if from_index == to_index or interpolate_prompt == 'No':
            weight_out = 1.0
        else:
            weight_out = (to_index - current_frame) / (to_index - from_index)
        return (current_prompt_out, next_prompt_out, weight_out, show_help)
```