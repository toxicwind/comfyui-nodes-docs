# Manual Append CameraCtrl Poses 🎭🅐🅓②
## Documentation
- Class name: ADE_CameraManualPoseAppend
- Category: Animate Diff 🎭🅐🅓/② Gen2 nodes ②/CameraCtrl/poses
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved.git

ADE_CameraManualPoseAppend is used to manually add camera control positions to allow auto-defined and extended camera movements in animations. This node helps to integrate user-defined camera positions and enhances the ability for dynamic visual narratives in animation projects.

## Input types
### Required
- poses_first
    - Specifies the additional initial camera to control the position set. It plays a key role in determining the starting point of the camera movement.
    - Comfy dtype: CAMERACTRL_POSES
    - Python dtype: list[list[float]]
- poses_last
    - Defines the final camera to be added to control the position set. It determines the end of the camera movement and allows seamless transition between camera states.
    - Comfy dtype: CAMERACTRL_POSES
    - Python dtype: list[list[float]]

## Output types
- cameractrl_poses
    - Comfy dtype: CAMERACTRL_POSES
    - The output combination of cameras controls the set of positions, representing the seamless integration of the initial and final positions in order to achieve dynamic camera movement in the animation.
    - Python dtype: list[list[float]]

## Usage tips
- Infra type: CPU
- Common nodes: unknown

## Source code
```python
class CameraCtrlManualAppendPose:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "poses_first": ("CAMERACTRL_POSES",),
                "poses_last": ("CAMERACTRL_POSES",),
            }
        }

    RETURN_TYPES = ("CAMERACTRL_POSES",)
    FUNCTION = "camera_manual_append"
    CATEGORY = "Animate Diff 🎭🅐🅓/② Gen2 nodes ②/CameraCtrl/poses"

    def camera_manual_append(self, poses_first: list[list[float]], poses_last: list[list[float]]):
        return (combine_poses(poses0=poses_first, poses1=poses_last),)