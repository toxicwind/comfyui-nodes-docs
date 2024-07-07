# Documentation
- Class name: ApplyInstantIDAdvanced
- Category: ImageProcessing
- Output node: False
- Repo Ref: https://github.com/cubiq/ComfyUI_InstantID.git

The ApplyInstantIDAdvanced node applies advanced image-processing techniques through the use of control networks and reconciliation input to enhance facial recognition.

# Input types
## Required
- instantid
    - InstantID is essential for the identification and tracking of individuals in image data as the only identifier for node processing.
    - Comfy dtype: INSTANTID
    - Python dtype: str
- insightface
    - InsightFace provides the analytical framework required for facial characterization and identification, which is essential for the function of the node.
    - Comfy dtype: FACEANALYSIS
    - Python dtype: str
- control_net
    - Control networks are essential to guide facial analysis at nodes to ensure that facial features are handled accurately and efficiently.
    - Comfy dtype: CONTROL_NET
    - Python dtype: str
- image
    - Image input is essential for the operation of nodes and provides visual data for facial recognition and enhancement.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image
- model
    - Model parameters are essential for the application of advanced facial recognition algorithms at nodes and for improving the accuracy of results.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- positive
    - Entering into the reconciliation is essential to perfect the facial recognition process to ensure that node output is accurate and relevant results.
    - Comfy dtype: CONDITIONING
    - Python dtype: str
- negative
    - Negative adjustment input helps filter off irrelevant or incorrect facial features and enhances the ability of nodes to produce accurate results.
    - Comfy dtype: CONDITIONING
    - Python dtype: str
## Optional
- ip_weight
    - The IP weight parameters affect the importance given to InstantID in facial recognition and the overall accuracy and relevance of the results.
    - Comfy dtype: FLOAT
    - Python dtype: float
- cn_strength
    - Control of network strength parameters adjusts the impact of the network on facial analysis and affects the accuracy and effectiveness of node operations.
    - Comfy dtype: FLOAT
    - Python dtype: float
- start_at
    - Start_at parameters define the beginning of facial characterization analysis, which is important for concentrating nodes processing in specific areas of the image.
    - Comfy dtype: FLOAT
    - Python dtype: float
- end_at
    - End_at parameters specify the end of the facial profiling paradigm to ensure that nodes are treated in the relevant parts of the image.
    - Comfy dtype: FLOAT
    - Python dtype: float
- noise
    - Noise parameters introduce controlled randomity in facial recognition, which can help to improve the stamina of node results.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- output_image
    - The output images are the result of node operations, showing enhanced facial features and improved identification capabilities.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image
- output_results
    - The output results include detailed information on the facial identification process, including the characteristics of the identification and the confidence points to which it corresponds.
    - Comfy dtype: DICT
    - Python dtype: Dict[str, Any]

# Usage tips
- Infra type: GPU

# Source code
```
class ApplyInstantIDAdvanced(ApplyInstantID):

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'instantid': ('INSTANTID',), 'insightface': ('FACEANALYSIS',), 'control_net': ('CONTROL_NET',), 'image': ('IMAGE',), 'model': ('MODEL',), 'positive': ('CONDITIONING',), 'negative': ('CONDITIONING',), 'ip_weight': ('FLOAT', {'default': 0.8, 'min': 0.0, 'max': 3.0, 'step': 0.01}), 'cn_strength': ('FLOAT', {'default': 0.8, 'min': 0.0, 'max': 10.0, 'step': 0.01}), 'start_at': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1.0, 'step': 0.001}), 'end_at': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.001}), 'noise': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1.0, 'step': 0.1})}, 'optional': {'image_kps': ('IMAGE',), 'mask': ('MASK',)}}
```