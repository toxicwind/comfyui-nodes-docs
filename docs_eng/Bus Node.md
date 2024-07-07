# Documentation
- Class name: WAS_Bus
- Category: WAS Suite/Utilities
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The SAS_Bus node serves as the central hub for managing and coordinating the various components in the SAS package. It ensures that models, clips and other practical tools are transmitted efficiently between different parts of the system and promotes seamless workflows.

# Input types
## Optional
- bus
    - The "bus " parameter, as a container, holds optional elements such as models, clips, wae, positive and negative. It is essential for the operation of nodes, as it allows the associated components to be tied together, thereby increasing the efficiency of data transmission within the system.
    - Comfy dtype: TUPLE[None, None, None, None, None]
    - Python dtype: Tuple[Optional[Any], Optional[Any], Optional[Any], Optional[Any], Optional[Any]]
- model
    - The "model" parameter is the key to the node function because it represents the core machine learning component. It is used to process and analyse data, and its existence is essential for the success of the node in carrying out its mission.
    - Comfy dtype: MODEL
    - Python dtype: Optional[torch.nn.Module]
- clip
    - The "clip" parameter is important because it involves multimedia aspects of node operations. It is essential for processing and managing video or audio clips, which are often key parts of the process.
    - Comfy dtype: CLIP
    - Python dtype: Optional[Any]
- vae
    - The "vae" parameter is essential for the ability of nodes to perform advanced data processing tasks. It represents a generation model and is essential for the creation and operation of data.
    - Comfy dtype: VAE
    - Python dtype: Optional[Any]
- positive
    - The “positive” parameter plays a crucial role in the ability to deal with the conditions of the node. It provides guidance on the desired outcome and guides the operation of the node towards the achievement of a particular result.
    - Comfy dtype: CONDITIONING
    - Python dtype: Optional[Any]
- negative
    - The "negative" parameter is the key to the ability of node to filter unwanted elements or results. It helps to refine node processing by specifying what should be avoided or excluded in the operation.
    - Comfy dtype: CONDITIONING
    - Python dtype: Optional[Any]

# Output types
- bus
    - The "bus" output covers processed components and provides a structured way of accessing models, clips, vae and condition elements. It is important because it allows organized retrieval and further use of these components.
    - Comfy dtype: TUPLE[MODEL, CLIP, VAE, CONDITIONING, CONDITIONING]
    - Python dtype: Tuple[torch.nn.Module, Any, Any, Any, Any]
- model
    - The "model" output is a processed machine learning component prepared for further analysis or follow-on tasks. It is a key element of node output because it carries computing intelligence derived from input data.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- clip
    - "clip" output represents multimedia data that has been processed or enhanced by nodes. It is important for applications that require audio or video operation and analysis.
    - Comfy dtype: CLIP
    - Python dtype: Any
- vae
    - The "vae" output is a generation model used in node operations. It is important for generating new data examples or performing data enhancement tasks.
    - Comfy dtype: VAE
    - Python dtype: Any
- positive
    - The 'positive' output reflects the guidance used to guide nodes towards desired results. It is essential for applications that require condition-based processing based on specific criteria.
    - Comfy dtype: CONDITIONING
    - Python dtype: Any
- negative
    - " Negative " output means elements that are filtered or excluded by operation of nodes. It is important for applications involving the removal or avoidance of certain data points.
    - Comfy dtype: CONDITIONING
    - Python dtype: Any

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Bus:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {}, 'optional': {'bus': ('BUS',), 'model': ('MODEL',), 'clip': ('CLIP',), 'vae': ('VAE',), 'positive': ('CONDITIONING',), 'negative': ('CONDITIONING',)}}
    RETURN_TYPES = ('BUS', 'MODEL', 'CLIP', 'VAE', 'CONDITIONING', 'CONDITIONING')
    RETURN_NAMES = ('bus', 'model', 'clip', 'vae', 'positive', 'negative')
    FUNCTION = 'bus_fn'
    CATEGORY = 'WAS Suite/Utilities'

    def bus_fn(self, bus=(None, None, None, None, None), model=None, clip=None, vae=None, positive=None, negative=None):
        (bus_model, bus_clip, bus_vae, bus_positive, bus_negative) = bus
        out_model = model or bus_model
        out_clip = clip or bus_clip
        out_vae = vae or bus_vae
        out_positive = positive or bus_positive
        out_negative = negative or bus_negative
        out_bus = (out_model, out_clip, out_vae, out_positive, out_negative)
        if not out_model:
            raise ValueError('Either model or bus containing a model should be supplied')
        if not out_clip:
            raise ValueError('Either clip or bus containing a clip should be supplied')
        if not out_vae:
            raise ValueError('Either vae or bus containing a vae should be supplied')
        return (out_bus, out_model, out_clip, out_vae, out_positive, out_negative)
```