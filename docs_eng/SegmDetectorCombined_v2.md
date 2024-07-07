# Documentation
- Class name: SegmDetectorCombined
- Category: ImpactPack/Detector
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The SegmDectorCombined node is designed to integrate and detect functions seamlessly. It uses a split detector to process images and generate a binary mask to distinguish objects of interest and background in images. This node is essential for applications that require precise positioning and partitioning, such as in autopilot systems or medical imaging.

# Input types
## Required
- segm_detector
    - The segm_detector parameter is essential because it represents the core model for the task of partitioning and testing. It is essential for the operation of the node, because it directly affects the quality and accuracy of the mask generated.
    - Comfy dtype: SEGM_DETECTOR
    - Python dtype: torch.nn.Module
- image
    - The Image parameter is the input for node processing. It is a basic component because all operations of the node revolve around the analysis and operation of this image to generate the required mask.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
## Optional
- threshold
    - The xreshold parameter is used to control the sensitivity of the test. It plays an important role in determining which objects are identified and included in the final mask, thus influencing the output of the node.
    - Comfy dtype: FLOAT
    - Python dtype: float
- dilation
    - The dilation parameter allows for the extension of the detected object boundary. It is important in fine-tuning the edges of the mask, especially in contexts where precise border demarcation is less critical.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- MASK
    - MASK output is the main result of the SegmDetectorCombined node. It is a binary mask that marks the separation of objects of interest from the rest of the image, which is essential for downstream processing tasks.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class SegmDetectorCombined:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'segm_detector': ('SEGM_DETECTOR',), 'image': ('IMAGE',), 'threshold': ('FLOAT', {'default': 0.5, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'dilation': ('INT', {'default': 0, 'min': -512, 'max': 512, 'step': 1})}}
    RETURN_TYPES = ('MASK',)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Detector'

    def doit(self, segm_detector, image, threshold, dilation):
        mask = segm_detector.detect_combined(image, threshold, dilation)
        if mask is None:
            mask = torch.zeros((image.shape[2], image.shape[1]), dtype=torch.float32, device='cpu')
        return (mask.unsqueeze(0),)
```