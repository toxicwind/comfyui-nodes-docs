
# Custom CFG Keyframe 🎭🅐🅓
## Documentation
- Class name: ADE_CustomCFGKeyframe
- Category: Animate Diff 🎭🅐🅓/sample settings
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved.git

ADE_CustomCFKeyframe nodes are designed to create and manage custom configuration key frames within the Animaté Diff framework. It allows animating parameters to be specified on animated time lines, so that the animated behaviour and appearance are precisely controlled.

## Input types
### Required
- cfg_multival
    - Defines the configuration value of the key frame, which influences all aspects of the animation process. It is essential for customizing the animated properties at a given time.
    - Comfy dtype: MULTIVAL
    - Python dtype: Union[float, torch.Tensor]
- start_percent
    - Specifies the starting point of the key frame in the animated time line, expressed as a percentage, allowing accurate time control.
    - Comfy dtype: FLOAT
    - Python dtype: float
- guarantee_steps
    - Determine the minimum number of steps to apply the key frame configuration to ensure a certain duration of impact.
    - Comfy dtype: INT
    - Python dtype: int

### Optional
- prev_custom_cfg
    - A complex animation sequence is achieved by designating a previous custom configuration group to allow a custom configuration of chain connections to the key frame.
    - Comfy dtype: CUSTOM_CFG
    - Python dtype: CustomCFGKeyframeGroup or None

## Output types
- custom_cfg
    - Comfy dtype: CUSTOM_CFG
    - Outputs a custom configuration object that defines the key frame and is prepared to be integrated into animated pipes.
    - Python dtype: CustomCFGKeyframeGroup

## Usage tips
- Infra type: CPU
- Common nodes: unknown

## Source code
```python
class CustomCFGKeyframeNode:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "cfg_multival": ("MULTIVAL",),
                "start_percent": ("FLOAT", {"default": 0.0, "min": 0.0, "max": 1.0, "step": 0.001}),
                "guarantee_steps": ("INT", {"default": 1, "min": 0, "max": BIGMAX}),
            },
            "optional": {
                "prev_custom_cfg": ("CUSTOM_CFG",),
            }
        }

    RETURN_TYPES = ("CUSTOM_CFG",)
    CATEGORY = "Animate Diff 🎭🅐🅓/sample settings"
    FUNCTION = "create_custom_cfg"

    def create_custom_cfg(self, cfg_multival: Union[float, Tensor], start_percent: float=0.0, guarantee_steps: int=1,
                          prev_custom_cfg: CustomCFGKeyframeGroup=None):
        if not prev_custom_cfg:
            prev_custom_cfg = CustomCFGKeyframeGroup()
        prev_custom_cfg = prev_custom_cfg.clone()
        keyframe = CustomCFGKeyframe(cfg_multival=cfg_multival, start_percent=start_percent, guarantee_steps=guarantee_steps)
        prev_custom_cfg.add(keyframe)
        return (prev_custom_cfg,)