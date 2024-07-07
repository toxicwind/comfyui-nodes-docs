# 🧪Inject I2V into AnimateDiff Model 🎭🅐🅓②
## Documentation
- Class name: ADE_InjectI2VIntoAnimateDiffModel
- Category: Animate Diff 🎭🅐🅓/② Gen2 nodes ②/AnimateLCM-I2V/🧪experimental
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved.git

This node is intended to integrate the I2V (Image to Video) model into the AnimatéDiff framework and enhance its functionality by introducing motion models. It serves as a bridge to enrich the AnimatéDiff animation process and to increase the number of motion dynamics, thus enabling more complex and detailed animations to be produced.

## Input types
### Required
- model_name
    - The designation of the name of the motion model to be loaded plays a crucial role in determining the motion dynamics of the animation.
    - Comfy dtype: COMBO[STRING]
    - Python dtype: str
- motion_model
    - The indication that motion model objects are to be injected into the AnimatéDiff model is essential for the application of specific motion dynamics in the animation process.
    - Comfy dtype: MOTION_MODEL_ADE
    - Python dtype: MotionModelPatcher

### Optional
- ad_settings
    - The optional settings of the AnimatéDiff process allow for the self-defined animated appearance and behaviour.
    - Comfy dtype: AD_SETTINGS
    - Python dtype: AnimateDiffSettings

## Output types
- MOTION_MODEL
    - Comfy dtype: MOTION_MODEL_ADE
    - An enhanced AnimateDiff model with I2V functionality was injected and prepared for animation missions.
    - Python dtype: MotionModelPatcher

## Usage tips
- Infra type: CPU
- Common nodes: unknown

## Source code
```python
class LoadAnimateDiffAndInjectI2VNode:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "model_name": (get_available_motion_models(),),
                "motion_model": ("MOTION_MODEL_ADE",),
            },
            "optional": {
                "ad_settings": ("AD_SETTINGS",),
            }
        }
    
    RETURN_TYPES = ("MOTION_MODEL_ADE",)
    RETURN_NAMES = ("MOTION_MODEL",)

    CATEGORY = "Animate Diff 🎭🅐🅓/② Gen2 nodes ②/AnimateLCM-I2V/🧪experimental"
    FUNCTION = "load_motion_model"

    def load_motion_model(self, model_name: str, motion_model: MotionModelPatcher, ad_settings: AnimateDiffSettings=None):
        # make sure model w/ encoder actually has encoder
        if motion_model.model.img_encoder is None:
            raise Exception("Passed-in motion model was expected to have an img_encoder, but did not.")
        # load motion module and motion settings, if included
        loaded_motion_model = load_motion_module_gen2(model_name=model_name, motion_model_settings=ad_settings)
        inject_img_encoder_into_model(motion_model=loaded_motion_model, w_encoder=motion_model)
        return (loaded_motion_model,)