# Documentation
- Class name: AnimeLineArt_Preprocessor_Provider_for_SEGS
- Category: InspirePack/SEGS/ControlNet
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Inspire-Pack.git

These nodes are responsible for converting the images entered into moving scripts, which are essential to strategizing visual effects in an immobilized and consistent way. They use the power of machine-learning models to generate detailed and performanceal line maps from source images to enhance the creative process in artistic creation tasks.

# Input types
## Required
- image
    - An image parameter is necessary because it is the source of the derived comic script. Enter the details and accuracy of the script that the quality and resolution of the image directly influences.
    - Comfy dtype: image
    - Python dtype: PIL.Image or numpy.ndarray
## Optional
- mask
    - The mask parameters, while optional, can fine-tune pre-processing by specifying the image areas that should be prioritized or excluded in the online bar art conversion process.
    - Comfy dtype: mask
    - Python dtype: numpy.ndarray

# Output types
- SEGS_PREPROCESSOR
    - The output of this node is an image that has been converted to a comic script. This is a key component in creating styled content, and visual appeal and artistic quality are essential.
    - Comfy dtype: image
    - Python dtype: numpy.ndarray

# Usage tips
- Infra type: GPU

# Source code
```
class AnimeLineArt_Preprocessor_Provider_for_SEGS:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {}}
    RETURN_TYPES = ('SEGS_PREPROCESSOR',)
    FUNCTION = 'doit'
    CATEGORY = 'InspirePack/SEGS/ControlNet'

    def doit(self):
        obj = AnimeLineArt_Preprocessor_wrapper()
        return (obj,)
```