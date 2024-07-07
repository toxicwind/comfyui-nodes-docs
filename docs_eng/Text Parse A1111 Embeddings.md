# Documentation
- Class name: WAS_Text_Parse_Embeddings_By_Name
- Category: WAS Suite/Text/Parse
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The `text_parse_embeddings'method is designed to interpret and replace text as the corresponding embedding. By identifying specific patterns in the input text that match the names of the embedded files and replace them with predefined formats containing the word 'embeding' behind the filename. This process is essential for preparing text data for further processing or analysis using embedded models.

# Input types
## Required
- text
    - The 'text'parameter is essential because it provides the original text data that the node will process. This is the input that the node execution mode matches and replaces to embed the appropriate reference embedded file.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- parsed_text
    - The 'parsed_text'output contains a modified text with an appropriately formatted embedded reference. It is the result of node operations and is important for any subsequent steps that require the use of embedded data.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Text_Parse_Embeddings_By_Name:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'text': (TEXT_TYPE, {'forceInput': True if TEXT_TYPE == 'STRING' else False})}}
    RETURN_TYPES = (TEXT_TYPE,)
    FUNCTION = 'text_parse_embeddings'
    CATEGORY = 'WAS Suite/Text/Parse'

    def text_parse_embeddings(self, text):
        return (self.convert_a1111_embeddings(text),)

    def convert_a1111_embeddings(self, text):
        for embeddings_path in comfy_paths.folder_names_and_paths['embeddings'][0]:
            for filename in os.listdir(embeddings_path):
                (basename, ext) = os.path.splitext(filename)
                pattern = re.compile('\\b{}\\b'.format(re.escape(basename)))
                replacement = 'embedding:{}'.format(basename)
                text = re.sub(pattern, replacement, text)
        return text
```