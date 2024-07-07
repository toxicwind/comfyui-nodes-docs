# Documentation
- Class name: LoadMotionBrushFromTrackingPointsWithoutModel
- Category: DragNUWA
- Output node: False
- Repo Ref: https://github.com/chaojie/ComfyUI-DragNUWA.git

The node abstractes the process by which motion data can be generated from a tracking point without a pre-storage model, and allows users to create motion brushes based on the points provided.

# Input types
## Required
- model_length
    - The length parameters of the model determine the duration of the motion sequence, which is essential for the operation of the node, as it determines the number of frames for the output of the motion brush.
    - Comfy dtype: INT
    - Python dtype: int
- width
    - Width parameters specify the horizontal resolution of motion brushes, which is essential for establishing the spatial context of motion data.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - Altitude parameters define the vertical resolution of the motion brush and play a key role in the node function by determining the spatial dimensions of the output.
    - Comfy dtype: INT
    - Python dtype: int
- tracking_points
    - The tracking point parameter is necessary because it provides raw tracking data for the construction of motion brushes, directly affecting the quality and accuracy of the movement.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- MotionBrush
    - The output MotionBrush is a volume of motion data on the specified duration and spatial dimensions and contains the main function of the node.
    - Comfy dtype: TORCH_TENSOR
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class LoadMotionBrushFromTrackingPointsWithoutModel:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'model_length': ('INT', {'default': 14}), 'width': ('INT', {'default': 36}), 'height': ('INT', {'default': 20}), 'tracking_points': ('STRING', {'multiline': True, 'default': '[[[1,1],[2,2]]]'})}}
    RETURN_TYPES = ('MotionBrush',)
    FUNCTION = 'run_inference'
    CATEGORY = 'DragNUWA'

    def run_inference(self, model_length, width, height, tracking_points):
        tracking_points = json.loads(tracking_points)
        motionbrush = load_motionbrush_from_tracking_points_without_model(model_length, width, height, tracking_points)
        return (motionbrush,)
```