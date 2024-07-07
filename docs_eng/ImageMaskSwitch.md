# Documentation
- Class name: ImageMaskSwitch
- Category: ImpactPack/Util
- Output node: True
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The ImageMaskSwitch node is designed to select the path to be entered by images and masks based on the selection parameters. It allows multiple images to be selected for further processing or analysis - the mask is correct, ensuring that only the required pair is passed on to the workflow.

# Input types
## Required
- select
    - The'select' parameter determines which image to use - the mask is right. It is vital because it directly influences the output of the node by selecting the appropriate pair based on its integer value.
    - Comfy dtype: INT
    - Python dtype: int
- images1
    - The 'images1' parameter means considering the first set of images to be used for switch operations. When'select' is set to 1, it plays an important role in the function of the node, as it will become an output set of images.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image or torch.Tensor
## Optional
- mask1_opt
    - The'mask1_opt' parameter corresponds to an optional mask corresponding to 'images1'. When'select' is 1 and wants to contain the mask of the image in the output, it becomes relevant.
    - Comfy dtype: MASK
    - Python dtype: PIL.Image or torch.Tensor
- images2_opt
    - The 'images2_opt' parameter represents the second group of selected images for switch operations. Use when'select' is set to 2.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image or torch.Tensor
- mask2_opt
    - The'mask2_opt' parameter corresponds to an optional mask corresponding to 'images2_opt'. When'select' is 2 and the output requires a mask with the image, it is considered.
    - Comfy dtype: MASK
    - Python dtype: PIL.Image or torch.Tensor
- images3_opt
    - The 'images3_opt' parameter indicates that the third group of selected images is operated by the switch. Use the'select' when set to 3 and requires a third group of images as output.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image or torch.Tensor
- mask3_opt
    - The'mask3_opt' parameter corresponds to an optional mask corresponding to 'images3_opt'. When'select' is 3 and the output requires a mask with the image, it is used.
    - Comfy dtype: MASK
    - Python dtype: PIL.Image or torch.Tensor
- images4_opt
    - The 'images4_opt' parameter indicates that a fourth group of selected images is operated by a switch. Use the'select' when set to 4 and requires a fourth group of images as an output.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image or torch.Tensor
- mask4_opt
    - The'mask4_opt' parameter corresponds to an optional mask corresponding to 'images4_opt'. When'select' is 4 and wishes to include the mask of the image in the output, it is considered.
    - Comfy dtype: MASK
    - Python dtype: PIL.Image or torch.Tensor

# Output types
- IMAGE
    - Output 'IMAGE' represents an image set selected on the basis of'select' input parameters. It is a key element of node function because it determines the flow of visual data within the system.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image or torch.Tensor
- MASK
    - Output 'MASK' corresponds to the mask of the selected image set. It is important when it needs to be analysed or processed together with the image.
    - Comfy dtype: MASK
    - Python dtype: PIL.Image or torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class ImageMaskSwitch:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'select': ('INT', {'default': 1, 'min': 1, 'max': 4, 'step': 1}), 'images1': ('IMAGE',)}, 'optional': {'mask1_opt': ('MASK',), 'images2_opt': ('IMAGE',), 'mask2_opt': ('MASK',), 'images3_opt': ('IMAGE',), 'mask3_opt': ('MASK',), 'images4_opt': ('IMAGE',), 'mask4_opt': ('MASK',)}}
    RETURN_TYPES = ('IMAGE', 'MASK')
    OUTPUT_NODE = True
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Util'

    def doit(self, select, images1, mask1_opt=None, images2_opt=None, mask2_opt=None, images3_opt=None, mask3_opt=None, images4_opt=None, mask4_opt=None):
        if select == 1:
            return (images1, mask1_opt)
        elif select == 2:
            return (images2_opt, mask2_opt)
        elif select == 3:
            return (images3_opt, mask3_opt)
        else:
            return (images4_opt, mask4_opt)
```