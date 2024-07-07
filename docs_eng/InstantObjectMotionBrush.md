# Documentation
- Class name: InstantObjectMotionBrush
- Category: DragNUWA
- Output node: False
- Repo Ref: https://github.com/chaojie/ComfyUI-DragNUWA.git

InstantObjectMotionBrush is designed to generate motion effects for objects in images or videos. This node identifies the trajectory of the object and applies motion brush effects according to specified parameters to enhance the visual performance of the movement in a creative or real way.

# Input types
## Required
- model_length
    - The length of the model determines the duration of the function and affects the smoothness and detail of the track.
    - Comfy dtype: INT
    - Python dtype: int
- brush_mask
    - A brush mask is essential to define the areas of interest in the image that will apply the effects of the campaign and to ensure accurate control over the application of the effects of the campaign.
    - Comfy dtype: MASK
    - Python dtype: numpy.ndarray
- action
    - Action parameters determine the type of movement to be simulated, such as magnifying, narrowing, moving to the left, moving to the right, moving up or down, which directly affects the visual results of the trajectory and effect of the movement.
    - Comfy dtype: COMBO
    - Python dtype: str
- speed
    - Speed adjusts the speed at which the effects of the movement are implemented, affecting the strength and the trueness of the movement.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- motion_brush
    - The output motion brush represents the calculated track of motion and movement information, which is essential for rendering the final effect of the movement.
    - Comfy dtype: MOTIONBRUSH
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class InstantObjectMotionBrush:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'model_length': ('INT', {'default': 14}), 'brush_mask': ('MASK',), 'action': (['left', 'right', 'up', 'down', 'zoomin', 'zoomout'], {'default': 'left'}), 'speed': ('FLOAT', {'default': 5})}}
    RETURN_TYPES = ('MotionBrush',)
    FUNCTION = 'run_inference'
    CATEGORY = 'DragNUWA'

    def run_inference(self, model_length, brush_mask, action, speed):
        model_width = brush_mask.shape[2]
        model_height = brush_mask.shape[1]
        from torchvision.ops import masks_to_boxes
        boxes = masks_to_boxes(brush_mask)
        box = boxes[0].int().tolist()
        print(f'model_width{model_width}model_height{model_height}box{box}')
        xcount = 10
        ycount = 10
        if box[2] - box[0] < xcount:
            xcount = box[2] - box[0]
        if box[3] - box[1] < ycount:
            ycount = box[3] - box[1]
        xratio = (box[2] - box[0]) / xcount
        yratio = (box[3] - box[1]) / ycount
        tracking_points = []
        if action == 'zoomin':
            for j in range(ycount - 1):
                for k in range(xcount - 1):
                    if not bool(brush_mask[0][box[1] + int(j * yratio)][box[0] + int(k * xratio)]):
                        continue
                    item = []
                    for i in range(model_length - 1):
                        width = box[2] - box[0]
                        height = box[3] - box[1]
                        xi = box[0] + int(k * xratio) + i * speed / (width / 2) * (k * xratio - width / 2)
                        yi = box[1] + int(j * yratio) + i * speed / (height / 2) * (j * yratio - height / 2)
                        if xi > model_width - 1:
                            xi = model_width - 1
                        if yi > model_height - 1:
                            yi = model_height - 1
                        if xi < 0:
                            xi = 0
                        if yi < 0:
                            yi = 0
                        item.append([xi, yi])
                    tracking_points.append(item)
        elif action == 'zoomout':
            for j in range(ycount - 1):
                for k in range(xcount - 1):
                    if not bool(brush_mask[0][box[1] + int(j * yratio)][box[0] + int(k * xratio)]):
                        continue
                    item = []
                    for i in range(model_length - 1):
                        width = box[2] - box[0]
                        height = box[3] - box[1]
                        xi = box[0] + int(k * xratio) + i * -speed / (width / 2) * (k * xratio - width / 2)
                        yi = box[1] + int(j * yratio) + i * -speed / (height / 2) * (j * yratio - height / 2)
                        if xi > model_width - 1:
                            xi = model_width - 1
                        if yi > model_height - 1:
                            yi = model_height - 1
                        if xi < 0:
                            xi = 0
                        if yi < 0:
                            yi = 0
                        item.append([xi, yi])
                    tracking_points.append(item)
        elif action == 'left':
            for j in range(ycount - 1):
                for k in range(xcount - 1):
                    if not bool(brush_mask[0][box[1] + int(j * yratio)][box[0] + int(k * xratio)]):
                        continue
                    item = []
                    for i in range(model_length - 1):
                        width = box[2] - box[0]
                        height = box[3] - box[1]
                        xi = box[0] + int(k * xratio) + i * -speed
                        yi = box[1] + int(j * yratio)
                        if xi > model_width - 1:
                            xi = model_width - 1
                        if yi > model_height - 1:
                            yi = model_height - 1
                        if xi < 0:
                            xi = 0
                        if yi < 0:
                            yi = 0
                        item.append([xi, yi])
                    tracking_points.append(item)
        elif action == 'right':
            for j in range(ycount - 1):
                for k in range(xcount - 1):
                    if not bool(brush_mask[0][box[1] + int(j * yratio)][box[0] + int(k * xratio)]):
                        continue
                    item = []
                    for i in range(model_length - 1):
                        width = box[2] - box[0]
                        height = box[3] - box[1]
                        xi = box[0] + int(k * xratio) + i * speed
                        yi = box[1] + int(j * yratio)
                        if xi > model_width - 1:
                            xi = model_width - 1
                        if yi > model_height - 1:
                            yi = model_height - 1
                        if xi < 0:
                            xi = 0
                        if yi < 0:
                            yi = 0
                        item.append([xi, yi])
                    tracking_points.append(item)
        elif action == 'up':
            for j in range(ycount - 1):
                for k in range(xcount - 1):
                    if not bool(brush_mask[0][box[1] + int(j * yratio)][box[0] + int(k * xratio)]):
                        continue
                    item = []
                    for i in range(model_length - 1):
                        width = box[2] - box[0]
                        height = box[3] - box[1]
                        xi = box[0] + int(k * xratio)
                        yi = box[1] + int(j * yratio) + i * -speed
                        if xi > model_width - 1:
                            xi = model_width - 1
                        if yi > model_height - 1:
                            yi = model_height - 1
                        if xi < 0:
                            xi = 0
                        if yi < 0:
                            yi = 0
                        item.append([xi, yi])
                    tracking_points.append(item)
        elif action == 'down':
            for j in range(ycount - 1):
                for k in range(xcount - 1):
                    if not bool(brush_mask[0][box[1] + int(j * yratio)][box[0] + int(k * xratio)]):
                        continue
                    item = []
                    for i in range(model_length - 1):
                        width = box[2] - box[0]
                        height = box[3] - box[1]
                        xi = box[0] + int(k * xratio)
                        yi = box[1] + int(j * yratio) + i * speed
                        if xi > model_width - 1:
                            xi = model_width - 1
                        if yi > model_height - 1:
                            yi = model_height - 1
                        if xi < 0:
                            xi = 0
                        if yi < 0:
                            yi = 0
                        item.append([xi, yi])
                    tracking_points.append(item)
        motion_brush = load_motionbrush_from_tracking_points_without_model(model_length, model_width, model_height, tracking_points)
        return (motion_brush,)
```