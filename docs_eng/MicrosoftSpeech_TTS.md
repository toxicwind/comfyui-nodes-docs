# Documentation
- Class name: Text2AudioEdgeTts
- Category: 😺dzNodes
- Output node: True
- Repo Ref: https://github.com/chflame163/ComfyUI_MSSpeech_TTS

The Text2Audio EdgeTts node is designed to convert text to audio files using the edge_tts library. It accepts text, a sound parameter and an optional speed adjustment to generate audio files that can be used for various applications, such as voice assistants or audio readers. The main objective of the node is to provide an efficient and customized text-to-voice conversion process.

# Input types
## Required
- voice
    - A sound parameter is essential to determine the sound features that generate audio. It concentrates on a particular sound from the predefined sound in the edge_tts library, which significantly influences the quality and tone of the output.
    - Comfy dtype: STRING
    - Python dtype: str
- text
    - Text parameters are the input text that you want to convert to audio. It is the core content of the node processing to generate the desired audio output. The quality of the text directly influences the validity of the conversion.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- rate
    - Rate parameters allow a speech speed adjustment. It can be set to negative values to slow down the speech speed, or positive values to accelerate the speech speed. This feature is important for fine-tuning audio output to meet specific requirements or preferences.
    - Comfy dtype: INT
    - Python dtype: int
- filename_prefix
    - The filename prefix is used to create a unique identifier for an output audio file. It is particularly useful when organizing and managing multiple audio files, as it ensures that each file has a unique and identifiable name.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- MP3 file
    - The output of the Text2AudioEdgeTts node is a MP3 file containing audio generated from input text. This document is important because it represents the result of node text to voice conversion and can be used for various downstream applications.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class Text2AudioEdgeTts:

    def __init__(self):
        self.output_dir = os.path.join(folder_paths.get_output_directory(), 'audio')
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    @classmethod
    def INPUT_TYPES(cls):
        VOICES = list(voice_dict.keys())
        return {'required': {'voice': (VOICES,), 'rate': ('INT', {'default': 0, 'min': -200, 'max': 200}), 'filename_prefix': ('STRING', {'default': 'comfyUI'}), 'text': ('STRING', {'multiline': True})}}
    RETURN_TYPES = ('STRING',)
    RETURN_NAMES = ('MP3 file: String',)
    FUNCTION = 'text_2_audio'
    OUTPUT_NODE = True
    CATEGORY = '😺dzNodes'

    def text_2_audio(self, voice, filename_prefix, text, rate):
        voice_name = voice_dict[voice]
        (full_output_folder, filename, counter, subfolder, filename_prefix) = folder_paths.get_save_image_path(filename_prefix, self.output_dir)
        _datetime = datetime.datetime.now().strftime('%Y%m%d')
        _datetime = _datetime + datetime.datetime.now().strftime('%H%M%S%f')
        file = f'{filename}_{_datetime}_{voice_name}.mp3'
        audio_path = os.path.join(full_output_folder, file)
        _rate = str(rate) + '%' if rate < 0 else '+' + str(rate) + '%'
        print(f"# 😺dzNodes: MSSpeech TTS: Generating voice files, voice=‘{voice_name}’, rate={rate}, audiofile_path='{audio_path}, 'text='{text}'")
        asyncio.run(gen_tts(text, voice_name, _rate, audio_path))
        return {'ui': {'text': 'Audio file：' + os.path.join(full_output_folder, file), 'audios': [{'filename': file, 'type': 'output', 'subfolder': 'audio'}]}, 'result': (audio_path,)}
```