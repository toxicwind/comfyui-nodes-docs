# Create CameraCtrl Poses (Adv.) 🎭🅐🅓②
## Documentation
- Class name: ADE_CameraPoseAdvanced
- Category: Animate Diff 🎭🅐🅓/② Gen2 nodes ②/CameraCtrl/poses
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved.git

ADE_CameraPoseAdvanced is designed to create a high-level camera control position for animations. It allows a combination of motion types and intensity to generate complex camera movements and enhance dynamic visual narratives in animation sequences.

## Input types
### Required
- motion_type1
    - Specifies the first type of camera motion to be applied, affecting the overall camera movement and its visual impact on animation.
    - Comfy dtype: COMBO[STRING]
    - Python dtype: str
- strength1
    - Specifies the strength multiplier of the first type of motion and adjusts the strength of the motion of the camera.
    - Comfy dtype: FLOAT
    - Python dtype: float
- motion_type2
    - The definition of the second type of camera motion helps to increase the complexity and depth of the camera path.
    - Comfy dtype: COMBO[STRING]
    - Python dtype: str
- strength2
    - Defines the strength multiplier for the second type of motion and changes the impact of the camera path.
    - Comfy dtype: FLOAT
    - Python dtype: float
- motion_type3
    - A third type of camera movement was instructed to add another layer of motion to the camera trajectory.
    - Comfy dtype: COMBO[STRING]
    - Python dtype: str
- strength3
    - Indicate the strength multiplier of the third type of motion to change the strength of the camera motion.
    - Comfy dtype: FLOAT
    - Python dtype: float
- motion_type4
    - A fourth type of camera movement is designated to further enrich the movement of the camera and its impact on the scene.
    - Comfy dtype: COMBO[STRING]
    - Python dtype: str
- strength4
    - Specifies the strength multiplier for the fourth type of motion to influence the depth of the camera trajectory.
    - Comfy dtype: FLOAT
    - Python dtype: float
- motion_type5
    - Defines the fifth type of video camera motion and enhances the animation through additional kinetic nuances.
    - Comfy dtype: COMBO[STRING]
    - Python dtype: str
- strength5
    - Defines the strength multipliers for the fifth type of motion, influencing the nuanced differences in the motion of the camera.
    - Comfy dtype: FLOAT
    - Python dtype: float
- motion_type6
    - The sixth type of camera movement is instructed to complete a motor set controlled by a complex camera.
    - Comfy dtype: COMBO[STRING]
    - Python dtype: str
- strength6
    - Indicate the strength multiplier of the sixth type of motion and fine-tune the complexity of the camera movement.
    - Comfy dtype: FLOAT
    - Python dtype: float
- speed
    - Controlling the speed of the camera movement affects the speed at which the camera moves between positions.
    - Comfy dtype: FLOAT
    - Python dtype: float
- frame_length
    - Determine the number of frames to be used for the motion of the camera and define the duration of the movement.
    - Comfy dtype: INT
    - Python dtype: int

### Optional
- prev_poses
    - It is optional. The former camera position, which can be combined with the new motion, allows seamless transitions in animations.
    - Comfy dtype: CAMERACTRL_POSES
    - Python dtype: list[list[float]]

## Output types
- cameractrl_poses
    - Comfy dtype: CAMERACTRL_POSES
    - The resulting camera control position represents the combined effect of the specified motion and parameters on the path of the camera in the animation.
    - Python dtype: list[list[float]]

## Usage tips
- Infra type: CPU
- Common nodes: unknown

## Source code
```python
class CameraCtrlPoseAdvanced:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "motion_type1": (CAM._LIST,),
                "strength1": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 10.0, "step": 0.01}),
                "motion_type2": (CAM._LIST,),
                "strength2": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 10.0, "step": 0.01}),
                "motion_type3": (CAM._LIST,),
                "strength3": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 10.0, "step": 0.01}),
                "motion_type4": (CAM._LIST,),
                "strength4": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 10.0, "step": 0.01}),
                "motion_type5": (CAM._LIST,),
                "strength5": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 10.0, "step": 0.01}),
                "motion_type6": (CAM._LIST,),
                "strength6": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 10.0, "step": 0.01}),
                "speed": ("FLOAT", {"default": 1.0, "min": -100.0, "max": 100.0, "step": 0.01}),
                "frame_length": ("INT", {"default": 16}),
            },
            "optional": {
                "prev_poses": ("CAMERACTRL_POSES",),
            }
        }

    RETURN_TYPES = ("CAMERACTRL_POSES",)
    FUNCTION = "camera_pose_combo"
    CATEGORY = "Animate Diff 🎭🅐🅓/② Gen2 nodes ②/CameraCtrl/poses"

    def camera_pose_combo(self,
                          motion_type1: str, motion_type2: str, motion_type3: str,
                          motion_type4: str, motion_type5: str, motion_type6: str,
                          speed: float, frame_length: int,
                          prev_poses: list[list[float]]=None,
                          strength1=1.0, strength2=1.0, strength3=1.0, strength4=1.0, strength5=1.0, strength6=1.0):
        return CameraCtrlPoseCombo.camera_pose_combo(self,
                                                     motion_type1=motion_type1, motion_type2=motion_type2, motion_type3=motion_type3,
                                                     motion_type4=motion_type4, motion_type5=motion_type5, motion_type6=motion_type6,
                                                     speed=speed, frame_length=frame_length, prev_poses=prev_poses,
                                                     strength1=strength1, strength2=strength2, strength3=strength3,
                                                     strength4=strength4, strength5=strength5, strength6=strength6)