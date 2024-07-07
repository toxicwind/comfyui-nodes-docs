# Documentation
- Class name: BatchPromptScheduleLatentInput
- Category: FizzNodes 📅🅕🅝/BatchScheduleNodes
- Output node: False
- Repo Ref: https://github.com/FizzleDorf/ComfyUI_FizzNodes

The `animate'method at BatchPromptScheduleLatentInput node is designed to process and generate animation tips, which are used to create animation sequences in batch processing environments. It accepts parameters, such as text, potential quantities and weights, to control the interpolation value of cross-frame tips. The main function of the node is to create a series of hints that can be used for animation sequences and have the ability to adjust the impact of each reminder using the weights provided. This method is essential for animation processes, as it sets conditions for each animation.

# Input types
## Required
- text
    - The 'text' parameter is a string that contains the animated basic hint. It is an essential part of the animated process because it defines the initial conditions of the animated sequence. The expected text format is the format in which the node can be explained and used to generate the hint.
    - Comfy dtype: STRING
    - Python dtype: str
- num_latents
    - The 'num_latents' parameter specifies the potential variables to be used in the animation process. It is essential to determine the scope and diversity of the animated frame. This parameter affects how potential spaces can be explored and used to create animations.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]
## Optional
- print_output
    - The 'print_output' parameter is a boolean symbol, which, when set to True, prints the output of animated tips to the control table. This is very useful for debug purposes or for intuitive examination tips when creating tips.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- start_frame
    - The'start_frame' parameter determines the frame from which the animation sequence begins. This is an optional parameter that allows custom animated drawings to start.
    - Comfy dtype: INT
    - Python dtype: int
- pw_a
    - The `pw_a' parameter is a floating point number, which indicates the weight of the animated hint plug. It affects the transition between frames and contributes to the smoothness of the animation.
    - Comfy dtype: FLOAT
    - Python dtype: float
- pre_text
    - The 'pre_text' parameter is an optional string that can be used to add text before each animation tip. This is useful for adding a consistent element at the beginning of each hint.
    - Comfy dtype: STRING
    - Python dtype: str
- app_text
    - The 'app_text' parameter is an optional string that can be used to add text after each animation tip. It allows for the addition of consistent elements at the end of each hint.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- POS
    - The " POS" output provides positive condition information for each frame animation. It is derived from the plug value of the positive hint, which is essential to guide the animation to the desired result.
    - Comfy dtype: CONDITIONING
    - Python dtype: torch.Tensor
- NEG
    - The NEG output provides negative condition information for each frame animation. It is derived from the plug value of the negative hint and helps to fine-tune the animation by directing it away from the desired result.
    - Comfy dtype: CONDITIONING
    - Python dtype: torch.Tensor
- INPUT_LATENTS
    - The 'INPUT_LATENTS' output contains the potential variables used in the animation process. These potential variables are essential for the creation of animated frames and represent the bottom of the data used to create the final animation.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]

# Usage tips
- Infra type: CPU

# Source code
```
class BatchPromptScheduleLatentInput:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'text': ('STRING', {'multiline': True, 'default': defaultPrompt}), 'clip': ('CLIP',), 'num_latents': ('LATENT',), 'print_output': ('BOOLEAN', {'default': False})}, 'optional': {'pre_text': ('STRING', {'multiline': True}), 'app_text': ('STRING', {'multiline': True}), 'start_frame': ('INT', {'default': 0.0, 'min': 0, 'max': 9999, 'step': 1}), 'pw_a': ('FLOAT', {'default': 0.0, 'min': -9999.0, 'max': 9999.0, 'step': 0.1}), 'pw_b': ('FLOAT', {'default': 0.0, 'min': -9999.0, 'max': 9999.0, 'step': 0.1}), 'pw_c': ('FLOAT', {'default': 0.0, 'min': -9999.0, 'max': 9999.0, 'step': 0.1}), 'pw_d': ('FLOAT', {'default': 0.0, 'min': -9999.0, 'max': 9999.0, 'step': 0.1})}}
    RETURN_TYPES = ('CONDITIONING', 'CONDITIONING', 'LATENT')
    RETURN_NAMES = ('POS', 'NEG', 'INPUT_LATENTS')
    FUNCTION = 'animate'
    CATEGORY = 'FizzNodes 📅🅕🅝/BatchScheduleNodes'

    def animate(self, text, num_latents, print_output, clip, start_frame, pw_a, pw_b, pw_c, pw_d, pre_text='', app_text=''):
        max_frames = sum((tensor.size(0) for tensor in num_latents.values()))
        max_frames += start_frame
        inputText = str('{' + text + '}')
        inputText = re.sub(',\\s*}', '}', inputText)
        animation_prompts = json.loads(inputText.strip())
        (pos, neg) = batch_split_weighted_subprompts(animation_prompts, pre_text, app_text)
        (pos_cur_prompt, pos_nxt_prompt, weight) = interpolate_prompt_series(pos, max_frames, start_frame, pre_text, app_text, pw_a, pw_b, pw_c, pw_d, print_output)
        pc = BatchPoolAnimConditioning(pos_cur_prompt, pos_nxt_prompt, weight, clip)
        (neg_cur_prompt, neg_nxt_prompt, weight) = interpolate_prompt_series(neg, max_frames, start_frame, pre_text, app_text, pw_a, pw_b, pw_c, pw_d, print_output)
        nc = BatchPoolAnimConditioning(neg_cur_prompt, neg_nxt_prompt, weight, clip)
        return (pc, nc, num_latents)
```