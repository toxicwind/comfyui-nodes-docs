# Documentation
- Class name: SeargeConditioningParameters
- Category: UI_INPUTS
- Output node: False
- Repo Ref: https://github.com/jobunk/SeargeSDXL.git

The node class covers the logic of adjusting the parameters in the search and rescue scenario and aims to optimize the search strategy according to different scales and scores.

# Input types
## Required
- base_conditioning_scale
    - The base condition ratio is a basic parameter that affects the initial conditions at the start of the search operation.
    - Comfy dtype: FLOAT
    - Python dtype: float
- refiner_conditioning_scale
    - This scale details the search process and allows for more detailed adjustments to the strategy as operations proceed.
    - Comfy dtype: FLOAT
    - Python dtype: float
- target_conditioning_scale
    - Target ratios are essential to focus search efforts on high-priority areas within the area of operation.
    - Comfy dtype: FLOAT
    - Python dtype: float
- positive_conditioning_scale
    - This parameter reinforces the positive aspects of the search and directs resources to areas with higher potential for success.
    - Comfy dtype: FLOAT
    - Python dtype: float
- negative_conditioning_scale
    - The proportion of negative conditions helps to avoid less effective regions and ensures that resources are not wasted in areas where success is less likely.
    - Comfy dtype: FLOAT
    - Python dtype: float
- positive_aesthetic_score
    - Positive aesthetic ratings contribute to the decision-making process by assessing the visual appeal of search areas and may lead to more efficient operations.
    - Comfy dtype: FLOAT
    - Python dtype: float
- negative_aesthetic_score
    - This rating reflects an undesired side of the search area and directs the search away from areas that may impede operational progress.
    - Comfy dtype: FLOAT
    - Python dtype: float
- precondition_mode
    - The preset model sets the operating framework of the conditions and determines how search parameters are applied at the start of the mission.
    - Comfy dtype: PRECONDITION_MODES
    - Python dtype: Enum
- precondition_strength
    - Pre-intensity affects the intensity of the application of the initial conditions and the overall search strategy.
    - Comfy dtype: FLOAT
    - Python dtype: float
## Optional
- data
    - Data streams provide a continuous flow of information that can be used to dynamically adjust search parameters in real time.
    - Comfy dtype: SRG_DATA_STREAM
    - Python dtype: Dict[str, Any]

# Output types
- data
    - The data stream has updated the parameters of the conditions to serve as the basis for continuous decision-making in search and rescue operations.
    - Comfy dtype: SRG_DATA_STREAM
    - Python dtype: Dict[str, Any]

# Usage tips
- Infra type: CPU

# Source code
```
class SeargeConditioningParameters:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'base_conditioning_scale': ('FLOAT', {'default': 2.0, 'min': 0.5, 'max': 4.0, 'step': 0.25}), 'refiner_conditioning_scale': ('FLOAT', {'default': 2.0, 'min': 0.5, 'max': 4.0, 'step': 0.25}), 'target_conditioning_scale': ('FLOAT', {'default': 2.0, 'min': 0.5, 'max': 4.0, 'step': 0.25}), 'positive_conditioning_scale': ('FLOAT', {'default': 1.5, 'min': 0.25, 'max': 2.0, 'step': 0.25}), 'negative_conditioning_scale': ('FLOAT', {'default': 0.75, 'min': 0.25, 'max': 2.0, 'step': 0.25}), 'positive_aesthetic_score': ('FLOAT', {'default': 6.0, 'min': 0.5, 'max': 10.0, 'step': 0.5}), 'negative_aesthetic_score': ('FLOAT', {'default': 2.5, 'min': 0.5, 'max': 10.0, 'step': 0.5}), 'precondition_mode': (UI.PRECONDITION_MODES,), 'precondition_strength': ('FLOAT', {'default': 0.1, 'min': 0.0, 'max': 1.0, 'step': 0.05})}, 'optional': {'data': ('SRG_DATA_STREAM',)}}
    RETURN_TYPES = ('SRG_DATA_STREAM',)
    RETURN_NAMES = ('data',)
    FUNCTION = 'get'
    CATEGORY = UI.CATEGORY_UI_INPUTS

    @staticmethod
    def create_dict(base_conditioning_scale, refiner_conditioning_scale, target_conditioning_scale, positive_conditioning_scale, negative_conditioning_scale, positive_aesthetic_score, negative_aesthetic_score, precondition_mode, precondition_strength):
        return {UI.F_BASE_CONDITIONING_SCALE: round(base_conditioning_scale, 3), UI.F_REFINER_CONDITIONING_SCALE: round(refiner_conditioning_scale, 3), UI.F_TARGET_CONDITIONING_SCALE: round(target_conditioning_scale, 3), UI.F_POSITIVE_CONDITIONING_SCALE: round(positive_conditioning_scale, 3), UI.F_NEGATIVE_CONDITIONING_SCALE: round(negative_conditioning_scale, 3), UI.F_POSITIVE_AESTHETIC_SCORE: round(positive_aesthetic_score, 3), UI.F_NEGATIVE_AESTHETIC_SCORE: round(negative_aesthetic_score, 3), UI.F_PRECONDITION_MODE: precondition_mode, UI.F_PRECONDITION_STRENGTH: round(precondition_strength, 3)}

    def get(self, base_conditioning_scale, refiner_conditioning_scale, target_conditioning_scale, positive_conditioning_scale, negative_conditioning_scale, positive_aesthetic_score, negative_aesthetic_score, precondition_mode, precondition_strength, data=None):
        if data is None:
            data = {}
        data[UI.S_CONDITIONING_PARAMETERS] = self.create_dict(base_conditioning_scale, refiner_conditioning_scale, target_conditioning_scale, positive_conditioning_scale, negative_conditioning_scale, positive_aesthetic_score, negative_aesthetic_score, precondition_mode, precondition_strength)
        return (data,)
```