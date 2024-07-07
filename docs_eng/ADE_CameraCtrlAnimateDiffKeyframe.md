# AnimateDiff+CameraCtrl Keyframe 🎭🅐🅓
## Documentation
- Class name: ADE_CameraCtrlAnimateDiffKeyframe
- Category: Animate Diff 🎭🅐🅓/② Gen2 nodes ②/CameraCtrl
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved.git

This node is designed to generate and manage animated key frames containing camera controls, thus creating dynamic and complex video motion within the AnimatéDiff framework. It allows the initial percentage of animation to be specified, multivalued for scaling, effect and camera control, and inherits missing values to ensure continuity between key frames.

## Input types
### Required
- start_percent
    - Specifies the starting percentage of the animation and allows precise control of the time of motion and effect of the camera in the animation.
    - Comfy dtype: FLOAT
    - Python dtype: float

### Optional
- prev_ad_keyframes
    - Optional. Allows the inclusion of previously defined AnimatéDiff key frames, allowing animated drawings to perform more complex sequence chains and layers.
    - Comfy dtype: AD_KEYFRAMES
    - Python dtype: ADKeyframeGroup or None
- scale_multival
    - Optional. Apply the zoom factor to the animation, allowing the animation element to be resized.
    - Comfy dtype: MULTIVAL
    - Python dtype: float or torch.Tensor
- effect_multival
    - Optional. Applying effects to animation, allows for visual enhancement or modification.
    - Comfy dtype: MULTIVAL
    - Python dtype: float or torch.Tensor
- cameractrl_multival
    - Selectable. Specifies multiple values for camera control and allows the creation of complex camera movements in animations.
    - Comfy dtype: MULTIVAL
    - Python dtype: float or torch.Tensor
- inherit_missing
    - Determine whether the missing values in the current key frame should be inherited from the preceding key frame to ensure the continuity of the animation.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- guarantee_steps
    - Specifies the minimum number of steps guaranteed in the animation to ensure a degree of smoothness and continuity.
    - Comfy dtype: INT
    - Python dtype: int

## Output types
- ad_keyframes
    - Comfy dtype: AD_KEYFRAMES
    - Generate a series of AnimatéDiff key frames, making animation complex video motion.
    - Python dtype: ADKeyframeGroup

## Usage tips
- Infra type: CPU
- Common nodes: unknown

## Source code
```python
class CameraCtrlADKeyframeNode:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "start_percent": ("FLOAT", {"default": 0.0, "min": 0.0, "max": 1.0, "step": 0.001}, ),
            },
            "optional": {
                "prev_ad_keyframes": ("AD_KEYFRAMES", ),
                "scale_multival": ("MULTIVAL",),
                "effect_multival": ("MULTIVAL",),
                "cameractrl_multival": ("MULTIVAL",),
                "inherit_missing": ("BOOLEAN", {"default": True}, ),
                "guarantee_steps": ("INT", {"default": 1, "min": 0, "max": BIGMAX}),
            }
        }
    
    RETURN_TYPES = ("AD_KEYFRAMES", )
    FUNCTION = "load_keyframe"

    CATEGORY = "Animate Diff 🎭🅐🅓/② Gen2 nodes ②/CameraCtrl"

    def load_keyframe(self,
                      start_percent: float, prev_ad_keyframes=None,
                      scale_multival: Union[float, torch.Tensor]=None, effect_multival: Union[float, torch.Tensor]=None,
                      cameractrl_multival: Union[float, torch.Tensor]=None,
                      inherit_missing: bool=True, guarantee_steps: int=1):
        return ADKeyframeNode.load_keyframe(self,
                    start_percent=start_percent, prev_ad_keyframes=prev_ad_keyframes,
                    scale_multival=scale_multival, effect_multival=effect_multival, cameractrl_multival=cameractrl_multival,
                    inherit_missing=inherit_missing, guarantee_steps=guarantee_steps
                )