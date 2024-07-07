# String Function 🐍
## Documentation
- Class name: StringFunction|pysssss
- Category: utils
- Output node: True
- Repo Ref: https://github.com/pythongosssss/ComfyUI-Custom-Scripts

String Action nodes provide practical tools for operating strings, including additions, replacements, and optional tag clean-up. It provides complex string operations in the abstract as a simple interface to meet various text-processing needs.

## Input types
### Required
- action
    - Specifies the string operations that you want to perform, such as adding or replacing content in text input.
    - Comfy dtype: COMBO[STRING]
    - Python dtype: Tuple[List[str], Dict]
- tidy_tags
    - Whether to clean up the HTML label in the text input and provide options for sorting or maintaining it as it is.
    - Comfy dtype: COMBO[STRING]
    - Python dtype: Tuple[List[str], Dict]
- text_a
    - is the main text input for the operation.
    - Comfy dtype: STRING
    - Python dtype: str
- text_b
    - Secondary text input for operations, used with 'text_a'.
    - Comfy dtype: STRING
    - Python dtype: str

### Optional
- text_c
    - Optional third text input is used for operations.
    - Comfy dtype: STRING
    - Python dtype: str

## Output types
- string
    - Comfy dtype: STRING
    - is the result of a string operation that returns as a single string.
    - Python dtype: str

## Usage tips
- Infra type: CPU
<!-- - Common nodes:
    - [CLIPTextEncode](../../Comfy/Nodes/CLIPTextEncode.md) -->

## Source code
```python
class StringFunction:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "action": (["append", "replace"], {}),
                "tidy_tags": (["yes", "no"], {}),
                "text_a": ("STRING", {"multiline": True, "dynamicPrompts": False}),
                "text_b": ("STRING", {"multiline": True, "dynamicPrompts": False}),
            },
            "optional": {
                "text_c": ("STRING", {"multiline": True, "dynamicPrompts": False})
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "exec"
    CATEGORY = "utils"
    OUTPUT_NODE = True

    def exec(self, action, tidy_tags, text_a, text_b, text_c=""):
        # Converted inputs are sent as the string of 'undefined' if not connected
        if text_a == "undefined":
            text_a = ""
        if text_b == "undefined":
            text_b = ""
        if text_c == "undefined":
            text_c = ""

        tidy_tags = tidy_tags == "yes"
        out = ""
        if action == "append":
            out = (", " if tidy_tags else "").join(filter(None, [text_a, text_b, text_c]))
        else:
           if text_c is None:
               text_c = ""
           if text_b.startswith("/") and text_b.endsWith("/"):
               regex = text_b[1:-1]
               out = re.sub(regex, text_c, text_a)
           else:
               out = text_a.replace(text_b, text_c)
        if tidy_tags:
            out = out.replace("  ", " ").replace(" ,", ",").replace(",,", ",").replace(",,", ",")
        return {"ui": {"text": (out,)}, "result": (out,)}