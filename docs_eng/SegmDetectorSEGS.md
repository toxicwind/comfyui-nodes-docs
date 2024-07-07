# Documentation
- Class name: SegmDetectorForEach
- Category: ImpactPack/Detector
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The SegmDectorForEach node is designed to divide the image for detection and analysis. It uses a partition model to identify different areas in the image and follows a specific detection confidence threshold. The node can handle parameters such as swelling, cropping factors, and the size of the sample to optimize the detection process. It also allows the parts detected based on label list filters to enhance their usefulness in the target analysis landscape.

# Input types
## Required
- segm_detector
    - The segm_detector parameter is essential to the operation of the node because it defines the partition model that will be used to analyse the input image. It plays a central role in the detection process, directly affecting the accuracy and quality of the split results.
    - Comfy dtype: SEGM_DETECTOR
    - Python dtype: torch.nn.Module
- image
    - Image input is essential for the SegmDectorForEach node, as it is the main data source for partitioning the detection. The quality and resolution of the image directly influences the ability of the node to accurately detect and divide different areas within the image.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
## Optional
- threshold
    - Threshold parameters are important for controlling the detection sensitivity of partition models. It determines the minimum confidence level required for a segment to be considered tested, thus influencing the output of nodes.
    - Comfy dtype: FLOAT
    - Python dtype: float
- dilation
    - The inflation parameter is important for the period detected in the reprocessing process. It controls the degree of morphological expansion applied to the segment, which helps to fine-tune the boundary and improve the quality of overall fragmentation.
    - Comfy dtype: INT
    - Python dtype: int
- crop_factor
    - The crop_factor parameter is used to resize the image before dividing the model process. It helps to focus on specific areas of interest in the image and improves the accuracy of the tests.
    - Comfy dtype: FLOAT
    - Python dtype: float
- drop_size
    - The drop_size parameter is related to the resolution of the operation of the control partition model. It can be used to balance the processing speed and the level of detail in the partition results.
    - Comfy dtype: INT
    - Python dtype: int
- labels
    - Labels parameters allow a section to be filtered on the basis of a list of specified paragraph types. It is particularly useful when the analysis needs to focus on a particular interest.
    - Comfy dtype: STRING
    - Python dtype: str
- detailer_hook
    - The detailer_hook parameter provides a mechanism for a customized detection process. It allows the integration of additional functions or reprocessing steps that are specific to user needs.
    - Comfy dtype: DETAILER_HOOK
    - Python dtype: Callable

# Output types
- segs
    - The output segs parameter represents the segment that is detected from the input image. It is the assembly of the segment areas, each with its own attributes and labels, and provides a detailed analysis of the image content.
    - Comfy dtype: SEGS
    - Python dtype: List[torch.Tensor]

# Usage tips
- Infra type: GPU

# Source code
```
class SegmDetectorForEach:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'segm_detector': ('SEGM_DETECTOR',), 'image': ('IMAGE',), 'threshold': ('FLOAT', {'default': 0.5, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'dilation': ('INT', {'default': 10, 'min': -512, 'max': 512, 'step': 1}), 'crop_factor': ('FLOAT', {'default': 3.0, 'min': 1.0, 'max': 100, 'step': 0.1}), 'drop_size': ('INT', {'min': 1, 'max': MAX_RESOLUTION, 'step': 1, 'default': 10}), 'labels': ('STRING', {'multiline': True, 'default': 'all', 'placeholder': 'List the types of segments to be allowed, separated by commas'})}, 'optional': {'detailer_hook': ('DETAILER_HOOK',)}}
    RETURN_TYPES = ('SEGS',)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Detector'

    def doit(self, segm_detector, image, threshold, dilation, crop_factor, drop_size, labels=None, detailer_hook=None):
        if len(image) > 1:
            raise Exception('[Impact Pack] ERROR: SegmDetectorForEach does not allow image batches.\nPlease refer to https://github.com/ltdrdata/ComfyUI-extension-tutorials/blob/Main/ComfyUI-Impact-Pack/tutorial/batching-detailer.md for more information.')
        segs = segm_detector.detect(image, threshold, dilation, crop_factor, drop_size, detailer_hook)
        if labels is not None and labels != '':
            labels = labels.split(',')
            if len(labels) > 0:
                (segs, _) = segs_nodes.SEGSLabelFilter.filter(segs, labels)
        return (segs,)
```