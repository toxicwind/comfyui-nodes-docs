# Documentation
- Class name: RepeatImageBatch
- Category: image/batch
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The `repeat' method of the RepeatImageBatch node is designed to copy a single image into a batch dimension, allowing the image to be repeated in a data concentration. This function is essential for creating an enhanced data set or a scenario requiring batch processing of consistent images. The function of the node is direct, focusing on copying the input image without changing its intrinsic properties.

# Input types
## Required
- image
    - The 'image'parameter is the input image that the node will process. It is essential for the operation of the node, because it is the object of the reproduction process. The effect of the parameter on node execution is direct, because the output is based on the duplicate image batch of this input.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image
## Optional
- amount
    - The 'amount'parameter specifies how many times the input image should be repeated in the batch dimension. It is an optional parameter with a default value of 1, i.e. it is not repeated if it is not specified. The parameter is important to determine the size of the output batch and directly influences subsequent data processing steps.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- output_image
    - The 'output_image' is the result of the'repeat' operation and contains images that are repeated as batches. Each image in the batch is a copy of the input image, the size of the batch is determined by the 'amount' parameter. This output is important because it forms the basis for further image processing or analysis in the context of batch processing.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image

# Usage tips
- Infra type: CPU

# Source code
```
class RepeatImageBatch:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'amount': ('INT', {'default': 1, 'min': 1, 'max': 4096})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'repeat'
    CATEGORY = 'image/batch'

    def repeat(self, image, amount):
        s = image.repeat((amount, 1, 1, 1))
        return (s,)
```