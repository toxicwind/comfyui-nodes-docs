# Documentation
- Class name: ShowTextForGPT
- Category: ♾️Mixlab/GPT
- Output node: True
- Repo Ref: https://github.com/shadowcz007/comfyui-mixlab-nodes.git

ShowTextForGPT node is designed to process and output text data. It accepts text input and writes them into the output file to ensure that each string is properly processed and stored. This node is essential for tasks that require text generation and subsequent file management and provides a simplified workflow for text processing.

# Input types
## Required
- text
    - The `text' parameter is essential because it represents the data to be processed by the node. This is the main input that determines the content and nature of the output. Without this input, node will have any data to process, making it a key component of the node operation.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- output_dir
    - The `output_dir' parameter is used to specify where the processed text will be saved, which has an impact on the organization and accessibility of the output file, allowing for better management and retrieval of the results. This parameter is optional, but enhances the function of the node when used.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- ui.text
    - The `ui.text' output parameter represents the processed text data. It is a direct reflection of input, showing the ability of nodes to process and output text efficiently. This output is important for visualizing the results in the user interface.
    - Comfy dtype: STRING
    - Python dtype: str
- result
    - The `redult' output parameter is a collection of processed text data, indicating the successful completion of node operations. This is a critical output, as it provides evidence of node function and text-processing validity.
    - Comfy dtype: COMBO[STRING]
    - Python dtype: List[str]

# Usage tips
- Infra type: CPU

# Source code
```
class ShowTextForGPT:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'text': ('STRING', {'forceInput': True, 'dynamicPrompts': False})}, 'optional': {'output_dir': ('STRING', {'forceInput': True, 'default': '', 'multiline': True, 'dynamicPrompts': False})}}
    INPUT_IS_LIST = True
    RETURN_TYPES = ('STRING',)
    FUNCTION = 'run'
    OUTPUT_NODE = True
    OUTPUT_IS_LIST = (True,)
    CATEGORY = '♾️Mixlab/GPT'

    def run(self, text, output_dir=['']):
        texts = []
        for t in text:
            if not isinstance(t, str):
                t = str(t)
            texts.append(t)
        text = texts
        if len(output_dir) == 1 and (output_dir[0] == '' or os.path.dirname(output_dir[0]) == ''):
            t = '\n'.join(text)
            output_dir = [os.path.join(folder_paths.get_temp_directory(), get_unique_hash(t) + '.txt')]
        elif len(output_dir) == 1:
            base = os.path.basename(output_dir[0])
            t = '\n'.join(text)
            if base == '' or os.path.splitext(base)[1] == '':
                base = get_unique_hash(t) + '.txt'
            output_dir = [os.path.join(output_dir[0], base)]
        if len(output_dir) == 1 and len(text) > 1:
            output_dir = [output_dir[0] for _ in range(len(text))]
        for i in range(len(text)):
            o_fp = output_dir[i]
            dirp = os.path.dirname(o_fp)
            if dirp == '':
                dirp = folder_paths.get_temp_directory()
                o_fp = os.path.join(folder_paths.get_temp_directory(), o_fp)
            if not os.path.exists(dirp):
                os.mkdir(dirp)
            if not os.path.splitext(o_fp)[1].lower() == '.txt':
                o_fp = o_fp + '.txt'
            t = text[i]
            with open(o_fp, 'w') as file:
                file.write(t)
        return {'ui': {'text': text}, 'result': (text,)}
```