# Documentation
- Class name: LoadPoseKeyPoints
- Category: DragNUWA
- Output node: False
- Repo Ref: https://github.com/chaojie/ComfyUI-DragNUWA.git

The node is intended to retrieve and disassemble position key data from designated documents to facilitate the analysis and processing of human attitude information in the system.

# Input types
## Required
- file_name
    - The file_name parameter is essential because it identifies the particular document where the attitude key data to be processed at the node are located.
    - Comfy dtype: COMBO[(os.listdir(folder_paths.output_directory), {'default': 'PoseKeypoint_00001.json'})]
    - Python dtype: Union[str, None]

# Output types
- POSE_KEYPOINT
    - The output provides a structured representation of position key point data that allows for further processing and analysis in the system.
    - Comfy dtype: JSON
    - Python dtype: Dict[str, Any]

# Usage tips
- Infra type: CPU

# Source code
```
class LoadPoseKeyPoints:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'file_name': (os.listdir(folder_paths.output_directory), {'default': 'PoseKeypoint_00001.json'})}}
    RETURN_TYPES = ('POSE_KEYPOINT',)
    FUNCTION = 'run'
    CATEGORY = 'DragNUWA'

    def run(self, file_name):
        path = os.path.join(folder_paths.output_directory, file_name)
        with open(path) as fr:
            return (json.load(fr),)
```