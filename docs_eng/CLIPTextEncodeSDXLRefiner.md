# Documentation
- Class name: CLIPTextEncodeSDXLRefiner
- Category: advanced/conditioning
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The CLIPTextEncode SDXLRefiner node is designed to fine-tune and encode text input using the CLIP model, which is good at understanding and generating visual expressions from text descriptions. It plays a key role in the reconciliation process, producing a comprehensive reconciliation signal by integrating United States fractions, dimensions and text information that can guide subsequent image synthesis or processing stages.

# Input types
## Required
- ascore
    - A US score parameter is essential to quantify the visual appeal of the content generated. It influences the aesthetic quality of the output by weighting the importance of the aesthetic process in the final adjustment signal.
    - Comfy dtype: FLOAT
    - Python dtype: float
- width
    - The width parameter specifies the desired width of the output image. It is a key factor in determining the resolution and plays an important role in the way the code text is visualized in the synthetic image.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - Altitude parameters set the vertical dimensions of the output image. Together with width, it defines the overall resolution, which is essential for correct scaling and displaying the coded content.
    - Comfy dtype: INT
    - Python dtype: int
- text
    - Text parameters are the main input of the node and contain text descriptions that will be coded to visual expressions. It is the core of the node function, as the quality and detail of the text directly influences the code signal generated.
    - Comfy dtype: STRING
    - Python dtype: str
- clip
    - The CLIP parameter represents the model used to encode the text. It is essential because it provides the basic mechanism for converting the text into a format that can be used for reconciliation in image synthesis.
    - Comfy dtype: CLIP
    - Python dtype: CLIP model instance

# Output types
- CONDITIONING
    - Reconciling output is a multi-dimensional signal that contains encoded text, aesthetic scores, and dimensions. It serves as a guide for follow-up image-processing tasks to ensure that the content generated is consistent with the initial text input.
    - Comfy dtype: CONDITIONING
    - Python dtype: Tuple[torch.Tensor, Dict[str, Union[torch.Tensor, float, int]]]

# Usage tips
- Infra type: GPU

# Source code
```
class CLIPTextEncodeSDXLRefiner:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'ascore': ('FLOAT', {'default': 6.0, 'min': 0.0, 'max': 1000.0, 'step': 0.01}), 'width': ('INT', {'default': 1024.0, 'min': 0, 'max': MAX_RESOLUTION}), 'height': ('INT', {'default': 1024.0, 'min': 0, 'max': MAX_RESOLUTION}), 'text': ('STRING', {'multiline': True, 'dynamicPrompts': True}), 'clip': ('CLIP',)}}
    RETURN_TYPES = ('CONDITIONING',)
    FUNCTION = 'encode'
    CATEGORY = 'advanced/conditioning'

    def encode(self, clip, ascore, width, height, text):
        tokens = clip.tokenize(text)
        (cond, pooled) = clip.encode_from_tokens(tokens, return_pooled=True)
        return ([[cond, {'pooled_output': pooled, 'aesthetic_score': ascore, 'width': width, 'height': height}]],)
```