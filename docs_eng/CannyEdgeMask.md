# Documentation
- Class name: CannyEdgeMask
- Category: postprocessing/Masks
- Output node: False
- Repo Ref: https://github.com/EllangoK/ComfyUI-post-processing-nodes

Such nodes encapsulate the function of applying the Canny margin detection algorithm to input images, generating a double edge mask that highlights the edges of the image according to the specified threshold values.

# Input types
## Required
- image
    - To apply the input image from Canny's edge detection. It is the key to node operations, because it is the primary data that algorithms process to create a margin mask.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- lower_threshold
    - The lower threshold parameter is essential to control the sensitivity of the margin detection. It works with the upper threshold to determine which edges are strong enough to be contained in the ultimate margin mask.
    - Comfy dtype: INT
    - Python dtype: int
- upper_threshold
    - The upper threshold parameter, along with the lower threshold, plays an important role in the criteria used to define the margin. It helps to fine-tune the edge by including only the edges that reach or exceed the threshold.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- edge_mask
    - Output is a two-value margin mask, representing the edge detected by the Canny algorithm. This mask is important because it is used for further image processing or analysis.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class CannyEdgeMask:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'lower_threshold': ('INT', {'default': 100, 'min': 0, 'max': 500, 'step': 10}), 'upper_threshold': ('INT', {'default': 200, 'min': 0, 'max': 500, 'step': 10})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'canny'
    CATEGORY = 'postprocessing/Masks'

    def canny(self, image: torch.Tensor, lower_threshold: int, upper_threshold: int):
        (batch_size, height, width, _) = image.shape
        result = torch.zeros(batch_size, height, width)
        for b in range(batch_size):
            tensor_image = image[b].numpy().copy()
            gray_image = (cv2.cvtColor(tensor_image, cv2.COLOR_RGB2GRAY) * 255).astype(np.uint8)
            canny = cv2.Canny(gray_image, lower_threshold, upper_threshold)
            tensor = torch.from_numpy(canny)
            result[b] = tensor
        return (result,)
```