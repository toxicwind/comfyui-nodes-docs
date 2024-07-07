# Load Text 🐍
## Documentation
- Class name: LoadText|pysssss
- Category: utils
- Output node: False
- Repo Ref: https://github.com/pythongosssss/ComfyUI-Custom-Scripts

LoadText node is used to load text from a file in the specified directory. It helps to retrieve text data so that it can be further processed or displayed in the workflow.

## Input types
### Required
- root_dir
    - Specifies the directory from which the file will be loaded. It is essential to locate the file and ensure that the correct path is used to access the file.
    - Comfy dtype: COMBO[STRING]
    - Python dtype: str
- file
    - This parameter is essential to determine the content of the text file to be retrieved and loaded.
    - Comfy dtype: COMBO[STRING]
    - Python dtype: str

## Output types
- string
    - Comfy dtype: STRING
    - Returns the content of the specified text file as a string.
    - Python dtype: str

## Usage tips
- Infra type: CPU
- Common nodes: unknown

## Source code
```python
class LoadText(TextFileNode):
    @classmethod
    def IS_CHANGED(self, **kwargs):
        return os.path.getmtime(self.file)

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "root_dir": (list(get_valid_dirs()), {}),
                "file": (["[none]"], {
                    "pysssss.binding": [{
                        "source": "root_dir",
                        "callback": [{
                            "type": "set",
                            "target": "$this.disabled",
                            "value": True
                        }, {
                            "type": "fetch",
                            "url": "/pysssss/text-file/{$source.value}",
                            "then": [{
                                "type": "set",
                                "target": "$this.options.values",
                                "value": "$result"
                            }, {
                                "type": "validate-combo"
                            }, {
                                "type": "set",
                                "target": "$this.disabled",
                                "value": False
                            }]
                        }],
                    }]
                })
            },
        }

    FUNCTION = "load_text"