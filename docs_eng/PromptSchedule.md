# Documentation
- Class name: PromptSchedule
- Category: FizzNodes 📅🅕🅝/ScheduleNodes
- Output node: False
- Repo Ref: https://github.com/FizzleDorf/ComfyUI_FizzNodes

PromptSchedule node is responsible for managing and animating text tips on specified frames. It creates smooth transitions by inserting a value key and applying weights to control the impact of each key frame. This node is essential for generating dynamic and consistent text animations over time.

# Input types
## Required
- text
    - The `text' parameter is a multi-line string that defines the initial state of the animated hint. It is essential for setting the basis on which the node will generate the animated sequence.
    - Comfy dtype: STRING
    - Python dtype: str
- max_frames
    - The'max_frames' parameter determines the total number of frames that the animation will run. It is a key factor in the length and rhythm of the overall animation.
    - Comfy dtype: INT
    - Python dtype: int
- current_frame
    - The `current_frame' parameter indicates the current position in the animation sequence. For nodes, it is essential to know where it is in the animated time line.
    - Comfy dtype: INT
    - Python dtype: int
- print_output
    - The 'print_output' parameter is a boolean symbol that, when set to True, prints the output of animated tips to the control table. This is very useful for debugging and real-time monitoring.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- clip
    - The `clip' parameter is a reference to the CLIP model used for text encoding in nodes. It plays a crucial role in converting texttips into an animated format.
    - Comfy dtype: CLIP
    - Python dtype: torch.nn.Module
## Optional
- pw_a
    - The `pw_a' parameter is a floating point number that indicates the weight to be applied to the current frame animation. It affects the transition between hints and contributes to the fluidity of the overall animation.
    - Comfy dtype: FLOAT
    - Python dtype: float
- pre_text
    - The `pre_text' parameter is an optional multi-line string that can be used for prefix animation tips. It provides additional context or settings for animated sequences.
    - Comfy dtype: STRING
    - Python dtype: str
- app_text
    - The `app_text' parameter is an optional multi-line string that can be used to add additional information to the animation hint. It expands the context or adds a suffix to the animation sequence.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- POS
    - The `POS' output represents the positive condition of the current frame animation. It is derived from the plug-in hint and is used to guide the positive creation of the animation.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Tuple[torch.Tensor, Dict[str, torch.Tensor]]]
- NEG
    - The `NG' output represents the negative conditions of the current frame animation. It is used to balance the positive conditions and ensure a balanced development of the animation sequence.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Tuple[torch.Tensor, Dict[str, torch.Tensor]]]

# Usage tips
- Infra type: CPU

# Source code
```
class PromptSchedule:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'text': ('STRING', {'multiline': True, 'default': defaultPrompt}), 'clip': ('CLIP',), 'max_frames': ('INT', {'default': 120.0, 'min': 1.0, 'max': 999999.0, 'step': 1.0}), 'current_frame': ('INT', {'default': 0.0, 'min': 0.0, 'max': 999999.0, 'step': 1.0}), 'print_output': ('BOOLEAN', {'default': False})}, 'optional': {'pre_text': ('STRING', {'multiline': True}), 'app_text': ('STRING', {'multiline': True}), 'pw_a': ('FLOAT', {'default': 0.0, 'min': -9999.0, 'max': 9999.0, 'step': 0.1}), 'pw_b': ('FLOAT', {'default': 0.0, 'min': -9999.0, 'max': 9999.0, 'step': 0.1}), 'pw_c': ('FLOAT', {'default': 0.0, 'min': -9999.0, 'max': 9999.0, 'step': 0.1}), 'pw_d': ('FLOAT', {'default': 0.0, 'min': -9999.0, 'max': 9999.0, 'step': 0.1})}}
    RETURN_TYPES = ('CONDITIONING', 'CONDITIONING')
    RETURN_NAMES = ('POS', 'NEG')
    FUNCTION = 'animate'
    CATEGORY = 'FizzNodes 📅🅕🅝/ScheduleNodes'

    def animate(self, text, max_frames, print_output, current_frame, clip, pw_a=0, pw_b=0, pw_c=0, pw_d=0, pre_text='', app_text=''):
        current_frame = current_frame % max_frames
        inputText = str('{' + text + '}')
        inputText = re.sub(',\\s*}', '}', inputText)
        animation_prompts = json.loads(inputText.strip())
        start_frame = 0
        (pos, neg) = batch_split_weighted_subprompts(animation_prompts, pre_text, app_text)
        (pos_cur_prompt, pos_nxt_prompt, weight) = interpolate_prompt_series(pos, max_frames, start_frame, pre_text, app_text, pw_a, pw_b, pw_c, pw_d, print_output)
        pc = PoolAnimConditioning(pos_cur_prompt[current_frame], pos_nxt_prompt[current_frame], weight[current_frame], clip)
        (neg_cur_prompt, neg_nxt_prompt, weight) = interpolate_prompt_series(neg, max_frames, start_frame, pre_text, app_text, pw_a, pw_b, pw_c, pw_d, print_output)
        nc = PoolAnimConditioning(neg_cur_prompt[current_frame], neg_nxt_prompt[current_frame], weight[current_frame], clip)
        return (pc, nc)
```