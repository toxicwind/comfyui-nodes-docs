# Load AnimateDiff Model 🎭🅐🅓②
## Documentation
- Class name: ADE_LoadAnimateDiffModel
- Category: Animate Diff 🎭🅐🅓/② Gen2 nodes ②
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved.git

This node is designed to load the AnimatéDiff model, which allows for the integration and application of motion models for animation purposes within the AnimatéDiff framework. It serves as the basic component in the animation pipeline, enabling users to take advantage of advanced animation techniques.

## Input types
### Required
- model_name
    - Specifies the name of the motion model that you want to load. This is a key input because it determines which motion model will be used for animation in the AnimatéDiff framework.
    - Comfy dtype: COMBO[STRING]
    - Python dtype: str

### Optional
- ad_settings
    - Optional parameters, allowing for the inclusion of specific animation settings, provide additional customization and control of the animation process.
    - Comfy dtype: AD_SETTINGS
    - Python dtype: AnimateDiffSettings

## Output types
- MOTION_MODEL
    - Comfy dtype: MOTION_MODEL_ADE
    - Output loaded motion models for further processing and application in animated pipes.
    - Python dtype: MotionModelPatcher

## Usage tips
- Infra type: GPU
<!-- - Common nodes:
    - [ADE_ApplyAnimateDiffModel](../../ComfyUI-AnimateDiff-Evolved/Nodes/ADE_ApplyAnimateDiffModel.md) -->

## Source code
```python
class LoadAnimateDiffModelNode:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "model_name": (get_available_motion_models(),),
            },
            "optional": {
                "ad_settings": ("AD_SETTINGS",),
            }
        }

    RETURN_TYPES = ("MOTION_MODEL_ADE",)
    RETURN_NAMES = ("MOTION_MODEL",)
    CATEGORY = "Animate Diff 🎭🅐🅓/② Gen2 nodes ②"
    FUNCTION = "load_motion_model"

    def load_motion_model(self, model_name: str, ad_settings: AnimateDiffSettings=None):
        # load motion module and motion settings, if included
        motion_model = load_motion_module_gen2(model_name=model_name, motion_model_settings=ad_settings)
        return (motion_model,)