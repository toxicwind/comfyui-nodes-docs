# Documentation
- Class name: AddCLIPSDXLRParams
- Category: conditioning/advanced
- Output node: False
- Repo Ref: https://github.com/BlenderNeko/ComfyUI_ADV_CLIP_emb

The AddcLIPSDXLRparams node is designed to enhance the input condition data for advanced encoded tasks. It receives the condition data and applies the specified dimensions and aesthetic scores to each element in preparation for follow-up processing.

# Input types
## Required
- conditioning
    - The conditioning parameter is essential to provide the initial data to be converted by the node. It is the core input that determines the follow-up and output of the node.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Any]
- width
    - The width parameter specifies the width to be applied to each element in the condition data. It plays a key role in determining the resolution of the coded data.
    - Comfy dtype: INT
    - Python dtype: float
- height
    - The header parameter sets the height size of the elements in the condition data. It is important for controlling the vertical resolution of the code output.
    - Comfy dtype: INT
    - Python dtype: float
- ascore
    - The aesthetic_score parameter assigns a aesthetic value to each element, which can affect the coding process according to the required aesthetic standards.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- conditioning
    - Output is a conversion version of the input, which is now equipped with specified dimensions and aesthetic scores to prepare for advanced encoding.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Any]

# Usage tips
- Infra type: CPU

# Source code
```
class AddCLIPSDXLRParams:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'conditioning': ('CONDITIONING',), 'width': ('INT', {'default': 1024.0, 'min': 0, 'max': MAX_RESOLUTION}), 'height': ('INT', {'default': 1024.0, 'min': 0, 'max': MAX_RESOLUTION}), 'ascore': ('FLOAT', {'default': 6.0, 'min': 0.0, 'max': 1000.0, 'step': 0.01})}}
    RETURN_TYPES = ('CONDITIONING',)
    FUNCTION = 'encode'
    CATEGORY = 'conditioning/advanced'

    def encode(self, conditioning, width, height, ascore):
        c = []
        for t in conditioning:
            n = [t[0], t[1].copy()]
            n[1]['width'] = width
            n[1]['height'] = height
            n[1]['aesthetic_score'] = ascore
            c.append(n)
        return (c,)
```