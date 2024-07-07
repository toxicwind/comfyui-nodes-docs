# Load AnimateDiff+CameraCtrl Model 🎭🅐🅓②
## Documentation
- Class name: ADE_LoadAnimateDiffModelWithCameraCtrl
- Category: Animate Diff 🎭🅐🅓/② Gen2 nodes ②/CameraCtrl
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved.git

This node is designed to load the AnimatéDiff model with integrated camera control functions, enabling the application of camera motion and adjustments directly within the AnimatéDiff framework. It helps to integrate dynamic camera control parameters into the AnimatéDiff model, thereby enhancing the animation process and achieving more complex visual effects.

## Input types
### Required
- model_name
    - Specifies the name of the motion model that you want to load. It is essential to identify the specific AnimateDiff model that will add camera control.
    - Comfy dtype: COMBO[STRING]
    - Python dtype: str
- camera_ctrl
    - Defines the camera control parameters that you want to inject into the AnimatéDiff model. This input is essential for customizing camera motion and effect in the animation.
    - Comfy dtype: COMBO[STRING]
    - Python dtype: str

### Optional
- ad_settings
    - The optional settings for the AnimateDiff model allow further customization of the animation process.
    - Comfy dtype: AD_SETTINGS
    - Python dtype: dict

## Output types
- MOTION_MODEL
    - Comfy dtype: MOTION_MODEL_ADE
    - A modified AnimatéDiff model incorporating camera control features was prepared for animation missions.
    - Python dtype: MotionModel

## Usage tips
- Infra type: CPU
- Common nodes: unknown

## Source code
```python
class LoadAnimateDiffModelWithCameraCtrl:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "model_name": (get_available_motion_models(),),
                "camera_ctrl": (get_available_motion_models(),),
            },
            "optional": {
                "ad_settings": ("AD_SETTINGS",),
            }
        }

    RETURN_TYPES = ("MOTION_MODEL_ADE",)
    RETURN_NAMES = ("MOTION_MODEL",)
    CATEGORY = "Animate Diff 🎭🅐🅓/② Gen2 nodes ②/CameraCtrl"
    FUNCTION = "load_camera_ctrl"

    def load_camera_ctrl(self, model_name: str, camera_ctrl: str, ad_settings: AnimateDiffSettings=None):
        loaded_motion_model = load_motion_module_gen2(model_name=model_name, motion_model_settings=ad_settings)
        inject_camera_encoder_into_model(motion_model=loaded_motion_model, camera_ctrl_name=camera_ctrl)
        return (loaded_motion_model,)