# Documentation
- Class name: WAS_SAM_Model_Loader
- Category: WAS Suite/Image/Masking
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The sam_load_model function is designed to load and initialize the pre-trained Powering Model (SAM) according to the size of the specified model. If the weight of the model does not exist, it downloads the weight of the model and sets the model for the next image split task. This node is essential for the image masking process and provides the basis for the high quality object partition in the SAS Suite.

# Input types
## Required
- model_size
    - The model_size parameter is essential to determine the specific SAM model to be loaded. It determines the complexity and size of the model, which directly affects the performance and accuracy of the split task. This parameter ensures that the correct pre-training model is used in the image cover.
    - Comfy dtype: COMBO['ViT-H', 'ViT-L', 'ViT-B']
    - Python dtype: str

# Output types
- SAM_MODEL
    - The output SAM_MODEL indicates that it is loaded and ready to be used. This is a pre-training depth learning model designed to separate high-quality objects. The model is a key component of the next step in the image masking workflow and allows for the accurate and efficient separation of objects in the image.
    - Comfy dtype: torch.nn.Module
    - Python dtype: torch.nn.Module

# Usage tips
- Infra type: GPU

# Source code
```
class WAS_SAM_Model_Loader:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        return {'required': {'model_size': (['ViT-H', 'ViT-L', 'ViT-B'],)}}
    RETURN_TYPES = ('SAM_MODEL',)
    FUNCTION = 'sam_load_model'
    CATEGORY = 'WAS Suite/Image/Masking'

    def sam_load_model(self, model_size):
        conf = getSuiteConfig()
        model_filename_mapping = {'ViT-H': 'sam_vit_h_4b8939.pth', 'ViT-L': 'sam_vit_l_0b3195.pth', 'ViT-B': 'sam_vit_b_01ec64.pth'}
        model_url_mapping = {'ViT-H': conf['sam_model_vith_url'] if conf.__contains__('sam_model_vith_url') else 'https://dl.fbaipublicfiles.com/segment_anything/sam_vit_h_4b8939.pth', 'ViT-L': conf['sam_model_vitl_url'] if conf.__contains__('sam_model_vitl_url') else 'https://dl.fbaipublicfiles.com/segment_anything/sam_vit_l_0b3195.pth', 'ViT-B': conf['sam_model_vitb_url'] if conf.__contains__('sam_model_vitb_url') else 'https://dl.fbaipublicfiles.com/segment_anything/sam_vit_b_01ec64.pth'}
        model_url = model_url_mapping[model_size]
        model_filename = model_filename_mapping[model_size]
        if 'GitPython' not in packages():
            install_package('gitpython')
        if not os.path.exists(os.path.join(WAS_SUITE_ROOT, 'repos' + os.sep + 'SAM')):
            from git.repo.base import Repo
            cstr('Installing SAM...').msg.print()
            Repo.clone_from('https://github.com/facebookresearch/segment-anything', os.path.join(WAS_SUITE_ROOT, 'repos' + os.sep + 'SAM'))
        sys.path.append(os.path.join(WAS_SUITE_ROOT, 'repos' + os.sep + 'SAM'))
        sam_dir = os.path.join(MODELS_DIR, 'sam')
        if not os.path.exists(sam_dir):
            os.makedirs(sam_dir, exist_ok=True)
        sam_file = os.path.join(sam_dir, model_filename)
        if not os.path.exists(sam_file):
            cstr('Selected SAM model not found. Downloading...').msg.print()
            r = requests.get(model_url, allow_redirects=True)
            open(sam_file, 'wb').write(r.content)
        from segment_anything import build_sam_vit_h, build_sam_vit_l, build_sam_vit_b
        if model_size == 'ViT-H':
            sam_model = build_sam_vit_h(sam_file)
        elif model_size == 'ViT-L':
            sam_model = build_sam_vit_l(sam_file)
        elif model_size == 'ViT-B':
            sam_model = build_sam_vit_b(sam_file)
        else:
            raise ValueError(f"SAM model does not match the model_size: '{model_size}'.")
        return (sam_model,)
```