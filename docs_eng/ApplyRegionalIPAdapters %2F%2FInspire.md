# Documentation
- Class name: ApplyRegionalIPAdapters
- Category: InspirePack/Regional
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Inspire-Pack.git

The `ApplyRegionalIPAdapters' node is designed to integrate a set of regional IP adapters and apply them in the given model pipeline. It streamlines the process of enhancing model function by dynamically integrating the various adaptors according to the given area. The node is designed to optimize the performance of the model in relation to the characteristics of a particular region, thereby increasing the accuracy and relevance of model output.

# Input types
## Required
- ipadapter_pipe
    - The `ipadapter_pipe' parameter is the key channel through which the IP adaptor is integrated into the pipe to the node. It contains the necessary components, including the IP adaptor itself, models and other support tools, which are essential for the node to perform its area-appropriate function effectively.
    - Comfy dtype: TUPLE
    - Python dtype: Tuple[IPAdapter, Model, ClipVision, InsightFace, LoraLoader]
## Optional
- regional_ipadapter1
    - The `regional_ipadapter1' parameter allows customizing IP adapters to regional needs. It provides flexibility to better adapt to a given regional context, thereby enhancing the functionality of the model and enhancing the adaptability and effectiveness of nodes.
    - Comfy dtype: REGIONAL_IPADAPTER
    - Python dtype: RegionalIPAdapter

# Output types
- MODEL
    - The output `MODEL' represents a model that has been adapted with a regional IP adapter. It marks the completion of node processing, when the model has become more capable of dealing with region-specific tasks.
    - Comfy dtype: MODEL
    - Python dtype: Model

# Usage tips
- Infra type: CPU

# Source code
```
class ApplyRegionalIPAdapters:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'ipadapter_pipe': ('IPADAPTER_PIPE',), 'regional_ipadapter1': ('REGIONAL_IPADAPTER',)}}
    RETURN_TYPES = ('MODEL',)
    FUNCTION = 'doit'
    CATEGORY = 'InspirePack/Regional'

    def doit(self, **kwargs):
        ipadapter_pipe = kwargs['ipadapter_pipe']
        (ipadapter, model, clip_vision, insightface, lora_loader) = ipadapter_pipe
        del kwargs['ipadapter_pipe']
        for (k, v) in kwargs.items():
            ipadapter_pipe = (ipadapter, model, clip_vision, insightface, lora_loader)
            model = v.doit(ipadapter_pipe)
        return (model,)
```