# Documentation
- Class name: SpeechRecognition
- Category: ♾️Mixlab/Audio
- Output node: False
- Repo Ref: https://github.com/shadowcz007/comfyui-mixlab-nodes.git

The speech recognition node is designed to convert audio input into text. It plays a key role in applications that require the conversion of spoken words into written form, for example, in voice command systems or transcording services. The node focuses on its ability to accurately process and interpret audio signals, providing users with a powerful voice-to-text tool.

# Input types
## Required
- upload
    - The `upload' parameter is essential for speech recognition nodes because it is the source of audio data that needs to be processed. This is a necessary input that directly affects the operation of nodes and the quality of speech recognition output.
    - Comfy dtype: AUDIOINPUTMIX
    - Python dtype: Union[str, bytes]
- start_by
    - The `start_by' parameter allows the user to specify the starting point of the voice recognition process in the audio file. Although it is optional, it can significantly influence the implementation of the node by concentrating the identification tasks on the specified parts of the audio, increasing efficiency and accuracy.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- prompt
    - The `prompt' output of the speech recognition node represents the text from which an audio transcribe is entered. This is an important result, which contains the primary function of the node and provides a text expression for the user's spoken content.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class SpeechRecognition:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'upload': ('AUDIOINPUTMIX',)}, 'optional': {'start_by': ('INT', {'default': 0, 'min': 0, 'max': 2048, 'step': 1, 'display': 'number'})}}
    RETURN_TYPES = ('STRING',)
    RETURN_NAMES = ('prompt',)
    FUNCTION = 'run'
    CATEGORY = '♾️Mixlab/Audio'
    INPUT_IS_LIST = False
    OUTPUT_IS_LIST = (False,)

    def run(self, upload, start_by):
        return {'ui': {'start_by': [start_by]}, 'result': (upload,)}
```