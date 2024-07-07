# Documentation
- Class name: KuwaharaBlur
- Category: postprocessing/Filters
- Output node: False
- Repo Ref: https://github.com/EllangoK/ComfyUI-post-processing-nodes

The KuwaharaBlur class is designed to apply Kuwahara filters to images, a non-linear digital filter for image processing. It can smooth images while keeping edges, especially for reducing image noise without blurring important details. The node is based on dividing images into smaller blocks and replacing each with a filtered version based on local variations, thus preserving the structural integrity of the image.

# Input types
## Required
- image
    - The image parameter is essential because it is the main input for the Kuwahara filter. It is the source of node-derived output, and the content and quality of the image directly influences the effectiveness of noise reduction and margin retention.
    - Comfy dtype: IMAGE
    - Python dtype: np.ndarray
- blur_radius
    - The blurry radius parameter determines the level of smoothness of the Kuwahara filter application. It affects the size of the block to be treated, thus directly affecting the balance between noise reduction and detail preservation.
    - Comfy dtype: INT
    - Python dtype: int
- method
    - The methodological parameters determine the type of Kuwahara filter to be applied, which can be'mean' or 'gaussian'. This selection affects filtering processes and result images,'mean' provides more even smoothness, while 'gaussian' provides more self-adapted smoothness depending on the local properties of the image.
    - Comfy dtype: COMBO
    - Python dtype: str

# Output types
- output_image
    - The output image represents a post-processed image using the Kuwahara filter. It reflects the main function of the node, the crystallization of noise reduction and margin retention efforts, providing clearer and clearer results.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class KuwaharaBlur:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'blur_radius': ('INT', {'default': 3, 'min': 0, 'max': 31, 'step': 1}), 'method': (['mean', 'gaussian'],)}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'apply_kuwahara_filter'
    CATEGORY = 'postprocessing/Filters'

    def apply_kuwahara_filter(self, image: np.ndarray, blur_radius: int, method: str):
        if blur_radius == 0:
            return (image,)
        out = torch.zeros_like(image)
        (batch_size, height, width, channels) = image.shape
        for b in range(batch_size):
            image = image[b].cpu().numpy() * 255.0
            image = image.astype(np.uint8)
            out[b] = torch.from_numpy(kuwahara(image, method=method, radius=blur_radius)) / 255.0
        return (out,)
```