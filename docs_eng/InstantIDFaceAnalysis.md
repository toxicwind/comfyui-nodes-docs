# Documentation
- Class name: InstantIDFaceAnalysis
- Category: InstantID
- Output node: False
- Repo Ref: https://github.com/cubiq/ComfyUI_InstantID.git

InstantIDface Analysis, a node for the implementation of high-level facial analysis, uses pre-training models to identify and analyse facial characteristics and properties and applies to applications that require accurate facial recognition and demographic analysis.

# Input types
## Required
- provider
    - The provider parameter is critical to the performance environment of the facial analysis node. It determines the computational backend to be used for facial analysis tasks, affecting the performance and efficiency of the node.
    - Comfy dtype: COMBO['CPU', 'CUDA', 'ROCM']
    - Python dtype: str

# Output types
- FACEANALYSIS
    - The output of the InstantIDface Analysis node is a detailed facial analysis that contains insights from imported facial data. This output is important because it provides the basis for further analysis or decision-making processes.
    - Comfy dtype: Tuple[FaceAnalysis]
    - Python dtype: Tuple[FaceAnalysis]

# Usage tips
- Infra type: CPU

# Source code
```
class InstantIDFaceAnalysis:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'provider': (['CPU', 'CUDA', 'ROCM'],)}}
    RETURN_TYPES = ('FACEANALYSIS',)
    FUNCTION = 'load_insight_face'
    CATEGORY = 'InstantID'

    def load_insight_face(self, provider):
        model = FaceAnalysis(name='antelopev2', root=INSIGHTFACE_DIR, providers=[provider + 'ExecutionProvider'])
        model.prepare(ctx_id=0, det_size=(640, 640))
        return (model,)
```