# Documentation
- Class name: CheckpointHash
- Category: Mikey/Loaders
- Output node: False
- Repo Ref: https://github.com/bash-j/mikey_nodes

The CheckpointHash node is designed to generate and retrieve encrypted Hashi files for the specified check point. It ensures the integrity and uniqueness of the check point by its content. This node plays a key role in verifying the authenticity of the check point during loading.

# Input types
## Required
- ckpt_name
    - The check point name is a key parameter for identifying the selected check point file that will be generated in Hash. It is used to match the file in the check point directory.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- extra_pnginfo
    - Additional information related to the PNG file format may be used for additional processing or metadata storage beyond the check point.
    - Comfy dtype: EXTRA_PNGINFO
    - Python dtype: Any
- prompt
    - Prompt objects are used to store and retrieve information relevant to the checkpoint, such as unique identifiers and calculated Hash for follow-up use in the workflow.
    - Comfy dtype: PROMPT
    - Python dtype: Dict[str, Dict[str, Any]]
- unique_id
    - The only identifier for the check point can be used to track and refer to the check point in the system.
    - Comfy dtype: UNIQUE_ID
    - Python dtype: str

# Output types
- ckpt_hash
    - The encryption of the site file has ensured its integrity and served as a means of verification.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CheckpointHash:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'ckpt_name': ('STRING', {'forceInput': True})}, 'hidden': {'unique_id': 'UNIQUE_ID', 'extra_pnginfo': 'EXTRA_PNGINFO', 'prompt': 'PROMPT'}}
    RETURN_TYPES = ('STRING',)
    RETURN_NAMES = ('ckpt_hash',)
    FUNCTION = 'get_hash'
    CATEGORY = 'Mikey/Loaders'

    def get_hash(self, ckpt_name, extra_pnginfo, prompt, unique_id):
        file_list = folder_paths.get_filename_list('checkpoints')
        matching_file = [s for s in file_list if ckpt_name in s][0]
        ckpt_path = folder_paths.get_full_path('checkpoints', matching_file)
        hash = get_file_hash(ckpt_path)
        ckpt_name = os.path.basename(ckpt_name)
        prompt.get(str(unique_id))['inputs']['output_ckpt_hash'] = hash
        prompt.get(str(unique_id))['inputs']['output_ckpt_name'] = ckpt_name
        return (get_file_hash(ckpt_path),)
```