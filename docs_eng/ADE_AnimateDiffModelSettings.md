# 🚫[DEPR] Motion Model Settings (Advanced) 🎭🅐🅓①
## Documentation
- Class name: ADE_AnimateDiffModelSettings
- Category: 
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved.git

This node is designed to configure the motion model settings of the AnimatéDiff process, allowing users to fine-tune the motion scale parameters to achieve the required animation effect.

## Input types
### Required
- pe_strength
    - Determines the intensity of position coding adjustments and influences the spatial dynamics of animations.
    - Comfy dtype: FLOAT
    - Python dtype: float
- attn_strength
    - Controls the intensity of attention adjustment and influences the focus and detail of animated elements.
    - Comfy dtype: FLOAT
    - Python dtype: float
- other_strength
    - Adjust the intensity of other model parameters to provide additional customization for animating effects.
    - Comfy dtype: FLOAT
    - Python dtype: float
- motion_pe_stretch
    - Specifies the degree of stretching of the position code, changing the time scale of the movement.
    - Comfy dtype: INT
    - Python dtype: int
- cap_initial_pe_length
    - Limits the length of the initial position encoding and sets the starting scale of the movement.
    - Comfy dtype: INT
    - Python dtype: int
- interpolate_pe_to_length
    - Defines the target length of the position code plug value, affecting the smoothness and fluidity of the animation.
    - Comfy dtype: INT
    - Python dtype: int
- initial_pe_idx_offset
    - Sets the initial position encoded index deviation and adjusts the starting point of the animation.
    - Comfy dtype: INT
    - Python dtype: int
- final_pe_idx_offset
    - Determines the final location code index deviation, affecting the animated endpoint.
    - Comfy dtype: INT
    - Python dtype: int

### Optional
- mask_motion_scale
    - Selective use of masks to zoom in different parts of the image enhances the authenticity and complexity of animations.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor
- min_motion_scale
    - Sets the minimum measure of the motion to ensure that the animation does not fall below this threshold.
    - Comfy dtype: FLOAT
    - Python dtype: float
- max_motion_scale
    - Defines the maximum measure of motion and limits the intensity of animated effects.
    - Comfy dtype: FLOAT
    - Python dtype: float

## Output types
- ad_settings
    - Comfy dtype: AD_SETTINGS
    - Output configured motion model settings, including adjustments to motion scale parameters.
    - Python dtype: AnimateDiffSettings

## Usage tips
- Infra type: CPU
- Common nodes: unknown

## Source code
```python
class AnimateDiffModelSettingsAdvanced:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "pe_strength": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 10.0, "step": 0.0001}),
                "attn_strength": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 10.0, "step": 0.0001}),
                "other_strength": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 10.0, "step": 0.0001}),
                "motion_pe_stretch": ("INT", {"default": 0, "min": 0, "step": 1}),
                "cap_initial_pe_length": ("INT", {"default": 0, "min": 0, "step": 1}),
                "interpolate_pe_to_length": ("INT", {"default": 0, "min": 0, "step": 1}),
                "initial_pe_idx_offset": ("INT", {"default": 0, "min": 0, "step": 1}),
                "final_pe_idx_offset": ("INT", {"default": 0, "min": 0, "step": 1}),
            },
            "optional": {
                "mask_motion_scale": ("MASK",),
                "min_motion_scale": ("FLOAT", {"default": 1.0, "min": 0.0, "step": 0.001}),
                "max_motion_scale": ("FLOAT", {"default": 1.0, "min": 0.0, "step": 0.001}),
            }
        }
    
    RETURN_TYPES = ("AD_SETTINGS",)
    CATEGORY = ""  #"Animate Diff 🎭🅐🅓/① Gen1 nodes ①/motion settings/experimental"
    FUNCTION = "get_motion_model_settings"

    def get_motion_model_settings(self, pe_strength: float, attn_strength: float, other_strength: float,
                                  motion_pe_stretch: int,
                                  cap_initial_pe_length: int, interpolate_pe_to_length: int,
                                  initial_pe_idx_offset: int, final_pe_idx_offset: int,
                                  mask_motion_scale: torch.Tensor=None, min_motion_scale: float=1.0, max_motion_scale: float=1.0):
        adjust_pe = AdjustGroup(AdjustPE(motion_pe_stretch=motion_pe_stretch,
                             cap_initial_pe_length=cap_initial_pe_length, interpolate_pe_to_length=interpolate_pe_to_length,
                             initial_pe_idx_offset=initial_pe_idx_offset, final_pe_idx_offset=final_pe_idx_offset))
        adjust_weight = AdjustGroup(AdjustWeight(
            pe_MULT=pe_strength,
            attn_MULT=attn_strength,
            other_MULT=other_strength,
        ))
        motion_model_settings = AnimateDiffSettings(
            adjust_pe=adjust_pe,
            adjust_weight=adjust_weight,
            mask_attn_scale=mask_motion_scale,
            mask_attn_scale_min=min_motion_scale,
            mask_attn_scale_max=max_motion_scale,
        )

        return (motion_model_settings,)