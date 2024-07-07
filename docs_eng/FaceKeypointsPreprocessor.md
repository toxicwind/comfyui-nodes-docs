# Documentation
- Class name: FaceKeypointsPreprocessor
- Category: InstantID
- Output node: False
- Repo Ref: https://github.com/cubiq/ComfyUI_InstantID.git

The FaceKeypointsPreprocessor node is designed to enhance facial recognition tasks by pre-processing images to extract and use facial critical points. The node uses advanced facial analysis techniques to identify and process facial features, which are essential to improve the accuracy and efficiency of subsequent facial recognition models. By focusing on key facial points, the node contributes to a more detailed understanding of facial structures, thus contributing to more effective facial analysis.

# Input types
## Required
- faceanalysis
    - The Faceanalysis parameter is necessary because it provides a facial analysis model for image pre-processing and its associated features. It plays a key role in the detection and extraction of facial critical points and has a direct impact on the effectiveness of pre-processing.
    - Comfy dtype: FACEANALYSIS
    - Python dtype: InsightFaceModel
- image
    - The image parameter is an input image processed by FaceKeyPointsPreprocessor. It is the basis for node operations and is the source of the key point for extracting the facial. The quality and resolution of the image directly influences the accuracy of facial characterization tests.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image

# Output types
- face_kps
    - FaceKeypointsPreprocessor output, face_kps, is an indication of facial critical points extracted from input images. These critical points are important because they provide the basis for subsequent facial recognition and analysis missions and allow for more accurate identification and understanding of facial features.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class FaceKeypointsPreprocessor:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'faceanalysis': ('FACEANALYSIS',), 'image': ('IMAGE',)}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'preprocess_image'
    CATEGORY = 'InstantID'

    def preprocess_image(self, faceanalysis, image):
        face_kps = extractFeatures(faceanalysis, image, extract_kps=True)
        if face_kps is None:
            face_kps = torch.zeros_like(image)
            print(f'\x1b[33mWARNING: no face detected, unable to extract the keypoints!\x1b[0m')
        return (face_kps,)
```