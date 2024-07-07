# Documentation
- Class name: LoadPromptsFromFile
- Category: InspirePack/Prompt
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Inspire-Pack.git

LoadPromptsFromFile is designed to read and resolve the reminder files from a specified directory. It extracts both positive and negative text paragraphs from each file, follows the predefined format, and organizes them into meta-groups. The node plays a key role in the reminder data to be further processed, such as training or evaluation generation models.

# Input types
## Required
- prompt_file
    - The 'prompt_file' parameter is a string that specifies the relative path of the text file containing the hint. It is essential for the operation of the node, as it determines the source of the hint to be loaded and processed.
    - Comfy dtype: "str"
    - Python dtype: str

# Output types
- ZIPPED_PROMPT
    - The 'ZIPPED_PROMPT' output is a matrix list, each of which contains both positive and negative text paragraphs extracted from the reminder file, as well as the name of the file. This output is important because it provides the structured data needed for downstream tasks.
    - Comfy dtype: COMBO["str", "str", "str"]
    - Python dtype: Tuple[str, str, str]

# Usage tips
- Infra type: CPU

# Source code
```
class LoadPromptsFromFile:

    @classmethod
    def INPUT_TYPES(cls):
        global prompts_path
        try:
            prompt_files = []
            for (root, dirs, files) in os.walk(prompts_path):
                for file in files:
                    if file.endswith('.txt'):
                        file_path = os.path.join(root, file)
                        rel_path = os.path.relpath(file_path, prompts_path)
                        prompt_files.append(rel_path)
        except Exception:
            prompt_files = []
        return {'required': {'prompt_file': (prompt_files,)}}
    RETURN_TYPES = ('ZIPPED_PROMPT',)
    OUTPUT_IS_LIST = (True,)
    FUNCTION = 'doit'
    CATEGORY = 'InspirePack/Prompt'

    def doit(self, prompt_file):
        prompt_path = os.path.join(prompts_path, prompt_file)
        prompts = []
        try:
            with open(prompt_path, 'r', encoding='utf-8') as file:
                prompt_data = file.read()
                prompt_list = re.split('\\n\\s*-+\\s*\\n', prompt_data)
                pattern = 'positive:(.*?)(?:\\n*|$)negative:(.*)'
                for prompt in prompt_list:
                    matches = re.search(pattern, prompt, re.DOTALL)
                    if matches:
                        positive_text = matches.group(1).strip()
                        negative_text = matches.group(2).strip()
                        result_tuple = (positive_text, negative_text, prompt_file)
                        prompts.append(result_tuple)
                    else:
                        print(f"[WARN] LoadPromptsFromFile: invalid prompt format in '{prompt_file}'")
        except Exception as e:
            print(f"[ERROR] LoadPromptsFromFile: an error occurred while processing '{prompt_file}': {str(e)}")
        return (prompts,)
```