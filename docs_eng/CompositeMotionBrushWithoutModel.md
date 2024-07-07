# Documentation
- Class name: CompositeMotionBrushWithoutModel
- Category: DragNUWA
- Output node: False
- Repo Ref: https://github.com/chaojie/ComfyUI-DragNUWA.git

The node integrates two layers of motor information to produce composite motion brushes. It prioritizes certain layers of motor data integration principles based on a defined operating model.

# Input types
## Required
- motion_brush_layer0
    - The first layer of campaign information is essential as the foundation layer for compound effects. It is essential in the initial expression of the campaign, which will be further refined in conjunction with the second layer.
    - Comfy dtype: MotionBrush
    - Python dtype: numpy.ndarray
- motion_brush_layer1
    - The second layer of motion information provides additional motion clues mixed with the base layer. Its importance is to be able to introduce new motion elements and adjust the overall compound effect.
    - Comfy dtype: MotionBrush
    - Python dtype: numpy.ndarray
- mode
    - Model parameters determine how the two layers of motion information are combined. It is critical in controlling the final output, because it determines which elements of motion are prioritized and how they interact in the complex.
    - Comfy dtype: CompositeMotionBrushMode
    - Python dtype: CompositeMotionBrushMode

# Output types
- results
    - The output represents the final composite motion brush, which mixes the two input layers according to the specified mode. It encapsulates the integrated motion data and is prepared for further processing or visualization.
    - Comfy dtype: MotionBrush
    - Python dtype: numpy.ndarray

# Usage tips
- Infra type: CPU

# Source code
```
class CompositeMotionBrushWithoutModel:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'motion_brush_layer0': ('MotionBrush',), 'motion_brush_layer1': ('MotionBrush',), 'mode': (CompositeMotionBrushMode, {'default': 'override'})}}
    RETURN_TYPES = ('MotionBrush',)
    FUNCTION = 'run_inference'
    CATEGORY = 'DragNUWA'

    def run_inference(self, motion_brush_layer0, motion_brush_layer1, mode):
        model_length = motion_brush_layer0.shape[0]
        height = motion_brush_layer0.shape[1]
        width = motion_brush_layer0.shape[2]
        results = motion_brush_layer0
        for i in range(model_length):
            xmasked = False
            for x in range(0, width):
                xpremasked = xmasked
                xmasked = False
                masked = False
                for y in range(0, height):
                    premasked = masked
                    masked = False
                    if abs(float(motion_brush_layer1[i][y][x][0])) > 0.0001 or abs(float(motion_brush_layer1[i][y][x][1])) > 0.0001:
                        masked = True
                        xmasked = True
                    elif premasked and y + 1 < height:
                        y1max = height
                        if y + 50 < y1max:
                            y1max = y + 50
                        for y1 in range(y + 1, y1max):
                            if abs(float(motion_brush_layer1[i][y1][x][0])) > 0.0001 or abs(float(motion_brush_layer1[i][y1][x][1])) > 0.0001:
                                masked = True
                                xmasked = True
                    if masked:
                        results[i][y][x][0] = motion_brush_layer1[i][y][x][0]
                        results[i][y][x][1] = motion_brush_layer1[i][y][x][1]
                    else:
                        if xpremasked and x + 1 < width:
                            x1max = width
                            if x + 50 < x1max:
                                x1max = x + 50
                            for x1 in range(x + 1, x1max):
                                if abs(float(motion_brush_layer1[i][y][x1][0])) > 0.0001 or abs(float(motion_brush_layer1[i][y][x1][1])) > 0.0001:
                                    masked = True
                                    xmasked = True
                        if masked:
                            results[i][y][x][0] = motion_brush_layer1[i][y][x][0]
                            results[i][y][x][1] = motion_brush_layer1[i][y][x][1]
                        else:
                            results[i][y][x][0] = motion_brush_layer0[i][y][x][0]
                            results[i][y][x][1] = motion_brush_layer0[i][y][x][1]
        return (results,)
```