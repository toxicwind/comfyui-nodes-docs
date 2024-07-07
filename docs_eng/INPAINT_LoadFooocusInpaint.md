# Documentation
- Class name: LoadFooocusInpaint
- Category: inpaint
- Output node: False
- Repo Ref: https://github.com/Acly/comfyui-inpaint-nodes

The node is intended to load and integrate two key components of the image restoration task: head model and patch data. It coordinates the process of loading head model and patch data from saved state dictionary to ensure that the two components are ready for use in image restoration.

# Input types
## Required
- head
    - The `head' parameter specifies the file path of the head model, which is essential to the image restoration process. It is used to guide the creation of the restoration.
    - Comfy dtype: str
    - Python dtype: str
- patch
    - The `patch' parameter represents the file path for patch data, which is essential for the image restoration task. It provides the information needed for the model to understand the context of the area to be repaired.
    - Comfy dtype: str
    - Python dtype: str

# Output types
- INPAINT_PATCH
    - The output consists of a pair of: loaded head model and patch data. These are essential to the image restoration process, as they provide the structure and context information needed to generate the final restoration results.
    - Comfy dtype: COMBO[(torch.nn.Module, Any)]
    - Python dtype: Tuple[torch.nn.Module, Any]

# Usage tips
- Infra type: CPU

# Source code
```
class LoadFooocusInpaint:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'head': (folder_paths.get_filename_list('inpaint'),), 'patch': (folder_paths.get_filename_list('inpaint'),)}}
    RETURN_TYPES = ('INPAINT_PATCH',)
    CATEGORY = 'inpaint'
    FUNCTION = 'load'

    def load(self, head: str, patch: str):
        head_file = folder_paths.get_full_path('inpaint', head)
        inpaint_head_model = InpaintHead()
        sd = torch.load(head_file, map_location='cpu')
        inpaint_head_model.load_state_dict(sd)
        patch_file = folder_paths.get_full_path('inpaint', patch)
        inpaint_lora = comfy.utils.load_torch_file(patch_file, safe_load=True)
        return ((inpaint_head_model, inpaint_lora),)
```