# Documentation
- Class name: LoadMotionBrushFromTrackingPoints
- Category: DragNUWA
- Output node: False
- Repo Ref: https://github.com/chaojie/ComfyUI-DragNUWA.git

The node facilitates the creation of motion brushes by explaining the tracking points, generating vector fields that represent the motion in the sequence.

# Input types
## Required
- tracking_points
    - Tracking points are necessary because they provide source data for motion detection and brush creation and determine the output of nodes.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- MotionBrush
    - The output represents a detailed motion vector field and is essential for visualization and application of motor effects.
    - Comfy dtype: TENSOR
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class LoadMotionBrushFromTrackingPoints:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'model': ('DragNUWA',), 'tracking_points': ('STRING', {'multiline': True, 'default': '[[[25,25],[128,128]]]'})}}
    RETURN_TYPES = ('MotionBrush',)
    FUNCTION = 'run_inference'
    CATEGORY = 'DragNUWA'

    def run_inference(self, model, tracking_points):
        return (model.load_motionbrush_from_tracking_points(tracking_points),)
```