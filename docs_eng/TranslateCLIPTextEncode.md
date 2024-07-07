# Documentation
- Class name: TranslateCLIPTextEncode
- Category: translate
- Output node: False
- Repo Ref: https://github.com/esheep/esheep_custom_nodes.git

The TranslateCLIPTextEncode node acts as an intermediary in coding text data into an understandable format for machine learning models (in particular models using the CLIP framework). It achieves this by translating input text into language suitable for the model and then tagging translated text. The primary function of the node is to prepare data for the follow-up processing of the AI model, emphasizing seamless integration of language translations and model coding.

# Input types
## Required
- text
    - The 'text' parameter is the original text input that the node will process. It is vital because it is the source information that will be encoded for use in the model. The node relies on this input to perform its translation and encoding tasks, making it an essential part of the node operation.
    - Comfy dtype: STRING
    - Python dtype: str
- clip
    - The `clip' parameter represents the node that will be used to tag and encode the CLIP model or its interface. It is an important component because it directly affects the ability of the node to convert the text to a suitable machine-learning application format.
    - Comfy dtype: CLIP
    - Python dtype: Any
- app_id
    - The `app_id' parameter is the identifier used for authentication when using external translation services. Although not necessary, it is important for accessing certain services and ensuring the integrity and security of the translation process.
    - Comfy dtype: STRING
    - Python dtype: str
- app_key
    - The 'app_key' parameter is used as a secret key for authentication with 'app_id'. It is not mandatory, but it plays an important role in ensuring secure access to translation services.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- CONDITIONING
    - The `conditioning' output is a structured expression of encoded text data, including the conditional vector and pool output of the CLIP model. This output is important because it provides processing information ready for downstream machine learning tasks.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Tuple[str, Dict[str, Any]}}

# Usage tips
- Infra type: CPU

# Source code
```
class TranslateCLIPTextEncode:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'text': ('STRING', {'multiline': True}), 'clip': ('CLIP',)}, 'hidden': {'app_id': ('STRING', {}), 'app_key': ('STRING', {})}}
    RETURN_TYPES = ('CONDITIONING',)
    FUNCTION = 'encode'
    CATEGORY = 'translate'

    def encode(self, clip, text, app_id='', app_key=''):
        tokens = clip.tokenize(translate(text, Credentials(app_id=app_id, app_key=app_key)))
        (cond, pooled) = clip.encode_from_tokens(tokens, return_pooled=True)
        return ([[cond, {'pooled_output': pooled}]],)
```