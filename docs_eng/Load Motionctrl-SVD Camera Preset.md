# Documentation
- Class name: LoadMotionCtrlSVDCameraPreset
- Category: motionctrl
- Output node: False
- Repo Ref: https://github.com/chaojie/ComfyUI-MotionCtrl-SVD.git

The node is designed to preset a predefined camera for motion control in a 3D environment. It enables users to select and apply different camera perspectives to enhance visual narratives or simulations.

# Input types
## Required
- motion_camera
    - The `motion_camera' parameter is essential to the operation of the node because it determines the setting of a specific camera to be loaded. This option can significantly influence the outcome of the movement control process and influence the eventual visualization or simulation.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- POINTS
    - Output 'POINTS' is the preset data for the loaded camera, which contains parameters for the location and direction of the camera. These data are essential for achieving the required movement control effects in the 3D application.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class LoadMotionCtrlSVDCameraPreset:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'motion_camera': (MOTION_CAMERA_OPTIONS,)}}
    RETURN_TYPES = ('STRING',)
    RETURN_NAMES = ('POINTS',)
    FUNCTION = 'load_motion_camera_preset'
    CATEGORY = 'motionctrl'

    def load_motion_camera_preset(self, motion_camera):
        data = '[]'
        comfy_path = os.path.dirname(folder_paths.__file__)
        with open(f'{comfy_path}/custom_nodes/ComfyUI-MotionCtrl-SVD/examples/camera_poses/test_camera_{motion_camera}.json') as f:
            data = f.read()
        return (data,)
```