# Documentation
- Class name: MediaPipeFaceMeshToSEGS
- Category: ImpactPack/Operation
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

MediaPipeFaceMeshToSEGS is designed to process facial images and convert them into structured split formats. It uses the MediaPipe FaceMesh model to detect facial tags and then creates a partition mask for each of the specified facial features. The node handles various facial components, such as face, mouth, eye, eye, eye and pupil, allowing for detailed separation according to the user's needs.

# Input types
## Required
- image
    - Enter the image is a key parameter for the MediaPipeFace MeshToSEGS node, as it is the basis for the facial tag detection and subsequent partition. The quality and resolution of the input image directly influences the accuracy of the facial characterization.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
## Optional
- crop_factor
    - The crop_factor parameter is used to adjust the size of the split output. It is an optional setting that allows users to control the detail level of the split by adjusting the output size.
    - Comfy dtype: FLOAT
    - Python dtype: float
- bbox_fill
    - The bbox_fill parameter determines whether the boundary box around the split facial features should be filled. This boolean sign can be used to define the look from the partition mask.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- crop_min_size
    - The crop_min_size parameter specifies the minimum size of the crop area around the features of the face. It ensures that the split output contains sufficient context around the detected mark.
    - Comfy dtype: INT
    - Python dtype: int
- drop_size
    - The drop_size parameter is used to control the spacing between partition points. It affects the density of the partition mask by determining the spacing between points.
    - Comfy dtype: INT
    - Python dtype: int
- dilation
    - The dilation parameter should be used to split the mask to increase the size of the partition area. This is particularly useful for fine-tuning the split of smaller facial features.
    - Comfy dtype: INT
    - Python dtype: int
- face
    - The face parameter is a boolean sign that indicates whether the facial area should be included in the partition. It allows for the selective separation of facial features according to the user's needs.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- mouth
    - The mouth parameter is a boolean symbol that determines whether the partition should include the mouth area. It provides flexibility when dividing certain facial features.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- left_eyebrow
    - The left_eyebrow parameter is used to change whether the left eyebrow is included in the split output. It allows the selective separation of individual facial features.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- left_eye
    - The left_eye parameter controls whether the left-eye area is part of the partition. It allows a specific facial area to be divided at the request of the user.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- left_pupil
    - The left_pupil parameter specifies whether the split should include the left pupil. It is used for the detailed division of the eye area.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- right_eyebrow
    - The right_eyebrow parameter is used to determine whether the right eyebrow should be included in the partition mask. It supports the split of facial features on request.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- right_eye
    - The right_eye parameter indicates whether the right-eye area should be included in the partition. It facilitates the division of a particular facial area as required.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- right_pupil
    - The right_pupil parameter controls whether the right pupil is included in the partition process. This is essential for the precise division of the eye area.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- SEGS
    - The SEGS output provides a structured representation of the segmentation of facial features. It includes the size of the partition mask and a list containing labels and corresponding partitions of the mass arrays of the mask.
    - Comfy dtype: COMBO[str, List[Tuple[int, torch.Tensor]]]
    - Python dtype: Tuple[int, List[Tuple[str, torch.Tensor]]]

# Usage tips
- Infra type: CPU

# Source code
```
class MediaPipeFaceMeshToSEGS:

    @classmethod
    def INPUT_TYPES(s):
        bool_true_widget = ('BOOLEAN', {'default': True, 'label_on': 'Enabled', 'label_off': 'Disabled'})
        bool_false_widget = ('BOOLEAN', {'default': False, 'label_on': 'Enabled', 'label_off': 'Disabled'})
        return {'required': {'image': ('IMAGE',), 'crop_factor': ('FLOAT', {'default': 3.0, 'min': 1.0, 'max': 100, 'step': 0.1}), 'bbox_fill': ('BOOLEAN', {'default': False, 'label_on': 'enabled', 'label_off': 'disabled'}), 'crop_min_size': ('INT', {'min': 10, 'max': MAX_RESOLUTION, 'step': 1, 'default': 50}), 'drop_size': ('INT', {'min': 1, 'max': MAX_RESOLUTION, 'step': 1, 'default': 1}), 'dilation': ('INT', {'default': 0, 'min': -512, 'max': 512, 'step': 1}), 'face': bool_true_widget, 'mouth': bool_false_widget, 'left_eyebrow': bool_false_widget, 'left_eye': bool_false_widget, 'left_pupil': bool_false_widget, 'right_eyebrow': bool_false_widget, 'right_eye': bool_false_widget, 'right_pupil': bool_false_widget}}
    RETURN_TYPES = ('SEGS',)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Operation'

    def doit(self, image, crop_factor, bbox_fill, crop_min_size, drop_size, dilation, face, mouth, left_eyebrow, left_eye, left_pupil, right_eyebrow, right_eye, right_pupil):
        result = core.mediapipe_facemesh_to_segs(image, crop_factor, bbox_fill, crop_min_size, drop_size, dilation, face, mouth, left_eyebrow, left_eye, left_pupil, right_eyebrow, right_eye, right_pupil)
        return (result,)
```