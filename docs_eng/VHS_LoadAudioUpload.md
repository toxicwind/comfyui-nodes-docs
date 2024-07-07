# Load Audio (Upload)🎥🅥🅗🅢
## Documentation
- Class name: VHS_LoadAudioUpload
- Category: Video Helper Suite 🎥🅥🅗🅢
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite.git

VHS_LoadAudioUpload node is used to upload and process audio files in the video assistant package. It allows users to upload audio files and specifies the start and duration of audio processing. This node is essential for applications that require audio operation or analysis and provides the basis for further audio-related operations in the package.

## Input types
### Required
- audio
    - Specifies the audio files that you want to upload and process. This parameter is essential for determining the audio content that will be processed.
    - Comfy dtype: COMBO[STRING]
    - Python dtype: str
- start_time
    - Defines the starting point (in seconds) for audio files. This parameter allows for selective processing of audio content and increases flexibility.
    - Comfy dtype: FLOAT
    - Python dtype: float
- duration
    - Specifies the duration of audio processing (in seconds) from the beginning. This allows accurate control of the segments of audio files to be analysed or operated.
    - Comfy dtype: FLOAT
    - Python dtype: float

## Output types
- audio
    - Comfy dtype: VHS_AUDIO
    - is the processed audio data to be used in the follow-up operation of the package.
    - Python dtype: torch.Tensor

## Usage tips
- Infra type: CPU
- Common nodes: unknown

## Source code
```python
class LoadAudioUpload:
    @classmethod
    def INPUT_TYPES(s):
        input_dir = folder_paths.get_input_directory()
        files = []
        for f in os.listdir(input_dir):
            if os.path.isfile(os.path.join(input_dir, f)):
                file_parts = f.split('.')
                if len(file_parts) > 1 and (file_parts[-1] in audio_extensions):
                    files.append(f)
        return {"required": {
                    "audio": (sorted(files),),
                    "start_time": ("FLOAT" , {"default": 0, "min": 0, "max": 10000000, "step": 0.01}),
                    "duration": ("FLOAT" , {"default": 0, "min": 0, "max": 10000000, "step": 0.01}),
                     },
                }

    CATEGORY = "Video Helper Suite 🎥🅥🅗🅢"

    RETURN_TYPES = ("VHS_AUDIO", )
    RETURN_NAMES = ("audio",)
    FUNCTION = "load_audio"

    def load_audio(self, start_time, duration, **kwargs):
        audio_file = folder_paths.get_annotated_filepath(kwargs['audio'].strip("\""))
        if audio_file is None or validate_path(audio_file) != True:
            raise Exception("audio_file is not a valid path: " + audio_file)

        audio = get_audio(audio_file, start_time, duration)

        return (lambda : audio,)

    @classmethod
    def IS_CHANGED(s, audio, start_time, duration):
        audio_file = folder_paths.get_annotated_filepath(audio.strip("\""))
        return hash_path(audio_file)

    @classmethod
    def VALIDATE_INPUTS(s, audio, **kwargs):
        audio_file = folder_paths.get_annotated_filepath(audio.strip("\""))
        return validate_path(audio_file, allow_none=True)