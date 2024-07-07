# Documentation
- Class name: WAS_CLIPSeg_Model_Loader
- Category: WAS Suite/Loaders
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

WAS_CLIPSeg_Model_Loader is a key component of the workflow that aims to efficiently load and integrate CLIPSeg models into the system. It simplifys the initialization of models and ensures that models are correctly set up for follow-on tasks (e.g. image splits). Through the complexity of abstract loading and cache models, the node simplifies the overall operation and enhances user experience.

# Input types
## Required
- model
    - The `model' parameter is essential to specify the CLIPSeg model to be loaded. It guides node to the correct pre-training model, which is essential for the quality of node execution and partition results. It ensures that appropriate resources are allocated and that the model operates as expected in the system.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- clipseg_model
    - The 'clipseg_model' output provides the loaded CLIPSeg model, which is intended to be used for image-separation tasks. It represents the results of node operations and encapsulates the downstream application of the model. This output is important because it makes further processing and analysis possible and serves as a bridge between model loading and actual use.
    - Comfy dtype: CLIPSEG_MODEL
    - Python dtype: Tuple[CLIPSegProcessor, CLIPSegForImageSegmentation]

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_CLIPSeg_Model_Loader:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'model': ('STRING', {'default': 'CIDAS/clipseg-rd64-refined', 'multiline': False})}}
    RETURN_TYPES = ('CLIPSEG_MODEL',)
    RETURN_NAMES = ('clipseg_model',)
    FUNCTION = 'clipseg_model'
    CATEGORY = 'WAS Suite/Loaders'

    def clipseg_model(self, model):
        from transformers import CLIPSegProcessor, CLIPSegForImageSegmentation
        cache = os.path.join(MODELS_DIR, 'clipseg')
        inputs = CLIPSegProcessor.from_pretrained(model, cache_dir=cache)
        model = CLIPSegForImageSegmentation.from_pretrained(model, cache_dir=cache)
        return ((inputs, model),)
```