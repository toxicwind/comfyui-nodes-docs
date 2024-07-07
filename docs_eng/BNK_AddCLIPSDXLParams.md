# Documentation
- Class name: AddCLIPSDXLParams
- Category: conditioning/advanced
- Output node: False
- Repo Ref: https://github.com/BlenderNeko/ComfyUI_ADV_CLIP_emb

The AddCLIPDXLParams node is designed to process and enhance condition data for advanced encoded tasks. It accepts parameters associated with image size and cropping and applies them to condition input to prepare for subsequent encoding steps. The node plays a key role in ensuring that the encoding process adapts to the specific requirements of the target application (e.g. image resolution and tailoring specifications).

# Input types
## Required
- conditioning
    - Conditional parameters are essential for nodes because they provide the basic data that will be operated and prepared for encoding. This is a key input that directly influences the output of nodes and the subsequent encoding process.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Any]
- width
    - Width parameters specify the width of the image to be processed. This is an important input because it determines the horizontal resolution of the image, which can significantly affect the quality and performance of the code.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - Altitude parameters define the vertical resolution of the image. It is a key input that determines the overall size of the image with width and is vital to the encoding process.
    - Comfy dtype: INT
    - Python dtype: int
- target_width
    - The target_width parameter sets the desired width for the final encoded image. This is an important parameter that affects the scaling and vertical ratio of the postcoded image.
    - Comfy dtype: INT
    - Python dtype: int
- target_height
    - The target_height parameter sets the expected height of the final encoded image. It is used in conjunction with the target_width to maintain the expected vertical ratio and dimensions of the encoded image.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- crop_w
    - Crop_w parameters indicate the width of the crop area in the image. It is an optional input that can be used to adjust the interest area in the image during the encoding process.
    - Comfy dtype: INT
    - Python dtype: int
- crop_h
    - The crop_h parameter specifies the height of the crop area. It works with crop_w to define the size of the crop area, which may be important to focus the code on particular parts of the image.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- encoded_conditioning
    - Encoded_conditioning is the condition data that you process and enhance. It contains changes to the original condition based on input parameters.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Any]

# Usage tips
- Infra type: CPU

# Source code
```
class AddCLIPSDXLParams:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'conditioning': ('CONDITIONING',), 'width': ('INT', {'default': 1024.0, 'min': 0, 'max': MAX_RESOLUTION}), 'height': ('INT', {'default': 1024.0, 'min': 0, 'max': MAX_RESOLUTION}), 'crop_w': ('INT', {'default': 0, 'min': 0, 'max': MAX_RESOLUTION}), 'crop_h': ('INT', {'default': 0, 'min': 0, 'max': MAX_RESOLUTION}), 'target_width': ('INT', {'default': 1024.0, 'min': 0, 'max': MAX_RESOLUTION}), 'target_height': ('INT', {'default': 1024.0, 'min': 0, 'max': MAX_RESOLUTION})}}
    RETURN_TYPES = ('CONDITIONING',)
    FUNCTION = 'encode'
    CATEGORY = 'conditioning/advanced'

    def encode(self, conditioning, width, height, crop_w, crop_h, target_width, target_height):
        c = []
        for t in conditioning:
            n = [t[0], t[1].copy()]
            n[1]['width'] = width
            n[1]['height'] = height
            n[1]['crop_w'] = crop_w
            n[1]['crop_h'] = crop_h
            n[1]['target_width'] = target_width
            n[1]['target_height'] = target_height
            c.append(n)
        return (c,)
```