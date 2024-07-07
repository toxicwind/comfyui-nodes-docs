# Documentation
- Class name: BboxDetectorForEach
- Category: ImpactPack/Detector
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The BboxDectorForEach node is designed to detect boundary frames for each segment of the image using a specified detector. It uses a given threshold to process the image and applies inflation to fine-tune the detection. The node also allows customization through parameters such as tailoring factors and reducing sizes, so that users can adjust the testing to their specific needs. It contributes to the overall partition process by identifying and isolating interested areas in the image.

# Input types
## Required
- bbox_detector
    - The bbox_detector parameter is essential for the BboxDetectorForEach node, as it defines the detector that will be used to identify the boundary box within the image. It plays a key role in the execution of the node and in the accuracy of the test results.
    - Comfy dtype: BBOX_DETECTOR
    - Python dtype: torch.nn.Module
- image
    - The image parameter is the basic input for the BboxDectorForEach node, which represents the visual data that will be processed for the border frame test. It is the main source of information for node operations, with direct effect on the results.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- threshold
    - The threshold parameter is essential to control the sensitivity of the border frame detection. It determines the detector's level of identification of potential bands and affects the ability of nodes to distinguish between relevant and unrelated areas in the image.
    - Comfy dtype: FLOAT
    - Python dtype: float
- dilation
    - An inflated parameter is important for fine-tuning the detected boundary frame by expanding the boundary. It allows for adjustments in the size and shape of the detected segment, which are particularly useful when processing different resolution images or requiring higher-level details.
    - Comfy dtype: INT
    - Python dtype: int
- crop_factor
    - Crops the factor parameters to influence the part of the image that is used for testing. It can be used to focus on specific areas of interest in the image or to exclude unrelated areas, thereby improving the efficiency and accuracy of the detection process.
    - Comfy dtype: FLOAT
    - Python dtype: float
- drop_size
    - The drop_size parameter determines the size of the segment that is discarded during the testing process. It is a key factor in controlling the particle size, allowing a balance to be struck between the number of segments detected and the computational resources required.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- labels
    - The Labors parameter allows users to specify the type of segment in which they are interested. It allows for selective testing by filtering those that do not need it. It streamlines subsequent processing steps and focuses on the most important parts of the image.
    - Comfy dtype: STRING
    - Python dtype: str
- detailer_hook
    - The detailer_hook parameter provides a mechanism for customizing the detection process using additional details or reprocessing steps. It is particularly useful for integrating nodes with other systems or applying the logic of a particular area to the test results.
    - Comfy dtype: DETAILER_HOOK
    - Python dtype: Callable

# Output types
- segs
    - The segs output represents the sum of the segments detected in the image. It is the main result of the operation of the BboxDetectorForEach node and contains the boundary boxes and related metadata for each segment.
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