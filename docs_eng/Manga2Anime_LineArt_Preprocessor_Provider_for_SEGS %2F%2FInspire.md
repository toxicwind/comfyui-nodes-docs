# Documentation
- Class name: Manga2Anime_LineArt_Preprocessor_Provider_for_SEGS
- Category: InspirePack/SEGS/ControlNet
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Inspire-Pack.git

The node, as the provider of the Manga2Anime script preprocessor, is designed to divide and enhance the script from comic-style images. It encapsulates the functionality needed to convert the image to fit for further processing and style, with a focus on maintaining the integrity and visual appeal of the original art work.

# Input types
## Required
- image
    - Enter the image that will be pre-processed in the script. This parameter is essential because it is the primary data source for node operations. Node processes the image to enhance and clarify the script features.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image or numpy.ndarray
- mask
    - An optional mask image can be used for pre-processing of the guide draft. The mask can influence the execution of the node by concentrating the processing in a specific area of the image.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image or numpy.ndarray

# Output types
- SEGS_PREPROCESSOR
    - The output is a pre-processed script image that has been enhanced for split purposes. This output is important because it lays the foundation for subsequent split tasks in the workflow.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image or numpy.ndarray

# Usage tips
- Infra type: CPU

# Source code
```
class Manga2Anime_LineArt_Preprocessor_Provider_for_SEGS:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {}}
    RETURN_TYPES = ('SEGS_PREPROCESSOR',)
    FUNCTION = 'doit'
    CATEGORY = 'InspirePack/SEGS/ControlNet'

    def doit(self):
        obj = Manga2Anime_LineArt_Preprocessor_wrapper()
        return (obj,)
```