# Apply AnimateDiff Model 🎭🅐🅓②
## Documentation
- Class name: ADE_ApplyAnimateDiffModelSimple
- Category: Animate Diff 🎭🅐🅓/② Gen2 nodes ②
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved.git

This node is designed to apply motion models to animated images or sequences, providing a simplified interface to integrate motion effects. It abstractes the complexity of the animation process and allows users to easily apply predefined motion models to their content.

## Input types
### Required
- motion_model
    - Specifies the motion model that you want to apply. It is essential to define the animated behaviour and effects of the target content.
    - Comfy dtype: MOTION_MODEL_ADE
    - Python dtype: MotionModelPatcher

### Optional
- motion_lora
    - Optional parameters for integrating campaign Lora adjustments to enhance animation effects.
    - Comfy dtype: MOTION_LORA
    - Python dtype: MotionLoraList
- scale_multival
    - Optional parameters are used to scale effects and provide flexibility in application of motion strength.
    - Comfy dtype: MULTIVAL
    - Python dtype: Optional[MultiVal]
- effect_multival
    - Optional parameters are used to adjust effects so that the visual effects of motion are self-defined.
    - Comfy dtype: MULTIVAL
    - Python dtype: Optional[MultiVal]
- ad_keyframes
    - Optional parameters, which specify the key frame, allow for more controlled and accurate animation effects.
    - Comfy dtype: AD_KEYFRAMES
    - Python dtype: Optional[ADKeyframeGroup]

## Output types
- m_models
    - Comfy dtype: M_MODELS
    - The output applied specified motor effects, key frames and adjusted motion models.
    - Python dtype: MotionModelGroup

## Usage tips
- Infra type: GPU
- Common nodes: unknown

## Source code
```python
class ApplyAnimateDiffModelBasicNode:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "motion_model": ("MOTION_MODEL_ADE",),
            },
            "optional": {
                "motion_lora": ("MOTION_LORA",),
                "scale_multival": ("MULTIVAL",),
                "effect_multival": ("MULTIVAL",),
                "ad_keyframes": ("AD_KEYFRAMES",),
            }
        }
    
    RETURN_TYPES = ("M_MODELS",)
    CATEGORY = "Animate Diff 🎭🅐🅓/② Gen2 nodes ②"
    FUNCTION = "apply_motion_model"

    def apply_motion_model(self,
                           motion_model: MotionModelPatcher, motion_lora: MotionLoraList=None,
                           scale_multival=None, effect_multival=None, ad_keyframes=None):
        # just a subset of normal ApplyAnimateDiffModelNode inputs
        return ApplyAnimateDiffModelNode.apply_motion_model(self, motion_model, motion_lora=motion_lora,
                                                            scale_multival=scale_multival, effect_multival=effect_multival,
                                                            ad_keyframes=ad_keyframes)