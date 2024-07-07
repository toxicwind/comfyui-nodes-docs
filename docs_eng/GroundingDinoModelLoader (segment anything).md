# Documentation
- Class name: GroundingDinoModelLoader
- Category: segment_anything
- Output node: False
- Repo Ref: https://github.com/storyicon/comfyui_segment_anything

The node is designed to load and prepare a GroupingDino model for image partitioning and understanding. It encapsulates the process of selecting models, loading their configuration and initializing model structures. The node ensures that models are ready for further processing by placing them on appropriate devices and setting them as assessment models.

# Input types
## Required
- model_name
    - Model name parameters are essential because it determines which GroundingDino models are to be loaded for processing. It influences the entire operation by specifying the model structure and its associated weights, which are essential to the performance of the model in the image-separation task.
    - Comfy dtype: list
    - Python dtype: str

# Output types
- GROUNDING_DINO_MODEL
    - The output provides a completely initialized and ready-to-use GroupingDino model. It encapsulates the structure of the model, learns the weight, and prepares for deployment in the image split task, marking its importance in the process.
    - Comfy dtype: model
    - Python dtype: torch.nn.Module

# Usage tips
- Infra type: GPU

# Source code
```
class GroundingDinoModelLoader:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'model_name': (list_groundingdino_model(),)}}
    CATEGORY = 'segment_anything'
    FUNCTION = 'main'
    RETURN_TYPES = ('GROUNDING_DINO_MODEL',)

    def main(self, model_name):
        dino_model = load_groundingdino_model(model_name)
        return (dino_model,)
```