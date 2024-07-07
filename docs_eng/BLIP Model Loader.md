# Documentation
- Class name: WAS_BLIP_Model_Loader
- Category: WAS Suite/Loaders
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

WAS_BLIP_Model_Loader Node aims to efficiently load and manage BLIP models for caption generation and query tasks. It ensures that the necessary packages are installed and processes the retrieval and initialization of BLIP models and provides simplified interfaces for model access within the WAS package.

# Input types
## Required
- blip_model
    - The parameter 'blip_model' is essential to specify the type of BLIP model that you want to load. It determines whether the node will be initialized for a caption generation or for a query model, thereby influencing the overall function and expected results.
    - Comfy dtype: str
    - Python dtype: str

# Output types
- BLIP_MODEL
    - Output BLIP_MODEL represents the loaded BLIP model, which is intended for caption generation or query tasks. It encapsulates the function of the model and is the central component for further processing within the application.
    - Comfy dtype: torch.nn.Module
    - Python dtype: torch.nn.Module

# Usage tips
- Infra type: GPU

# Source code
```
class WAS_BLIP_Model_Loader:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'blip_model': (['caption', 'interrogate'],)}}
    RETURN_TYPES = ('BLIP_MODEL',)
    FUNCTION = 'blip_model'
    CATEGORY = 'WAS Suite/Loaders'

    def blip_model(self, blip_model):
        if 'timm' not in packages() or 'transformers' not in packages() or 'fairscale' not in packages():
            cstr(f"Modules or packages are missing to use BLIP models. Please run the `{os.path.join(WAS_SUITE_ROOT, 'requirements.txt')}` through ComfyUI's python executable.").error.print()
            exit
        if 'transformers==4.26.1' not in packages(True):
            cstr(f"`transformers==4.26.1` is required for BLIP models. Please run the `{os.path.join(WAS_SUITE_ROOT, 'requirements.txt')}` through ComfyUI's python executable.").error.print()
            exit
        device = 'cpu'
        conf = getSuiteConfig()
        size = 384
        if blip_model == 'caption':
            from .modules.BLIP.blip_module import blip_decoder
            blip_dir = os.path.join(MODELS_DIR, 'blip')
            if not os.path.exists(blip_dir):
                os.makedirs(blip_dir, exist_ok=True)
            torch.hub.set_dir(blip_dir)
            if conf.__contains__('blip_model_url'):
                model_url = conf['blip_model_url']
            else:
                model_url = 'https://storage.googleapis.com/sfr-vision-language-research/BLIP/models/model_base_capfilt_large.pth'
            model = blip_decoder(pretrained=model_url, image_size=size, vit='base')
            model.eval()
            model = model.to(device)
        elif blip_model == 'interrogate':
            from .modules.BLIP.blip_module import blip_vqa
            blip_dir = os.path.join(MODELS_DIR, 'blip')
            if not os.path.exists(blip_dir):
                os.makedirs(blip_dir, exist_ok=True)
            torch.hub.set_dir(blip_dir)
            if conf.__contains__('blip_model_vqa_url'):
                model_url = conf['blip_model_vqa_url']
            else:
                model_url = 'https://storage.googleapis.com/sfr-vision-language-research/BLIP/models/model_base_vqa_capfilt_large.pth'
            model = blip_vqa(pretrained=model_url, image_size=size, vit='base')
            model.eval()
            model = model.to(device)
        result = (model, blip_model)
        return (result,)
```