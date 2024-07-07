# Documentation
- Class name: Yoloworld_ESAM_DetectorProvider_Zho
- Category: ImpactPack
- Output node: False
- Repo Ref: https://github.com/ZHO-ZHO-ZHO/ComfyUI-YoloWorld-EfficientSAM.git

The node uses a YOLO-based model to detect the specified object in the image and can choose to use ESAM for object partitioning. The node is designed to provide an accurate border frame and split detection to enhance understanding of visual content in the image.

# Input types
## Required
- yolo_world_model
    - The YOLO model is essential for the detection process, as it defines the neural network structure used for object identification in the image.
    - Comfy dtype: YOLOWORLDMODEL
    - Python dtype: YOLOWorldModel
- categories
    - The object categories to be tested are important parameters that guide the testing process to focus on the relevant categories.
    - Comfy dtype: STRING
    - Python dtype: str
- iou_threshold
    - The IoU threshold is a key parameter that affects the accuracy of the tests by controlling the overlap between the predicted boundary box and the true boundary box.
    - Comfy dtype: FLOAT
    - Python dtype: float
- with_class_agnostic_nms
    - This parameter activates the unknown non-significant inhibition of the category, which is important for reducing the overlap detection and improving the accuracy of the results.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
## Optional
- esam_model_opt
    - When the ESAM model option is available, the detection process is enhanced by enabling the separation of detected objects, providing a more detailed analysis of the image content.
    - Comfy dtype: ESAMMODEL
    - Python dtype: ESAMModel

# Output types
- BBOX_DETECTOR
    - The BBOX detector output provides the boundary box of the object detected, which is the basic step in understanding the spatial distribution of the object in the image.
    - Comfy dtype: BBOX_DETECTOR
    - Python dtype: YoloworldBboxDetector
- SEGM_DETECTOR
    - The SEGM detector output provides a partition mask for the detected object, adding an additional level of detail to the analysis by describing the precise boundary of each object.
    - Comfy dtype: SEGM_DETECTOR
    - Python dtype: YoloworldSegmDetector

# Usage tips
- Infra type: GPU

# Source code
```
class Yoloworld_ESAM_DetectorProvider_Zho:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'yolo_world_model': ('YOLOWORLDMODEL',), 'categories': ('STRING', {'default': '', 'placeholder': 'Please enter the objects to be detected separated by commas.', 'multiline': True}), 'iou_threshold': ('FLOAT', {'default': 0.1, 'min': 0, 'max': 1, 'step': 0.01}), 'with_class_agnostic_nms': ('BOOLEAN', {'default': False})}, 'optional': {'esam_model_opt': ('ESAMMODEL',)}}
    RETURN_TYPES = ('BBOX_DETECTOR', 'SEGM_DETECTOR')
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack'

    def doit(self, yolo_world_model, categories, iou_threshold, with_class_agnostic_nms, esam_model_opt=None):
        bbox_detector = YoloworldBboxDetector(yolo_world_model, categories, iou_threshold, with_class_agnostic_nms)
        if esam_model_opt is not None:
            segm_detector = YoloworldSegmDetector(bbox_detector, esam_model_opt)
        else:
            segm_detector = None
        return (bbox_detector, segm_detector)
```