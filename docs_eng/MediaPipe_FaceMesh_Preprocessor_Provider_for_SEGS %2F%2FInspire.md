# Documentation
- Class name: MediaPipe_FaceMesh_Preprocessor_Provider_for_SEGS
- Category: InspirePack/SEGS/ControlNet
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Inspire-Pack.git

The node uses the MediaPipe FaceMesh model to pre-process the image in order to semantically divide the task, test the face and generate the corresponding mask. It enhances the partitioning of the input image by focusing on facial features, which is essential for applications requiring detailed surface cutting.

# Input types
## Required
- max_faces
    - This parameter determines the maximum number of faces that the model should detect in the input image. It is essential to control the particle size of the facial test and affects the balance between performance and accuracy.
    - Comfy dtype: INT
    - Python dtype: int
- min_confidence
    - The minimum confidence threshold for facial tests. It filters the detection below this confidence level, which is important to ensure the quality of the partition mask generated.
    - Comfy dtype: FLOAT
    - Python dtype: float
- resolution_upscale_by
    - This parameter enters the resolution of the image by scaling the factor in whole. Magnifying the image increases the accuracy of the detection, but it may increase the computational need.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- SEGS_PREPROCESSOR
    - Output is a pre-processed image with detected facial and partition mask as input to a downstream semantic split task.
    - Comfy dtype: SEGS_PREPROCESSOR
    - Python dtype: object

# Usage tips
- Infra type: CPU

# Source code
```
class MediaPipe_FaceMesh_Preprocessor_Provider_for_SEGS:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'max_faces': ('INT', {'default': 10, 'min': 1, 'max': 50, 'step': 1}), 'min_confidence': ('FLOAT', {'default': 0.5, 'min': 0.01, 'max': 1.0, 'step': 0.01}), 'resolution_upscale_by': ('FLOAT', {'default': 1.0, 'min': 0.5, 'max': 100, 'step': 0.1})}}
    RETURN_TYPES = ('SEGS_PREPROCESSOR',)
    FUNCTION = 'doit'
    CATEGORY = 'InspirePack/SEGS/ControlNet'

    def doit(self, max_faces, min_confidence, resolution_upscale_by):
        obj = MediaPipe_FaceMesh_Preprocessor_wrapper(max_faces, min_confidence, upscale_factor=resolution_upscale_by)
        return (obj,)
```