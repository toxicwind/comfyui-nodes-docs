# Documentation
- Class name: FaceParsingProcessorLoader
- Category: face_parsing
- Output node: False
- Repo Ref: https://github.com/Ryuukeisyou/comfyui_face_parsing

FaceParsingProcessorLoader is a node for loading and initializing facial resolution processors. It gives an abstract view of the complexity of setting facial resolution models to allow users to integrate facial resolution functions seamlessly into their applications without having to go into the bottom model architecture or pre-processing steps.

# Input types
## Required
- face_parsing_path
    - The face_parsing_path parameter is essential for the FaceParsingProcessorLoader node, as it assigns the location of the loaded facial resolution processor. This path is essential for the model files and configuration required for node access to facial resolution operations.
    - Comfy dtype: "str"
    - Python dtype: str

# Output types
- processor
    - The output of the FaceParsingProcessorLoader node is a processor object that has been initialised and ready for facial resolution. This processor covers the pre-processed images required for facial resolution models, making them easier for developers to use.
    - Comfy dtype: SegformerImageProcessor
    - Python dtype: transformers.SegformerImageProcessor

# Usage tips
- Infra type: CPU

# Source code
```
class FaceParsingProcessorLoader:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {}}
    RETURN_TYPES = ('FACE_PARSING_PROCESSOR',)
    FUNCTION = 'main'
    CATEGORY = 'face_parsing'

    def main(self):
        from transformers import SegformerImageProcessor
        processor = SegformerImageProcessor.from_pretrained(face_parsing_path)
        return (processor,)
```