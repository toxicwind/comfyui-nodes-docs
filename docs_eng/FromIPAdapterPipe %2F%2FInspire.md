# Documentation
- Class name: FromIPAdapterPipe
- Category: InspirePack/Util
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Inspire-Pack.git

The node coordinates the integration process of various components, such as IP adapters, machine learning models and facial recognition systems, in order to simplify data management and analysis in given pipes.

# Input types
## Required
- ipadapter_pipe
    - This parameter is necessary because, as the main input, it contains a series of interconnected elements that nodes will process and use in their operations.
    - Comfy dtype: IPADAPTER_PIPE
    - Python dtype: Tuple[IPADAPTER_PIPE]

# Output types
- ipadapter
    - The key output components, IP adapters, facilitate communication within the system and ensure the efficient transmission of data between different modules.
    - Comfy dtype: IPADAPTER
    - Python dtype: IPADAPTER
- model
    - Model outputs represent machine learning components, which are essential for forecasting and data processing based on learning models.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- clip_vision
    - This output is important for the interpretation of visual data because it uses visual systems to analyse and understand image content.
    - Comfy dtype: CLIP_VISION
    - Python dtype: CLIP_VISION
- insight_face
    - Insight of facial output is essential in facial recognition missions and provides the means to identify and verify individuals on the basis of facial characteristics.
    - Comfy dtype: INSIGHTFACE
    - Python dtype: INSIGHTFACE

# Usage tips
- Infra type: CPU

# Source code
```
class FromIPAdapterPipe:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'ipadapter_pipe': ('IPADAPTER_PIPE',)}}
    RETURN_TYPES = ('IPADAPTER', 'MODEL', 'CLIP_VISION', 'INSIGHTFACE')
    RETURN_NAMES = ('ipadapter', 'model', 'clip_vision', 'insight_face')
    FUNCTION = 'doit'
    CATEGORY = 'InspirePack/Util'

    def doit(self, ipadapter_pipe):
        (ipadapter, model, clip_vision, insightface, _) = ipadapter_pipe
        return (ipadapter, model, clip_vision, insightface)
```