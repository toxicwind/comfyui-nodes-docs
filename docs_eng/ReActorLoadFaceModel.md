# Documentation
- Class name: LoadFaceModel
- Category: 🌌 ReActor
- Output node: False
- Repo Ref: https://github.com/Gourieff/comfyui-reactor-node.git

The node facilitates loading and preparation of facial identification models, which are essential for subsequent facial processing tasks. It covers the complexity of model retrieval and ensures the use of appropriate models based on input specifications, thereby increasing the flexibility and adaptability of the system.

# Input types
## Required
- face_model
    - The `face_model' parameter is essential because it determines which facial recognition model the node will load. It affects the entire processing process by determining the particular features and algorithms to be applied in subsequent operations.
    - Comfy dtype: COMBO[get_model_names(get_facemodels())]
    - Python dtype: Union[str, None]

# Output types
- FACE_MODEL
    - The output represents the facial identification model loaded, which is a key component of the further facial analysis and processing task. It encapsulates the features learned by the model and is prepared for downstream operations.
    - Comfy dtype: Face
    - Python dtype: insightface.app.common.Face

# Usage tips
- Infra type: CPU

# Source code
```
class LoadFaceModel:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'face_model': (get_model_names(get_facemodels),)}}
    RETURN_TYPES = ('FACE_MODEL',)
    FUNCTION = 'load_model'
    CATEGORY = '🌌 ReActor'

    def load_model(self, face_model):
        self.face_model = face_model
        self.face_models_path = FACE_MODELS_PATH
        if self.face_model != 'none':
            face_model_path = os.path.join(self.face_models_path, self.face_model)
            out = load_face_model(face_model_path)
        else:
            out = None
        return (out,)
```