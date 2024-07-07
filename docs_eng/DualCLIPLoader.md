# Documentation
- Class name: DualCLIPLoader
- Category: advanced/loaders
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The DualCLIPLoader node is designed to efficiently load and manage the double-CLIP (comparison language-image pre-training) model. It focuses on seamless integration of two different CLIP models and promotes their joint operation in the larger system. The node abstracts the complexity of loading and accessing CLIP models, ensuring that users can use them at minimal cost.

# Input types
## Required
- clip_name1
    - Parameter'clip_name1' specifies the first CLIP model to load. It plays a key role in determining the specific model to be used in the system. This parameter directly affects the ability of nodes to access and process the required CLIP model.
    - Comfy dtype: str
    - Python dtype: str
- clip_name2
    - Parameters'clip_name2' specify the second CLIP model to be loaded. Similar to 'clip_name1', it is essential to identify and load the models required. Nodes rely on 'clip_name1' and'clip_name2' to work effectively with the double CLIP model.
    - Comfy dtype: str
    - Python dtype: str

# Output types
- CLIP
    - Output 'CLIP' represents the loaded CLIP model, which can be a combination of images and text embedded. It is important because it allows further processing and analysis in applications and provides the basis for various downstream tasks.
    - Comfy dtype: COMBO[str, torch.Tensor]
    - Python dtype: Tuple[str, torch.Tensor]

# Usage tips
- Infra type: CPU

# Source code
```
class DualCLIPLoader:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'clip_name1': (folder_paths.get_filename_list('clip'),), 'clip_name2': (folder_paths.get_filename_list('clip'),)}}
    RETURN_TYPES = ('CLIP',)
    FUNCTION = 'load_clip'
    CATEGORY = 'advanced/loaders'

    def load_clip(self, clip_name1, clip_name2):
        clip_path1 = folder_paths.get_full_path('clip', clip_name1)
        clip_path2 = folder_paths.get_full_path('clip', clip_name2)
        clip = comfy.sd.load_clip(ckpt_paths=[clip_path1, clip_path2], embedding_directory=folder_paths.get_folder_paths('embeddings'))
        return (clip,)
```