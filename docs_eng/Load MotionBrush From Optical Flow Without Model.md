# Documentation
- Class name: LoadMotionBrushFromOpticalFlowWithoutModel
- Category: DragNUWA
- Output node: False
- Repo Ref: https://github.com/chaojie/ComfyUI-DragNUWA.git

The node helps interpret light flow data to generate motion brush effects, which are essential for visual simulation and effect generation and are not dependent on pre-training models.

# Input types
## Required
- optical_flow
    - The light flow data are essential because it provides the basic information needed to extrapolate motion patterns and create motion brushing effects.
    - Comfy dtype: OPTICAL_FLOW
    - Python dtype: numpy.ndarray

# Output types
- MotionBrush
    - The output represents the synthetic motion brush, which contains the mode of motion extrapolated from the light flow data.
    - Comfy dtype: MOTION_BRUSH
    - Python dtype: tuple

# Usage tips
- Infra type: CPU

# Source code
```
class LoadMotionBrushFromOpticalFlowWithoutModel:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'optical_flow': ('OPTICAL_FLOW',)}}
    RETURN_TYPES = ('MotionBrush',)
    FUNCTION = 'run_inference'
    CATEGORY = 'DragNUWA'

    def run_inference(self, optical_flow):
        return (optical_flow,)
```