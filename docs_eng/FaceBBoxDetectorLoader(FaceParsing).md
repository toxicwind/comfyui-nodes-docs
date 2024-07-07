# Documentation
- Class name: FaceBBoxDetectorLoader
- Category: face_parsing
- Output node: False
- Repo Ref: https://github.com/Ryuukeisyou/comfyui_face_parsing

The FaceBoxDectorLoader node is designed to load and manage facial detection models that enable input data to be used to identify and locate the face in the image. It encapsulates the functionality of the initializing YOLO-based model, which is essential for subsequent facial-related analytical tasks.

# Input types
## Required
- model_name
    - The model_name parameter is essential for the facial test model to be used in the given node. It determines the structure of the model, thus affecting the accuracy and performance of the test. The selection of the model directly affects the ability of the node to process and analyse facial data.
    - Comfy dtype: COMBO['bbox/face_yolov5s.pt', 'bbox/face_yolov5m.pt', ...]
    - Python dtype: Union[str, List[str]

# Output types
- BBOX_DETECTOR
    - The output of the FacingBoxDector Loader node is a well-positioned facial detection model prepared for use in facial images. This output is very important because it provides the basis for further facial analysis and enables downstream tasks to be performed effectively.
    - Comfy dtype: Tuple[YOLO]
    - Python dtype: Tuple[YOLO]

# Usage tips
- Infra type: CPU

# Source code
```
class FaceBBoxDetectorLoader:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        files = folder_paths.get_filename_list('ultralytics_bbox')
        face_detect_models = list(filter(lambda x: 'face' in x, files))
        bboxs = ['bbox/' + x for x in face_detect_models]
        return {'required': {'model_name': (bboxs, {})}}
    RETURN_TYPES = ('BBOX_DETECTOR',)
    FUNCTION = 'main'
    CATEGORY = 'face_parsing'

    def main(self, model_name):
        model_path = folder_paths.get_full_path('ultralytics', model_name)
        model = YOLO(model_path)
        return (model,)
```