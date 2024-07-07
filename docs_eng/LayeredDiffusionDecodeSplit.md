# Documentation
- Class name: LayeredDiffusionDecodeSplit
- Category: Image Processing
- Output node: False
- Repo Ref: https://github.com/huchenlei/ComfyUI-layerdiffuse.git

The LayeredDiffusionDeodeSplit class is designed to decode RGBA images efficiently in batches and improve the handling of throughput and memory management. It processes large image data sets by decoding smaller groups of images, thereby optimizing the computational resources and simplifying the decoding process for various applications.

# Input types
## Required
- samples
    - The samples parameter is necessary because it contains the potential expressions needed to understand the code process. It directly affects the quality and accuracy of decoded images and is the basis of the whole operation.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]
- images
    - The “images” parameter is essential to the decoding process and provides input images that need to be processed. It is the core of node execution and influences the final output, deciding to understand the visual aspects of the code image.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- frames
    - The 'frames' parameter determines the frequency of image decoding and effectively controls the size of the sub-batch. It plays a key role in balancing computing efficiency and memory use, ensuring that the process is smooth and optimized.
    - Comfy dtype: INT
    - Python dtype: int
- sd_version
    - The " sd_version " parameter specifies the version of the stable diffusion model to be used, which is essential for determining the decoding algorithm and its compatibility with the input data. It affects overall performance and the quality of the image generated.
    - Comfy dtype: ENUM
    - Python dtype: StableDiffusionVersion
- sub_batch_size
    - The “sub_batch_size” parameter is essential for managing the calculation of loads, as it defines the number of images to be processed in each batch. It plays an important role in optimizing the speed of the decoding process and the allocation of resources.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- image
    - The "image" output represents a decoded RGBA image, which is the main result of node operations. It encapsifies visual information obtained from input data processing and demonstrates the ability of nodes to convert potential expressions to perceptible visual content.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- alpha
    - The alpha output of alpha channel information containing decoded images is important for applications that require transparency. It highlights the ability of nodes to process complex image properties and contributes to the enrichment of the final visual output.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class LayeredDiffusionDecodeSplit(LayeredDiffusionDecodeRGBA):
    """Decode RGBA every N images."""

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'samples': ('LATENT',), 'images': ('IMAGE',), 'frames': ('INT', {'default': 2, 'min': 2, 'max': s.MAX_FRAMES, 'step': 1}), 'sd_version': ([StableDiffusionVersion.SD1x.value, StableDiffusionVersion.SDXL.value], {'default': StableDiffusionVersion.SDXL.value}), 'sub_batch_size': ('INT', {'default': 16, 'min': 1, 'max': 4096, 'step': 1})}}
    MAX_FRAMES = 3
    RETURN_TYPES = ('IMAGE',) * MAX_FRAMES

    def decode(self, samples, images: torch.Tensor, frames: int, sd_version: str, sub_batch_size: int):
        sliced_samples = copy.copy(samples)
        sliced_samples['samples'] = sliced_samples['samples'][::frames]
        return tuple((super(LayeredDiffusionDecodeSplit, self).decode(sliced_samples, imgs, sd_version, sub_batch_size)[0] if i == 0 else imgs for i in range(frames) for imgs in (images[i::frames],))) + (None,) * (self.MAX_FRAMES - frames)
```