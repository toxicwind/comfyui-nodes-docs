# Documentation
- Class name: PerpNegGuider
- Category: _for_testing
- Output node: True
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The PerpNegGuider node is designed to guide the generation process by providing a condition input that influences model output. It guides the generation process by setting positive and negative conditions and an empty condition to achieve the desired result. The node also allows for the configuration of a zoom factor and a control parameter that enhances the flexibility and accuracy of the guidance.

# Input types
## Required
- model
    - Model parameters are essential because they define the production models with which nodes interact. They form the basis of the node function and make it possible to direct the generation process according to the specified conditions.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- positive
    - The adjustment parameter is essential to define the positive aspects that the guide should focus on during the generation process. It helps to create the desired quality from the output plastic.
    - Comfy dtype: CONDITIONING
    - Python dtype: str
- negative
    - Negative adjustment parameters are used to specify what should be avoided in the output generated. It plays a key role in refining the content to exclude elements that are not needed.
    - Comfy dtype: CONDITIONING
    - Python dtype: str
- empty_conditioning
    - An empty condition parameter is used to set a baseline or neutral state for the generation process. It is important for the establishment of a reference point from which positive and negative conditions can effectively guide the output.
    - Comfy dtype: CONDITIONING
    - Python dtype: str
## Optional
- cfg
    - The cfg parameter is used as a control factor to adjust the effect of the conditions on the generation process. It is important in fine-tuning the balance between guidance and the natural propensity of the model.
    - Comfy dtype: FLOAT
    - Python dtype: float
- neg_scale
    - Neg_scale parameters adjust the effect of negative reconciliations to allow fine-tuning of the extent to which the creation does not encourage undesirable aspects.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- guider
    - The guider output is a configured guiding object that covers the conditions and settings provided by the node. It plays an important role in guiding the generation model to produce an output that is consistent with the specified guidance.
    - Comfy dtype: GUIDER
    - Python dtype: comfy.samplers.CFGGuider

# Usage tips
- Infra type: CPU

# Source code
```
class PerpNegGuider:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'positive': ('CONDITIONING',), 'negative': ('CONDITIONING',), 'empty_conditioning': ('CONDITIONING',), 'cfg': ('FLOAT', {'default': 8.0, 'min': 0.0, 'max': 100.0, 'step': 0.1, 'round': 0.01}), 'neg_scale': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 100.0, 'step': 0.01})}}
    RETURN_TYPES = ('GUIDER',)
    FUNCTION = 'get_guider'
    CATEGORY = '_for_testing'

    def get_guider(self, model, positive, negative, empty_conditioning, cfg, neg_scale):
        guider = Guider_PerpNeg(model)
        guider.set_conds(positive, negative, empty_conditioning)
        guider.set_cfg(cfg, neg_scale)
        return (guider,)
```