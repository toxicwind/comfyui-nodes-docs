# Documentation
- Class name: AdvancedCLIPTextEncodeSDXL
- Category: conditioning/advanced
- Output node: False
- Repo Ref: https://github.com/BlenderNeko/ComfyUI_ADV_CLIP_emb

The Advanced CLIPTextEncodeSDXL node is designed to convert text input into a form that can be used for advanced condition tasks. It uses the capabilities of SDXLClipModel to generate embedded semantic information that captures text. This node is particularly suitable for applications that require a fine understanding of text content, such as natural language processing or content-based filtering systems.

# Input types
## Required
- text_l
    - The 'text_l' parameter is a string that indicates the main text to be encoded. It is a key input, because the semantic abundance of the text directly affects the embedded quality generated, which is essential for node downstream tasks.
    - Comfy dtype: STRING
    - Python dtype: str
- text_g
    - The 'text_g' parameter is used as a secondary text input for nodes. It is used with 'text_l' to provide more comprehensive encoding, taking into account additional text context. This parameter is essential for applications that benefit from wider text nuances.
    - Comfy dtype: STRING
    - Python dtype: str
- clip
    - The 'clip' parameter is an example of SDXLClipModel used to execute text code. This is a mandatory input, because the model is based on the core components that are provided to generate embedded text input.
    - Comfy dtype: CLIP
    - Python dtype: SDXLClipModel
## Optional
- token_normalization
    - The 'token_normation' parameter determines how tags can be normalized before they are embedded into the final embedding. It provides different strategies that can influence the distribution and importance of the embedded generation and thus the performance of nodes in downstream tasks.
    - Comfy dtype: COMBO[none, mean, length, length+mean]
    - Python dtype: str
- weight_interpretation
    - The 'weight_interpretation' parameter defines the method of interpreting weights associated with text tags during the encoding process. It can significantly change the emphasis on different parts of the text, which is important for special attention to be given to the application of text elements.
    - Comfy dtype: COMBO[comfy, A1111, compel, comfy++, down_weight]
    - Python dtype: str
- balance
    - The 'balance' parameter adjusts the general and specific balance of the text during the encoding process. It is a floating point value that allows fine-tuning to better adapt to the requirements of the current application.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- CONDITIONING
    - The output of the Advanced CLIPTextEncodeSDXL node is a coded `conditioning' object. This output is important because it forms the basis of the advanced condition task and allows for more complex and contextually sensitive processing.
    - Comfy dtype: CONDITIONING
    - Python dtype: Tuple[torch.Tensor, Dict[str, torch.Tensor]]

# Usage tips
- Infra type: CPU

# Source code
```
class AdvancedCLIPTextEncodeSDXL:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'text_l': ('STRING', {'multiline': True}), 'text_g': ('STRING', {'multiline': True}), 'clip': ('CLIP',), 'token_normalization': (['none', 'mean', 'length', 'length+mean'],), 'weight_interpretation': (['comfy', 'A1111', 'compel', 'comfy++', 'down_weight'],), 'balance': ('FLOAT', {'default': 0.5, 'min': 0.0, 'max': 1.0, 'step': 0.01})}}
    RETURN_TYPES = ('CONDITIONING',)
    FUNCTION = 'encode'
    CATEGORY = 'conditioning/advanced'

    def encode(self, clip, text_l, text_g, token_normalization, weight_interpretation, balance, affect_pooled='disable'):
        (embeddings_final, pooled) = advanced_encode_XL(clip, text_l, text_g, token_normalization, weight_interpretation, w_max=1.0, clip_balance=balance, apply_to_pooled=affect_pooled == 'enable')
        return ([[embeddings_final, {'pooled_output': pooled}]],)
```