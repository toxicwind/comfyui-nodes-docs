# Documentation
- Class name: ToIPAdapterPipe
- Category: InspirePack/Util
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Inspire-Pack.git

ToIPAdapterPipe is a node designed to promote the integration of image-processing models and adaptors. It organizes data streams through pipes to ensure that images are properly processed by specified models prior to transmission to the next stage. The node is designed to simplify image-processing workflows, improve efficiency, and allow the seamless use of different models in a single pipe.

# Input types
## Required
- ipadapter
    - The ipadapter parameter is essential to the operation of the node because it defines the specific adaptor for pre-processing of the image. It plays a key role in ensuring that the input image is properly formatted and prepared for follow-up model processing in the pipe.
    - Comfy dtype: IPADAPTER
    - Python dtype: torch.nn.Module
- model
    - Model input is essential because it represents the core image processing model to be used at the node. It is the main component of the image conversion required and is essential for the function of the node.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- clip_vision
    - The clip_vision parameter is optional, but it can be used to integrate additional visual-based processing capabilities into the pipeline. It expands the function of nodes to allow more complex and diverse image analysis tasks.
    - Comfy dtype: CLIP_VISION
    - Python dtype: torch.nn.Module
- insightface
    - When providing insightface parameters, you can make nodes include facial recognition in their processing pipes. This is particularly useful for applications that require the identification or validation of individuals through facial characterization.
    - Comfy dtype: INSIGHTFACE
    - Python dtype: torch.nn.Module

# Output types
- IPADAPTER_PIPE
    - The IPADAPTER_PIPE output covers the results of the processing of the data through the node pipe. It represents the completion of the image processing task and is ready for further use or analysis.
    - Comfy dtype: IPADAPTER_PIPE
    - Python dtype: Tuple[torch.nn.Module, torch.nn.Module, torch.nn.Module, Optional[torch.nn.Module], Callable]

# Usage tips
- Infra type: GPU

# Source code
```
class ToIPAdapterPipe:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'ipadapter': ('IPADAPTER',), 'model': ('MODEL',)}, 'optional': {'clip_vision': ('CLIP_VISION',), 'insightface': ('INSIGHTFACE',)}}
    RETURN_TYPES = ('IPADAPTER_PIPE',)
    FUNCTION = 'doit'
    CATEGORY = 'InspirePack/Util'

    def doit(self, ipadapter, model, clip_vision, insightface=None):
        pipe = (ipadapter, model, clip_vision, insightface, lambda x: x)
        return (pipe,)
```