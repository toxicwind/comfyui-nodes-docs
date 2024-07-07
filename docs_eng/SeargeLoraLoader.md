# Documentation
- Class name: SeargeLoraLoader
- Category: Searge/_deprecated_/Files
- Output node: False
- Repo Ref: https://github.com/jobunk/SeargeSDXL.git

The node facilitates the loading and integration of LORA models, which is essential to fine-tune pre-training models to suit specific tasks or data sets. It enables users to enhance model performance by adjusting the impact of LORA layers and CLAIP models, thus providing indications of customization of given data sets.

# Input types
## Required
- model
    - Model parameters are essential because it defines the basis for LORA adaptation. It determines the initial understanding and ability of the model before any fine-tuning.
    - Comfy dtype: MODEL
    - Python dtype: Any
- clip
    - The clip parameter, which is essential for the entire process, represents the CLIP model component that will be used in conjunction with the LORA model to create synergies and enhance the overall expression and adaptability of the final model.
    - Comfy dtype: CLIP
    - Python dtype: Any
- lora_name
    - The lora_name parameter specifies the identity of the LORA layer, which is essential to distinguish the various LORA configurations and to use the right layer in the adaptation process.
    - Comfy dtype: LORA_NAME
    - Python dtype: str
- strength_model
    - Strength_model parameters adjust the impact of the LORA layer on the overall model to allow fine-tuning of the representations of the model to better adapt to the specific characteristics of the target data set.
    - Comfy dtype: FLOAT
    - Python dtype: float
- strength_clip
    - Strength_clip parameters regulate the impact of the CLIP module to ensure that the combination of the CLIP and LORA models is optimized for the desired results.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- MODEL
    - The output model represents the results of LORA and CLIP integration and provides an enhanced and adaptive sign ready for further treatment or assessment.
    - Comfy dtype: MODEL
    - Python dtype: Any
- CLIP
    - The CLIP component in the output represents a successful integration with the LORA model, ensuring that the model has the capacity to understand and generate content based on the target data set.
    - Comfy dtype: CLIP
    - Python dtype: Any

# Usage tips
- Infra type: CPU

# Source code
```
class SeargeLoraLoader:

    def __init__(self):
        self.lora_loader = nodes.LoraLoader()

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'clip': ('CLIP',), 'lora_name': ('LORA_NAME',), 'strength_model': ('FLOAT', {'default': 1.0, 'min': -10.0, 'max': 10.0, 'step': 0.01}), 'strength_clip': ('FLOAT', {'default': 1.0, 'min': -10.0, 'max': 10.0, 'step': 0.01})}}
    RETURN_TYPES = ('MODEL', 'CLIP')
    FUNCTION = 'load_lora'
    CATEGORY = 'Searge/_deprecated_/Files'

    def load_lora(self, model, clip, lora_name, strength_model, strength_clip):
        return self.lora_loader.load_lora(model, clip, lora_name, strength_model, strength_clip)
```