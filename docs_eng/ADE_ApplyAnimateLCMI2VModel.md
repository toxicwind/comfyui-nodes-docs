# Apply AnimateLCM-I2V Model 🎭🅐🅓②
## Documentation
- Class name: ADE_ApplyAnimateLCMI2VModel
- Category: Animate Diff 🎭🅐🅓/② Gen2 nodes ②/AnimateLCM-I2V
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved.git

This node is designed to use the AnimatéLCM-I2V model to animate the image by using the underlying code motion reasoning of the I2V function (image to video). It combines motion models and key frame groups, generating dynamic animation visual effects from static images and increasing their motion and effect according to specified parameters.

## Input types
### Required
- motion_model
    - The motion model parameters are essential for defining the properties and dynamics of the movement that will be applied to static images. They influence the implementation of nodes and function by identifying the types of animations and motor effects that will be introduced.
    - Comfy dtype: MOTION_MODEL_ADE
    - Python dtype: MotionModelPatcher
- ref_latent
    - This parameter preserves the reference potential of the image to be animated. It is essential to preserve the original properties of the image in the application of motion effects.
    - Comfy dtype: LATENT
    - Python dtype: dict
- ref_drift
    - Specifies the extent to which the activity deviates from the original image properties and allows subtle or significant changes in animated output.
    - Comfy dtype: FLOAT
    - Python dtype: float
- apply_ref_when_disabled
    - Determines whether reference properties (e.g. drift) are applied even when the motion model is disabled to ensure continuity of the animation process.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- start_percent
    - Defines the starting point of the animation in the motion model time line and allows accurate control of the beginning of the animation effect.
    - Comfy dtype: FLOAT
    - Python dtype: float
- end_percent
    - Sets the end point of the animation in the motion model time line, allowing the duration and end of the animation to be customised.
    - Comfy dtype: FLOAT
    - Python dtype: float

### Optional
- motion_lora
    - A group of motion-specific LoRA settings could be used to further define the animated effects and dynamics.
    - Comfy dtype: MOTION_LORA
    - Python dtype: MotionLoraList
- scale_multival
    - The multiplier of the scaling effect provides additional control over the size and proportion of animated elements.
    - Comfy dtype: MULTIVAL
    - Python dtype: Optional[List[float]]
- effect_multival
    - The multipliers for the various effects provide the ability to provide further self-defined animated visual appearance and dynamics.
    - Comfy dtype: MULTIVAL
    - Python dtype: Optional[List[float]]
- ad_keyframes
    - Designate a key frame group for advanced animation control, allowing detailed customizing of movements and effects over time.
    - Comfy dtype: AD_KEYFRAMES
    - Python dtype: ADKeyframeGroup
- prev_m_models
    - The previously applied group of motion models enables nodes to be constructed or modified on the basis of existing animations to enhance or change effects.
    - Comfy dtype: M_MODELS
    - Python dtype: MotionModelGroup

## Output types
- m_models
    - Comfy dtype: M_MODELS
    - An updated list of motion models, including the latest used models with their configuration animations and effects.
    - Python dtype: MotionModelGroup

## Usage tips
- Infra type: GPU
- Common nodes: unknown

## Source code
```python
class ApplyAnimateLCMI2VModel:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "motion_model": ("MOTION_MODEL_ADE",),
                "ref_latent": ("LATENT",),
                "ref_drift": ("FLOAT", {"default": 0.0, "min": 0.0, "max": 10.0, "step": 0.001}),
                "apply_ref_when_disabled": ("BOOLEAN", {"default": False}),
                "start_percent": ("FLOAT", {"default": 0.0, "min": 0.0, "max": 1.0, "step": 0.001}),
                "end_percent": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 1.0, "step": 0.001}),
            },
            "optional": {
                "motion_lora": ("MOTION_LORA",),
                "scale_multival": ("MULTIVAL",),
                "effect_multival": ("MULTIVAL",),
                "ad_keyframes": ("AD_KEYFRAMES",),
                "prev_m_models": ("M_MODELS",),
            }
        }
    
    RETURN_TYPES = ("M_MODELS",)
    CATEGORY = "Animate Diff 🎭🅐🅓/② Gen2 nodes ②/AnimateLCM-I2V"
    FUNCTION = "apply_motion_model"

    def apply_motion_model(self, motion_model: MotionModelPatcher, ref_latent: dict, ref_drift: float=0.0, apply_ref_when_disabled=False, start_percent: float=0.0, end_percent: float=1.0,
                           motion_lora: MotionLoraList=None, ad_keyframes: ADKeyframeGroup=None,
                           scale_multival=None, effect_multival=None,
                           prev_m_models: MotionModelGroup=None,):
        new_m_models = ApplyAnimateDiffModelNode.apply_motion_model(self, motion_model, start_percent=start_percent, end_percent=end_percent,
                                                                    motion_lora=motion_lora, ad_keyframes=ad_keyframes,
                                                                    scale_multival=scale_multival, effect_multival=effect_multival, prev_m_models=prev_m_models)
        # most recent added model will always be first in list;
        curr_model = new_m_models[0].models[0]
        # confirm that model contains img_encoder
        if curr_model.model.img_encoder is None:
            raise Exception(f"Motion model '{curr_model.model.mm_info.mm_name}' does not contain an img_encoder; cannot be used with Apply AnimateLCM-I2V Model node.")
        curr_model.orig_img_latents = ref_latent["samples"]
        curr_model.orig_ref_drift = ref_drift
        curr_model.orig_apply_ref_when_disabled = apply_ref_when_disabled
        return new_m_models