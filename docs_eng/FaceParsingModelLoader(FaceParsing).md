# Documentation
- Class name: FaceParsingModelLoader
- Category: face_parsing
- Output node: False
- Repo Ref: https://github.com/Ryuukeisyou/comfyui_face_parsing

FaceParsingModelLoader node aims to efficiently load and use pre-training semantic semantics models specific to facial resolution tasks. It abstractes the complexity of the model’s initialization and allows users to integrate facial resolution functions seamlessly into their applications. The node ensures that the model is correctly exemplified and ready for reasoning, focusing on promoting advanced facial feature extraction without going into the details of the model loading process.

# Input types
## Required
- face_parsing_path
    - The parameter'face_parsing_path' specifies the file path for the pre-training facial resolution model. This path is critical because it guides nodes to load the correct model, enabling subsequent facial resolution tasks. This parameter ensures that the model used is suitable for the intended application, thereby affecting the accuracy and performance of facial resolution operations.
    - Comfy dtype: str
    - Python dtype: str

# Output types
- FACE_PARSING_MODEL
    - The 'FACE_PARSING_MODEL' output provides a loaded pre-training facial dissection model for semantic tasks. This output is important because it represents the main asset extracted from facial features and allows downstream processing and analysis of facial data. The model output ensures that users can access a powerful tool for dissecting and understanding facial structures in images.
    - Comfy dtype: torch.nn.Module
    - Python dtype: torch.nn.Module

# Usage tips
- Infra type: GPU

# Source code
```
class FaceParsingModelLoader:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {}}
    RETURN_TYPES = ('FACE_PARSING_MODEL',)
    FUNCTION = 'main'
    CATEGORY = 'face_parsing'

    def main(self):
        from transformers import AutoModelForSemanticSegmentation
        model = AutoModelForSemanticSegmentation.from_pretrained(face_parsing_path)
        return (model,)
```