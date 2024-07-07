# Documentation
- Class name: UltraalyticsDetectorProvider
- Category: ImpactPack
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The UltraalyticsDetectorProvider node is designed to facilitate the loading and use of object testing models provided by Ultraalytics. It abstracts the complexity of initialization of models and allows users to easily perform border frames and split tests. The node emphasizes seamless integration of detection functions into a broader system, providing an advanced interface for detection tasks, without the need for in-depth knowledge of the bottom model architecture or the reasoning process.

# Input types
## Required
- model_name
    - The model_name parameter is essential to specify which of the pre-trained YOLO models will be loaded for object detection tasks. Its value determines the configuration of the model and the type of detection that the node will perform (border frame or split). This parameter directly affects the execution of the node and the quality of the test results.
    - Comfy dtype: str
    - Python dtype: str

# Output types
- BBOX_DETECTOR
    - The BBOX_DETECTOR output provides a detector object that is specifically designed to identify and locate objects in images through border frames. It encapsulates the function of performing the detection, is the key component of the object's detection of the waterline, and provides a structured method for obtaining and using the results.
    - Comfy dtype: UltraBBoxDetector
    - Python dtype: UltraBBoxDetector
- SEGM_DETECTOR
    - The SEGM_DETECTOR output provides a detector object that not only locates the object in the image, but also provides a partition mask. This output is important for applications that require a more detailed understanding of the shape and boundaries of the object and provides a comprehensive detection solution, including split functions.
    - Comfy dtype: UltraSegmDetector
    - Python dtype: UltraSegmDetector

# Usage tips
- Infra type: GPU

# Source code
```
class UltralyticsDetectorProvider:

    @classmethod
    def INPUT_TYPES(s):
        bboxs = ['bbox/' + x for x in folder_paths.get_filename_list('ultralytics_bbox')]
        segms = ['segm/' + x for x in folder_paths.get_filename_list('ultralytics_segm')]
        return {'required': {'model_name': (bboxs + segms,)}}
    RETURN_TYPES = ('BBOX_DETECTOR', 'SEGM_DETECTOR')
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack'

    def doit(self, model_name):
        model_path = folder_paths.get_full_path('ultralytics', model_name)
        model = subcore.load_yolo(model_path)
        if model_name.startswith('bbox'):
            return (subcore.UltraBBoxDetector(model), core.NO_SEGM_DETECTOR())
        else:
            return (subcore.UltraBBoxDetector(model), subcore.UltraSegmDetector(model))
```