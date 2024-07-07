# Documentation
- Class name: GLIGENTextBoxApply
- Category: conditioning/gligen
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The GLIGENTextBoxApply node is designed to add text-based conditions to the existing set of conditions. It processes the input text, integrates it with the given model, and allows text-based elements to be operated in graphic or data-driven context.

# Input types
## Required
- conditioning_to
    - Convention_to parameters are essential because it defines the objectives that will be subject to text-based conditions. It plays a key role in determining the context of the application of the text.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Any]
- clip
    - The clip parameter is necessary to encode the text into a format that the model can process. It is essential to convert text information into an appropriate expression for further analysis.
    - Comfy dtype: CLIP
    - Python dtype: Dict[str, Any]
- gligen_textbox_model
    - The gligen_textbox_model parameter is necessary for applying text conditions. It handles the logic specific to the model, how the logical management text is integrated into the set of conditions.
    - Comfy dtype: GLIGEN
    - Python dtype: torch.nn.Module
- text
    - The text parameter is the core input of the node and contains text information that will be processed and attached to the condition. It is the main data source for node operations.
    - Comfy dtype: STRING
    - Python dtype: str
- width
    - The width parameter specifies the width size of the text application, which is important for defining the context of the text in the space where conditions are concentrated.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - The height parameter defines the high size of the text application and plays an important role in establishing the vertical context of the text in the framework of the conditions.
    - Comfy dtype: INT
    - Python dtype: int
- x
    - The x parameter determines the horizontal position of the text in which the conditions are applied centrally, affecting the overall layout of the text-based conditions.
    - Comfy dtype: INT
    - Python dtype: int
- y
    - y Arguments set the vertical position of the text application, which is essential for the precise placement of the text within the framework of the conditions.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- conditioning
    - The output conditioning parameter represents the updated set of conditions now containing text-based elements. It is important because it reflects changes made in node operations.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Any]

# Usage tips
- Infra type: CPU

# Source code
```
class GLIGENTextBoxApply:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'conditioning_to': ('CONDITIONING',), 'clip': ('CLIP',), 'gligen_textbox_model': ('GLIGEN',), 'text': ('STRING', {'multiline': True, 'dynamicPrompts': True}), 'width': ('INT', {'default': 64, 'min': 8, 'max': MAX_RESOLUTION, 'step': 8}), 'height': ('INT', {'default': 64, 'min': 8, 'max': MAX_RESOLUTION, 'step': 8}), 'x': ('INT', {'default': 0, 'min': 0, 'max': MAX_RESOLUTION, 'step': 8}), 'y': ('INT', {'default': 0, 'min': 0, 'max': MAX_RESOLUTION, 'step': 8})}}
    RETURN_TYPES = ('CONDITIONING',)
    FUNCTION = 'append'
    CATEGORY = 'conditioning/gligen'

    def append(self, conditioning_to, clip, gligen_textbox_model, text, width, height, x, y):
        c = []
        (cond, cond_pooled) = clip.encode_from_tokens(clip.tokenize(text), return_pooled='unprojected')
        for t in conditioning_to:
            n = [t[0], t[1].copy()]
            position_params = [(cond_pooled, height // 8, width // 8, y // 8, x // 8)]
            prev = []
            if 'gligen' in n[1]:
                prev = n[1]['gligen'][2]
            n[1]['gligen'] = ('position', gligen_textbox_model, prev + position_params)
            c.append(n)
        return (c,)
```