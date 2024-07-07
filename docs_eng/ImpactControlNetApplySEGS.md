# Documentation
- Class name: ControlNetApplySEGS
- Category: ImpactPack/Util
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The ControlNetApplySEGS node is designed to enhance the partitioning process by applying the control network to fine-tune the partition mask. It ensures the seamless integration of the control network output with the split result by adjusting the control network's influence to the specified strength parameters.

# Input types
## Required
- segs
    - The `segs' parameter is essential because it provides the initial split data that the node will process. It is essential for the implementation of the node because it forms the basis for the application control network.
    - Comfy dtype: SEGS
    - Python dtype: List[impact.core.SEG]
- control_net
    - The `control_net' parameter is essential for the node because it defines the control network used to fine-tune the split. It directly affects the quality and accuracy of the final split output.
    - Comfy dtype: CONTROL_NET
    - Python dtype: impact.core.ControlNet
- strength
    - The `strength' parameter determines the extent to which the control network affects the partitioning process. It is a key factor in balancing the division detail with the original split data.
    - Comfy dtype: FLOAT
    - Python dtype: float
## Optional
- segs_preprocessor
    - The optional `segs_preprocessor' parameter allows pre-processing of split data before the control network is used. This may be important to ensure that input data are in the correct format or have undergone the necessary conversions.
    - Comfy dtype: SEGS_PREPROCESSOR
    - Python dtype: Callable
- control_image
    - The `control_image' parameter provided is used to enhance the application of the control network by providing additional image context. This enhances the ability of nodes to adjust splits more wisely.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image

# Output types
- SEGS
    - The output 'SEGS' contains a thin division mask after applying the control network. It represents the outcome of node processing and is important for further analysis or downstream tasks.
    - Comfy dtype: SEGS
    - Python dtype: Tuple[str, List[impact.core.SEG]]

# Usage tips
- Infra type: CPU

# Source code
```
class ControlNetApplySEGS:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'segs': ('SEGS',), 'control_net': ('CONTROL_NET',), 'strength': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 10.0, 'step': 0.01})}, 'optional': {'segs_preprocessor': ('SEGS_PREPROCESSOR',), 'control_image': ('IMAGE',)}}
    RETURN_TYPES = ('SEGS',)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Util'

    def doit(self, segs, control_net, strength, segs_preprocessor=None, control_image=None):
        new_segs = []
        for seg in segs[1]:
            control_net_wrapper = core.ControlNetWrapper(control_net, strength, segs_preprocessor, seg.control_net_wrapper, original_size=segs[0], crop_region=seg.crop_region, control_image=control_image)
            new_seg = SEG(seg.cropped_image, seg.cropped_mask, seg.confidence, seg.crop_region, seg.bbox, seg.label, control_net_wrapper)
            new_segs.append(new_seg)
        return ((segs[0], new_segs),)
```