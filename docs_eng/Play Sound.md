# Documentation
- Class name: Play_Sound_Now
- Category: 😺dzNodes
- Output node: True
- Repo Ref: https://github.com/chflame163/ComfyUI_MSSpeech_TTS

Play_Sound_Now node is designed to enable audio files to be played instantaneously. It performs the play by loading specified audio files and using a separate thread to ensure minimum interference with the main program process. This node is particularly suitable for applications that require audio feedback or alarms and delay smaller applications.

# Input types
## Required
- path
    - The 'path' parameter specifies the file path of the audio file to be played. It is essential for the operation of the node because it guides the node to find the right audio file. Without a valid path, the node will not work, so this is a necessary parameter.
    - Comfy dtype: STRING
    - Python dtype: str
- volume
    - The `volume' parameter is used to adjust the volume of audio play. It is an important setting to control the level of audio output and to ensure that it meets the requirements of the application. The volume can be set between 0.0 and 1.0, of which 1.0 represents the default volume.
    - Comfy dtype: FLOAT
    - Python dtype: float
- speed
    - The'speed' parameter changes the speed at which the audio is played. It is important to change the rhythm of the sound without changing its height. Speed can vary between 0.1 and 2.0, allowing many options for the speed of play.
    - Comfy dtype: FLOAT
    - Python dtype: float
- trigger
    - The 'trigger'parameter decides whether to start audio play. It is a key control that directly affects the execution of the node's main function. If set to True, the audio is played; otherwise it will remain silent.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- result
    - Play_Sound_Now node's `resource' parameter does not return any particular data, but represents a successful start of the audio play. It is the placeholder for any possible future enhancements or status messages associated with node operations.
    - Comfy dtype: DICT
    - Python dtype: Dict[str, Any]

# Usage tips
- Infra type: CPU

# Source code
```
class Play_Sound_Now:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'path': ('STRING', {'default': 'comfyui.mp3'}), 'volume': ('FLOAT', {'default': 1, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'speed': ('FLOAT', {'default': 1, 'min': 0.1, 'max': 2.0, 'step': 0.1}), 'trigger': ('BOOLEAN', {'default': True})}, 'optional': {}}
    RETURN_TYPES = ()
    FUNCTION = 'do_playsound'
    OUTPUT_NODE = True
    CATEGORY = '😺dzNodes'

    def do_playsound(self, path, volume, speed, trigger):
        print(f'# 😺dzNodes: PlaySound: path={path},volume={volume},speed={speed},trigger={trigger}')
        if trigger:
            t = threading.Thread(target=Play(path, volume, speed))
            t.start()
        return {}
```