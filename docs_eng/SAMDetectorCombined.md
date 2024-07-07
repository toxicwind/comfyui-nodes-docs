# Documentation
- Class name: SAMDetectorCombined
- Category: ImpactPack/Detector
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

SAMDectorCombined node is designed to detect and divide objects in images using SAM (Segment Anything Model). It uses the specified SAM model, split hints and other parameters to process the input image to create a mask for the object that has been sampled. This node is essential for applications that require precise physical location and partition, such as in computer visual and image analysis missions.

# Input types
## Required
- sam_model
    - The SAM model parameter is essential for the operation of the node because it defines the model that will be used to detect and divide objects. The selection of the node directly affects the ability to accurately identify and divide objects in the image.
    - Comfy dtype: SAM_MODEL
    - Python dtype: torch.nn.Module
- segs
    - The segs parameters provide partition tips that guide the SAM model to detect a particular area in the image. These tips are essential to improve the accuracy of the split process, especially in complex scenarios with multiple objects.
    - Comfy dtype: SEGS
    - Python dtype: List[impact.core.SEG]
- image
    - The image parameter is the input of the node, which is necessary for the detection process. The quality and resolution of the image directly influences the performance of the node in the detection and separation of objects.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
## Optional
- detection_hint
    - The detection hint parameter allows you to specify the type of detection strategy to be used. It affects how the SAM model interprets and processes the split tips, and thus affects the results of the object's detection.
    - Comfy dtype: COMBO['center-1', 'horizontal-2', 'vertical-2', 'rect-4', 'diamond-4', 'mask-area', 'mask-points', 'mask-point-bbox', 'none']
    - Python dtype: str
- dilation
    - The inflation parameter is used to control the extension of the boundary box around the detected object. It plays an important role in the reprocessing of the partition mask, which may improve its coverage of the object.
    - Comfy dtype: INT
    - Python dtype: int
- threshold
    - The threshold parameter is essential for determining the confidence level that the object is considered to be detected. It directly affects the sensitivity of the node to identify the object in the image.
    - Comfy dtype: FLOAT
    - Python dtype: float
- bbox_expansion
    - The bbox_expansion parameter defines the extension of the boundary box to be applied to the object detected. This helps to adjust the closeness of the partition mask around the object.
    - Comfy dtype: INT
    - Python dtype: int
- mask_hint_threshold
    - The mask_hint_threshold parameter is used to set the threshold for using the mask hint in the split. It affects the reliance of node on the mask hint when identifying the object boundary.
    - Comfy dtype: FLOAT
    - Python dtype: float
- mask_hint_use_negative
    - The mask_hint_use_negative parameter determines how negative hints are used in the split. It enhances the ability of nodes to distinguish objects from background.
    - Comfy dtype: COMBO['False', 'Small', 'Outter']
    - Python dtype: str

# Output types
- MASK
    - The MASK output provides the ultimate partition mask after the detection and partition process. It is a key output for further analysis or for downstream tasks requiring object separation.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class SAMDetectorCombined:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'sam_model': ('SAM_MODEL',), 'segs': ('SEGS',), 'image': ('IMAGE',), 'detection_hint': (['center-1', 'horizontal-2', 'vertical-2', 'rect-4', 'diamond-4', 'mask-area', 'mask-points', 'mask-point-bbox', 'none'],), 'dilation': ('INT', {'default': 0, 'min': -512, 'max': 512, 'step': 1}), 'threshold': ('FLOAT', {'default': 0.93, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'bbox_expansion': ('INT', {'default': 0, 'min': 0, 'max': 1000, 'step': 1}), 'mask_hint_threshold': ('FLOAT', {'default': 0.7, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'mask_hint_use_negative': (['False', 'Small', 'Outter'],)}}
    RETURN_TYPES = ('MASK',)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Detector'

    def doit(self, sam_model, segs, image, detection_hint, dilation, threshold, bbox_expansion, mask_hint_threshold, mask_hint_use_negative):
        return (core.make_sam_mask(sam_model, segs, image, detection_hint, dilation, threshold, bbox_expansion, mask_hint_threshold, mask_hint_use_negative),)
```