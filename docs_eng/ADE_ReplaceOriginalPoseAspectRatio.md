---

tags:
- Animation
- CameraControl

---

# Replace Orig. Pose Aspect Ratio 🎭🅐🅓②
## Documentation
- Class name: ADE_ReplaceOriginalPoseAspectRatio
- Category: Animate Diff 🎭🅐🅓/② Gen2 nodes ②/CameraCtrl/poses
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved.git

This node is designed to adjust the vertical ratio of the original position within the AnimatéDiff framework, especially for camera control applications. It changes the size of the position to match the new vertical ratio to ensure that animation and visual effects are accurately rendered according to the required spatial dimensions.

## Input types
### Required
- poses
    - A list of positions to adjust. Each position is a list of floating points, representing the space and rotation parameters of the camera control point.
    - Comfy dtype: CAMERACTRL_POSES
    - Python dtype: list[list[float]]
- orig_pose_width
    - The original width of the position will be used to calculate the new vertical ratio.
    - Comfy dtype: INT
    - Python dtype: int
- orig_pose_height
    - The original height of the position will be used to calculate the new vertical ratio.
    - Comfy dtype: INT
    - Python dtype: int

## Output types
- cameractrl_poses
    - Comfy dtype: CAMERACTRL_POSES
    - Applying the adjusted position after the new vertical ratio to prepare for further processing or animation within the AnimatéDiff framework.
    - Python dtype: list[list[float]]

## Usage tips
- Infra type: CPU
- Common nodes: unknown

## Source code
```python
class CameraCtrlSetOriginalAspectRatio:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "poses":("CAMERACTRL_POSES",),
                "orig_pose_width": ("INT", {"default": 1280, "min": 1, "max": BIGMAX}),
                "orig_pose_height": ("INT", {"default": 720, "min": 1, "max": BIGMAX}),
            }
        }
    
    RETURN_TYPES = ("CAMERACTRL_POSES",)
    FUNCTION = "set_aspect_ratio"
    CATEGORY = "Animate Diff 🎭🅐🅓/② Gen2 nodes ②/CameraCtrl/poses"

    def set_aspect_ratio(self, poses: list[list[float]], orig_pose_width: int, orig_pose_height: int):
        return (set_original_pose_dims(poses, pose_width=orig_pose_width, pose_height=orig_pose_height),)