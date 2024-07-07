# Documentation
- Class name: SeargeOutput4
- Category: Searge/_deprecated_/UI/Outputs
- Output node: False
- Repo Ref: https://github.com/jobunk/SeargeSDXL.git

The node is designed to facilitate the separation and identification of model components in complex systems. It receives structured model name input and deconstructs it to provide individual access to each model type, thereby enhancing the modularization and organization of output data.

# Input types
## Required
- model_names
    - This parameter is essential because it contains all the model names required for node operations. It is a composite structure with the names of different models, each playing a different role in the system.
    - Comfy dtype: COMBO[{'base_model': str, 'refiner_model': str, 'vae_model': str, 'main_upscale_model': str, 'support_upscale_model': str, 'lora_model': str}]
    - Python dtype: Dict[str, str]

# Output types
- model_names
    - The output maintains the structured format of the input, providing a clear and structured expression of the model name. This facilitates further processing and analysis of the other components of the system.
    - Comfy dtype: COMBO[{'base_model': str, 'refiner_model': str, 'vae_model': str, 'main_upscale_model': str, 'support_upscale_model': str, 'lora_model': str}]
    - Python dtype: Dict[str, str]
- base_model
    - This output represents the underlying model in the system, which provides the basis for other models and processes. Identification is essential for understanding the structure and hierarchy of the models involved.
    - Comfy dtype: str
    - Python dtype: str
- refiner_model
    - The refined model output demonstrates a model designed to enhance or improve the output of the underlying model. It plays a key role in improving the overall accuracy and quality of the system's results.
    - Comfy dtype: str
    - Python dtype: str
- vae_model
    - This output assigns the VAE model, which plays an important role in learning to generate new data expressions. It is a key component of the data generation and feature extraction tasks.
    - Comfy dtype: str
    - Python dtype: str
- main_upscale_model
    - The primary magnification model output refers to the primary model responsible for improving the resolution of data. It is essential for improving the visual quality and detail of the output in image-processing tasks.
    - Comfy dtype: str
    - Python dtype: str
- support_upscale_model
    - This output represents a support model that complements the magnification process and complements the magnification model. It helps to increase the overall effectiveness and efficiency of the magnification mission.
    - Comfy dtype: str
    - Python dtype: str
- lora_model
    - The LORA (low adaptation) model output is associated with an effective pre-adaptation model to a new task. It is important because it can improve model performance at the lowest calculation cost.
    - Comfy dtype: str
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class SeargeOutput4:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model_names': ('MODEL_NAMES',)}}
    RETURN_TYPES = ('MODEL_NAMES', 'CHECKPOINT_NAME', 'CHECKPOINT_NAME', 'VAE_NAME', 'UPSCALER_NAME', 'UPSCALER_NAME', 'LORA_NAME')
    RETURN_NAMES = ('model_names', 'base_model', 'refiner_model', 'vae_model', 'main_upscale_model', 'support_upscale_model', 'lora_model')
    FUNCTION = 'demux'
    CATEGORY = 'Searge/_deprecated_/UI/Outputs'

    def demux(self, model_names):
        base_model = model_names['base_model']
        refiner_model = model_names['refiner_model']
        vae_model = model_names['vae_model']
        main_upscale_model = model_names['main_upscale_model']
        support_upscale_model = model_names['support_upscale_model']
        lora_model = model_names['lora_model']
        return (model_names, base_model, refiner_model, vae_model, main_upscale_model, support_upscale_model, lora_model)
```