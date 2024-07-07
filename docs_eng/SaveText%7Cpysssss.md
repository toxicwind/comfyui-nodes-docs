# Save Text 🐍
## Documentation
- Class name: SaveText|pysssss
- Category: utils
- Output node: False
- Repo Ref: https://github.com/pythongosssss/ComfyUI-Custom-Scripts

SaveText is used to write text to a file and provides options for attaching it to an existing file or creating a new one. It abstractes the complexity of file processing and ensures that text data is accurately stored according to the specified parameters.

## Input types
### Required
- root_dir
    - Specifies the root directory to which the file will be saved. It is essential to determine where the file is stored and to ensure that the file path is correctly constructed.
    - Comfy dtype: COMBO[STRING]
    - Python dtype: str
- file
    - The name of the file that you want to save the text. This parameter is essential for determining the particular file that you want to write or create.
    - Comfy dtype: STRING
    - Python dtype: str
- append
    - Whether the control text should be attached to the existing document or whether a new document should be created. It affects the way the text is stored, by adding it to the existing text or by restarting it.
    - Comfy dtype: COMBO[STRING]
    - Python dtype: str
- insert
    - Decides whether line breaks should be inserted before adding text to the existing document. It affects the formatting of the additional text.
    - Comfy dtype: BOOLEAN
    - Python dtype: str
- text
    - The text content of the file that you want to write to. This parameter is the core of the node function, as it specifies the actual data that you want to save.
    - Comfy dtype: STRING
    - Python dtype: str

## Output types
- string
    - Comfy dtype: STRING
    - Returns the text written to the file to provide feedback on the successful operation.
    - Python dtype: str

## Usage tips
- Infra type: CPU
- Common nodes: unknown

## Source code
```python
class SaveText(TextFileNode):
    @classmethod
    def IS_CHANGED(self, **kwargs):
        return float("nan")

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "root_dir": (list(get_valid_dirs()), {}),
                "file": ("STRING", {"default": "file.txt"}),
                "append": (["append", "overwrite", "new only"], {}),
                "insert": ("BOOLEAN", {
                    "default": True, "label_on": "new line", "label_off": "none",
                    "pysssss.binding": [{
                        "source": "append",
                        "callback": [{
                            "type": "if",
                            "condition": [{
                                "left": "$source.value",
                                "op": "eq",
                                "right": '"append"'
                            }],
                            "true": [{
                                "type": "set",
                                "target": "$this.disabled",
                                "value": False
                            }],
                            "false": [{
                                "type": "set",
                                "target": "$this.disabled",
                                "value": True
                            }],
                        }]
                    }]
                }),
                "text": ("STRING", {"forceInput": True, "multiline": True})
            },
        }

    FUNCTION = "write_text"

    def write_text(self, **kwargs):
        self.file = get_file(kwargs["root_dir"], kwargs["file"])
        if kwargs["append"] == "new only" and os.path.exists(self.file):
            raise FileExistsError(
                self.file + " already exists and 'new only' is selected.")
        with open(self.file, "a+" if kwargs["append"] == "append" else "w") as f:
            is_append = f.tell() != 0
            if is_append and kwargs["insert"]:
                f.write("\n")
            f.write(kwargs["text"])

        return super().load_text(**kwargs)