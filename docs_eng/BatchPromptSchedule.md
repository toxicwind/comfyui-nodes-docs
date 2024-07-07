# Documentation
- Class name: BatchPromptSchedule
- Category: FizzNodes 📅🅕🅝/BatchScheduleNodes
- Output node: False
- Repo Ref: https://github.com/FizzleDorf/ComfyUI_FizzNodes

The CatchPromptSchedule node is designed to manage and animate tips in a batch processing environment. It accepts parameters to customize animation processes, including text, editing references, and frame specifications. The main function of the node is to coordinate animation sequences to ensure smooth transition between frames by applying weights and conditions. It is particularly suitable for creating complex animations that require precise control of each frame content.

# Input types
## Required
- text
    - The 'text' parameter is a string that contains animated hints. It is essential to define the content and sequence of animated drawings. This input drives the overall description and structure of animated output.
    - Comfy dtype: STRING
    - Python dtype: str
- clip
    - The 'clip' parameter is a reference to multimedia clips used in animation. It plays an important role in the visual expression of animation and is essential for integrating audio-visual elements into animation.
    - Comfy dtype: CLIP
    - Python dtype: Any
- max_frames
    - The'max_frames' parameter specifies the maximum number of frames for the animation sequence. It is a key determinant of the duration and rhythm of the animation, affecting the overall time and process of the animation.
    - Comfy dtype: INT
    - Python dtype: int
- print_output
    - The 'print_output' parameter is a boolean symbol that, when set to True, prints the intermediate results of the animation process. This helps to debug and understand the operation of the nodes.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
## Optional
- pre_text
    - The 'pre_text' parameter is an optional string that provides additional context or setting for animation tips. It can be used to introduce or frame animated content.
    - Comfy dtype: STRING
    - Python dtype: str
- app_text
    - The 'app_text' parameter is an optional string that adds a closing phrase or a closing statement to the animated hint. It helps to complete or summarize the animated information.
    - Comfy dtype: STRING
    - Python dtype: str
- start_frame
    - The'start_frame' parameter is an optional integer that sets the starting point of the animation. It allows the starting point of the animation sequence to be defined.
    - Comfy dtype: INT
    - Python dtype: int
- pw_a
    - The 'pw_a'parameter is an optional float number that indicates the weight to be applied to animation tips. It is used to adjust the effects of some of the hints in the animation.
    - Comfy dtype: FLOAT
    - Python dtype: float
- pw_b
    - The 'pw_b' parameter is another optional floating point number that is used as a secondary weight for animation tips. It further refines the control of animation content according to the assigned weight.
    - Comfy dtype: FLOAT
    - Python dtype: float
- pw_c
    - The 'pw_c' parameter is an optional floating point number, which is the third weight of the animated hint. It helps to fine-tune the animated progress.
    - Comfy dtype: FLOAT
    - Python dtype: float
- pw_d
    - The 'pw_d' parameter is an optional float number, representing the four-dollar weight of the animation hint. It provides an additional layer of control for the details of the animation.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- POS
    - The 'POS' output provides positive data derived from animation alerts. It is important to channel animated direction and tone to more favourable outcomes.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Tuple[torch.Tensor, Dict[str, torch.Tensor]]]
- NEG
    - The NEG output provides data on negative conditions extracted from animation tips. It is essential to create comparisons and balances in animations by highlighting less popular elements.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Tuple[torch.Tensor, Dict[str, torch.Tensor]]]

# Usage tips
- Infra type: CPU

# Source code
```
class BatchPromptSchedule:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'text': ('STRING', {'multiline': True, 'default': defaultPrompt}), 'clip': ('CLIP',), 'max_frames': ('INT', {'default': 120.0, 'min': 1.0, 'max': 999999.0, 'step': 1.0}), 'print_output': ('BOOLEAN', {'default': False})}, 'optional': {'pre_text': ('STRING', {'multiline': True}), 'app_text': ('STRING', {'multiline': True}), 'start_frame': ('INT', {'default': 0, 'min': 0, 'max': 9999, 'step': 1}), 'pw_a': ('FLOAT', {'default': 0.0, 'min': -9999.0, 'max': 9999.0, 'step': 0.1}), 'pw_b': ('FLOAT', {'default': 0.0, 'min': -9999.0, 'max': 9999.0, 'step': 0.1}), 'pw_c': ('FLOAT', {'default': 0.0, 'min': -9999.0, 'max': 9999.0, 'step': 0.1}), 'pw_d': ('FLOAT', {'default': 0.0, 'min': -9999.0, 'max': 9999.0, 'step': 0.1})}}
    RETURN_TYPES = ('CONDITIONING', 'CONDITIONING')
    RETURN_NAMES = ('POS', 'NEG')
    FUNCTION = 'animate'
    CATEGORY = 'FizzNodes 📅🅕🅝/BatchScheduleNodes'

    def animate(self, text, max_frames, print_output, clip, start_frame, pw_a, pw_b, pw_c, pw_d, pre_text='', app_text=''):
        inputText = str('{' + text + '}')
        inputText = re.sub(',\\s*}', '}', inputText)
        max_frames += start_frame
        animation_prompts = json.loads(inputText.strip())
        (pos, neg) = batch_split_weighted_subprompts(animation_prompts, pre_text, app_text)
        (pos_cur_prompt, pos_nxt_prompt, weight) = interpolate_prompt_series(pos, max_frames, start_frame, pre_text, app_text, pw_a, pw_b, pw_c, pw_d, print_output)
        pc = BatchPoolAnimConditioning(pos_cur_prompt, pos_nxt_prompt, weight, clip)
        (neg_cur_prompt, neg_nxt_prompt, weight) = interpolate_prompt_series(neg, max_frames, start_frame, pre_text, app_text, pw_a, pw_b, pw_c, pw_d, print_output)
        nc = BatchPoolAnimConditioning(neg_cur_prompt, neg_nxt_prompt, weight, clip)
        return (pc, nc)
```