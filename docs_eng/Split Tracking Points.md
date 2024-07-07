# Documentation
- Class name: SplitTrackingPoints
- Category: DragNUWA
- Output node: True
- Repo Ref: https://github.com/chaojie/ComfyUI-DragNUWA.git

The SpringTrackingPoints node is designed to process and operate tracking points from position key data. It allows for the splitting of tracking points into different entities, making analysis and tracking operations more sophisticated. This node is particularly suitable for applications that require detailed tracking of human motion within defined areas and helps to understand motion patterns in greater detail.

# Input types
## Required
- pose_kps
    - The position key point data is critical for the node, as it is the main input for tracking and analysis. This parameter has a direct impact on the ability of the node to process and divide the tracking point, as well as on the accuracy and reliability of the tracking operation.
    - Comfy dtype: POSE_KEYPOINT
    - Python dtype: List[Dict[str, Union[int, float, List[Union[str, int, float]]]]]
- split_index
    - The split_index parameter controls the partition of the tracking point, allowing for the separation of different entities in the tracking data. This is essential for the proper running of the node and for achieving the desired split of the tracking point.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - The height parameter defines the vertical dimensions of the tracking area, which are important for filtering and processing the tracking points within the specified boundary. It ensures that tracking operations are limited to the relevant area and improves the effectiveness of the node.
    - Comfy dtype: INT
    - Python dtype: int
- width
    - The width parameter sets the horizontal dimensions of the tracking area and plays a key role in the filtering and processing of the tracking point. It is essential to ensure the relevance of the tracking point to the designated area and helps to improve the accuracy and efficiency of the node.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- last_pose_kps
    - Last_pose_kps parameters, when provided, serve as a reference for the initial tracking point and help to track the continuity and consistency of the process. It enhances the ability of nodes to maintain accurate tracking over time.
    - Comfy dtype: POSE_KEYPOINT
    - Python dtype: List[Dict[str, Union[int, float, List[Union[str, int, float]]]]]

# Output types
- tracking_points
    - The tracking_points output, which provides a split track point, indicates that the processed data are packaged in a structured and easily accessible format. This output is essential for further analysis and integration into downstream applications.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class SplitTrackingPoints:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'pose_kps': ('POSE_KEYPOINT',), 'split_index': ('INT', {'default': 0}), 'height': ('INT', {'default': 320}), 'width': ('INT', {'default': 576})}, 'optional': {'last_pose_kps': ('POSE_KEYPOINT', {'default': None})}}
    RETURN_TYPES = ('STRING',)
    RETURN_NAMES = ('tracking_points',)
    FUNCTION = 'split_tracking_points'
    OUTPUT_NODE = True
    CATEGORY = 'DragNUWA'

    def split_tracking_points(self, pose_kps, split_index, height, width, last_pose_kps=None):
        if split_index != 0:
            if last_pose_kps is not None:
                pose_kps[split_index * 14] = last_pose_kps[0]
        trajs = []
        for ipose in range(int(len(pose_kps[split_index * 14]['people'][0]['pose_keypoints_2d']) / 3)):
            traj = []
            for itracking in range(14):
                people = pose_kps[split_index * 14 + itracking]['people']
                if people[0]['pose_keypoints_2d'][ipose * 3 + 2] == 1.0:
                    x = people[0]['pose_keypoints_2d'][ipose * 3]
                    y = people[0]['pose_keypoints_2d'][ipose * 3 + 1]
                    if x <= width and y <= height:
                        traj.append([x, y])
                    else:
                        break
                elif len(traj) > 0:
                    traj.append(traj[len(traj) - 1])
                else:
                    break
        if len(traj) > 0:
            trajs.append(traj)
        return (json.dumps(trajs),)
```