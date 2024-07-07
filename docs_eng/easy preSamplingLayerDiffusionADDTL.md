# Documentation
- Class name: layerDiffusionSettingsADDTL
- Category: EasyUse/PreSampling
- Output node: True
- Repo Ref: https://github.com/yolain/ComfyUI-Easy-Use.git

Such nodes are responsible for setting additional texttips for layer diffusion models in order to optimize the input conditions of the generation process.

# Input types
## Required
- pipe
    - The `pipe' parameter is the basis for node operations and provides important context and data for the diffusion process.
    - Comfy dtype: PIPE_LINE
    - Python dtype: Dict
- foreground_prompt
    - This parameter, which allows users to enter foreground tips, is essential for guiding the model to generate content that meets the desired focus.
    - Comfy dtype: STRING
    - Python dtype: str
- background_prompt
    - By providing background tips, users can set the context or scenario for the model to ensure that the content generated is consistent with the expected context.
    - Comfy dtype: STRING
    - Python dtype: str
- blended_prompt
    - Mixed hint parameters allow multiple hints to be combined to create more detailed and detailed outputs, thereby enhancing the wealth of content generated.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- optional_fg_cond
    - This optional parameter provides additional reconciliation input for the future and flexibility to customize model generation to specific user requirements.
    - Comfy dtype: CONDITIONING
    - Python dtype: Any
- optional_bg_cond
    - Similarly, this optional parameter expands the ability of the context to regulate and allows for more complex and contextual generation.
    - Comfy dtype: CONDITIONING
    - Python dtype: Any
- optional_blended_cond
    - This parameter provides a method of mixing multiple reconciliation inputes and allows for a more harmonious and integrated generation of results.
    - Comfy dtype: CONDITIONING
    - Python dtype: Any

# Output types
- pipe
    - The updated `pipe' output contains new stratum spreading conditions, which are essential for the next steps in the stream.
    - Comfy dtype: PIPE_LINE
    - Python dtype: Dict

# Usage tips
- Infra type: CPU

# Source code
```
class layerDiffusionSettingsADDTL:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'pipe': ('PIPE_LINE',), 'foreground_prompt': ('STRING', {'default': '', 'placeholder': 'Foreground Additional Prompt', 'multiline': True}), 'background_prompt': ('STRING', {'default': '', 'placeholder': 'Background Additional Prompt', 'multiline': True}), 'blended_prompt': ('STRING', {'default': '', 'placeholder': 'Blended Additional Prompt', 'multiline': True})}, 'optional': {'optional_fg_cond': ('CONDITIONING',), 'optional_bg_cond': ('CONDITIONING',), 'optional_blended_cond': ('CONDITIONING',)}, 'hidden': {'prompt': 'PROMPT', 'extra_pnginfo': 'EXTRA_PNGINFO', 'my_unique_id': 'UNIQUE_ID'}}
    RETURN_TYPES = ('PIPE_LINE',)
    RETURN_NAMES = ('pipe',)
    OUTPUT_NODE = True
    FUNCTION = 'settings'
    CATEGORY = 'EasyUse/PreSampling'

    def settings(self, pipe, foreground_prompt, background_prompt, blended_prompt, optional_fg_cond=None, optional_bg_cond=None, optional_blended_cond=None, prompt=None, extra_pnginfo=None, my_unique_id=None):
        (fg_cond, bg_cond, blended_cond) = (None, None, None)
        clip = pipe['clip']
        if optional_fg_cond is not None:
            fg_cond = optional_fg_cond
        elif foreground_prompt != '':
            (fg_cond,) = CLIPTextEncode().encode(clip, foreground_prompt)
        if optional_bg_cond is not None:
            bg_cond = optional_bg_cond
        elif background_prompt != '':
            (bg_cond,) = CLIPTextEncode().encode(clip, background_prompt)
        if optional_blended_cond is not None:
            blended_cond = optional_blended_cond
        elif blended_prompt != '':
            (blended_cond,) = CLIPTextEncode().encode(clip, blended_prompt)
        new_pipe = {**pipe, 'loader_settings': {**pipe['loader_settings'], 'layer_diffusion_cond': (fg_cond, bg_cond, blended_cond)}}
        del pipe
        return (new_pipe,)
```