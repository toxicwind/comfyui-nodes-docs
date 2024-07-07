# Documentation
- Class name: BrushMotion
- Category: DragNUWA
- Output node: False
- Repo Ref: https://github.com/chaojie/ComfyUI-DragNUWA.git

The BrushMotion node produces motor effects by dynamically adjusting the visual content through motion data entered according to specified mask scaling and plug-in values.

# Input types
## Required
- model
    - Model parameters are essential and define the infrastructure and characteristics of the campaign effect to be produced.
    - Comfy dtype: DragNUWA
    - Python dtype: torchvision.models.video.DragNUWA
- motion_brush
    - The motion brush parameters are essential for the provision of raw movement data, which will be processed and scaled according to the mask.
    - Comfy dtype: MotionBrush
    - Python dtype: torch.Tensor
- brush_mask
    - The brush mask parameter is important because it determines the motion effect area to be modified to ensure accurate control over visual adjustments.
    - Comfy dtype: MASK
    - Python dtype: numpy.ndarray

# Output types
- results
    - The result parameters contain the final movement effects, showing the movement adjusted to the input mask and model specifications.
    - Comfy dtype: MotionBrush
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class BrushMotion:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'model': ('DragNUWA',), 'motion_brush': ('MotionBrush',), 'brush_mask': ('MASK',)}}
    RETURN_TYPES = ('MotionBrush',)
    FUNCTION = 'run_inference'
    CATEGORY = 'DragNUWA'

    def run_inference(self, model, motion_brush, brush_mask):
        from torchvision.ops import masks_to_boxes
        boxes = masks_to_boxes(brush_mask)
        box = boxes[0].int().tolist()
        print(box)
        xratio = (box[2] - box[0]) / motion_brush.shape[2]
        yratio = (box[3] - box[1]) / motion_brush.shape[1]
        xmotionbrush = motion_brush[:, :, :, :1]
        ymotionbrush = motion_brush[:, :, :, 1:]
        xmotionbrush = xmotionbrush * xratio
        ymotionbrush = ymotionbrush * yratio
        motionbrush = torch.cat([xmotionbrush, ymotionbrush], 3)
        results = torch.zeros(model.model_length - 1, model.height, model.width, 2)
        for i in range(model.model_length - 1):
            temp = F.interpolate(motionbrush[i].unsqueeze(0).permute(0, 3, 1, 2).float(), size=(box[3] - box[1], box[2] - box[0]), mode='bilinear', align_corners=True).squeeze().permute(1, 2, 0)
            for x in range(box[0], box[2]):
                for y in range(box[1], box[3]):
                    if brush_mask[0][y][x]:
                        results[i][y][x][0] = temp[y - box[1]][x - box[0]][0]
                        results[i][y][x][1] = temp[y - box[1]][x - box[0]][1]
        return (results,)
```