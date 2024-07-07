# Documentation
- Class name: ONNXDetectorProvider
- Category: ImpactPack
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The ONNXDectorProvider node is designed to facilitate the loading and provision of an ONNX model for detection tasks. It serves as an interface to integrate an ONNX-based detection model into the workflow, abstractly synthesizing the complexity of the model loading and setting.

# Input types
## Required
- model_name
    - The model_name parameter is essential for identifying a specific ONNX model to load. It ensures that the correct model is used for testing tasks, thus affecting the execution of nodes and the accuracy of the results.
    - Comfy dtype: str
    - Python dtype: str

# Output types
- BBOX_DETECTOR
    - The BBOX_DETECTOR output provides a configured ONNXDetector object to perform object detection tasks. The object covers the function of the ONNX model and is the core component of the detection process.
    - Comfy dtype: ONNXDetector
    - Python dtype: ONNXDetector

# Usage tips
- Infra type: CPU

# Source code
```
class ONNXDetectorProvider:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model_name': (folder_paths.get_filename_list('onnx'),)}}
    RETURN_TYPES = ('BBOX_DETECTOR',)
    FUNCTION = 'load_onnx'
    CATEGORY = 'ImpactPack'

    def load_onnx(self, model_name):
        model = folder_paths.get_full_path('onnx', model_name)
        return (core.ONNXDetector(model),)
```