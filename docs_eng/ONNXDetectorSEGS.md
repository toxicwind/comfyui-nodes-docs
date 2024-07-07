# Documentation
- Class name: BboxDetectorForEach
- Category: ImpactPack/Detector
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The BboxDectorForEach node is designed to detect boundary boxes for each segment of the image. It uses bbox_detector to identify and locate segments based on the threshold and other parameters provided to ensure that only the most relevant parts are detected. The node plays a key role in the segment monitoring workflow, simplifying the process by automating the identification and isolation of specific areas of interest in the image.

# Input types
## Required
- bbox_detector
    - The bbox_detector is the key component of the node and is responsible for the physical detection of the boundary frame in the image. It is essential for the implementation of the node, as it directly affects the accuracy and efficiency of the testing process.
    - Comfy dtype: BBOX_DETECTOR
    - Python dtype: torch.nn.Module
- image
    - The Image parameter is the input data for the node, which bbox_detector uses to perform its detection tasks. It is the basis for node operations, because the quality and resolution of the image can significantly influence the results.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- threshold
    - The threshold parameter determines the sensitivity of bbox_detector in identifying the boundary box. It is an important adjustment factor that can influence the number and accuracy of the detected segments.
    - Comfy dtype: FLOAT
    - Python dtype: float
- dilation
    - The inflation parameter controls the extension of the detected boundary box. It plays an important role in the post-detection process and may enhance the coverage of the detected segment.
    - Comfy dtype: INT
    - Python dtype: int
- crop_factor
    - The crop_factor parameter is used to adjust the size of the crop segment after the test. It is essential to fine-tune the split process to meet specific application needs.
    - Comfy dtype: FLOAT
    - Python dtype: float
- drop_size
    - The drop_size parameter specifies the minimum size of the segment to be considered during the test process. It is essential to filter out noise and irrelevant data, and therefore improves the quality of the test.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- labels
    - Labels parameters allow you to specify the type of segment to be tested. It is an optional but useful feature that can be used to focus on specific interest segments.
    - Comfy dtype: STRING
    - Python dtype: str
- detailer_hook
    - The detailer_hook parameter provides a mechanism for customizing the detected boundary box. It is an advanced feature that can be used to integrate additional processing steps into the testing workflow.
    - Comfy dtype: DETAILER_HOOK
    - Python dtype: Callable

# Output types
- segs
    - The output of the segs contains the parts detected in the image, each of which contains information on its boundary box. This is the main result of node operations and is essential for further analysis or processing.
    - Comfy dtype: SEGS
    - Python dtype: List[impact.core.SEG]

# Usage tips
- Infra type: CPU

# Source code
```
class BboxDetectorForEach:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'bbox_detector': ('BBOX_DETECTOR',), 'image': ('IMAGE',), 'threshold': ('FLOAT', {'default': 0.5, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'dilation': ('INT', {'default': 10, 'min': -512, 'max': 512, 'step': 1}), 'crop_factor': ('FLOAT', {'default': 3.0, 'min': 1.0, 'max': 100, 'step': 0.1}), 'drop_size': ('INT', {'min': 1, 'max': MAX_RESOLUTION, 'step': 1, 'default': 10}), 'labels': ('STRING', {'multiline': True, 'default': 'all', 'placeholder': 'List the types of segments to be allowed, separated by commas'})}, 'optional': {'detailer_hook': ('DETAILER_HOOK',)}}
    RETURN_TYPES = ('SEGS',)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Detector'

    def doit(self, bbox_detector, image, threshold, dilation, crop_factor, drop_size, labels=None, detailer_hook=None):
        if len(image) > 1:
            raise Exception('[Impact Pack] ERROR: BboxDetectorForEach does not allow image batches.\nPlease refer to https://github.com/ltdrdata/ComfyUI-extension-tutorials/blob/Main/ComfyUI-Impact-Pack/tutorial/batching-detailer.md for more information.')
        segs = bbox_detector.detect(image, threshold, dilation, crop_factor, drop_size, detailer_hook)
        if labels is not None and labels != '':
            labels = labels.split(',')
            if len(labels) > 0:
                (segs, _) = segs_nodes.SEGSLabelFilter.filter(segs, labels)
        return (segs,)
```