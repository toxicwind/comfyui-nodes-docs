# Documentation
- Class name: LoadMotionTrajPreset
- Category: motionctrl
- Output node: False
- Repo Ref: https://github.com/chaojie/ComfyUI-MotionCtrl.git

The LoadMotionTrajPreset node is designed to load and process predefined track tracks for motion control applications. It accepts specific trajectory presets and frame lengths, then reads and zooms out of text files to match the length of frames required to ensure seamless integration with the motion control system.

# Input types
## Required
- motion_traj
    - The movement_traj parameter specifies the predefined name of the trajectory to be loaded. It is essential to determine the specific mode of movement that the node will address.
    - Comfy dtype: STRING
    - Python dtype: str
- frame_length
    - The frame_legth parameter allows the user to define the number of frames of the motion trajectory. This is important for adjusting the movement to the duration of the animation or simulation.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- POINTS
    - POINTS output contains a list of processed points representing the movement trajectory, which is prepared for downstream motion control processes.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class LoadMotionTrajPreset:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'motion_traj': (MOTION_TRAJ_OPTIONS,), 'frame_length': ('INT', {'default': 16})}}
    RETURN_TYPES = ('STRING',)
    RETURN_NAMES = ('POINTS',)
    FUNCTION = 'load_motion_traj_preset'
    CATEGORY = 'motionctrl'

    def load_motion_traj_preset(self, motion_traj, frame_length):
        comfy_path = os.path.dirname(folder_paths.__file__)
        points = read_points(f'{comfy_path}/custom_nodes/ComfyUI-MotionCtrl/examples/trajectories/{motion_traj}.txt', frame_length)
        return (json.dumps(points),)
```