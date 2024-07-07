# Documentation
- Class name: ultralyticsDetectorForDetailerFix
- Category: EasyUse/Fix
- Output node: False
- Repo Ref: https://github.com/yolain/ComfyUI-Easy-Use.git

The node is integrated with the Ultralytics detector, which processes border frames and divides data to improve the accuracy and detail of the object detection in the image. It is designed to improve the overall quality of image analysis by adjusting the detection parameters and applying specific processing steps.

# Input types
## Required
- model_name
    - The model_name parameter specifies the source of the monitoring model, which is essential for the operation of the node, as it determines the data to be used for object detection and partitioning.
    - Comfy dtype: COMBO[bboxs, segms]
    - Python dtype: Union[str, List[str]]
- bbox_threshold
    - The bbox_threshold parameter fine-tunes the sensitivity of the border frame detection, affecting the ability of nodes to identify and isolate objects in the image.
    - Comfy dtype: FLOAT
    - Python dtype: float
- bbox_dilation
    - The bbox_dilation parameter resizes the boundary box, which is essential to accurately frame and focus the objects detected.
    - Comfy dtype: INT
    - Python dtype: int
- bbox_crop_factor
    - The bbox_crop_factor parameter influences image cropping around the detected object to ensure that details are captured effectively for further analysis.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- bbox_segm_pipe
    - The output of the node is a flow line that combines refined boundary frames and partition results and provides a comprehensive set of data for detailed image analysis.
    - Comfy dtype: PIPE_LINE
    - Python dtype: Tuple[Any, float, int, float, Any]

# Usage tips
- Infra type: CPU

# Source code
```
class ultralyticsDetectorForDetailerFix:

    @classmethod
    def INPUT_TYPES(s):
        bboxs = ['bbox/' + x for x in folder_paths.get_filename_list('ultralytics_bbox')]
        segms = ['segm/' + x for x in folder_paths.get_filename_list('ultralytics_segm')]
        return {'required': {'model_name': (bboxs + segms,), 'bbox_threshold': ('FLOAT', {'default': 0.5, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'bbox_dilation': ('INT', {'default': 10, 'min': -512, 'max': 512, 'step': 1}), 'bbox_crop_factor': ('FLOAT', {'default': 3.0, 'min': 1.0, 'max': 10, 'step': 0.1})}}
    RETURN_TYPES = ('PIPE_LINE',)
    RETURN_NAMES = ('bbox_segm_pipe',)
    FUNCTION = 'doit'
    CATEGORY = 'EasyUse/Fix'

    def doit(self, model_name, bbox_threshold, bbox_dilation, bbox_crop_factor):
        if 'UltralyticsDetectorProvider' not in ALL_NODE_CLASS_MAPPINGS:
            raise Exception(f"[ERROR] To use UltralyticsDetectorProvider, you need to install 'Impact Pack'")
        cls = ALL_NODE_CLASS_MAPPINGS['UltralyticsDetectorProvider']
        (bbox_detector, segm_detector) = cls().doit(model_name)
        pipe = (bbox_detector, bbox_threshold, bbox_dilation, bbox_crop_factor, segm_detector)
        return (pipe,)
```