# Documentation
- Class name: ControlNetApplyAdvancedSEGS
- Category: ImpactPack/Util
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The ControlNetApplyAdvancedSEGS node is designed to fine-tune the partitioning mask by applying the control network to enhance the partitioning process. It ensures a smooth transition from one region to another by adjusting the impact of the control network throughout the image without visible seams. This node is particularly suitable for scenarios that require precise control of the partition output.

# Input types
## Required
- segs
    - The'segs' parameter is essential because it provides the initial split data that nodes will process. It directly influences the execution of nodes by determining the starting point for the detail of the control network.
    - Comfy dtype: SEGS
    - Python dtype: List[Tuple[Image, List[NamedTuple], BoundingBox, Label, ControlNetAdvancedWrapper]]
- control_net
    - The 'control_net' parameter defines the control network that will guide the partition process. It is essential for the function of the node, as it determines how to fine-tune the partition mask.
    - Comfy dtype: CONTROL_NET
    - Python dtype: torch.nn.Module
- strength
    - The'strength' parameter adjusts the intensity of the influence of the control network on the partition. It is a key factor in determining the final quality of the split output and allows fine-tuning of the influence of the network.
    - Comfy dtype: FLOAT
    - Python dtype: float
- start_percent
    - The'start_percent' parameter specifies the starting percentage to control network effects. It is important to control the transition area at the start of the split process.
    - Comfy dtype: FLOAT
    - Python dtype: float
- end_percent
    - The 'end_percent' parameter defines the end percentage for controlling network effects. It is essential to manage the transition area at the end of the split process.
    - Comfy dtype: FLOAT
    - Python dtype: float
## Optional
- segs_preprocessor
    - The optional'segs_preprocessor' parameter allows pre-processing before the split data is entered into the control network. It enhances the performance of the node by preparing the data in a way that is more conducive to controlling the network process.
    - Comfy dtype: SEGS_PREPROCESSOR
    - Python dtype: Callable
- control_image
    - The optional `control_image' parameter provides an additional image that can be used to influence the decision-making of the control network. It is particularly useful when additional context is needed to achieve a more accurate division.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image

# Output types
- segs
    - The'segs' output contains the fine-splitting data after the application control network. It represents the final result of node operations and is important for downstream processing.
    - Comfy dtype: SEGS
    - Python dtype: List[Tuple[Image, List[NamedTuple], BoundingBox, Label, ControlNetAdvancedWrapper]]

# Usage tips
- Infra type: GPU

# Source code
```
class ControlNetApplyAdvancedSEGS:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'segs': ('SEGS',), 'control_net': ('CONTROL_NET',), 'strength': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 10.0, 'step': 0.01}), 'start_percent': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1.0, 'step': 0.001}), 'end_percent': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.001})}, 'optional': {'segs_preprocessor': ('SEGS_PREPROCESSOR',), 'control_image': ('IMAGE',)}}
    RETURN_TYPES = ('SEGS',)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Util'

    def doit(self, segs, control_net, strength, start_percent, end_percent, segs_preprocessor=None, control_image=None):
        new_segs = []
        for seg in segs[1]:
            control_net_wrapper = core.ControlNetAdvancedWrapper(control_net, strength, start_percent, end_percent, segs_preprocessor, seg.control_net_wrapper, original_size=segs[0], crop_region=seg.crop_region, control_image=control_image)
            new_seg = SEG(seg.cropped_image, seg.cropped_mask, seg.confidence, seg.crop_region, seg.bbox, seg.label, control_net_wrapper)
            new_segs.append(new_seg)
        return ((segs[0], new_segs),)
```