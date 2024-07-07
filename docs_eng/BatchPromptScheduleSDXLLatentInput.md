# Documentation
- Class name: BatchPromptScheduleEncodeSDXLLatentInput
- Category: FizzNodes 📅🅕🅝/BatchScheduleNodes
- Output node: False
- Repo Ref: https://github.com/FizzleDorf/ComfyUI_FizzNodes

CatchPromptScheduleEncodeSDXLlatentInput is designed to process a batch of tips and encode them as potential expressions suitable for use in the generation model. It handles the complexity of hint plug-in and conditionality, abstractes the details of the process and provides a simplified interface to generate potential input.

# Input types
## Required
- width
    - Width parameters are essential for defining the size of an input image. They play a key role in the operation of nodes, determining the resolution of image processing.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - Altitude parameters, similar to width, are essential to specify the vertical dimensions of the input image and affect how the node handles and encodes the image data.
    - Comfy dtype: INT
    - Python dtype: int
- text_g
    - The text_g input is a string that contains model tips. It is a key component of the node function, as it directly affects the generation of potential expressions.
    - Comfy dtype: STRING
    - Python dtype: str
- num_latents
    - Num_lates parameters specify the number of potential vectors generated by nodes. It is important because it determines the output size of potential spatial expressions.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]

# Output types
- POS
    - The POS output provides positive condition data for the generation of models, which is important for channelling the generation process to the desired results.
    - Comfy dtype: CONDITIONING
    - Python dtype: torch.Tensor
- NEG
    - The NEG output contains negative condition data to guide the generation process away from the desired result.
    - Comfy dtype: CONDITIONING
    - Python dtype: torch.Tensor
- LATENT
    - LATENT output represents the potential vector generated by nodes as input for further processing or direct use in the generation model.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]

# Usage tips
- Infra type: CPU

# Source code
```
class BatchPromptScheduleEncodeSDXLLatentInput:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'width': ('INT', {'default': 1024.0, 'min': 0, 'max': MAX_RESOLUTION}), 'height': ('INT', {'default': 1024.0, 'min': 0, 'max': MAX_RESOLUTION}), 'crop_w': ('INT', {'default': 0, 'min': 0, 'max': MAX_RESOLUTION}), 'crop_h': ('INT', {'default': 0, 'min': 0, 'max': MAX_RESOLUTION}), 'target_width': ('INT', {'default': 1024.0, 'min': 0, 'max': MAX_RESOLUTION}), 'target_height': ('INT', {'default': 1024.0, 'min': 0, 'max': MAX_RESOLUTION}), 'text_g': ('STRING', {'multiline': True}), 'clip': ('CLIP',), 'text_l': ('STRING', {'multiline': True}), 'clip': ('CLIP',), 'num_latents': ('LATENT',), 'print_output': ('BOOLEAN', {'default': False})}, 'optional': {'pre_text_G': ('STRING', {'multiline': True}), 'app_text_G': ('STRING', {'multiline': True}), 'pre_text_L': ('STRING', {'multiline': True}), 'app_text_L': ('STRING', {'multiline': True}), 'pw_a': ('FLOAT', {'default': 0.0, 'min': -9999.0, 'max': 9999.0, 'step': 0.1}), 'pw_b': ('FLOAT', {'default': 0.0, 'min': -9999.0, 'max': 9999.0, 'step': 0.1}), 'pw_c': ('FLOAT', {'default': 0.0, 'min': -9999.0, 'max': 9999.0, 'step': 0.1}), 'pw_d': ('FLOAT', {'default': 0.0, 'min': -9999.0, 'max': 9999.0, 'step': 0.1})}}
    RETURN_TYPES = ('CONDITIONING', 'CONDITIONING', 'LATENT')
    RETURN_NAMES = ('POS', 'NEG')
    FUNCTION = 'animate'
    CATEGORY = 'FizzNodes 📅🅕🅝/BatchScheduleNodes'

    def animate(self, clip, width, height, crop_w, crop_h, target_width, target_height, text_g, text_l, app_text_G, app_text_L, pre_text_G, pre_text_L, num_latents, print_output, pw_a, pw_b, pw_c, pw_d):
        max_frames = sum((tensor.size(0) for tensor in num_latents.values()))
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
        return (p, n, num_latents)
```