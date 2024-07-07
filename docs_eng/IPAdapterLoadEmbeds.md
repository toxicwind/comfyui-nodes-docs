# Documentation
- Class name: IPAdapterLoadEmbeds
- Category: ipadapter/embeds
- Output node: False
- Repo Ref: https://github.com/cubiq/ComfyUI_IPAdapter_plus.git

The `load'method for IPAdapterLoadEmbeds nodes is designed to retrieve and process embedded data from specified files. It is a key component for processing embedded data in the system, ensuring that embedded data are correctly loaded and providing us with usability for downstream tasks.

# Input types
## Required
- embeds
    - The parameter 'embeds' is a list that contains the embedded data storage file path. This parameter is critical because it guides node to the correct location of the data so that node can successfully load and process embedded data.
    - Comfy dtype: List[str]
    - Python dtype: List[str]

# Output types
- EMBEDS
    - The output parameter 'EMBEDS'means the embedded data loaded as a load. This load is important because it is a processing form of input data and is prepared for subsequent analysis or model training.
    - Comfy dtype: torch.Tensor
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class IPAdapterLoadEmbeds:

    @classmethod
    def INPUT_TYPES(s):
        input_dir = folder_paths.get_input_directory()
        files = [os.path.relpath(os.path.join(root, file), input_dir) for (root, dirs, files) in os.walk(input_dir) for file in files if file.endswith('.ipadpt')]
        return {'required': {'embeds': [sorted(files)]}}
    RETURN_TYPES = ('EMBEDS',)
    FUNCTION = 'load'
    CATEGORY = 'ipadapter/embeds'

    def load(self, embeds):
        path = folder_paths.get_annotated_filepath(embeds)
        return (torch.load(path).cpu(),)
```