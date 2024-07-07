# Documentation
- Class name: CompositeMotionBrush
- Category: DragNUWA
- Output node: False
- Repo Ref: https://github.com/chaojie/ComfyUI-DragNUWA.git

The node integrates multiple motion layers into a single composite layer, using a mixed algorithm based on a predefined model, giving priority to certain motion vectors, thereby enhancing the overall movement expression.

# Input types
## Required
- model
    - Model parameters define the structural basis of the motor layer and determine the dimensions and length of the input of campaign data, which are essential for the operation of nodes.
    - Comfy dtype: DragNUWA
    - Python dtype: DragNUWA
- motion_brush_layer0
    - This parameter represents the base layer of motor information, which is used as the initial input for the node mixing process and significantly influences the final composite motor output.
    - Comfy dtype: MotionBrush
    - Python dtype: MotionBrush
- motion_brush_layer1
    - The secondary sports layer, which provides additional vectors for consideration during the mixing process, influences the final composite movement by introducing new elements of the movement.
    - Comfy dtype: MotionBrush
    - Python dtype: MotionBrush
- mode
    - This parameter determines the mix strategy used by the node for the integrated motor layer, defaulting to `override', which determines how to prioritize motion vectors in the final output.
    - Comfy dtype: CompositeMotionBrushMode
    - Python dtype: CompositeMotionBrushMode

# Output types
- results
    - The output represents the composite motor layer and provides an enhanced expression of the movement based on the combination of the mode of input to the motor layer.
    - Comfy dtype: MotionBrush
    - Python dtype: MotionBrush

# Usage tips
- Infra type: CPU

# Source code
```
class CompositeMotionBrush:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'model': ('DragNUWA',), 'motion_brush_layer0': ('MotionBrush',), 'motion_brush_layer1': ('MotionBrush',), 'mode': (CompositeMotionBrushMode, {'default': 'override'})}}
    RETURN_TYPES = ('MotionBrush',)
    FUNCTION = 'run_inference'
    CATEGORY = 'DragNUWA'

    def run_inference(self, model, motion_brush_layer0, motion_brush_layer1, mode):
        results = motion_brush_layer0
        for i in range(model.model_length):
            for x in range(0, model.width):
                masked = False
                for y in range(0, model.height):
                    premasked = masked
                    masked = False
                    if abs(float(motion_brush_layer1[i][y][x][0])) > 0.0001 or abs(float(motion_brush_layer1[i][y][x][1])) > 0.0001:
                        masked = True
                    elif premasked and y + 1 < model.height:
                        y1max = model.height
                        if y + 50 < y1max:
                            y1max = y + 50
                        for y1 in range(y + 1, y1max):
                            if abs(float(motion_brush_layer1[i][y1][x][0])) > 0.0001 or abs(float(motion_brush_layer1[i][y1][x][1])) > 0.0001:
                                masked = True
                    if masked:
                        results[i][y][x][0] = motion_brush_layer1[i][y][x][0]
                        results[i][y][x][1] = motion_brush_layer1[i][y][x][1]
                    else:
                        results[i][y][x][0] = motion_brush_layer0[i][y][x][0]
                        results[i][y][x][1] = motion_brush_layer0[i][y][x][1]
        return (results,)
```