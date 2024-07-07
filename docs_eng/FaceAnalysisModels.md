# Documentation
- Class name: FaceAnalysisModels
- Category: FaceAnalysis
- Output node: False
- Repo Ref: https://github.com/cubiq/ComfyUI_FaceAnalysis.git

Methodology `load_models'is designed to initialize and load the models needed for facial analysis missions. It is essential for setting the operating environment with appropriate models and providers, ensuring that subsequent facial analysis operations can be performed effectively.

# Input types
## Required
- library
    - Parameters `library'specifies the facial library to be used. It is essential to determine which models and algorithms will be loaded for facial testing and identification tasks.
    - Comfy dtype: "str"
    - Python dtype: str
- provider
    - The parameter `provider'is specified as the backend for the execution of the model. It is important because it affects the performance of the model and its compatibility with the hardware of the system.
    - Comfy dtype: COMBO["CPU", "CUDA", "DirectML", "OpenVINO", "ROCM", "CoreML"]
    - Python dtype: str

# Output types
- out
    - The parameter `out'contains loaded models and relevant information. It is important because it provides the necessary tools for subsequent facial analysis operations.
    - Comfy dtype: Dict[str, Any]
    - Python dtype: Dict[str, Union[FaceAnalysis, dlib.face_detector, dlib.shape_predictor, dlib.face_recognition_model_v1]]

# Usage tips
- Infra type: GPU

# Source code
```
class FaceAnalysisModels:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'library': (INSTALLED_LIBRARIES,), 'provider': (['CPU', 'CUDA', 'DirectML', 'OpenVINO', 'ROCM', 'CoreML'],)}}
    RETURN_TYPES = ('ANALYSIS_MODELS',)
    FUNCTION = 'load_models'
    CATEGORY = 'FaceAnalysis'

    def load_models(self, library, provider):
        out = {}
        if library == 'insightface':
            out = {'library': library, 'detector': FaceAnalysis(name='buffalo_l', root=INSIGHTFACE_DIR, providers=[provider + 'ExecutionProvider'])}
            out['detector'].prepare(ctx_id=0, det_size=(640, 640))
        else:
            out = {'library': library, 'detector': dlib.get_frontal_face_detector(), 'shape_predict': dlib.shape_predictor(os.path.join(DLIB_DIR, 'shape_predictor_68_face_landmarks.dat')), 'face_recog': dlib.face_recognition_model_v1(os.path.join(DLIB_DIR, 'dlib_face_recognition_resnet_model_v1.dat'))}
        return (out,)
```