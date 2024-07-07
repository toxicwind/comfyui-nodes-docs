# Documentation
- Class name: RestoreFace
- Category: 🌌 ReActor
- Output node: False
- Repo Ref: https://github.com/Gourieff/comfyui-reactor-node.git

RestoreFace nodes are designed to enhance and restore facial features in images using advanced facial restoration models. It improves the visual quality of facials by using in-depth learning techniques, which are particularly useful for applications requiring high-quality facial images.

# Input types
## Required
- image
    - The image parameter is critical to the facial recovery process and provides the source material for facial restoration. It has a direct impact on the quality and accuracy of facial restoration.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image or torch.Tensor
- facedetection
    - The faceDetection parameter specifies the detection model that is used to identify the face in the input image. It is essential for accurate facial positioning, which is a prerequisite for effective facial recovery.
    - Comfy dtype: COMBO[retinaface_resnet50,retinaface_mobile0.25,YOLOv5l,YOLOv5n]
    - Python dtype: str
- model
    - Model parameters determine the facial restoration model to be applied and specify the algorithms and techniques to be used to enhance facial characteristics.
    - Comfy dtype: COMBO[get_model_names(get_restorers)]
    - Python dtype: str
- visibility
    - Visible parameters are adjusted to restore the level of transparency in the face, allowing fine-tuning of the degree of mixing of the original and recovery features.
    - Comfy dtype: FLOAT
    - Python dtype: float
- codeformer_weight
    - The codeformer_weight parameter affects the contribution of the CodeFormer model in the recovery process, with higher values emphasizing the impact of the model on the final result.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- output_image
    - The output image represents the final result of facial recovery, in which the image's face has been enhanced and restored to a higher quality.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image or torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class RestoreFace:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'facedetection': (['retinaface_resnet50', 'retinaface_mobile0.25', 'YOLOv5l', 'YOLOv5n'],), 'model': (get_model_names(get_restorers),), 'visibility': ('FLOAT', {'default': 1, 'min': 0.0, 'max': 1, 'step': 0.05}), 'codeformer_weight': ('FLOAT', {'default': 0.5, 'min': 0.0, 'max': 1, 'step': 0.05})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'execute'
    CATEGORY = '🌌 ReActor'

    def __init__(self):
        self.face_helper = None

    def execute(self, image, model, visibility, codeformer_weight, facedetection):
        result = reactor.restore_face(self, image, model, visibility, codeformer_weight, facedetection)
        return (result,)
```