# Documentation
- Class name: SeargeInput4
- Category: Searge/_deprecated_/UI/Inputs
- Output node: False
- Repo Ref: https://github.com/jobunk/SeargeSDXL.git

The node serves as a multi-routine repeater for multiple model input, integrating and organizing them for further processing. It ensures that appropriate models are selected on the basis of the set-up provided, simplifying work processes and increasing the efficiency of model integration.

# Input types
## Required
- base_model
    - The basic model is the basic neural network architecture that constitutes further improvement and enhancement. Its choice is critical, as it directly affects the quality and applicability of the output.
    - Comfy dtype: COMBO[folder_paths.get_filename_list('checkpoints'),]
    - Python dtype: List[str]
- refiner_model
    - The fine-tuning model is a step-by-step version of the underlying model, focusing on specific aspects of improving its performance. Its inclusion is essential for achieving greater accuracy and detail in the results.
    - Comfy dtype: COMBO[folder_paths.get_filename_list('checkpoints'),]
    - Python dtype: List[str]
- vae_model
    - The VAE (distribution from encoder) model is used to lower the peacekeeping generation of new data points similar to input data. Its role in creating compressed expressions and facilitating the generation of new data is critical.
    - Comfy dtype: COMBO[folder_paths.get_filename_list('vae'),]
    - Python dtype: List[str]
- main_upscale_model
    - The primary magnification model is responsible for increasing the resolution of the input data. It plays a key role in improving the visual quality and detail of the output and ensuring that the results of the magnification meet the desired standards.
    - Comfy dtype: COMBO[folder_paths.get_filename_list('upscale_models'),]
    - Python dtype: List[str]
- support_upscale_model
    - Supporting magnification models assist in the magnification process and provide additional support for the magnification model. Their presence helps to increase the robustness and reliability of the magnification process and ensures the quality of the final output.
    - Comfy dtype: COMBO[folder_paths.get_filename_list('upscale_models'),]
    - Python dtype: List[str]
- lora_model
    - The LORA (low-adaptation) model is used to adapt the pre-training model effectively to new tasks or data. It plays an important role in achieving adaptation and flexibility in the use of the model, allowing for better performance on diverse data sets.
    - Comfy dtype: COMBO[folder_paths.get_filename_list('loras'),]
    - Python dtype: List[str]
## Optional
- model_settings
    - Model settings are optional configurations that can be used to customize model behaviour according to specific requirements or preferences without changing the underlying model itself.
    - Comfy dtype: Dict[str, str]
    - Python dtype: Optional[Dict[str, str]]

# Output types
- model_names
    - The output is a dictionary of model names that provides a structured overview of the models selected for different purposes in the workflow. This organized expression is essential for the proper use of appropriate models in subsequent steps.
    - Comfy dtype: Dict[str, str]
    - Python dtype: Dict[str, str]

# Usage tips
- Infra type: CPU

# Source code
```
class SeargeInput4:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'base_model': (folder_paths.get_filename_list('checkpoints'),), 'refiner_model': (folder_paths.get_filename_list('checkpoints'),), 'vae_model': (folder_paths.get_filename_list('vae'),), 'main_upscale_model': (folder_paths.get_filename_list('upscale_models'),), 'support_upscale_model': (folder_paths.get_filename_list('upscale_models'),), 'lora_model': (folder_paths.get_filename_list('loras'),)}, 'optional': {'model_settings': ('MODEL_SETTINGS',)}}
    RETURN_TYPES = ('MODEL_NAMES',)
    RETURN_NAMES = ('model_names',)
    FUNCTION = 'mux'
    CATEGORY = 'Searge/_deprecated_/UI/Inputs'

    def mux(self, base_model, refiner_model, vae_model, main_upscale_model, support_upscale_model, lora_model, model_settings=None):
        if model_settings is None:
            model_names = {}
        else:
            model_names = model_settings
        model_names['base_model'] = base_model
        model_names['refiner_model'] = refiner_model
        model_names['vae_model'] = vae_model
        model_names['main_upscale_model'] = main_upscale_model
        model_names['support_upscale_model'] = support_upscale_model
        model_names['lora_model'] = lora_model
        return (model_names,)
```