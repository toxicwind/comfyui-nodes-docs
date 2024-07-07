# Documentation
- Class name: MiDaS_Model_Loader
- Category: WAS Suite/Loaders
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The MiDaS_Model_Loader node is responsible for loading and preparing the MiDaS model for deployment. It ensures that the necessary dependency items are installed and processes downloading and loading the specified MiDaS variant.

# Input types
## Required
- midas_model
    - The'midas_model'parameter specifies the MiDaS model type that you want to load. It is essential to determine the weight and configuration of the pre-training model for the depth estimation task.
    - Comfy dtype: str
    - Python dtype: str

# Output types
- midas_model
    - The'midas_model' output provides a group of components containing the loaded MiDaS model and its associated conversion functions. This output is essential for follow-up processing and analysis of depth information.
    - Comfy dtype: Tuple[torch.nn.Module, Callable]
    - Python dtype: Tuple[torch.nn.Module, Callable[[torch.Tensor], torch.Tensor]]

# Usage tips
- Infra type: GPU

# Source code
```
class MiDaS_Model_Loader:

    def __init__(self):
        self.midas_dir = os.path.join(MODELS_DIR, 'midas')

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'midas_model': (['DPT_Large', 'DPT_Hybrid'],)}}
    RETURN_TYPES = ('MIDAS_MODEL',)
    RETURN_NAMES = ('midas_model',)
    FUNCTION = 'load_midas_model'
    CATEGORY = 'WAS Suite/Loaders'

    def load_midas_model(self, midas_model):
        global MIDAS_INSTALLED
        if not MIDAS_INSTALLED:
            self.install_midas()
        if midas_model == 'DPT_Large':
            model_name = 'dpt_large_384.pt'
        elif midas_model == 'DPT_Hybrid':
            model_name = 'dpt_hybrid_384.pt'
        else:
            model_name = 'dpt_large_384.pt'
        model_path = os.path.join(self.midas_dir, 'checkpoints' + os.sep + model_name)
        torch.hub.set_dir(self.midas_dir)
        if os.path.exists(model_path):
            cstr(f'Loading MiDaS Model from `{model_path}`').msg.print()
            midas_type = model_path
        else:
            cstr('Downloading and loading MiDaS Model...').msg.print()
        midas = torch.hub.load('intel-isl/MiDaS', midas_model, trust_repo=True)
        device = torch.device('cpu')
        cstr(f'MiDaS is using passive device `{device}` until in use.').msg.print()
        midas.to(device)
        midas_transforms = torch.hub.load('intel-isl/MiDaS', 'transforms')
        transform = midas_transforms.dpt_transform
        return ((midas, transform),)

    def install_midas(self):
        global MIDAS_INSTALLED
        if 'timm' not in packages():
            install_package('timm')
        MIDAS_INSTALLED = True
```