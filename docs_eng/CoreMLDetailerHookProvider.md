# Documentation
- Class name: CoreMLDetailerHookProvider
- Category: ImpactPack/Detailer
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The CoreMlDetailerHookProvider node is intended to promote the integration of the CoreML model in the ImpactPack/Detailer category. It provides a method for generating a hook that can be used to customize the behaviour of the model in image processing tasks. This node is particularly suitable for adjusting the resolution and width of the image to meet the requirements of the CoreML model.

# Input types
## Required
- mode
    - The mode parameter specifies the resolution and width ratio for image processing. It is critical because it determines how the CoreML model will deal with the input image. Node uses this information to adjust the size of the image to the requirements of the model.
    - Comfy dtype: str
    - Python dtype: str

# Output types
- DETAILER_HOOK
    - The output of the node is a CoreMLHook object, a special hook designed to work with the CoreML model. It includes methods for pre-processing and reprocessing samples to ensure their compatibility with the model's expected input and output formats.
    - Comfy dtype: CoreMLHook
    - Python dtype: CoreMLHook

# Usage tips
- Infra type: CPU

# Source code
```
class CoreMLDetailerHookProvider:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'mode': (['512x512', '768x768', '512x768', '768x512'],)}}
    RETURN_TYPES = ('DETAILER_HOOK',)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Detailer'

    def doit(self, mode):
        hook = hooks.CoreMLHook(mode)
        return (hook,)
```