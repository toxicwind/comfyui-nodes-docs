# Documentation
- Class name: IPAdapterUnifiedLoader
- Category: ipadapter
- Output node: False
- Repo Ref: https://github.com/cubiq/ComfyUI_IPAdapter_plus.git

IPAdapterUnied Loader nodes are designed to simplify the loading and management of models required for image-processing tasks. It concentrates on the process of loading Clip Vision, IPAdapter, LoRA, and InsightFace models, ensuring that the correct models are used according to specified presets and offers. The function of the nodes is focused on providing uniform interfaces for model loads, reducing redundancy and increasing the efficiency of the system as a whole.

# Input types
## Required
- model
    - Model parameters are essential for the operation of nodes, as they define the underlying models to be used for processing. They influence the execution of nodes by determining the structure and function of the models.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- preset
    - Preset parameters are necessary because it determines the specific configuration of the model to be loaded. It influences the execution of the node by selecting appropriate model presets according to the user’s needs.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- lora_strength
    - The LoRA intensity parameter is optional and is used to adjust the impact of the LoRA model on the base model. It plays a role in fine-tuning model performance for specific tasks.
    - Comfy dtype: FLOAT
    - Python dtype: float
- provider
    - Provides program parameters to specify the implementation supply program for the InsightFace model. It is important to determine the hardware acceleration method to be used during the model implementation.
    - Comfy dtype: STRING
    - Python dtype: str
- ipadapter
    - The optional ipadapter parameter allows you to specify a custom IPAdapter model file. Use it when the user needs to load a specific version or configuration of the IPAdapter model.
    - Comfy dtype: IPADAPTER
    - Python dtype: Dict[str, Any]

# Output types
- model
    - Model output represents the base model that has been loaded and configured, which is ready for use in image-processing tasks. It is the node function's apex and provides a model tailored to the user's specified requirements.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- ipadapter
    - The ipadapter output contains the loaded IPAdapter model, which is a key component of some image-processing tasks. It provides additional functionality and customization options for the model.
    - Comfy dtype: IPADAPTER
    - Python dtype: Dict[str, Any]

# Usage tips
- Infra type: CPU

# Source code
```
class IPAdapterUnifiedLoader:

    def __init__(self):
        self.lora = None
        self.clipvision = {'file': None, 'model': None}
        self.ipadapter = {'file': None, 'model': None}
        self.insightface = {'provider': None, 'model': None}

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'preset': (['LIGHT - SD1.5 only (low strength)', 'STANDARD (medium strength)', 'VIT-G (medium strength)', 'PLUS (high strength)', 'PLUS FACE (portraits)', 'FULL FACE - SD1.5 only (portraits stronger)'],)}, 'optional': {'ipadapter': ('IPADAPTER',)}}
    RETURN_TYPES = ('MODEL', 'IPADAPTER')
    RETURN_NAMES = ('model', 'ipadapter')
    FUNCTION = 'load_models'
    CATEGORY = 'ipadapter'

    def load_models(self, model, preset, lora_strength=0.0, provider='CPU', ipadapter=None):
        pipeline = {'clipvision': {'file': None, 'model': None}, 'ipadapter': {'file': None, 'model': None}, 'insightface': {'provider': None, 'model': None}}
        if ipadapter is not None:
            pipeline = ipadapter
        clipvision_file = get_clipvision_file(preset)
        if clipvision_file is None:
            raise Exception('ClipVision model not found.')
        if clipvision_file != self.clipvision['file']:
            if clipvision_file != pipeline['clipvision']['file']:
                self.clipvision['file'] = clipvision_file
                self.clipvision['model'] = load_clip_vision(clipvision_file)
                print(f'\x1b[33mINFO: Clip Vision model loaded from {clipvision_file}\x1b[0m')
            else:
                self.clipvision = pipeline['clipvision']
        is_sdxl = isinstance(model.model, (comfy.model_base.SDXL, comfy.model_base.SDXLRefiner, comfy.model_base.SDXL_instructpix2pix))
        (ipadapter_file, is_insightface, lora_pattern) = get_ipadapter_file(preset, is_sdxl)
        if ipadapter_file is None:
            raise Exception('IPAdapter model not found.')
        if ipadapter_file != self.ipadapter['file']:
            if pipeline['ipadapter']['file'] != ipadapter_file:
                self.ipadapter['file'] = ipadapter_file
                self.ipadapter['model'] = ipadapter_model_loader(ipadapter_file)
                print(f'\x1b[33mINFO: IPAdapter model loaded from {ipadapter_file}\x1b[0m')
            else:
                self.ipadapter = pipeline['ipadapter']
        if lora_pattern is not None:
            lora_file = get_lora_file(lora_pattern)
            lora_model = None
            if lora_file is None:
                raise Exception('LoRA model not found.')
            if self.lora is not None:
                if lora_file == self.lora['file']:
                    lora_model = self.lora['model']
                else:
                    self.lora = None
                    torch.cuda.empty_cache()
            if lora_model is None:
                lora_model = comfy.utils.load_torch_file(lora_file, safe_load=True)
                self.lora = {'file': lora_file, 'model': lora_model}
                print(f'\x1b[33mINFO: LoRA model loaded from {lora_file}\x1b[0m')
            if lora_strength > 0:
                (model, _) = load_lora_for_models(model, None, lora_model, lora_strength, 0)
        if is_insightface:
            if provider != self.insightface['provider']:
                if pipeline['insightface']['provider'] != provider:
                    self.insightface['provider'] = provider
                    self.insightface['model'] = insightface_loader(provider)
                    print(f'\x1b[33mINFO: InsightFace model loaded with {provider} provider\x1b[0m')
                else:
                    self.insightface = pipeline['insightface']
        return (model, {'clipvision': self.clipvision, 'ipadapter': self.ipadapter, 'insightface': self.insightface})
```