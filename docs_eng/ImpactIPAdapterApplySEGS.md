# Documentation
- Class name: IPAdapterApplySEGS
- Category: ImpactPack/Util
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

IPAdapterApplySEGS is designed to integrate and apply block masks as part of the ImpactPack tool package. Using the power of the IPAdapter framework, it adjusts images to reference images and allows the transmission of themes or styles. This node is essential for the task that requires accurate control of the generation process, ensuring that the output closely follows the aesthetic or subject matter elements required.

# Input types
## Required
- segs
    - The `segs' parameter is essential because it defines the segment mask that the node will handle. These masks are essential to guide the generation of images that meet specific criteria or constraints. The correct application of the parameters directly affects the ability of the node to produce accurate and relevant outputs.
    - Comfy dtype: SEGS
    - Python dtype: List[NamedTuple]
- ipadapter_pipe
    - The `ipadapter_pipe' parameter is a key component for achieving the integration of the IPAcapter model. It is responsible for seamless application of images to image reconciliation, which is essential for achieving the required style or theme shift in the image generated.
    - Comfy dtype: IPADAPTER_PIPE
    - Python dtype: Tuple[Any, ...]
- weight
    - The 'weight'parameter plays an important role in adjusting the impact of the reference image on the generation process. It allows fine-tuning of style or subject shift to ensure that the final output meets the user's expectations and is not over-dominant with the reference image.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- SEGS
    - The output `SEGS' represents a processed segment mask that is reconciled with the IPAcapter model. This output is important because it contains the ability to refine and adjust the input mask to better meet the required generation criteria.
    - Comfy dtype: SEGS
    - Python dtype: List[NamedTuple]

# Usage tips
- Infra type: GPU

# Source code
```
class IPAdapterApplySEGS:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'segs': ('SEGS',), 'ipadapter_pipe': ('IPADAPTER_PIPE',), 'weight': ('FLOAT', {'default': 0.7, 'min': -1, 'max': 3, 'step': 0.05}), 'noise': ('FLOAT', {'default': 0.4, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'weight_type': (['original', 'linear', 'channel penalty'], {'default': 'channel penalty'}), 'start_at': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1.0, 'step': 0.001}), 'end_at': ('FLOAT', {'default': 0.9, 'min': 0.0, 'max': 1.0, 'step': 0.001}), 'unfold_batch': ('BOOLEAN', {'default': False}), 'faceid_v2': ('BOOLEAN', {'default': False}), 'weight_v2': ('FLOAT', {'default': 1.0, 'min': -1, 'max': 3, 'step': 0.05}), 'context_crop_factor': ('FLOAT', {'default': 1.2, 'min': 1.0, 'max': 100, 'step': 0.1}), 'reference_image': ('IMAGE',)}, 'optional': {'combine_embeds': (['concat', 'add', 'subtract', 'average', 'norm average'],), 'neg_image': ('IMAGE',)}}
    RETURN_TYPES = ('SEGS',)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Util'

    def doit(self, segs, ipadapter_pipe, weight, noise, weight_type, start_at, end_at, unfold_batch, faceid_v2, weight_v2, context_crop_factor, reference_image, combine_embeds='concat', neg_image=None):
        if len(ipadapter_pipe) == 4:
            print(f'[Impact Pack] IPAdapterApplySEGS: Installed Inspire Pack is outdated.')
            raise Exception('Inspire Pack is outdated.')
        new_segs = []
        (h, w) = segs[0]
        if reference_image.shape[2] != w or reference_image.shape[1] != h:
            reference_image = tensor_resize(reference_image, w, h)
        for seg in segs[1]:
            context_crop_region = make_crop_region(w, h, seg.crop_region, context_crop_factor)
            cropped_image = crop_image(reference_image, context_crop_region)
            control_net_wrapper = core.IPAdapterWrapper(ipadapter_pipe, weight, noise, weight_type, start_at, end_at, unfold_batch, weight_v2, cropped_image, neg_image=neg_image, prev_control_net=seg.control_net_wrapper, combine_embeds=combine_embeds)
            new_seg = SEG(seg.cropped_image, seg.cropped_mask, seg.confidence, seg.crop_region, seg.bbox, seg.label, control_net_wrapper)
            new_segs.append(new_seg)
        return ((segs[0], new_segs),)
```