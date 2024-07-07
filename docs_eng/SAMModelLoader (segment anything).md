# Documentation
- Class name: SAMModelLoader
- Category: segment_anything
- Output node: False
- Repo Ref: https://github.com/storyicon/comfyui_segment_anything

SAMModelLoader Node is responsible for loading and preparing for use in image partitioning tasks. It ensures that the correct model is loaded according to the specified model name, making it a key component of the initial partitioning process.

# Input types
## Required
- model_name
    - The model_name parameter is essential to identify the particular Council Anything Model that you want to load. It guides nodes to the correct model configuration and ensures that appropriate resources are allocated to the task.
    - Comfy dtype: str
    - Python dtype: str

# Output types
- SAM_MODEL
    - SAM_MODEL output, which is intended for image-separation tasks, is the result of node operations and provides a basic model for follow-up steps.
    - Comfy dtype: torch.nn.Module
    - Python dtype: torch.nn.Module

# Usage tips
- Infra type: GPU

# Source code
```
class SAMModelLoader:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'model_name': (list_sam_model(),)}}
    CATEGORY = 'segment_anything'
    FUNCTION = 'main'
    RETURN_TYPES = ('SAM_MODEL',)

    def main(self, model_name):
        sam_model = load_sam_model(model_name)
        return (sam_model,)
```