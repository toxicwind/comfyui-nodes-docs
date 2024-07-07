# Documentation
- Class name: CustomCFGNode
- Category: Animate Diff 🎭🅐🅓/sample settings
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved.git

CustomCfGNode is a node for the creation of a custom control flow map (CFG) for animation and sampling settings. It allows users to define key frames with specific multivalue configurations that determine the behaviour of the sampling process. The node provides users with an advanced interface that allows them to customize the animation process without going into the details of the bottom model operation.

# Input types
## Required
- cfg_multival
    - The cfg_multival parameter is essential to define the multivalue configuration of a given frame in the animation. It determines how the properties of the key frame affect the sampling process. This parameter is essential for achieving the required animation effect and controlling variability in the generation of the sample.
    - Comfy dtype: MULTIVAL
    - Python dtype: Union[float, torch.Tensor]

# Output types
- CUSTOM_CFG
    - Output CUSTOM_CFG represents a custom-defined key frame group used to control the sampling process. It covers multivalue configurations and their corresponding starting percentage, allowing for fine particle size control over the progress of animations and the generation of different samples.
    - Comfy dtype: CUSTOM_CFG
    - Python dtype: CustomCFGKeyframeGroup

# Usage tips
- Infra type: CPU

# Source code
```
class CustomCFGNode:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'cfg_multival': ('MULTIVAL',)}}
    RETURN_TYPES = ('CUSTOM_CFG',)
    CATEGORY = 'Animate Diff 🎭🅐🅓/sample settings'
    FUNCTION = 'create_custom_cfg'

    def create_custom_cfg(self, cfg_multival: Union[float, Tensor]):
        keyframe = CustomCFGKeyframe(cfg_multival=cfg_multival)
        cfg_custom = CustomCFGKeyframeGroup()
        cfg_custom.add(keyframe)
        return (cfg_custom,)
```