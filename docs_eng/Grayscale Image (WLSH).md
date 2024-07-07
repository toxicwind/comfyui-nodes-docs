# Documentation
- Class name: WLSH_Image_Grayscale
- Category: WLSH Nodes/image
- Output node: False
- Repo Ref: https://github.com/wallish77/wlsh_nodes

The node is intended to convert colour images to greyscale images, a basic operation in image processing that reduces the complexity of the images by removing colour information, thus focusing on the structure and brightness of the images.

# Input types
## Required
- original
    - The original image is the input needed for the greyscale conversion process. It is essential because it is the object of the conversion and the quality and resolution of the original image directly influences the results.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image or numpy.ndarray

# Output types
- grayscale
    - Output is the greyscale version of the input image, which is processed to focus on brightness and structure details, free from colour interference.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class WLSH_Image_Grayscale:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'original': ('IMAGE',)}}
    RETURN_TYPES = ('IMAGE',)
    RETURN_NAMES = ('grayscale',)
    FUNCTION = 'make_grayscale'
    CATEGORY = 'WLSH Nodes/image'

    def make_grayscale(self, original):
        image = tensor2pil(original)
        image = ImageOps.grayscale(image)
        image = image.convert('RGB')
        image = np.array(image).astype(np.float32) / 255.0
        image = torch.from_numpy(image)[None,]
        return (image,)
```