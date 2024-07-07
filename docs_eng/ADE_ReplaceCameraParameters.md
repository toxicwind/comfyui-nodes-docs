# Replace Camera Parameters 🎭🅐🅓②
## Documentation
- Class name: ADE_ReplaceCameraParameters
- Category: Animate Diff 🎭🅐🅓/② Gen2 nodes ②/CameraCtrl/poses
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved.git

This node is intended to modify the camera control parameters in animated or image-processing pipes to allow the camera position to be adjusted to predefined or dynamically generated standards. This function is essential for achieving a specific visual effect, perspective, or animation that requires a particular camera direction or motion.

## Input types
### Required
- poses
    - indicates the parameters of the camera position that you want to modify. It plays a key role in determining the final output, adjusting by specifying the location and direction of the initial camera.
    - Comfy dtype: CAMERACTRL_POSES
    - Python dtype: list[list[float]]
- fx
    - The camera focuses on the x-axis. Adjusting this parameter affects the camera's vision along the x-axis, and thus the angle and scale of the rehearsing scene.
    - Comfy dtype: FLOAT
    - Python dtype: float
- fy
    - Cameras focus on the y-axis. Similar to "fx", this parameter changes the horizon along the y-axis and affects the depth and altitude of the scene.
    - Comfy dtype: FLOAT
    - Python dtype: float
- cx
    - The x-coordinate of the optical center of the camera. Change the level of this value to move the centre of the scene, which can be used to correct or achieve certain visual effects.
    - Comfy dtype: FLOAT
    - Python dtype: float
- cy
    - The y-coordinate of the optical center of the camera. This parameter moves vertically to the centre of the scene, allowing either vertical alignment or simulation of the camera tilt effect.
    - Comfy dtype: FLOAT
    - Python dtype: float

## Output types
- cameractrl_poses
    - Comfy dtype: CAMERACTRL_POSES
    - Change the camera position after applying new camera parameters. This output is essential for downstream processes that rely on the rendering or further processing of the direction of the updated camera.
    - Python dtype: list[list[float]]

## Usage tips
- Infra type: CPU
- Common nodes: unknown

## Source code
```python
class CameraCtrlReplaceCameraParameters:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "poses":("CAMERACTRL_POSES",),
                "fx": ("FLOAT", {"default": CAM.DEFAULT_FX, "min": 0, "max": 1, "step": 0.000000001}),
                "fy": ("FLOAT", {"default": CAM.DEFAULT_FY, "min": 0, "max": 1, "step": 0.000000001}),
                "cx": ("FLOAT", {"default": CAM.DEFAULT_CX, "min": 0, "max": 1, "step": 0.01}),
                "cy": ("FLOAT", {"default": CAM.DEFAULT_CY, "min": 0, "max": 1, "step": 0.01}),
            },
        }
    
    RETURN_TYPES = ("CAMERACTRL_POSES",)
    FUNCTION = "set_camera_parameters"
    CATEGORY = "Animate Diff 🎭🅐🅓/② Gen2 nodes ②/CameraCtrl/poses"

    def set_camera_parameters(self, poses: list[list[float]], fx: float, fy: float, cx: float, cy: float):
        new_poses = copy.deepcopy(poses)
        for pose in new_poses:
            # fx,fy,cx,fy are in indexes 1-4 of the 19-long pose list
            pose[1] = fx
            pose[2] = fy
            pose[3] = cx
            pose[4] = cy
        return (new_poses,)