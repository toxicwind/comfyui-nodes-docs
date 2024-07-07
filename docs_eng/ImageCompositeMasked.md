# Documentation
- Class name: ImageCompositeMasked
- Category: image
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The 'composite'method of the ImageComposite Masked node is designed to synthesize source images seamlessly to the designated location of the target image, with the option of using a mask to define the mixed area. It contributes to the overall image editing process by allowing accurate control of the image combination.

# Input types
## Required
- destination
    - The target image serves as the basis for the synthetic source image. This is a key parameter, because it determines the canvas in which the synthesis takes place.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- source
    - The source image that will be placed on the target image. It plays an important role in the assembly process, as it is the main visual element that is operated.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- x
    - The x coordinates determine the horizontal position of the source image on the target image. This is an important parameter because it controls the alignment of the source image in the target image.
    - Comfy dtype: INT
    - Python dtype: int
- y
    - y coordinates specify the vertical position of the source image on the target image. It is essential to control the vertical placement of the source image in a combination.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- resize_source
    - The'resize_source' parameter determines whether the source image should be resized to fit the size of the target image. It is important to adjust the size of the source image in a combination.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- mask
    - The optional mask parameter allows you to specify the areas in the source image that should be visible in the synthesis. It applies to the creation of complex images that only parts of the source image need to show.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Output types
- output
    - The output of the 'composite'method is the image that is ultimately synthesized as a result of the synthesis of the source image to the target image under the influence of the specified position and optional mask.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class ImageCompositeMasked:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'destination': ('IMAGE',), 'source': ('IMAGE',), 'x': ('INT', {'default': 0, 'min': 0, 'max': MAX_RESOLUTION, 'step': 1}), 'y': ('INT', {'default': 0, 'min': 0, 'max': MAX_RESOLUTION, 'step': 1}), 'resize_source': ('BOOLEAN', {'default': False})}, 'optional': {'mask': ('MASK',)}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'composite'
    CATEGORY = 'image'

    def composite(self, destination, source, x, y, resize_source, mask=None):
        destination = destination.clone().movedim(-1, 1)
        output = composite(destination, source.movedim(-1, 1), x, y, mask, 1, resize_source).movedim(1, -1)
        return (output,)
```