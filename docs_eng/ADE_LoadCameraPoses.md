# Load CameraCtrl Poses (File) 🎭🅐🅓②
## Documentation
- Class name: ADE_LoadCameraPoses
- Category: Animate Diff 🎭🅐🅓/② Gen2 nodes ②/CameraCtrl/poses
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved.git

`ADE_LoadCameraPoses' node is designed to control the position from the specified file by loading the camera into the position so that it can be manipulated and animated within the Animaté Diff framework. It is used as a basic element for creating dynamic and complex camera movements for animation sequences.

## Input types
### Required
- pose_filename
    - Specifies the name of the file from which you want to load the camera to control the position. This name should be a file containing the required camera position so that nodes can retrieve and use the position to animate it.
    - Comfy dtype: COMBO[STRING]
    - Python dtype: str

## Output types
- cameractrl_poses
    - Comfy dtype: CAMERACTRL_POSES
    - The output of a series of camera control positions, which consist of a list of floating points indicating the position, direction and other relevant parameters of the camera in the context of the animation.
    - Python dtype: list[list[float]]

## Usage tips
- Infra type: CPU
- Common nodes: unknown

## Source code
```python
class LoadCameraPoses:
    @classmethod
    def INPUT_TYPES(s):
        input_dir = folder_paths.get_input_directory()
        files = [f for f in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, f))]
        files = [f for f in files if f.endswith(".txt")]
        return {
            "required": {
                "pose_filename": (sorted(files),),
            }
        }

    RETURN_TYPES = ("CAMERACTRL_POSES",)
    CATEGORY = "Animate Diff 🎭🅐🅓/② Gen2 nodes ②/CameraCtrl/poses"
    FUNCTION = "load_camera_poses"

    def load_camera_poses(self, pose_filename: str):
        file_path = folder_paths.get_annotated_filepath(pose_filename)
        with open(file_path, 'r') as f:
            poses = f.readlines()
        # first line of file is the link to source, so can be skipped,
        # and the rest is a header-less CSV file separated by single spaces
        poses = [pose.strip().split(' ') for pose in poses[1:]]
        poses = [[float(x) for x in pose] for pose in poses]
        poses = set_original_pose_dims(poses, pose_width=CAM.DEFAULT_POSE_WIDTH, pose_height=CAM.DEFAULT_POSE_HEIGHT)
        return (poses,)