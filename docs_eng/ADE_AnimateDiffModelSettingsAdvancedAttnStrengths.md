# 🚫[DEPR] Motion Model Settings (Adv. Attn) 🎭🅐🅓①
## Documentation
- Class name: ADE_AnimateDiffModelSettingsAdvancedAttnStrengths
- Category: 
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved.git

This node is designed to configure the high-level attention intensity in the AnimatéDiff model settings. It allows for fine-tuning the attention mechanisms of the model by adjusting the intensity of the various attention components, thus controlling the animation process in more detail.

## Input types
### Required
- pe_strength
    - Specifies the strength of the position code adjustment to influence the spatial perception of the model.
    - Comfy dtype: FLOAT
    - Python dtype: float
- attn_strength
    - Defines the overall intensity of the attention mechanism and how the impact model focuses on different parts of the input.
    - Comfy dtype: FLOAT
    - Python dtype: float
- attn_q_strength
    - Adjust the intensity of the query components in the attention mechanism and fine-tune the query process of the model.
    - Comfy dtype: FLOAT
    - Python dtype: float
- attn_k_strength
    - Modifys the intensity of the middle-key component of the attention mechanism to influence how the model matches the query and the key.
    - Comfy dtype: FLOAT
    - Python dtype: float
- attn_v_strength
    - Change the intensity of the median component of the attention mechanism to influence the output based on matching queries and keys.
    - Comfy dtype: FLOAT
    - Python dtype: float
- attn_out_weight_strength
    - Control the intensity of the weight of the export of attention, affecting the impact of the final export of attention.
    - Comfy dtype: FLOAT
    - Python dtype: float
- attn_out_bias_strength
    - To adjust the intensity of the concentration output deviation, fine-tuning should be applied to the deviation of the attention output.
    - Comfy dtype: FLOAT
    - Python dtype: float
- other_strength
    - Specify the intensity of other model adjustments directly related to attention and provide broader control over model behaviour.
    - Comfy dtype: FLOAT
    - Python dtype: float
- motion_pe_stretch
    - Defines the stretching factor of the position code in the motion and affects the spatial representation of the motion.
    - Comfy dtype: INT
    - Python dtype: int
- cap_initial_pe_length
    - Limits the length of the initial position code and limits the spatial range from the beginning of the animation.
    - Comfy dtype: INT
    - Python dtype: int
- interpolate_pe_to_length
    - Determines the length of the position code plug value, affecting the spatial resolution over time.
    - Comfy dtype: INT
    - Python dtype: int
- initial_pe_idx_offset
    - Sets the initial deviation of the position code index and adjusts the starting space reference point.
    - Comfy dtype: INT
    - Python dtype: int
- final_pe_idx_offset
    - Sets the final deviation of the position encoded index and adjusts the end of the space reference point.
    - Comfy dtype: INT
    - Python dtype: int

### Optional
- mask_motion_scale
    - The optional volume is used for selective zooming, allowing movement to zoom in different parts of the animation.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor
- min_motion_scale
    - Sets the minimum scale of the movement to ensure the lower limit of the strength of the movement.
    - Comfy dtype: FLOAT
    - Python dtype: float
- max_motion_scale
    - The maximum scale of the movement is set to ensure the upper limit of the strength of the movement.
    - Comfy dtype: FLOAT
    - Python dtype: float

## Output types
- ad_settings
    - Comfy dtype: AD_SETTINGS
    - Returns the advanced attention intensity set of the AnimateDiff model to allow accurate control of the animated process.
    - Python dtype: AnimateDiffSettings

## Usage tips
- Infra type: CPU
- Common nodes: unknown

## Source code
```python
class AnimateDiffModelSettingsAdvancedAttnStrengths:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "pe_strength": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 10.0, "step": 0.0001}),
                "attn_strength": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 10.0, "step": 0.0001}),
                "attn_q_strength": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 10.0, "step": 0.0001}),
                "attn_k_strength": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 10.0, "step": 0.0001}),
                "attn_v_strength": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 10.0, "step": 0.0001}),
                "attn_out_weight_strength": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 10.0, "step": 0.0001}),
                "attn_out_bias_strength": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 10.0, "step": 0.0001}),
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

    def get_motion_model_settings(self, pe_strength: float, attn_strength: float,
                                  attn_q_strength: float,
                                  attn_k_strength: float,
                                  attn_v_strength: float,
                                  attn_out_weight_strength: float,
                                  attn_out_bias_strength: float,
                                  other_strength: float,
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
            attn_q_MULT=attn_q_strength,
            attn_k_MULT=attn_k_strength,
            attn_v_MULT=attn_v_strength,
            attn_out_weight_MULT=attn_out_weight_strength,
            attn_out_bias_MULT=attn_out_bias_strength,
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