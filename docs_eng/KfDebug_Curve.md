# Documentation
- Class name: KfDebug_Curve
- Category: debug
- Output node: True
- Repo Ref: https://github.com/dmarx/ComfyUI-Keyframed

The node is designed to visualize and analyse the curvature of the key frame path, clearly indicating the smoothness and continuity of the animation. It helps to understand the trajectory and ensure that the movement is as desired, which is essential to maintain the aesthetic and fluidity desired in the final output.

# Input types
## Required
- curve_data
    - This parameter saves numerical data that represent the debugging curve. It is essential because it forms the basis for visualization and analysis, enabling nodes to effectively process and display the features of the curve.
    - Comfy dtype: numpy.ndarray
    - Python dtype: numpy.ndarray

# Output types
- visualized_curve
    - The output is a visual expression of the input curve, which is essential for quick identification of any irregular or improved areas. It provides a tangible way to assess the performance of the curve and make the necessary adjustments.
    - Comfy dtype: PIL.Image
    - Python dtype: PIL.Image

# Usage tips
- Infra type: CPU

# Source code
```
class KfDebug_Curve(KfDebug_Passthrough):
    RETURN_TYPES = ('KEYFRAMED_CURVE',)
```