# Documentation
- Class name: instantIDApply
- Category: EasyUse/Adapter
- Output node: True
- Repo Ref: https://github.com/yolain/ComfyUI-Easy-Use.git

The instantIDApply node is designed to simplify the process of applying the sole identifier to a given image or data set and to facilitate the integration of models and control mechanisms to achieve the desired results.

# Input types
## Required
- pipe
    - The pipe parameter serves as the main channel for data flows within nodes, making possible the coordination of follow-up operations and integration of different components.
    - Comfy dtype: PIPE_LINE
    - Python dtype: Dict[str, Any]
- image
    - Image parameters are critical in providing visual data to nodes, which are essential for processing and analysis within the system.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image
- instantid_file
    - Instantid_file parameters are essential for the identification and management of the only identifier in the system to ensure the accuracy and consistency of data.
    - Comfy dtype: COMBO[folder_paths.get_filename_list('instantid')]
    - Python dtype: str
- insightface
    - Insightface parameters play an important role in determining the computational backend of facial analysis tasks, thus affecting the performance and efficiency of nodes.
    - Comfy dtype: COMBO[['CPU', 'CUDA', 'ROCM']]
    - Python dtype: str
- control_net_name
    - The control_net_name parameter is essential in the designation of the control network to be used, which shapes the overall behaviour and output of the nodes.
    - Comfy dtype: COMBO[folder_paths.get_filename_list('controlnet')]
    - Python dtype: str
- cn_strength
    - cn_strength parameter reconciliation controls the extent to which the network affects results and is an important tool for optimizing and fine-tuning point performance.
    - Comfy dtype: FLOAT
    - Python dtype: float
- cn_soft_weights
    - The cn_soft_rights parameters determine the softness of control of network influences and affect the subtleness of node adjustments.
    - Comfy dtype: FLOAT
    - Python dtype: float
- weight
    - Weight parameters are essential for balancing the contribution of different components within nodes, ensuring a harmonious integration of characteristics.
    - Comfy dtype: FLOAT
    - Python dtype: float
- start_at
    - The start_at parameter defines the starting point for node processing and lays the foundation for follow-up operations and results.
    - Comfy dtype: FLOAT
    - Python dtype: float
- end_at
    - End_at parameters mark the final point at which the node process ends and determine the scope and limits of the node function.
    - Comfy dtype: FLOAT
    - Python dtype: float
- noise
    - Noise parameters introduce random elements in the operation of nodes, contributing to the diversity and creativity of outcomes.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- pipe
    - Pipe output is a comprehensive indication of node processing data, wrapping the results and facilitating further transmission within the system.
    - Comfy dtype: PIPE_LINE
    - Python dtype: Dict[str, Any]
- model
    - Model output provides a refined and optimized version of the input model optimized by node processing capacity.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- positive
    - Postive output is a data set that represents desired results or characteristics and is used to guide and inform the follow-up process.
    - Comfy dtype: CONDITIONING
    - Python dtype: str
- negative
    - Negative output contains data representing non-expected results or characteristics as a reference for avoiding certain outcomes in future operations.
    - Comfy dtype: CONDITIONING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class instantIDApply(instantID):

    def __init__(self):
        super().__init__()
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'pipe': ('PIPE_LINE',), 'image': ('IMAGE',), 'instantid_file': (folder_paths.get_filename_list('instantid'),), 'insightface': (['CPU', 'CUDA', 'ROCM'],), 'control_net_name': (folder_paths.get_filename_list('controlnet'),), 'cn_strength': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 10.0, 'step': 0.01}), 'cn_soft_weights': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.001}), 'weight': ('FLOAT', {'default': 0.8, 'min': 0.0, 'max': 5.0, 'step': 0.01}), 'start_at': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1.0, 'step': 0.001}), 'end_at': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.001}), 'noise': ('FLOAT', {'default': 0.35, 'min': 0.0, 'max': 1.0, 'step': 0.05})}, 'optional': {'image_kps': ('IMAGE',), 'mask': ('MASK',), 'control_net': ('CONTROL_NET',)}, 'hidden': {'prompt': 'PROMPT', 'extra_pnginfo': 'EXTRA_PNGINFO', 'my_unique_id': 'UNIQUE_ID'}}
    RETURN_TYPES = ('PIPE_LINE', 'MODEL', 'CONDITIONING', 'CONDITIONING')
    RETURN_NAMES = ('pipe', 'model', 'positive', 'negative')
    OUTPUT_NODE = True
    FUNCTION = 'apply'
    CATEGORY = 'EasyUse/Adapter'

    def apply(self, pipe, image, instantid_file, insightface, control_net_name, cn_strength, cn_soft_weights, weight, start_at, end_at, noise, image_kps=None, mask=None, control_net=None, prompt=None, extra_pnginfo=None, my_unique_id=None):
        positive = pipe['positive']
        negative = pipe['negative']
        return self.run(pipe, image, instantid_file, insightface, control_net_name, cn_strength, cn_soft_weights, weight, start_at, end_at, noise, image_kps, mask, control_net, positive, negative, prompt, extra_pnginfo, my_unique_id)
```