# Documentation
- Class name: BatchPromptScheduleEncodeSDXL
- Category: FizzNodes 📅🅕🅝/BatchScheduleNodes
- Output node: False
- Repo Ref: https://github.com/FizzleDorf/ComfyUI_FizzNodes

The CatchPromptScheduleEncodeSDXL node is designed to process and generate an animated series of tips for images or videos. It receives parameters, such as text tips, sizes and plug-in weights, to create dynamic sequences of hints, and then encodes them for use in the generation model. The node plays a key role in the animated water flow line by generating the necessary conditional data for a consistent and smooth transition between frames and frames.

# Input types
## Required
- width
    - The width parameter is essential to define the size of the media that produces it. It works with the height parameter to ensure that the output adheres to the vertical ratio and resolution required.
    - Comfy dtype: INT
    - Python dtype: int
- text_g
    - Text_g Enter a string containing graphic tips for animating. It is a key component in shaping the visual output of animated sequences.
    - Comfy dtype: STRING
    - Python dtype: str
- max_frames
    - The max_frames parameter sets the maximum number of frames to be generated for animation. It is a key factor in determining the length and complexity of the final output.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- pw_a
    - The pw_a parameter is the optional weight factor used in the plugin process. It allows the effect of certain hints in the micromobilization series.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- POS
    - The POS output provides positive data derived from the reminder to guide the generation process towards more favourable outcomes.
    - Comfy dtype: CONDITIONING
    - Python dtype: torch.Tensor
- NEG
    - The NEG output contains data on negative conditions that, by providing counter-practices or constraints, help guide the generation process to avoid undesirable outcomes.
    - Comfy dtype: CONDITIONING
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class BatchPromptScheduleEncodeSDXL:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'width': ('INT', {'default': 1024.0, 'min': 0, 'max': MAX_RESOLUTION}), 'height': ('INT', {'default': 1024.0, 'min': 0, 'max': MAX_RESOLUTION}), 'crop_w': ('INT', {'default': 0, 'min': 0, 'max': MAX_RESOLUTION}), 'crop_h': ('INT', {'default': 0, 'min': 0, 'max': MAX_RESOLUTION}), 'target_width': ('INT', {'default': 1024.0, 'min': 0, 'max': MAX_RESOLUTION}), 'target_height': ('INT', {'default': 1024.0, 'min': 0, 'max': MAX_RESOLUTION}), 'text_g': ('STRING', {'multiline': True}), 'clip': ('CLIP',), 'text_l': ('STRING', {'multiline': True}), 'clip': ('CLIP',), 'max_frames': ('INT', {'default': 120.0, 'min': 1.0, 'max': 999999.0, 'step': 1.0}), 'print_output': ('BOOLEAN', {'default': False})}, 'optional': {'pre_text_G': ('STRING', {'multiline': True}), 'app_text_G': ('STRING', {'multiline': True}), 'pre_text_L': ('STRING', {'multiline': True}), 'app_text_L': ('STRING', {'multiline': True}), 'pw_a': ('FLOAT', {'default': 0.0, 'min': -9999.0, 'max': 9999.0, 'step': 0.1}), 'pw_b': ('FLOAT', {'default': 0.0, 'min': -9999.0, 'max': 9999.0, 'step': 0.1}), 'pw_c': ('FLOAT', {'default': 0.0, 'min': -9999.0, 'max': 9999.0, 'step': 0.1}), 'pw_d': ('FLOAT', {'default': 0.0, 'min': -9999.0, 'max': 9999.0, 'step': 0.1})}}
    RETURN_TYPES = ('CONDITIONING', 'CONDITIONING')
    RETURN_NAMES = ('POS', 'NEG')
    FUNCTION = 'animate'
    CATEGORY = 'FizzNodes 📅🅕🅝/BatchScheduleNodes'

    def animate(self, clip, width, height, crop_w, crop_h, target_width, target_height, text_g, text_l, app_text_G, app_text_L, pre_text_G, pre_text_L, max_frames, print_output, pw_a, pw_b, pw_c, pw_d):
        inputTextG = str('{' + text_g + '}')
        inputTextL = str('{' + text_l + '}')
        inputTextG = re.sub(',\\s*}', '}', inputTextG)
        inputTextL = re.sub(',\\s*}', '}', inputTextL)
        animation_promptsG = json.loads(inputTextG.strip())
        animation_promptsL = json.loads(inputTextL.strip())
        (posG, negG) = batch_split_weighted_subprompts(animation_promptsG, pre_text_G, app_text_G)
        (posL, negL) = batch_split_weighted_subprompts(animation_promptsL, pre_text_L, app_text_L)
        (pc, pn, pw) = BatchInterpolatePromptsSDXL(posG, posL, max_frames, clip, app_text_G, app_text_L, pre_text_G, pre_text_L, pw_a, pw_b, pw_c, pw_d, width, height, crop_w, crop_h, target_width, target_height, print_output)
        p = BatchPoolAnimConditioningSDXL(pc, pn, pw)
        (nc, nn, nw) = BatchInterpolatePromptsSDXL(negG, negL, max_frames, clip, app_text_G, app_text_L, pre_text_G, pre_text_L, pw_a, pw_b, pw_c, pw_d, width, height, crop_w, crop_h, target_width, target_height, print_output)
        n = BatchPoolAnimConditioningSDXL(nc, nn, nw)
        return (p, n)
```