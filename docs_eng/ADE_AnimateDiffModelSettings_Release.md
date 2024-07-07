# 🚫[DEPR] Motion Model Settings 🎭🅐🅓①
## Documentation
- Class name: ADE_AnimateDiffModelSettings_Release
- Category: 
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved.git

This node is designed to configure the motion model settings of the AnimatéDiff process, with an emphasis on high-level attention intensity adjustments. It is designed to provide users with the ability to fine-tune the animation effects applied through the AnimatéDiff framework.

## Input types
### Required
- min_motion_scale
    - Specifies the minimum measure of motion that affects the fineness or intensity of the animated effect.
    - Comfy dtype: FLOAT
    - Python dtype: float
- max_motion_scale
    - Define the maximum measure of motion, the impact of which can be applied to the intensity of the motion for animation.
    - Comfy dtype: FLOAT
    - Python dtype: float

### Optional
- mask_motion_scale
    - A masked mass allows movement to zoom in with fine control over the different areas entered.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

## Output types
- ad_settings
    - Comfy dtype: AD_SETTINGS
    - The output is the configuration set of the AnimateDiff model, which contains adjustments to the motion scale and potential other parameters.
    - Python dtype: AnimateDiffSettings

## Usage tips
- Infra type: CPU
- Common nodes: unknown

## Source code
```python
class AnimateDiffModelSettings:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "min_motion_scale": ("FLOAT", {"default": 1.0, "min": 0.0, "step": 0.001}),
                "max_motion_scale": ("FLOAT", {"default": 1.0, "min": 0.0, "step": 0.001}),
            },
            "optional": {
                "mask_motion_scale": ("MASK",),
            }
        }
    
    RETURN_TYPES = ("AD_SETTINGS",)
    CATEGORY = ""  #"Animate Diff 🎭🅐🅓/① Gen1 nodes ①/motion settings"
    FUNCTION = "get_motion_model_settings"

    def get_motion_model_settings(self, mask_motion_scale: torch.Tensor=None, min_motion_scale: float=1.0, max_motion_scale: float=1.0):
        motion_model_settings = AnimateDiffSettings(
            mask_attn_scale=mask_motion_scale,
            mask_attn_scale_min=min_motion_scale,
            mask_attn_scale_max=max_motion_scale,
            )

        return (motion_model_settings,)