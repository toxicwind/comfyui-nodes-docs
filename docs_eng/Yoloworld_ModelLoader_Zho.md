# Documentation
- Class name: Yoloworld_ModelLoader_Zho
- Category: 🔎YOLOWORLD_ESAM
- Output node: False
- Repo Ref: https://github.com/ZHO-ZHO-ZHO/ComfyUI-YoloWorld-EfficientSAM.git

Yoloword_ModelLoader_Zho class is a YOLO (You Only Look Once) target detection model designed to facilitate loading and initialization of specific applications. It encapsulates the complexity of the model load so that users can easily integrate the YOLO model into their projects without having to delve into the complex details of the model configuration.

# Input types
## Required
- yolo_world_model
    - The parameter ` yoolo_world_model'is essential for specifying the YOLO model variant to be loaded. It determines the specific configuration and pre-training weight to be used at the node, which directly affects the performance and accuracy of the model in the target detection task.
    - Comfy dtype: str
    - Python dtype: str

# Output types
- yolo_world_model
    - Output `yolo_world_model'represents the loaded YOLO model, which is intended for use in target detection missions. It is the final result of node functions and provides a structured interface to interact with models to implement reasoning for new data.
    - Comfy dtype: YOLOWORLDMODEL
    - Python dtype: YOLOWorld

# Usage tips
- Infra type: CPU

# Source code
```
class Yoloworld_ModelLoader_Zho:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'yolo_world_model': (['yolo_world/l', 'yolo_world/m', 'yolo_world/s'],)}}
    RETURN_TYPES = ('YOLOWORLDMODEL',)
    RETURN_NAMES = ('yolo_world_model',)
    FUNCTION = 'load_yolo_world_model'
    CATEGORY = '🔎YOLOWORLD_ESAM'

    def load_yolo_world_model(self, yolo_world_model):
        YOLO_WORLD_MODEL = YOLOWorld(model_id=yolo_world_model)
        return [YOLO_WORLD_MODEL]
```