# Documentation
- Class name: KfDebug_Segs
- Category: Debugging
- Output node: True
- Repo Ref: https://github.com/dmarx/ComfyUI-Keyframed

The node, within the framework of further learning, facilitates visualization and analysis of split results, enabling users to examine and understand the performance of models in distinguishing between different parts of the image.

# Input types
## Required
- image
    - The image or array of the input is essential to the operation of the node because it is the basis for the partition. The quality and resolution of the input directly influences the accuracy and detail of the split result.
    - Comfy dtype: COMBO["Image", "ndarray"]
    - Python dtype: Image or torch.Tensor
## Optional
- mask
    - The provision of mask parameters helps to fine-tune the partition process by specifying the interest areas in the image. It enhances the ability of nodes to focus on specific segments, thereby improving the overall partition result.
    - Comfy dtype: ndarray
    - Python dtype: numpy.ndarray

# Output types
- segmented_image
    - The output represents the results of the split process, and the different parts of the input image are identified and differentiated. This is essential for further analysis and understanding of the model's performance.
    - Comfy dtype: Image
    - Python dtype: PIL.Image
- segmentation_map
    - The output provides a detailed map of the partition, indicating the boundaries and classifications of each segment of the image. This is essential for assessing the accuracy and validity of the partition algorithm.
    - Comfy dtype: ndarray
    - Python dtype: numpy.ndarray

# Usage tips
- Infra type: CPU

# Source code
```
class KfDebug_Segs(KfDebug_Passthrough):
    RETURN_TYPES = ('SEGS',)
```