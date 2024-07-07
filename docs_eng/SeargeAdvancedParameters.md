# Documentation
- Class name: SeargeAdvancedParameters
- Category: UI_INPUTS
- Output node: False
- Repo Ref: https://github.com/jobunk/SeargeSDXL.git

The node class covers advanced parameters for fine-tuning visual elements such as image details, managing dynamic configuration, and adjusting contrast and saturation. It is designed to provide fine particle size control over image enhancement processes, rather than directly involving bottom model operations.

# Input types
## Required
- dynamic_cfg_method
    - This parameter sets out the methods to be used in the dynamic configuration of the image enhancement process. It is essential to adjust the behaviour of the nodes to different input requirements and to achieve the desired output quality.
    - Comfy dtype: COMBO[str]
    - Python dtype: str
- dynamic_cfg_factor
    - This factor affects the extent of dynamic configuration applied to image enhancement. It is important in fine-tuning the balance between efficiency and output details.
    - Comfy dtype: FLOAT
    - Python dtype: float
- refiner_detail_boost
    - This parameter controls the level of detail enhancement applied during the refining process. It is essential to increase the clarity and clarity of the final output.
    - Comfy dtype: FLOAT
    - Python dtype: float
- contrast_factor
    - This factor is important for creating visual shocks and enhancing the overall beauty of the output.
    - Comfy dtype: FLOAT
    - Python dtype: float
- saturation_factor
    - This parameter manages the saturation level of the image, affecting the vibrancy of the colour and the richness of the visual experience.
    - Comfy dtype: FLOAT
    - Python dtype: float
- latent_detailer
    - This parameter selects a potential detail booster to further enhance the delicate detail of the image. It plays a key role in achieving more detailed and realistic visual results.
    - Comfy dtype: COMBO[str]
    - Python dtype: str
## Optional
- data
    - This parameter is used to transmit the data that will be processed by the node. It is important for the node to function correctly and to produce the desired results.
    - Comfy dtype: SRG_DATA_STREAM
    - Python dtype: Any

# Output types
- data
    - The output contains post-processing data for which advanced parameters have been applied and is intended for further use in the image enhancement process.
    - Comfy dtype: SRG_DATA_STREAM
    - Python dtype: Any

# Usage tips
- Infra type: CPU

# Source code
```
class SeargeAdvancedParameters:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'dynamic_cfg_method': (UI.DYNAMIC_CFG_METHODS, {'default': UI.NONE}), 'dynamic_cfg_factor': ('FLOAT', {'default': 0.0, 'min': -1.0, 'max': 1.0, 'step': 0.05}), 'refiner_detail_boost': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1.0, 'step': 0.05}), 'contrast_factor': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1.0, 'step': 0.05}), 'saturation_factor': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1.0, 'step': 0.05}), 'latent_detailer': (UI.LATENT_DETAILERS, {'default': UI.NONE})}, 'optional': {'data': ('SRG_DATA_STREAM',)}}
    RETURN_TYPES = ('SRG_DATA_STREAM',)
    RETURN_NAMES = ('data',)
    FUNCTION = 'get'
    CATEGORY = UI.CATEGORY_UI_INPUTS

    @staticmethod
    def create_dict(dynamic_cfg_method, dynamic_cfg_factor, refiner_detail_boost, contrast_factor, saturation_factor, latent_detailer):
        return {UI.F_DYNAMIC_CFG_METHOD: dynamic_cfg_method, UI.F_DYNAMIC_CFG_FACTOR: round(dynamic_cfg_factor, 3), UI.F_REFINER_DETAIL_BOOST: round(refiner_detail_boost, 3), UI.F_CONTRAST_FACTOR: round(contrast_factor, 3), UI.F_SATURATION_FACTOR: round(saturation_factor, 3), UI.F_LATENT_DETAILER: latent_detailer}

    def get(self, dynamic_cfg_method, dynamic_cfg_factor, refiner_detail_boost, contrast_factor, saturation_factor, latent_detailer, data=None):
        if data is None:
            data = {}
        data[UI.S_ADVANCED_PARAMETERS] = self.create_dict(dynamic_cfg_method, dynamic_cfg_factor, refiner_detail_boost, contrast_factor, saturation_factor, latent_detailer)
        return (data,)
```