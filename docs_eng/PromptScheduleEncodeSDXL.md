# Documentation
- Class name: PromptScheduleEncodeSDXL
- Category: FizzNodes 📅🅕🅝/ScheduleNodes
- Output node: False
- Repo Ref: https://github.com/FizzleDorf/ComfyUI_FizzNodes

PromptScheduleEncodeSDXL node is designed to create and encode a series of frames in the video. It takes into account parameters such as width, height, tailor size and texttips to generate a series of hints, and then encodes them to create conditions for further processing. This node plays a key role in the animation pipeline, managing the complexity of the tips and ensuring a smooth transition between frames.

# Input types
## Required
- width
    - Width parameters specify the width of the frame. It is essential to determine the resolution and width ratio of the output video, affecting the overall visual quality and the way the animation is presented.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - Altitude parameters set the vertical resolution of the video frame. It works in conjunction with the width parameters to ensure the correct scaling and display of video content.
    - Comfy dtype: INT
    - Python dtype: int
- text_g
    - Text_g parameters save text tips for the green channel. These tips are essential to guide the animation process and define the story or visual elements that will appear in the final animation.
    - Comfy dtype: STRING
    - Python dtype: str
- max_frames
    - Mac_frames parameters define the maximum number of frames to be included. This setting is important for controlling the length of animations and managing computing resources.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- print_output
    - The torrent_output parameter is an optional symbol that, when set to True, you will print debugging information during the node execution. This helps developers monitor progress and remove problems that may arise.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- POS
    - POS output provides positive data derived from input tips and parameters. This output is important because it provides the basis for subsequent video processing steps and influences the end result of the animation.
    - Comfy dtype: CONDITIONING
    - Python dtype: Tuple[str, Dict[str, torch.Tensor]]
- NEG
    - The NEG output provides negative condition data to supplement the POS output by providing additional context or comparison. This output is used to refine the animation and increase the depth of visual narratives.
    - Comfy dtype: CONDITIONING
    - Python dtype: Tuple[str, Dict[str, torch.Tensor]]

# Usage tips
- Infra type: CPU

# Source code
```
class PromptScheduleEncodeSDXL:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'width': ('INT', {'default': 1024.0, 'min': 0, 'max': MAX_RESOLUTION}), 'height': ('INT', {'default': 1024.0, 'min': 0, 'max': MAX_RESOLUTION}), 'crop_w': ('INT', {'default': 0, 'min': 0, 'max': MAX_RESOLUTION}), 'crop_h': ('INT', {'default': 0, 'min': 0, 'max': MAX_RESOLUTION}), 'target_width': ('INT', {'default': 1024.0, 'min': 0, 'max': MAX_RESOLUTION}), 'target_height': ('INT', {'default': 1024.0, 'min': 0, 'max': MAX_RESOLUTION}), 'text_g': ('STRING', {'multiline': True}), 'clip': ('CLIP',), 'text_l': ('STRING', {'multiline': True}), 'clip': ('CLIP',), 'max_frames': ('INT', {'default': 120.0, 'min': 1.0, 'max': 999999.0, 'step': 1.0}), 'current_frame': ('INT', {'default': 0.0, 'min': 0.0, 'max': 999999.0, 'step': 1.0}), 'print_output': ('BOOLEAN', {'default': False})}, 'optional': {'pre_text_G': ('STRING', {'multiline': True}), 'app_text_G': ('STRING', {'multiline': True}), 'pre_text_L': ('STRING', {'multiline': True}), 'app_text_L': ('STRING', {'multiline': True}), 'pw_a': ('FLOAT', {'default': 0.0, 'min': -9999.0, 'max': 9999.0, 'step': 0.1}), 'pw_b': ('FLOAT', {'default': 0.0, 'min': -9999.0, 'max': 9999.0, 'step': 0.1}), 'pw_c': ('FLOAT', {'default': 0.0, 'min': -9999.0, 'max': 9999.0, 'step': 0.1}), 'pw_d': ('FLOAT', {'default': 0.0, 'min': -9999.0, 'max': 9999.0, 'step': 0.1})}}
    RETURN_TYPES = ('CONDITIONING', 'CONDITIONING')
    RETURN_NAMES = ('POS', 'NEG')
    FUNCTION = 'animate'
    CATEGORY = 'FizzNodes 📅🅕🅝/ScheduleNodes'

    def animate(self, clip, width, height, crop_w, crop_h, target_width, target_height, text_g, text_l, app_text_G, app_text_L, pre_text_G, pre_text_L, max_frames, current_frame, print_output, pw_a, pw_b, pw_c, pw_d):
        current_frame = current_frame % max_frames
        inputTextG = str('{' + text_g + '}')
        inputTextL = str('{' + text_l + '}')
        inputTextG = re.sub(',\\s*}', '}', inputTextG)
        inputTextL = re.sub(',\\s*}', '}', inputTextL)
        animation_promptsG = json.loads(inputTextG.strip())
        animation_promptsL = json.loads(inputTextL.strip())
        (posG, negG) = batch_split_weighted_subprompts(animation_promptsG, pre_text_G, app_text_G)
        (posL, negL) = batch_split_weighted_subprompts(animation_promptsL, pre_text_L, app_text_L)
        (pc, pn, pw) = BatchInterpolatePromptsSDXL(posG, posL, max_frames, clip, app_text_G, app_text_L, pre_text_G, pre_text_L, pw_a, pw_b, pw_c, pw_d, width, height, crop_w, crop_h, target_width, target_height, print_output)
        p = addWeighted(pc[current_frame], pn[current_frame], pw[current_frame])
        (nc, nn, nw) = BatchInterpolatePromptsSDXL(negG, negL, max_frames, clip, app_text_G, app_text_L, pre_text_G, pre_text_L, pw_a, pw_b, pw_c, pw_d, width, height, crop_w, crop_h, target_width, target_height, print_output)
        n = addWeighted(nc[current_frame], nn[current_frame], nw[current_frame])
        return (p, n)
```