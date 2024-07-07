# Documentation
- Class name: SimpleDetectorForEach
- Category: ImpactPack/Detector
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The SimpleDectorForEach node is designed to test individual images using a border frame (bbox) detector. It processes the input image to identify and locate objects, applying various thresholds and expansion techniques to improve the detection process. The node can be integrated with the semantic perception mask (SAM) model to improve the accuracy of the detection and can also work with the split detector for more detailed analysis. The output is a cluster of sub-objects, each with relevant metadata, such as confidence fractions and boundary frames.

# Input types
## Required
- bbox_detector
    - The bbox_detector parameter is critical to the detection process, as it defines the mechanism for identifying and locating objects in the input image. It plays a key role in the implementation of the node and has a direct impact on the accuracy and quality of the results.
    - Comfy dtype: BBOX_DETECTOR
    - Python dtype: impact.core.BBoxDetector
- image
    - The image parameter is the main input to the SimpleDectorForEach node. It represents the image data that the node will analyse for the object. The quality and resolution of the image directly influences the ability of the node to accurately detect the object.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- bbox_threshold
    - The bbox_threshold parameter is used to set the confidence level for the detection border box. It is a key factor in determining which subjects are considered valid and therefore included in the final output.
    - Comfy dtype: FLOAT
    - Python dtype: float
- bbox_dilation
    - bbox_dilation parameters control the extension of the boundary box detected. This is an important parameter for adjusting the size of the detection area to better fit the actual object.
    - Comfy dtype: INT
    - Python dtype: int
- crop_factor
    - The crop_factor parameter is used to determine the zoom factor for the crop area around the detected object. It affects the size of the crop area and therefore the level of detail in the partition.
    - Comfy dtype: FLOAT
    - Python dtype: float
- drop_size
    - The drop_size parameter specifies the range or step size to be used in the detection process. It affects the particle size of the test and allows nodes to detect objects at different scales.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- sub_threshold
    - The sub_threshold parameter is used to fine-tune the detection process, especially when working with the split detector. It helps with the detection by setting sub-thresholds for object identification.
    - Comfy dtype: FLOAT
    - Python dtype: float
- sub_dilation
    - Sub_dilation parameters allow the partition process to be adjusted by controlling the expansion of the detected partitions. This is particularly useful for fine-tuning the boundaries of the detected objects.
    - Comfy dtype: INT
    - Python dtype: int
- sub_bbox_expansion
    - The sub_bbox_expansion parameter is used to expand the boundary box of the detected object during the split. It helps to ensure that the object is contained in the partition mask.
    - Comfy dtype: INT
    - Python dtype: int
- sam_mask_hint_threshold
    - The sam_mask_hint_threshold parameter is used when integrated with the SAM model to generate a mask. It sets a threshold to create a more accurate mask using the detected partitioned hint.
    - Comfy dtype: FLOAT
    - Python dtype: float
- post_dilation
    - Post_dilation parameters are eventually inflated after the detection process. It can be used to smooth the edges of the mask and ensure better coverage of objects.
    - Comfy dtype: INT
    - Python dtype: int
- sam_model_opt
    - The sam_model_opt parameter is an optional configuration of nodes when using the SAM model to generate a mask. It is specified as a model for creating a more detailed partition of the mask.
    - Comfy dtype: SAM_MODEL
    - Python dtype: impact.core.SAMModel
- segm_detector_opt
    - The segm_detector_opt parameter allows the partition detector to be integrated into the detection process. It provides an option for using a more professional detector for certain types of objects or scenarios.
    - Comfy dtype: SEGM_DETECTOR
    - Python dtype: impact.core.SegmDetector

# Output types
- segs
    - The output parameters of the segs represent the array of sub-objects detected by the node. Each part includes details of the image, the mask, the confidence score, the area of the crop, the boundary box, and the label.
    - Comfy dtype: SEGS
    - Python dtype: Tuple[impact.core.SEG, List[impact.core.SEG]]

# Usage tips
- Infra type: CPU

# Source code
```
class SimpleDetectorForEach:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'bbox_detector': ('BBOX_DETECTOR',), 'image': ('IMAGE',), 'bbox_threshold': ('FLOAT', {'default': 0.5, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'bbox_dilation': ('INT', {'default': 0, 'min': -512, 'max': 512, 'step': 1}), 'crop_factor': ('FLOAT', {'default': 3.0, 'min': 1.0, 'max': 100, 'step': 0.1}), 'drop_size': ('INT', {'min': 1, 'max': MAX_RESOLUTION, 'step': 1, 'default': 10}), 'sub_threshold': ('FLOAT', {'default': 0.5, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'sub_dilation': ('INT', {'default': 0, 'min': -512, 'max': 512, 'step': 1}), 'sub_bbox_expansion': ('INT', {'default': 0, 'min': 0, 'max': 1000, 'step': 1}), 'sam_mask_hint_threshold': ('FLOAT', {'default': 0.7, 'min': 0.0, 'max': 1.0, 'step': 0.01})}, 'optional': {'post_dilation': ('INT', {'default': 0, 'min': -512, 'max': 512, 'step': 1}), 'sam_model_opt': ('SAM_MODEL',), 'segm_detector_opt': ('SEGM_DETECTOR',)}}
    RETURN_TYPES = ('SEGS',)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Detector'

    @staticmethod
    def detect(bbox_detector, image, bbox_threshold, bbox_dilation, crop_factor, drop_size, sub_threshold, sub_dilation, sub_bbox_expansion, sam_mask_hint_threshold, post_dilation=0, sam_model_opt=None, segm_detector_opt=None, detailer_hook=None):
        if len(image) > 1:
            raise Exception('[Impact Pack] ERROR: SimpleDetectorForEach does not allow image batches.\nPlease refer to https://github.com/ltdrdata/ComfyUI-extension-tutorials/blob/Main/ComfyUI-Impact-Pack/tutorial/batching-detailer.md for more information.')
        if segm_detector_opt is not None and hasattr(segm_detector_opt, 'bbox_detector') and (segm_detector_opt.bbox_detector == bbox_detector):
            segs = segm_detector_opt.detect(image, sub_threshold, sub_dilation, crop_factor, drop_size, detailer_hook=detailer_hook)
        else:
            segs = bbox_detector.detect(image, bbox_threshold, bbox_dilation, crop_factor, drop_size, detailer_hook=detailer_hook)
            if sam_model_opt is not None:
                mask = core.make_sam_mask(sam_model_opt, segs, image, 'center-1', sub_dilation, sub_threshold, sub_bbox_expansion, sam_mask_hint_threshold, False)
                segs = core.segs_bitwise_and_mask(segs, mask)
            elif segm_detector_opt is not None:
                segm_segs = segm_detector_opt.detect(image, sub_threshold, sub_dilation, crop_factor, drop_size, detailer_hook=detailer_hook)
                mask = core.segs_to_combined_mask(segm_segs)
                segs = core.segs_bitwise_and_mask(segs, mask)
        segs = core.dilate_segs(segs, post_dilation)
        return (segs,)

    def doit(self, bbox_detector, image, bbox_threshold, bbox_dilation, crop_factor, drop_size, sub_threshold, sub_dilation, sub_bbox_expansion, sam_mask_hint_threshold, post_dilation=0, sam_model_opt=None, segm_detector_opt=None):
        return SimpleDetectorForEach.detect(bbox_detector, image, bbox_threshold, bbox_dilation, crop_factor, drop_size, sub_threshold, sub_dilation, sub_bbox_expansion, sam_mask_hint_threshold, post_dilation=post_dilation, sam_model_opt=sam_model_opt, segm_detector_opt=segm_detector_opt)
```