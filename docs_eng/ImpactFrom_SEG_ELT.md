# Documentation
- Class name: From_SEG_ELT
- Category: ImpactPack/Util
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The From_SEG_ELT node is designed to process and transform SEG_ELT objects into structured formats containing images, masks, and various metadata. It plays a key role in preparing data for further analysis and operation in the ImpactPack practical application package.

# Input types
## Required
- seg_elt
    - The seg_elt parameter is essential because it represents the core input of the node. It contains image data and associated metadata for processing. The function of the node depends to a large extent on the integrity and format of the seg_elt input.
    - Comfy dtype: SEG_ELT
    - Python dtype: SEG_ELT

# Output types
- seg_elt
    - The seg_elt output is the original SEG_ELT object that transmits nodes and may be enhanced or modified during the processing.
    - Comfy dtype: SEG_ELT
    - Python dtype: SEG_ELT
- cropped_image
    - The cropped_image output provides a tablet of image data, which is essential for a machine learning model that requires a volume input format.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- cropped_mask
    - Cropped_mask output is a volume that depicts the area of interest in the image and is a key component of the split task.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor
- crop_region
    - The crop_region output specifies the coordinates and dimensions of the area to be cropped in the image, which is essential for understanding the spatial context of the data.
    - Comfy dtype: SEG_ELT_crop_region
    - Python dtype: Tuple[int, int, int, int]
- bbox
    - The bbox output provides the boundary frame coordinates of objects of interest in the image, which are essential for object detection and positioning tasks.
    - Comfy dtype: SEG_ELT_bbox
    - Python dtype: List[int]
- control_net_wrapper
    - The control_net_wrapper output covers additional control information or parameters that may need to be used for advanced processing or analysis.
    - Comfy dtype: SEG_ELT_control_net_wrapper
    - Python dtype: Any
- confidence
    - Confidence output reflects certainty in partitioning or classification results, which is important for assessing the reliability of model output.
    - Comfy dtype: FLOAT
    - Python dtype: float
- label
    - Label output assigns a classification identifier to processed data, which is essential for classification and comment purposes.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class From_SEG_ELT:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'seg_elt': ('SEG_ELT',)}}
    RETURN_TYPES = ('SEG_ELT', 'IMAGE', 'MASK', 'SEG_ELT_crop_region', 'SEG_ELT_bbox', 'SEG_ELT_control_net_wrapper', 'FLOAT', 'STRING')
    RETURN_NAMES = ('seg_elt', 'cropped_image', 'cropped_mask', 'crop_region', 'bbox', 'control_net_wrapper', 'confidence', 'label')
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Util'

    def doit(self, seg_elt):
        cropped_image = to_tensor(seg_elt.cropped_image) if seg_elt.cropped_image is not None else None
        return (seg_elt, cropped_image, to_tensor(seg_elt.cropped_mask), seg_elt.crop_region, seg_elt.bbox, seg_elt.control_net_wrapper, seg_elt.confidence, seg_elt.label)
```