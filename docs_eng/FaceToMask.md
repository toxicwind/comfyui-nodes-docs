# Documentation
- Class name: FaceToMask
- Category: ♾️Mixlab/Mask
- Output node: False
- Repo Ref: https://github.com/shadowcz007/comfyui-mixlab-nodes.git

The node uses image-processing techniques to identify and isolate facial features from input images, focusing on green passages to create masks that highlight the detected facial features.

# Input types
## Required
- image
    - The input image is essential for the operation of the node, as it is the source from which the facial features are extracted and the mask is created.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image

# Output types
- MASK
    - The output mask represents the facial area of the image, using the green channel data to indicate the presence of the face.
    - Comfy dtype: TENSOR
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class FaceToMask:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',)}}
    RETURN_TYPES = ('MASK',)
    FUNCTION = 'run'
    CATEGORY = '♾️Mixlab/Mask'
    INPUT_IS_LIST = False
    OUTPUT_IS_LIST = (False,)

    def run(self, image):
        im = tensor2pil(image)
        mask = detect_faces(im)
        mask = pil2tensor(mask)
        channels = ['red', 'green', 'blue', 'alpha']
        mask = mask[:, :, :, channels.index('green')]
        return (mask,)
```