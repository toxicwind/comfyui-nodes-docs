# Documentation
- Class name: MediaPipeFaceMeshDetectorProvider
- Category: InspirePack/Detector
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Inspire-Pack.git

MediaPipeFaceMeshDectorProvider is designed to detect and divide facial features in images using the MediaPipe FaceMesh model. It provides the function of identifying and isolating facial features, such as facial contours, eyes, eyebrows and mouths. The main objective of this node is to enhance facial detail in images, which is particularly useful for applications involving facial recognition, animation or enhancement of low-resolution facial images.

# Input types
## Required
- max_faces
    - The parameter'max_faces' defines the maximum number of facials that the detector should identify in the input image. It plays a key role in controlling the scope of the detection process and is directly related to the performance and accuracy of the facial test.
    - Comfy dtype: INT
    - Python dtype: int
- face
    - Parameter 'face'indicates whether the detector should include the entire facial area in the testing process. Enable this option to ensure that the facial area is captured, which is essential for the task that requires full facial detail.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
## Optional
- mouth
    - When the'mouth'parameter is enabled, the indicator detector specifically recognizes the mouth area in the face detected. This is important for applications that require attention to mouth movements or emoticons.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- left_eyebrow
    - The parameter'left_eyebrow' allows left eyebrows to be included in facial signature tests. This is particularly useful for applications that require detailed analysis of facial expressions or reconstruction of facial features in images.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- left_eye
    - The parameter 'Left_eye' allows left-eye testing, which is important for detailed analysis of eye movements or applications that generate accurate facial characterizations.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- left_pupil
    - The parameter'left_pupil'is used to detect left pupils in the facial area. This is essential for applications that require accurate eye tracking or enhancing the clarity of the iris in the facial image.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- right_eyebrow
    - The parameter 'right_eyebrow'specifies whether the right eyebrow should be included in the test. It helps capture the full facial expression and is particularly useful for analysing or simulating applications for detailed facial movements.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- right_eye
    - The parameter 'right_eye' activates the right eye test, which is essential for a comprehensive facial test setting that allows detailed eye motion analysis or facial re-establishment.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- right_pupil
    - The parameter 'right_pupil', which monitors right pupils, plays a key role in applications that require eyes to track the details of the iris in high accuracy or enhanced facial images.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- bbox_detector
    - The output 'bbox_detector'provides the border frame coordinates of the detected face, which is essential for locating and further processing the facial area in the image.
    - Comfy dtype: BBOX_DETECTOR
    - Python dtype: List[Tuple[int, int, int, int]]
- segm_detector
    - The output'segm_detector' provides the detected split mask for the face, allowing for high accuracy isolation and operational facial features.
    - Comfy dtype: SEGM_DETECTOR
    - Python dtype: List[torch.Tensor]

# Usage tips
- Infra type: CPU

# Source code
```
class MediaPipeFaceMeshDetectorProvider:

    @classmethod
    def INPUT_TYPES(s):
        bool_true_widget = ('BOOLEAN', {'default': True, 'label_on': 'enable', 'label_off': 'disable'})
        bool_false_widget = ('BOOLEAN', {'default': False, 'label_on': 'enable', 'label_off': 'disable'})
        return {'required': {'max_faces': ('INT', {'default': 10, 'min': 1, 'max': 50, 'step': 1}), 'face': bool_true_widget, 'mouth': bool_false_widget, 'left_eyebrow': bool_false_widget, 'left_eye': bool_false_widget, 'left_pupil': bool_false_widget, 'right_eyebrow': bool_false_widget, 'right_eye': bool_false_widget, 'right_pupil': bool_false_widget}}
    RETURN_TYPES = ('BBOX_DETECTOR', 'SEGM_DETECTOR')
    FUNCTION = 'doit'
    CATEGORY = 'InspirePack/Detector'

    def doit(self, max_faces, face, mouth, left_eyebrow, left_eye, left_pupil, right_eyebrow, right_eye, right_pupil):
        bbox_detector = MediaPipeFaceMeshDetector(face, mouth, left_eyebrow, left_eye, left_pupil, right_eyebrow, right_eye, right_pupil, max_faces, is_segm=False)
        segm_detector = MediaPipeFaceMeshDetector(face, mouth, left_eyebrow, left_eye, left_pupil, right_eyebrow, right_eye, right_pupil, max_faces, is_segm=True)
        return (bbox_detector, segm_detector)
```