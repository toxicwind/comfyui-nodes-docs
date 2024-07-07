# Documentation
- Class name: CR_SimplePromptScheduler
- Category: Comfyroll/Animation/Schedulers
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_SimplePromptScheduler is a node for managing and scheduling tips based on the key frame list. It allows automatic changes to the hint in a given frame, thus facilitating the creation of dynamic and specific frame content without the need for manual intervention. This node is essential to simplify the painting process, especially when processing complex sequences that require precise hint adjustments.

# Input types
## Required
- keyframe_list
    - The key frame list is a key parameter that defines the sequence of hints and their corresponding frames. It enables nodes to efficiently schedule tips to ensure that the correct hints are displayed at the right time in the animation.
    - Comfy dtype: STRING
    - Python dtype: str
- current_frame
    - The current frame parameter is essential because it indicates the current point on the animated timeline. The node uses this information to determine which hint in the key frame list should be active for the ongoing frame.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- keyframe_format
    - Keyframe format parameters specify the structure of the key frame data, allowing nodes to correctly interpret and interpret the key frame list. It is important to maintain the integrity and accuracy of the schedule tips.
    - Comfy dtype: COMBO['CR', 'Deforum']
    - Python dtype: str

# Output types
- current_prompt
    - The current reminder output provides an active reminder of the current frame. It is important because it directly affects what is displayed or processed in the animation.
    - Comfy dtype: STRING
    - Python dtype: str
- next_prompt
    - The next hint output instruction will be activated in the next frame. This allows the expected content to be expected and can be used for smooth transitions between hints.
    - Comfy dtype: STRING
    - Python dtype: str
- weight
    - The weight output indicates the transitional weight between the current and next tip. It is used to insert the value hints to achieve gradual change and enhance the flow of animations.
    - Comfy dtype: FLOAT
    - Python dtype: float
- show_help
    - Displays that the help output provides a link to the document for further help. This is useful for users who need more information about node functionality or troubleshooting support.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_SimplePromptScheduler:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'keyframe_list': ('STRING', {'multiline': True, 'default': 'frame_number, text'}), 'current_frame': ('INT', {'default': 0.0, 'min': 0.0, 'max': 9999.0, 'step': 1.0}), 'keyframe_format': (['CR', 'Deforum'],)}}
    RETURN_TYPES = ('STRING', 'STRING', 'FLOAT', 'STRING')
    RETURN_NAMES = ('current_prompt', 'next_prompt', 'weight', 'show_help')
    FUNCTION = 'simple_schedule'
    CATEGORY = icons.get('Comfyroll/Animation/Schedulers')

    def simple_schedule(self, keyframe_list, keyframe_format, current_frame):
        keyframes = list()
        if keyframe_list == '':
            print(f'[Error] CR Simple Prompt Scheduler. No lines in keyframe list')
            return ()
        lines = keyframe_list.split('\n')
        for line in lines:
            if keyframe_format == 'Deforum':
                line = line.replace(':', ',')
                line = line.rstrip(',')
            if not line.strip():
                print(f'[Warning] CR Simple Prompt Scheduler. Skipped blank line at line {i}')
                continue
            keyframes.extend([('SIMPLE', line)])
        (current_prompt, next_prompt, current_keyframe, next_keyframe) = prompt_scheduler(keyframes, 'SIMPLE', current_frame)
        if current_prompt == '':
            print(f'[Warning] CR Simple Prompt Scheduler. No prompt found for frame. Simple schedules must start at frame 0.')
        else:
            try:
                current_prompt_out = str(current_prompt)
                next_prompt_out = str(next_prompt)
                from_index = int(current_keyframe)
                to_index = int(next_keyframe)
            except ValueError:
                print(f'[Warning] CR Simple Text Scheduler. Invalid keyframe at frame {current_frame}')
            if from_index == to_index:
                weight_out = 1.0
            else:
                weight_out = (to_index - current_frame) / (to_index - from_index)
            show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Scheduler-Nodes#cr-simple-prompt-scheduler'
            return (current_prompt_out, next_prompt_out, weight_out, show_help)
```