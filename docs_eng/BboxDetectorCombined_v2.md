# Documentation
- Class name: BboxDetectorCombined
- Category: Detection
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The BboxDectorCombined node is designed to detect and divide objects in the image using a pre-trained border frame detector. It processes the input image to identify interest areas and creates a mask that depicts them. This node is essential for applications that require precise object location and partition, such as monitoring, robotic technology and autonomous systems.

# Input types
## Required
- bbox_detector
    - The bbox_detector parameter is essential for the operation of the node because it provides a pre-training model for the detection of objects in the image. It is a key component that allows the node to accurately identify and locate the object.
    - Comfy dtype: BBOX_DETECTOR
    - Python dtype: torch.nn.Module
- image
    - The Image parameter is the input of node processing to detect and divide objects. It is the basis of the node function, and the performance of the node depends to a large extent on the quality and resolution of the input image.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
## Optional
- threshold
    - The threshold parameter is used to set the confidence level of the object. It plays an important role in filtering false positives and ensuring that only objects with a higher level of confidence are tested.
    - Comfy dtype: FLOAT
    - Python dtype: float
- dilation
    - The dilation parameter should be applied to detect object masks to extend their boundaries. This is useful in fine-tuning the partitions to ensure that the mask covers the object as a whole, even if the edges of the object are not properly detected.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- mask
    - The mask output is a binary image that indicates the split of objects detected in the input image. It is an important result of node operations and provides a clear division of objects for further analysis or processing.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class BboxDetectorCombined(SegmDetectorCombined):

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'bbox_detector': ('BBOX_DETECTOR',), 'image': ('IMAGE',), 'threshold': ('FLOAT', {'default': 0.5, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'dilation': ('INT', {'default': 4, 'min': -512, 'max': 512, 'step': 1})}}

    def doit(self, bbox_detector, image, threshold, dilation):
        mask = bbox_detector.detect_combined(image, threshold, dilation)
        if mask is None:
            mask = torch.zeros((image.shape[2], image.shape[1]), dtype=torch.float32, device='cpu')
        return (mask.unsqueeze(0),)
```