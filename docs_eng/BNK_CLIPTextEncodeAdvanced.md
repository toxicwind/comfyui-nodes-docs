# Documentation
- Class name: AdvancedCLIPTextEncode
- Category: conditioning/advanced
- Output node: False
- Repo Ref: https://github.com/BlenderNeko/ComfyUI_ADV_CLIP_emb

The Advanced CLIPTextEncode node is designed to convert text input into a form that can be used for advanced condition tasks. It uses the ability of the CLIP model to generate embedded captures of text semantic properties. This node is particularly suitable for applications that require a deeper understanding of the input text, such as the generation of models or natural language processing tasks that require a deeper understanding of the input text.

# Input types
## Required
- text
    - The 'text' parameter is the main input of the node, which represents the text that needs to be coded. It should be a string and contain multiple lines of text, allowing for more complex and longer text input. This parameter is essential because the quality of the code depends to a large extent on the accuracy and richness of the text provided.
    - Comfy dtype: STRING
    - Python dtype: str
- clip
    - The 'clip'parameter is assigned to the CLIP model for text encoding. It is a necessary input, as node relies on the structure and capacity of the CLIP model to generate meaningful embedding from text input.
    - Comfy dtype: CLIP
    - Python dtype: Any
- token_normalization
    - The 'token_normation' parameter determines how the tags are regularized in the pre-coding text. It can use different strategies, such as 'one','mean', 'length' or 'lenghth+mean', which affect the distribution and scale of the marker embedded. This parameter is important for controlling the variance in the embedded text and can affect the performance of the condition.
    - Comfy dtype: COMBO[none, mean, length, length+mean]
    - Python dtype: str
- weight_interpretation
    - The 'weight_interpretation' parameter affects the interpretation of tag weights during the encoding process. It provides options such as 'comfy', 'A1111', 'compel', 'comfy++' or 'down_weight', each of which may lead to different emphasis on certain aspects of the text. This parameter is essential for fine-tuning codes to meet the specific requirements of the downstream task.
    - Comfy dtype: COMBO[comfy, A1111, compel, comfy++, down_weight]
    - Python dtype: str
## Optional
- affect_pooled
    - The 'affect_pooled' parameter is an optional input to control whether the CLIP model should be influenced by the encoded process. It accepts the 'enable' or 'disable' value, which determines whether the pool output is included in the final embedding.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- CONDITIONING
    - The output of the Advanced CLIPTextEncode node is a volume that represents the coded text. This volume is used as a condition input for further processing or generating the task. It contains semantic information extracted from the text and provides a rich and detailed indication that can guide the next steps in the workflow.
    - Comfy dtype: TENSOR
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class AdvancedCLIPTextEncode:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'text': ('STRING', {'multiline': True}), 'clip': ('CLIP',), 'token_normalization': (['none', 'mean', 'length', 'length+mean'],), 'weight_interpretation': (['comfy', 'A1111', 'compel', 'comfy++', 'down_weight'],)}}
    RETURN_TYPES = ('CONDITIONING',)
    FUNCTION = 'encode'
    CATEGORY = 'conditioning/advanced'

    def encode(self, clip, text, token_normalization, weight_interpretation, affect_pooled='disable'):
        (embeddings_final, pooled) = advanced_encode(clip, text, token_normalization, weight_interpretation, w_max=1.0, apply_to_pooled=affect_pooled == 'enable')
        return ([[embeddings_final, {'pooled_output': pooled}]],)
```