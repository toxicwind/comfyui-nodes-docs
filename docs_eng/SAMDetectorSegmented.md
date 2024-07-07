# Documentation
- Class name: SAMDetectorSegmented
- Category: ImpactPack/Detector
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

SAMDectorSegmented is designed to detect and divide objects in the image using SAM (separation and shielding) models. It processes the input image and split hints, generating a combination mask and a separate batch, which is essential for further analysis and operation within the ImpactPack framework.

# Input types
## Required
- sam_model
    - The SAM model parameters are essential because they define the machine learning models that will be used to split tasks. They directly affect the ability of nodes to accurately detect and divide objects in the image.
    - Comfy dtype: SAM_MODEL
    - Python dtype: torch.nn.Module
- segs
    - The segs parameter contains partition tips that guide the SAM model to detect specific areas in the image. It plays an important role in improving node performance by concentrating the detection process on areas of interest.
    - Comfy dtype: SEGS
    - Python dtype: List[SEG]
- image
    - The image parameter is the input for node processing. It is the main data source for split and detect tasks and is the basic aspect of the node function.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
## Optional
- detection_hint
    - The detection hint parameter provides a method of fine-tuning the detection process. It allows for the assignment of different detection strategies, which are essential to optimize node performance according to the characteristics of the input image.
    - Comfy dtype: COMBO['center-1', 'horizontal-2', 'vertical-2', 'rect-4', 'diamond-4', 'mask-area', 'mask-points', 'mask-point-bbox', 'none']
    - Python dtype: str
- dilation
    - The inflation parameter is used to control the hidden expansion detected. It may be important to adjust the output of nodes to better adapt to the requirements of subsequent processing steps.
    - Comfy dtype: INT
    - Python dtype: int
- threshold
    - The threshold parameter determines the level of confidence that is considered to be effective. It is a key factor in controlling the balance of accuracy and recall rates in node operations.
    - Comfy dtype: FLOAT
    - Python dtype: float
- bbox_expansion
    - The bbox_expansion parameter allows the extension of the boundary box used in the detection process. This may be useful to ensure that the detected shield covers the entire object of interest.
    - Comfy dtype: INT
    - Python dtype: int
- mask_hint_threshold
    - The mask_hint_threshold parameter is used to set the sensitivity of the mask hint. It affects how the node interprets and responds to the split hint provided, and affects the quality of the partition.
    - Comfy dtype: FLOAT
    - Python dtype: float
- mask_hint_use_negative
    - The mask_hint_use_negative parameter specifies how to use the negative mask hint. It may significantly affect the ability of nodes to distinguish objects from the background of the image.
    - Comfy dtype: COMBO['False', 'Small', 'Outter']
    - Python dtype: str

# Output types
- combined_mask
    - Combined_mask output parameters represent the condensed result of the split process. It is a single mask containing all the detected objects and provides an integrated view of the split result.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor
- batch_masks
    - Match_masks output parameters provide a separate masked array corresponding to each object detected. This allows detailed analysis and operation of each object in the split context.
    - Comfy dtype: MASK
    - Python dtype: List[torch.Tensor]

# Usage tips
- Infra type: GPU

# Source code
```
class SAMDetectorSegmented:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'sam_model': ('SAM_MODEL',), 'segs': ('SEGS',), 'image': ('IMAGE',), 'detection_hint': (['center-1', 'horizontal-2', 'vertical-2', 'rect-4', 'diamond-4', 'mask-area', 'mask-points', 'mask-point-bbox', 'none'],), 'dilation': ('INT', {'default': 0, 'min': -512, 'max': 512, 'step': 1}), 'threshold': ('FLOAT', {'default': 0.93, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'bbox_expansion': ('INT', {'default': 0, 'min': 0, 'max': 1000, 'step': 1}), 'mask_hint_threshold': ('FLOAT', {'default': 0.7, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'mask_hint_use_negative': (['False', 'Small', 'Outter'],)}}
    RETURN_TYPES = ('MASK', 'MASK')
    RETURN_NAMES = ('combined_mask', 'batch_masks')
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Detector'

    def doit(self, sam_model, segs, image, detection_hint, dilation, threshold, bbox_expansion, mask_hint_threshold, mask_hint_use_negative):
        (combined_mask, batch_masks) = core.make_sam_mask_segmented(sam_model, segs, image, detection_hint, dilation, threshold, bbox_expansion, mask_hint_threshold, mask_hint_use_negative)
        return (combined_mask, batch_masks)
```