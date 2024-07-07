# Documentation
- Class name: DefaultImageForSEGS
- Category: ImpactPack/Util
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The 'doit' method for DefaultImageForSEGS nodes is designed to treat partitions by scaling them up to the size of the given image. It also provides an option to allow new crop-based areas to be used to cover existing cut images. This method is essential to prepare for further analysis or visualization of split data.

# Input types
## Required
- segs
    - The'segs' parameter is the grouping of split objects that the node will process. It is essential for the operation of the node, as it determines the data that will be scaled and may overlay the image.
    - Comfy dtype: SEGS
    - Python dtype: List[SEG]
- image
    - The 'image'parameter indicates a reference image that will scale the split. It is a key input because it determines the size of the split data that must be matched for downstream processing.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
## Optional
- override
    - The 'override' parameter is a boolean symbol, and when set to True, the indicator node produces a new crop image for splits, ignoring any existing crop. This is very useful for refreshing the crop based on the updated split data.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- segs
    - Output'segs' contains treated split objects. Each object is scaled up to match the size of the input image, and if the 'override' parameter is set to True, it may be overwrite the image.
    - Comfy dtype: SEGS
    - Python dtype: Tuple[List[SEG], List[SEG]]

# Usage tips
- Infra type: CPU

# Source code
```
class DefaultImageForSEGS:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'segs': ('SEGS',), 'image': ('IMAGE',), 'override': ('BOOLEAN', {'default': True})}}
    RETURN_TYPES = ('SEGS',)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Util'

    def doit(self, segs, image, override):
        results = []
        segs = core.segs_scale_match(segs, image.shape)
        if len(segs[1]) > 0:
            if segs[1][0].cropped_image is not None:
                batch_count = len(segs[1][0].cropped_image)
            else:
                batch_count = len(image)
            for seg in segs[1]:
                if seg.cropped_image is not None and (not override):
                    cropped_image = seg.cropped_image
                else:
                    cropped_image = None
                    for i in range(0, batch_count):
                        ref_image = image[i].unsqueeze(0)
                        cropped_image2 = crop_image(ref_image, seg.crop_region)
                        if cropped_image is None:
                            cropped_image = cropped_image2
                        else:
                            cropped_image = torch.cat((cropped_image, cropped_image2), dim=0)
                new_seg = SEG(cropped_image, seg.cropped_mask, seg.confidence, seg.crop_region, seg.bbox, seg.label, seg.control_net_wrapper)
                results.append(new_seg)
            return ((segs[0], results),)
        else:
            return (segs,)
```