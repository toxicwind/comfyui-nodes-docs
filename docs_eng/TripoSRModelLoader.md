# Documentation
- Class name: TripoSRModelLoader
- Category: Flowty TripoSR
- Output node: False
- Repo Ref: https://github.com/flowtyone/ComfyUI-Flowty-TripoSR

TripoSRModelLoader aims to efficiently manage and initialize the TripoSR model, ensuring that it is properly loaded with the specified configuration and resources. It abstractes the complexity of the model loading and setting, providing a direct interface to users to access the model function.

# Input types
## Required
- model
    - The `model' parameter is essential for designating the path of the model check point. It directly affects the initialization of the TripoSR model and is essential for the operation of the node, as it determines which weights and configurations will be used.
    - Comfy dtype: COMBO[str]
    - Python dtype: str
## Optional
- chunk_size
    - The `chunk_size' parameter optimizes the memory use of models by controlling batch processing sizes. It plays an important role in balancing performance and resource consumption, allowing for the efficient processing of large-scale data.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- TRIPOSR_MODEL
    - The output provides an initialized and prepared TripoSR model. It covers the entire function of the model and allows users to perform various ultra-resolution tasks using it.
    - Comfy dtype: COMBO[torch.nn.Module]
    - Python dtype: torch.nn.Module

# Usage tips
- Infra type: GPU

# Source code
```
class TripoSRModelLoader:

    def __init__(self):
        self.initialized_model = None

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': (get_filename_list('checkpoints'),), 'chunk_size': ('INT', {'default': 8192, 'min': 1, 'max': 10000})}}
    RETURN_TYPES = ('TRIPOSR_MODEL',)
    FUNCTION = 'load'
    CATEGORY = 'Flowty TripoSR'

    def load(self, model, chunk_size):
        device = get_torch_device()
        if not torch.cuda.is_available():
            device = 'cpu'
        if not self.initialized_model:
            print('Loading TripoSR model')
            self.initialized_model = TSR.from_pretrained_custom(weight_path=get_full_path('checkpoints', model), config_path=path.join(path.dirname(__file__), 'config.yaml'))
            self.initialized_model.renderer.set_chunk_size(chunk_size)
            self.initialized_model.to(device)
        return (self.initialized_model,)
```