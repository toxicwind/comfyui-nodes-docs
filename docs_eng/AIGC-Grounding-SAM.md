# Documentation
- Class name: AIGCImageRemoveBackgroundRembg
- Category: AIGC
- Output node: False
- Repo Ref: https://github.com/esheep/esheep_custom_nodes.git

AGCIMAGERemoveBackgroundRembg node is designed to remove the image background seamlessly using advanced image partitioning techniques. It uses SAM (Segment Anything Model) and GroundingDono models to achieve high-quality background removal, providing users with clean prospective objects for further use.

# Input types
## Required
- image
    - The image parameter is essential for the operation of the node, as it is the source from which the background will be removed. The quality and format of the image directly influences the execution of the node and the accuracy of the mask generated.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- text
    - Text parameters are used to guide the split process to ensure that areas of interest are correctly identified and retained. They play a key role in the ability of nodes to understand and process the contents of images.
    - Comfy dtype: STRING
    - Python dtype: str
- sam_model_name
    - The sam_model_name parameter is assigned to the pre-training SAM model for partitioning. The selection of the model affects the performance of nodes and the quality of the partition results.
    - Comfy dtype: COMBO["sam_vit_h_4b8939.pth", "sam_vit_l_0b3195.pth", "sam_vit_b_01ec64.pth"]
    - Python dtype: str
- groundingdino_model_name
    - The groundingdino_model_name parameter determines the Grounding DNO model that should be used to identify areas of interest in the image. This parameter is essential for accurate object identification and partitioning.
    - Comfy dtype: COMBO["GroundingDINO_SwinT_OGC", "GroundingDINO_SwinB"]
    - Python dtype: str
## Optional
- dino_box_threshold
    - dino_box_threshold parameters are used to set thresholds for Grouping DNO model output. It influences which areas are considered for partition.
    - Comfy dtype: FLOAT
    - Python dtype: float
- highest_confidence_mode
    - This is an important factor in determining the quality of the final output.
    - Comfy dtype: INT
    - Python dtype: int
- return_index
    - Return_index parameters indicate which of the created masks should be returned. It allows the user to select the desired output from multiple split results.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- new_image
    - New_image output contains processed images and the background has been removed for further use or display.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- mask
    - The mask output provides split binary expressions, highlighting areas that have been removed from the original image.
    - Comfy dtype: MASK
    - Python dtype: np.ndarray

# Usage tips
- Infra type: GPU

# Source code
```
class AIGCImageRemoveBackgroundRembg:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'text': ('STRING', {'multiline': False}), 'sam_model_name': (['sam_vit_h_4b8939.pth', 'sam_vit_l_0b3195.pth', 'sam_vit_b_01ec64.pth'],), 'groundingdino_model_name': (['GroundingDINO_SwinT_OGC', 'GroundingDINO_SwinB'],), 'dino_box_threshold': ('FLOAT', {'default': 0.3, 'min': -100.0, 'max': 100.0, 'step': 0.1}), 'highest_confidence_mode': ('INT', {'default': 0, 'min': 0, 'max': 1, 'step': 1}), 'return_index': ('INT', {'default': 0})}}
    RETURN_TYPES = ('IMAGE', 'MASK')
    FUNCTION = 'sam'
    CATEGORY = 'AIGC'

    def sam(self, image, text: str, sam_model_name: str, groundingdino_model_name: str, dino_box_threshold: float, highest_confidence_mode: int, return_index: int):
        (new_image, mask) = sam_with_groundingdino(image, text, sam_model_name, groundingdino_model_name, dino_box_threshold, bool(highest_confidence_mode), return_index)
        return (new_image, mask)
```