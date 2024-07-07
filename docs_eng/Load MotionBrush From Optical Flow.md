# Documentation
- Class name: LoadMotionBrushFromOpticalFlow
- Category: DragNUWA
- Output node: False
- Repo Ref: https://github.com/chaojie/ComfyUI-DragNUWA.git

The node can generate motion brushes from light flow data, enabling users to use motion information for multiple applications such as video processing or animation.

# Input types
## Required
- model
    - Model parameters are essential to the motion brushing process and define the basic structure and parameters of the production process.
    - Comfy dtype: DragNUWA
    - Python dtype: torch.nn.Module
- optical_flow
    - The light flow input is essential for the node, as it provides the campaign information needed to create a motion brush.
    - Comfy dtype: OPTICAL_FLOW
    - Python dtype: torch.Tensor

# Output types
- MotionBrush
    - The output representative produces motion brushes, which encapsify motion information in a structured format.
    - Comfy dtype: MOTION_BRUSH
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class LoadMotionBrushFromOpticalFlow:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'model': ('DragNUWA',), 'optical_flow': ('OPTICAL_FLOW',)}}
    RETURN_TYPES = ('MotionBrush',)
    FUNCTION = 'run_inference'
    CATEGORY = 'DragNUWA'

    def run_inference(self, model, optical_flow):
        return (model.load_motionbrush_from_optical_flow(optical_flow),)
```