# Documentation
- Class name: TranslateNode
- Category: translate
- Output node: True
- Repo Ref: https://github.com/esheep/esheep_custom_nodes.git

The node is designed to process and convert text data into the required language, and to achieve multilingual communication and content understanding. The main function of the node is to build bridges of language communication to enhance the accessibility and coverage of information.

# Input types
## Required
- text
    - Text parameters are necessary because they are the source content that requires translation. They are the input of the translation process, which directly affects the relevance and accuracy of the output. Without this parameter, nodes cannot perform their intended functions.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- app_id
    - App_id parameters, although not necessary, are essential for validating requests for translation services. It ensures that nodes are able to access the necessary resources and perform translations within permitted limits.
    - Comfy dtype: STRING
    - Python dtype: str
- app_key
    - Similar to the app_id, the app_key is another necessary authentication document that is essential for the correct function of the node. It plays a role in ensuring that connection security and translation requests are authorized.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- result
    - The result parameter represents the translated text and is the main output of the node. It directly reflects the validity of the translation process and is essential for achieving the node's purpose.
    - Comfy dtype: COMBO[STRING]
    - Python dtype: List[str]

# Usage tips
- Infra type: CPU

# Source code
```
class TranslateNode:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'text': ('STRING', {'multiline': True})}, 'hidden': {'app_id': ('STRING', {}), 'app_key': ('STRING', {})}}
    RETURN_TYPES = ('STRING',)
    FUNCTION = 'main'
    CATEGORY = 'translate'
    OUTPUT_IS_LIST = (True,)
    OUTPUT_NODE = True

    def main(self, text, app_id='', app_key=''):
        result = translate(text, Credentials(app_id=app_id, app_key=app_key))
        return {'ui': {'result': [result]}, 'result': ([result],)}
```