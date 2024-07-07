# Documentation
- Class name: isSDXL
- Category: EasyUse/Logic
- Output node: False
- Repo Ref: https://github.com/yolain/ComfyUI-Easy-Use.git

The node is classified according to the compatibility of the input with the particular model to ensure the correct application of the model in the process.

# Input types
## Optional
- optional_pipe
    - This parameter provides the context of the current water line, which contains the condition phase model, and influences the decision-making process of the nodes.
    - Comfy dtype: COMBO[PIPE_LINE]
    - Python dtype: Dict[str, Any]
- optional_clip
    - This parameter provides an alternative input for nodes to work with the clip model, which is essential for certain operations.
    - Comfy dtype: CLIP
    - Python dtype: Union[SDXLClipModel, SDXLRefinerClipModel, SDXLClipG]

# Output types
- boolean
    - The output indicates the success of the operation, True indicates compatibility, and False indicates a mismatch.
    - Comfy dtype: BOOLEAN
    - Python dtype: Tuple[bool]

# Usage tips
- Infra type: CPU

# Source code
```
class isSDXL:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {}, 'optional': {'optional_pipe': ('PIPE_LINE',), 'optional_clip': ('CLIP',)}}
    RETURN_TYPES = ('BOOLEAN',)
    RETURN_NAMES = ('boolean',)
    FUNCTION = 'execute'
    CATEGORY = 'EasyUse/Logic'

    def execute(self, optional_pipe=None, optional_clip=None):
        if optional_pipe is None and optional_clip is None:
            raise Exception(f'[ERROR] optional_pipe or optional_clip is missing')
        clip = optional_clip if optional_clip is not None else optional_pipe['clip']
        if isinstance(clip.cond_stage_model, (SDXLClipModel, SDXLRefinerClipModel, SDXLClipG)):
            return (True,)
        else:
            return (False,)
```