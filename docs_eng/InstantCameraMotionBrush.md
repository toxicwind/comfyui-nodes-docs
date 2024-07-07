# Documentation
- Class name: InstantCameraMotionBrush
- Category: DragNUWA
- Output node: False
- Repo Ref: https://github.com/chaojie/ComfyUI-DragNUWA.git

InstantCameraMotionBrush is designed to simulate the motion effects of the camera in the virtual environment. This is achieved by generating motion brushes that indicate that the camera moves its trajectory in the frame. The main function of the node is to create dynamic visual expressions of the motion of the camera, such as shifting, scalding and tilting, which can be used to enhance the true sense of the scene or to add artistic effects to later production.

# Input types
## Required
- model_length
    - Model length parameters determine the duration of the sequence of motion of the camera. It is essential to determine the range of motion brushing effects and the manner in which they are carried out over time. Long sequences allow for more complex motion paths, while shorter sequences lead to faster and more sudden movements.
    - Comfy dtype: INT
    - Python dtype: int
- width
    - The width parameters specify the horizontal resolution that will be applied to the motion of the camera. This is important to zoom the motion brush accurately into the size of the scene and to ensure that the motion appears natural and proportionate in the frame context.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - The altitude parameter defines the vertical resolution of the frame. Similar to width, it is important for the correct scaling of motion brushes to fit the frame size, contributing to overall consistency and visual appeal of motion effects.
    - Comfy dtype: INT
    - Python dtype: int
- action
    - The action parameter determines the type of camera movement that you want to simulate. It affects the movement trajectory and the motion brush that will represent the way the camera moves, meeting the different creative needs and narratives in the visual content.
    - Comfy dtype: COMBO
    - Python dtype: str
- speed
    - The velocity parameter adjusts the speed at which the camera moves. It directly affects the intensity and rhythm of the activity, allowing for fine control of the final visual result.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- MotionBrush
    - The output MotionBrush is a measure of the movement trajectory of the computing camera. It contains the essence of the movement of the camera and provides the basis for further processing and integration into the visual work.
    - Comfy dtype: Tensor
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class InstantCameraMotionBrush:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'model_length': ('INT', {'default': 14}), 'width': ('INT', {'default': 576}), 'height': ('INT', {'default': 320}), 'action': (['left', 'right', 'up', 'down', 'zoomin', 'zoomout'], {'default': 'left'}), 'speed': ('FLOAT', {'default': 1})}}
    RETURN_TYPES = ('MotionBrush',)
    FUNCTION = 'run_inference'
    CATEGORY = 'DragNUWA'

    def run_inference(self, model_length, width, height, action, speed):
        motion_brush = torch.zeros(model_length - 1, height, width, 2)
        xmotionbrush = motion_brush[:, :, :, :1]
        ymotionbrush = motion_brush[:, :, :, 1:]
        xcount = 10
        ycount = 10
        if width < xcount:
            xcount = width
        if height < ycount:
            ycount = height
        xratio = width / xcount
        yratio = height / ycount
        model_width = width
        model_height = height
        box = [0, 0, width, height]
        tracking_points = []
        if action == 'zoomin':
            for j in range(ycount - 1):
                for k in range(xcount - 1):
                    item = []
                    for i in range(model_length - 1):
                        xi = int(k * xratio) + i * speed / (width / 2) * (k * xratio - width / 2)
                        yi = int(j * yratio) + i * speed / (height / 2) * (j * yratio - height / 2)
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
                    item = []
                    for i in range(model_length - 1):
                        xi = int(k * xratio) + i * -speed / (width / 2) * (k * xratio - width / 2)
                        yi = int(j * yratio) + i * -speed / (height / 2) * (j * yratio - height / 2)
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
                    item = []
                    for i in range(model_length - 1):
                        xi = int(k * xratio) + i * -speed
                        yi = int(j * yratio)
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
                    item = []
                    for i in range(model_length - 1):
                        xi = int(k * xratio) + i * speed
                        yi = int(j * yratio)
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
                    item = []
                    for i in range(model_length - 1):
                        xi = int(k * xratio)
                        yi = int(j * yratio) + i * -speed
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
                    item = []
                    for i in range(model_length - 1):
                        xi = int(k * xratio)
                        yi = int(j * yratio) + i * speed
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