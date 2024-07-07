# Documentation
- Class name: CLIPSetLastLayer
- Category: conditioning
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

Method `set_last_layer'is designed to modify the last layer of the CLIP model. It allows the output layer of the neural network to be customised to specific needs, ensuring that the model is adapted to different tasks without changing its core structure.

# Input types
## Required
- clip
    - The parameter 'clip' is necessary because it represents the CLIP model that will be modified at the last level. It is the main input, which determines the operation of the node and the subsequent output.
    - Comfy dtype: CLIP
    - Python dtype: torch.nn.Module
- stop_at_clip_layer
    - The parameter'stop_at_clip_layer'specifies the index that the hierarchy of the CLIP model should stop. It plays a key role in determining the ultimate configuration of the model structure.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- modified_clip
    - Output'modified_clip' is the last layer of the CLIP model adjusted to input parameters. It marks the successful application of the node function and achieves the required model configuration.
    - Comfy dtype: CLIP
    - Python dtype: torch.nn.Module

# Usage tips
- Infra type: GPU

# Source code
```
class CLIPSetLastLayer:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'clip': ('CLIP',), 'stop_at_clip_layer': ('INT', {'default': -1, 'min': -24, 'max': -1, 'step': 1})}}
    RETURN_TYPES = ('CLIP',)
    FUNCTION = 'set_last_layer'
    CATEGORY = 'conditioning'

    def set_last_layer(self, clip, stop_at_clip_layer):
        clip = clip.clone()
        clip.clip_layer(stop_at_clip_layer)
        return (clip,)
```