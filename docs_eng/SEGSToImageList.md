# Documentation
- Class name: SEGSToImageList
- Category: ImpactPack/Util
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

SEGSToImageList is designed to convert the split data into a list of image lengths. It divides the size of the data and processes the backup images provided to match, or if the image is not provided, generates the default load. This node plays a key role in the image data that is ready for further analysis or visualization in the ImpactPack application package.

# Input types
## Required
- segs
    - The's segs' parameter is the split data pool processed by the node. It is essential for the operation of the node, as it directly affects the content and structure of the list of output images.
    - Comfy dtype: SEGS
    - Python dtype: List[SEG]
## Optional
- fallback_image_opt
    - The optional `fallback_image_opt' parameter provides a default image that is used when there is no available split image. It ensures that nodes produce consistent output even when data are incomplete.
    - Comfy dtype: IMAGE
    - Python dtype: Optional[torch.Tensor]

# Output types
- results
    - The'reults' output is a list of image lengths derived from split data. It represents the main output of nodes and is important for downstream tasks that require image data.
    - Comfy dtype: IMAGE
    - Python dtype: List[torch.Tensor]

# Usage tips
- Infra type: CPU

# Source code
```
class SEGSToImageList:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'segs': ('SEGS',)}, 'optional': {'fallback_image_opt': ('IMAGE',)}}
    RETURN_TYPES = ('IMAGE',)
    OUTPUT_IS_LIST = (True,)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Util'

    def doit(self, segs, fallback_image_opt=None):
        results = list()
        if fallback_image_opt is not None:
            segs = core.segs_scale_match(segs, fallback_image_opt.shape)
        for seg in segs[1]:
            if seg.cropped_image is not None:
                cropped_image = to_tensor(seg.cropped_image)
            elif fallback_image_opt is not None:
                cropped_image = to_tensor(crop_image(fallback_image_opt, seg.crop_region))
            else:
                cropped_image = empty_pil_tensor()
            results.append(cropped_image)
        if len(results) == 0:
            results.append(empty_pil_tensor())
        return (results,)
```