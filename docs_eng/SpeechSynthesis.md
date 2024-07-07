# Documentation
- Class name: SpeechSynthesis
- Category: ♾️Mixlab/Audio
- Output node: True
- Repo Ref: https://github.com/shadowcz007/comfyui-mixlab-nodes.git

The node is designed to transform the text provided into a human-like voice, allowing applications to communicate with users in the form of sound. It converts text data into audio output, which allows for the creation of a highly interactive and fascinating audio experience.

# Input types
## Required
- text
    - Text parameters are essential for the running of nodes because they are input to speech synthesis. It determines the content and context of the voice generation and directly influences the output of the nodes.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- result
    - The output is a synthetic voice, the main purpose of which is to use this node. It represents the conversion of the input text to the hearing format and is ready for play.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class SpeechSynthesis:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'text': ('STRING', {'forceInput': True})}}
    INPUT_IS_LIST = True
    RETURN_TYPES = ('STRING',)
    FUNCTION = 'run'
    OUTPUT_NODE = True
    OUTPUT_IS_LIST = (True,)
    CATEGORY = '♾️Mixlab/Audio'

    def run(self, text):
        return {'ui': {'text': text}, 'result': (text,)}
```