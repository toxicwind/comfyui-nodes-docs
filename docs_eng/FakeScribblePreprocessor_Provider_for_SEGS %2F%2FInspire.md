# Documentation
- Class name: FakeScribblePreprocessor_Provider_for_SEGS
- Category: Image Processing
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Inspire-Pack.git

The FakeScribblePreprocessor_Provider_for_SEGS node is designed to enhance image partition tasks by applying pre-processing steps for simulated graffiti. The node uses the ability of the HED (full volume margin detection) algorithm to create alert images, which helps to divide the process. It is particularly suitable for generating detailed and clear partition maps by providing additional context information for partition models.

# Input types
## Required
- safe
    - The'safty'parameter determines whether security measures should be taken in the application of pre-treatment to prevent potential data damage or loss. This is essential to ensure the integrity of the data entered during the pre-processing phase.
    - Comfy dtype: bool
    - Python dtype: bool

# Output types
- result
    - The output of the FakeScribblePreprocessor_Provider_for_SEGS node is a pre-processed step image. This image can be used directly as input to the split model, increasing the ability of the model to produce an accurate partition.
    - Comfy dtype: image
    - Python dtype: PIL.Image or numpy.ndarray

# Usage tips
- Infra type: CPU

# Source code
```
class FakeScribblePreprocessor_Provider_for_SEGS(HEDPreprocessor_Provider_for_SEGS):

    def doit(self, safe):
        obj = HED_Preprocessor_wrapper(safe, 'FakeScribblePreprocessor')
        return (obj,)
```