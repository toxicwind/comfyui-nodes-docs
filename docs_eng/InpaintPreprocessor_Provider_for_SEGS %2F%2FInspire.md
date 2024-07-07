# Documentation
- Class name: InpaintPreprocessor_Provider_for_SEGS
- Category: InspirePack/SEGS/ControlNet
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Inspire-Pack.git

The node facilitates the image restoration process, which is used to fill missing or masked areas in the image and to fill them with content that matches the surrounding context. It is seamlessly integrated with the ComfyUI ecosystem using the restoration capacity of the ControlNet auxiliary processor.

# Input types
## Required
- image
    - An image parameter is necessary because it provides an input image that will perform the restoration operation. The quality and resolution of the input image directly influences the effectiveness of the restoration process.
    - Comfy dtype: COMBO[torch.Tensor]
    - Python dtype: torch.Tensor
## Optional
- mask
    - Mask parameter, when provided, specifies the image area that needs to be repaired. It is a two-value mask that helps guide the restoration process to focus on the target area.
    - Comfy dtype: COMBO[torch.Tensor]
    - Python dtype: torch.Tensor

# Output types
- output
    - The output of the restoration process is an image in which the masked area has been filled. The image now has a more complete original scene, the content of which is naturally integrated with the rest of the image.
    - Comfy dtype: COMBO[torch.Tensor]
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class InpaintPreprocessor_Provider_for_SEGS:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {}}
    RETURN_TYPES = ('SEGS_PREPROCESSOR',)
    FUNCTION = 'doit'
    CATEGORY = 'InspirePack/SEGS/ControlNet'

    def doit(self):
        obj = InpaintPreprocessor_wrapper()
        return (obj,)
```