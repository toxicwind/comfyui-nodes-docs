# Documentation
- Class name: StringSchedule
- Category: FizzNodes 📅🅕🅝/ScheduleNodes
- Output node: False
- Repo Ref: https://github.com/FizzleDorf/ComfyUI_FizzNodes

StringSchedule node is designed to process and animate the text-based agenda. It accepts parameters to customise the animation process, including text, frame limits and the current frame index. The main function of the node is to generate a series of tips that can be used for animation or scheduling purposes, abstracting the complexity of frame-based animations into a simple text-driven interface.

# Input types
## Required
- text
    - The `text' parameter is the original text input used by the node to generate animated tips. It is vital because it directly affects the content and structure of the output tips. The parameter supports multiline input, allowing complex and detailed descriptions.
    - Comfy dtype: STRING
    - Python dtype: str
- max_frames
    - The `max_frames' parameter defines the maximum frame number of animated sequences. It plays an important role in determining the duration and spacing of the animation, affecting overall rhythm and flow.
    - Comfy dtype: INT
    - Python dtype: int
- current_frame
    - The `current_frame' parameter indicates the current position in the animation sequence. It is essential to determine which hint to use at any given moment, so as to control the animated state.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- print_output
    - The `print_output' parameter is an optional symbol, and when set to True, the output of the animated reminder is printed on the control table. This is very useful for debuging or visualizing the animation sequence in text-based formats.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- pre_text
    - The 'pre_text' parameter is used to add text to each frame's hint. It can be used to add context or additional information that should appear at the beginning of each reminder in the animation sequence.
    - Comfy dtype: STRING
    - Python dtype: str
- app_text
    - The 'app_text'parameter is added to the hint for each frame to allow the end or additional text to be added to the animation sequence. It enhances the final output by additional details or closing words.
    - Comfy dtype: STRING
    - Python dtype: str
- pw_a
    - The `pw_a' parameter is the weighted factor used in the animation hint plug. It influences the balance and distribution of the reminder in the animation and allows micro-mobilization to progress.
    - Comfy dtype: FLOAT
    - Python dtype: float
- pw_b
    - The `pw_b' parameter is another weighted factor in the animated value, complementary to `pw_a', in order to achieve the desired effect or emphasis in the sequence.
    - Comfy dtype: FLOAT
    - Python dtype: float
- pw_c
    - The `pw_c' parameter is part of the weighted system used to insert value tips and provides additional controls for the details of animation development.
    - Comfy dtype: FLOAT
    - Python dtype: float
- pw_d
    - The `pw_d' parameter is the last weighting factor in the weight series and provides the effect on the last dimension of the indication of how values are inserted in the animation.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- POS
    - The 'POS' output represents a current positive hint derived from input text and parameters. It is a key part of the animation sequence and provides positive or primary content for the frame.
    - Comfy dtype: STRING
    - Python dtype: str
- NEG
    - The `NG' output, which represents the current negative hint, increases the overall depth and complexity of the animation by supplementing the `POS' output with comparative or substitute content for the frame.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class StringSchedule:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'text': ('STRING', {'multiline': True, 'default': defaultPrompt}), 'max_frames': ('INT', {'default': 120.0, 'min': 1.0, 'max': 999999.0, 'step': 1.0}), 'current_frame': ('INT', {'default': 0.0, 'min': 0.0, 'max': 999999.0, 'step': 1.0}), 'print_output': ('BOOLEAN', {'default': False})}, 'optional': {'pre_text': ('STRING', {'multiline': True}), 'app_text': ('STRING', {'multiline': True}), 'pw_a': ('FLOAT', {'default': 0.0, 'min': -9999.0, 'max': 9999.0, 'step': 0.1}), 'pw_b': ('FLOAT', {'default': 0.0, 'min': -9999.0, 'max': 9999.0, 'step': 0.1}), 'pw_c': ('FLOAT', {'default': 0.0, 'min': -9999.0, 'max': 9999.0, 'step': 0.1}), 'pw_d': ('FLOAT', {'default': 0.0, 'min': -9999.0, 'max': 9999.0, 'step': 0.1})}}
    RETURN_TYPES = ('STRING', 'STRING')
    RETURN_NAMES = ('POS', 'NEG')
    FUNCTION = 'animate'
    CATEGORY = 'FizzNodes 📅🅕🅝/ScheduleNodes'

    def animate(self, text, max_frames, current_frame, pw_a=0, pw_b=0, pw_c=0, pw_d=0, pre_text='', app_text='', print_output=False):
        current_frame = current_frame % max_frames
        inputText = str('{' + text + '}')
        inputText = re.sub(',\\s*}', '}', inputText)
        animation_prompts = json.loads(inputText.strip())
        start_frame = 0
        (pos, neg) = batch_split_weighted_subprompts(animation_prompts, pre_text, app_text)
        (pos_cur_prompt, pos_nxt_prompt, weight) = interpolate_prompt_series(pos, max_frames, 0, pre_text, app_text, pw_a, pw_b, pw_c, pw_d, print_output)
        (neg_cur_prompt, neg_nxt_prompt, weight) = interpolate_prompt_series(neg, max_frames, start_frame, pre_text, app_text, pw_a, pw_b, pw_c, pw_d, print_output)
        return (pos_cur_prompt[current_frame], neg_cur_prompt[current_frame])
```