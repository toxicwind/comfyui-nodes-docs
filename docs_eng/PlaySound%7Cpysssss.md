# PlaySound 🐍
## Documentation
- Class name: PlaySound|pysssss
- Category: utils
- Output node: True
- Repo Ref: https://github.com/pythongosssss/ComfyUI-Custom-Scripts

PlaySound node is used to play audio files with customised settings (e.g. volume and mode of play). It abstractes the complexity of audio play and provides a simple interface for triggering sound or notification in the workflow.

## Input types
### Required
- any
    - Enter as a wildcard, allowing for flexible integration with various data types or structures, without enforcing a specific format.
    - Comfy dtype: *
    - Python dtype: AnyType
- mode
    - Determines the conditions for playing, which may be that the sound is always played or is only played in the queue when it is empty, thereby controlling the occurrence of the sound.
    - Comfy dtype: COMBO[STRING]
    - Python dtype: List[str]
- volume
    - Controls audio volume from 0 to 1 and allows fine-tuning of sound levels.
    - Comfy dtype: FLOAT
    - Python dtype: float
- file
    - Specifies the audio files that you want to play, providing a default option to allow custom sound effects.
    - Comfy dtype: STRING
    - Python dtype: str

## Output types
- *
    - Comfy dtype: *
    - unknown
    - Python dtype: unknown
- ui
    - Returns a UI component structure, although in this context it appears to be a placeholder with no active element.

## Usage tips
- Infra type: CPU
- Common nodes: unknown

## Source code
```python
class PlaySound:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
            "any": (any, {}),
            "mode": (["always", "on empty queue"], {}),
            "volume": ("FLOAT", {"min": 0, "max": 1, "step": 0.1, "default": 0.5}),
            "file": ("STRING", { "default": "notify.mp3" })
        }}

    FUNCTION = "nop"
    INPUT_IS_LIST = True
    OUTPUT_IS_LIST = (True,)
    OUTPUT_NODE = True
    RETURN_TYPES = (any,)

    CATEGORY = "utils"

    def IS_CHANGED(self, **kwargs):
        return float("NaN")

    def nop(self, any, mode, volume, file):
        return {"ui": {"a": []}, "result": (any,)}