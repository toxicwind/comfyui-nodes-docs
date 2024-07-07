# Documentation
- Class name: LoadAudio
- Category: Video Helper Suite 🎥🅥🅗🅢
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite.git

LoadAudio nodes are designed to load and process audio files efficiently. It can handle various audio file formats and provide a function to jump to a given number of seconds in the audio stream. This node is essential for applications that require audio operation or analysis as part of a larger multimedia processing workflow.

# Input types
## Required
- audio_file
    - The audio_file parameter specifies the path of the audio file that you want to load. This is a basic parameter, because the operation of the node revolves around the audio file provided. The node will verify the path and ensure that the file is accessible and in a supported format.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- seek_seconds
    - Seek_seconds parameters allow nodes to process audio from the specified time deviation (seconds). This is very useful when only part of the audio files is relevant, thus improving efficiency and reducing unnecessary processing.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- audio
    - Audio output from LoadAudio nodes represents the audio data that is loaded and selected for processing. It is a key output because it is entered into the subsequent audio analysis or operation phase of the multimedia workflow.
    - Comfy dtype: VHS_AUDIO
    - Python dtype: bytes

# Usage tips
- Infra type: CPU

# Source code
```
class LoadAudio:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'audio_file': ('STRING', {'default': 'input/', 'vhs_path_extensions': ['wav', 'mp3', 'ogg', 'm4a', 'flac']})}, 'optional': {'seek_seconds': ('FLOAT', {'default': 0, 'min': 0})}}
    RETURN_TYPES = ('VHS_AUDIO',)
    RETURN_NAMES = ('audio',)
    CATEGORY = 'Video Helper Suite 🎥🅥🅗🅢'
    FUNCTION = 'load_audio'

    def load_audio(self, audio_file, seek_seconds):
        if audio_file is None or validate_path(audio_file) != True:
            raise Exception('audio_file is not a valid path: ' + audio_file)
        audio = get_audio(audio_file, start_time=seek_seconds)
        return (lambda : audio,)

    @classmethod
    def IS_CHANGED(s, audio_file, seek_seconds):
        return hash_path(audio_file)

    @classmethod
    def VALIDATE_INPUTS(s, audio_file, **kwargs):
        return validate_path(audio_file, allow_none=True)
```