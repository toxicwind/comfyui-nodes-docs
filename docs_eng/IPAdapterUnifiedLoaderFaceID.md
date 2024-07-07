# Documentation
- Class name: IPAdapterUnifiedLoaderFaceID
- Category: ipadapter/faceid
- Output node: False
- Repo Ref: https://github.com/cubiq/ComfyUI_IPAdapter_plus.git

The IPAdapterUnified LoaderFaceID class serves as a dedicated interface for loading and managing facial recognition models to ensure compatibility and seamless integration within the system.

# Input types
## Required
- model
    - Model parameters are essential for the design of facial identification models to be used in the system, guiding the overall function and expected results.
    - Comfy dtype: MODEL
    - Python dtype: str
- preset
    - Predefined parameters determine the variant of the facial identification model to be applied, affecting the performance and accuracy of the facial recognition process.
    - Comfy dtype: COMBO[preset]
    - Python dtype: str
- lora_strength
    - The adaptation of the lora_strength parameter fine-tuning model allows fine-tuning during facial recognition to obtain the best results.
    - Comfy dtype: FLOAT
    - Python dtype: float
- provider
    - The provider parameters are essential for determining the environment for the implementation of the facial identification model, affecting its operational efficiency and resource utilization.
    - Comfy dtype: COMBO[provider]
    - Python dtype: str

# Output types
- MODEL
    - The output MODEL represents the loaded facial identification model to be deployed in multiple tasks and applications within the system.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- ipadapter
    - The ipadapter output facilitates the integration of facial recognition models with other components of the system, ensuring smooth operation and data flow.
    - Comfy dtype: IPADAPTER
    - Python dtype: IPADAPTER

# Usage tips
- Infra type: CPU

# Source code
```
class IPAdapterUnifiedLoaderFaceID(IPAdapterUnifiedLoader):

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'preset': (['FACEID', 'FACEID PLUS - SD1.5 only', 'FACEID PLUS V2', 'FACEID PORTRAIT (style transfer)'],), 'lora_strength': ('FLOAT', {'default': 0.6, 'min': 0, 'max': 1, 'step': 0.01}), 'provider': (['CPU', 'CUDA', 'ROCM', 'DirectML', 'OpenVINO', 'CoreML'],)}, 'optional': {'ipadapter': ('IPADAPTER',)}}
    RETURN_NAMES = ('MODEL', 'ipadapter')
    CATEGORY = 'ipadapter/faceid'
```