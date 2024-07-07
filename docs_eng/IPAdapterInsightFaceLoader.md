# Documentation
- Class name: IPAdapterInsightFaceLoader
- Category: ipadapter/loaders
- Output node: False
- Repo Ref: https://github.com/cubiq/ComfyUI_IPAdapter_plus.git

The IPAdapterInsightFaceLoader node is designed to facilitate loading and preparation of the InsightFace model for facial analysis. It encapsifies the complexity of the initialization model using the specified implementation delivery program and abstractes the underlying technical details. The node ensures that the InsightFace model is ready for advanced operations, such as facial testing and recognition.

# Input types
## Required
- provider
    - The `provider' parameter assigns an implementation delivery program for the InsightFace model. This is essential for determining how the model will be implemented, which may significantly affect performance and compatibility with different hardware settings.
    - Comfy dtype: str
    - Python dtype: str

# Output types
- model
    - The `model' output represents the loaded and prepared InsightFace model, which can be used for facial analysis operations. It is the end result of node functions and provides users with advanced interfaces to interact with the model.
    - Comfy dtype: FaceAnalysis
    - Python dtype: insightface.app.FaceAnalysis

# Usage tips
- Infra type: CPU

# Source code
```
class IPAdapterInsightFaceLoader:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'provider': (['CPU', 'CUDA', 'ROCM'],)}}
    RETURN_TYPES = ('INSIGHTFACE',)
    FUNCTION = 'load_insightface'
    CATEGORY = 'ipadapter/loaders'

    def load_insightface(self, provider):
        return (insightface_loader(provider),)
```