# Create CameraCtrl Poses 🎭🅐🅓②
## Documentation
- Class name: ADE_CameraPoseBasic
- Category: Animate Diff 🎭🅐🅓/② Gen2 nodes ②/CameraCtrl/poses
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved.git

This node is intended to create a basic camera control position according to the specified type of motion, speed and frame size. It allows the creation of positions that can be used to control the motion and direction of the camera in the 3D environment, leading to dynamic and customized animations.

## Input types
### Required
- motion_type
    - Specifies the type of motion to be applied to the camera to influence the direction and nature of the movement of the camera.
    - Comfy dtype: COMBO[STRING]
    - Python dtype: str
- speed
    - Determine the speed at which the camera moves and allow the rhythm of the animation to be controlled.
    - Comfy dtype: FLOAT
    - Python dtype: float
- frame_length
    - Defines the number of frames for applying the camera movement and sets the duration of the camera movement.
    - Comfy dtype: INT
    - Python dtype: int

### Optional
- prev_poses
    - Selectable. Provides a previous camera position to combine it with the newly created position and achieves a seamless transition between animations.
    - Comfy dtype: CAMERACTRL_POSES
    - Python dtype: list[list[float]]

## Output types
- cameractrl_poses
    - Comfy dtype: CAMERACTRL_POSES
    - The output-generated camera control position is prepared for animation.
    - Python dtype: list[list[float]]

## Usage tips
- Infra type: CPU
- Common nodes: unknown

## Source code
```python
class CameraCtrlPoseBasic:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "motion_type": (CAM._LIST,),
                "speed": ("FLOAT", {"default": 1.0, "min": -100.0, "max": 100.0, "step": 0.01}),
                "frame_length": ("INT", {"default": 16}),
            },
            "optional": {
                "prev_poses": ("CAMERACTRL_POSES",),
            }
        }

    RETURN_TYPES = ("CAMERACTRL_POSES",)
    FUNCTION = "camera_pose_basic"
    CATEGORY = "Animate Diff 🎭🅐🅓/② Gen2 nodes ②/CameraCtrl/poses"

    def camera_pose_basic(self, motion_type: str, speed: float, frame_length: int, prev_poses: list[list[float]]=None):
        motion = CAM.get(motion_type)
        RT = get_camera_motion(motion.rotate, motion.translate, speed, frame_length)
        new_motion = ndarray_to_poses(RT=RT)
        if prev_poses is not None:
            new_motion = combine_poses(prev_poses, new_motion)
        return (new_motion,)