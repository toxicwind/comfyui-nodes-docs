# Documentation
- Class name: PromptScheduleNodeFlowEnd
- Category: FizzNodes 📅🅕🅝/ScheduleNodes
- Output node: False
- Repo Ref: https://github.com/FizzleDorf/ComfyUI_FizzNodes

The `animate'method in the `PromptScheduleNodeFlowEnd'class is responsible for generating animate tips based on the given text and a series of parameters. It processes the input text to create a series of hints that can be used to drive the animation sequence, taking into account weights and conditions to ensure smooth transition between frames.

# Input types
## Required
- text
    - The `text'parameter is the key input to the node because it provides the original text that will be used to generate animation tips. It is important because it directly affects the content and flow of animations.
    - Comfy dtype: STRING
    - Python dtype: str
- max_frames
    - The'max_frames'parameter defines the maximum number of frames for animated sequences. It is vital because it determines the total length of animated drawings and affects the distribution of tips in frames.
    - Comfy dtype: INT
    - Python dtype: int
- print_output
    - The 'print_output'parameter is used to control the intermediate results of animated processes that should be printed. This is useful for debugging purposes or for providing feedback when creating animated drawings.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- current_frame
    - The 'current_frame'parameter indicates the current position in the animation sequence. It is important because it helps the node to determine which hint is used at any given moment in the animation.
    - Comfy dtype: INT
    - Python dtype: int
- clip
    - The `clip'parameter is an important input to the node because it represents the CLIP model that will be used to mark the hint and encode it into an animated format.
    - Comfy dtype: CLIP
    - Python dtype: torch.nn.Module
## Optional
- pre_text
    - The `pre_text' parameter is used to add context to the main animation hint. It affects the initial state of the animation, which is particularly useful when it is needed.
    - Comfy dtype: STRING
    - Python dtype: str
- app_text
    - The 'app_text'parameter is used to add context after the main animation hint. It can be used to extend the animation with additional information or to provide a conclusion for the sequence.
    - Comfy dtype: STRING
    - Python dtype: str
- pw_a
    - The 'pw_a'parameter is an optional weight used to adjust the impact of some of the hints in the animation. It provides a method for micromobilizing drawings in response to specific creative requirements.
    - Comfy dtype: FLOAT
    - Python dtype: float
- pw_b
    - `pw_b' parameters are similar to `pw_a'but allow for independent control of different aspects of animated weights.
    - Comfy dtype: FLOAT
    - Python dtype: float
- pw_c
    - The `pw_c' parameter expands the custom option for animation weights and provides an additional layer of control for the animation process.
    - Comfy dtype: FLOAT
    - Python dtype: float
- pw_d
    - The `pw_d' parameter is another optional weight that can help fine-tune animations and allow precise adjustments to animated progress.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- POS
    - The `POS'output provides animated positive reconciliation data, which represents the desired direction or result that animation should take in each frame.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Tuple[torch.Tensor, Dict[str, torch.Tensor]]]
- NEG
    - The `NEG'output provides negative flow reconciliation data, which are used to define the content of animation that should be avoided or remote from each frame.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Tuple[torch.Tensor, Dict[str, torch.Tensor]]]

# Usage tips
- Infra type: CPU

# Source code
```
class PromptScheduleNodeFlowEnd:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'text': ('STRING', {'multiline': False, 'forceInput': True}), 'clip': ('CLIP',), 'max_frames': ('INT', {'default': 0.0, 'min': 0.0, 'max': 999999.0, 'step': 1.0}), 'print_output': ('BOOLEAN', {'default': False}), 'current_frame': ('INT', {'default': 0.0, 'min': 0.0, 'max': 999999.0, 'step': 1.0})}, 'optional': {'pre_text': ('STRING', {'multiline': True}), 'app_text': ('STRING', {'multiline': True}), 'pw_a': ('FLOAT', {'default': 0.0, 'min': -9999.0, 'max': 9999.0, 'step': 0.1}), 'pw_b': ('FLOAT', {'default': 0.0, 'min': -9999.0, 'max': 9999.0, 'step': 0.1}), 'pw_c': ('FLOAT', {'default': 0.0, 'min': -9999.0, 'max': 9999.0, 'step': 0.1}), 'pw_d': ('FLOAT', {'default': 0.0, 'min': -9999.0, 'max': 9999.0, 'step': 0.1})}}
    RETURN_TYPES = ('CONDITIONING', 'CONDITIONING')
    RETURN_NAMES = ('POS', 'NEG')
    FUNCTION = 'animate'
    CATEGORY = 'FizzNodes 📅🅕🅝/ScheduleNodes'

    def animate(self, text, max_frames, print_output, current_frame, clip, pw_a=0, pw_b=0, pw_c=0, pw_d=0, pre_text='', app_text=''):
        current_frame = current_frame % max_frames
        if text[-1] == ',':
            text = text[:-1]
        if text[0] == ',':
            text = text[:0]
        start_frame = 0
        inputText = str('{' + text + '}')
        inputText = re.sub(',\\s*}', '}', inputText)
        animation_prompts = json.loads(inputText.strip())
        max_frames += start_frame
        (pos, neg) = batch_split_weighted_subprompts(animation_prompts, pre_text, app_text)
        (pos_cur_prompt, pos_nxt_prompt, weight) = interpolate_prompt_series(pos, max_frames, start_frame, pre_text, app_text, pw_a, pw_b, pw_c, pw_d, print_output)
        pc = PoolAnimConditioning(pos_cur_prompt[current_frame], pos_nxt_prompt[current_frame], weight[current_frame], clip)
        (neg_cur_prompt, neg_nxt_prompt, weight) = interpolate_prompt_series(neg, max_frames, start_frame, pre_text, app_text, pw_a, pw_b, pw_c, pw_d, print_output)
        nc = PoolAnimConditioning(neg_cur_prompt[current_frame], neg_nxt_prompt[current_frame], weight[current_frame], clip)
        return (pc, nc)
```