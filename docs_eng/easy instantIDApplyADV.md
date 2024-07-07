# Documentation
- Class name: instantIDApplyAdvanced
- Category: EasyUse/Adapter
- Output node: True
- Repo Ref: https://github.com/yolain/ComfyUI-Easy-Use.git

The node is designed to improve the quality and specificity of the output image processing by integrating various features and control functions. It produces refined results by applying complex image processing techniques, controlling networks and combinations of condition input.

# Input types
## Required
- pipe
    - The pipe parameter is essential for the operation of the node because it provides the basic data structure of the image processing workflow. It contains all the necessary information, including positive and negative data.
    - Comfy dtype: PIPE_LINE
    - Python dtype: Dict
- image
    - The image parameter is essential for the node because it is the main input to the image-processing task. It directly affects the output and the validity of its application conversion.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- instantid_file
    - Instantid_file parameters are important because they provide the necessary files related to the identity of the object in the image. They are used to ensure the accuracy and relevance of image processing.
    - Comfy dtype: FILEPATH
    - Python dtype: List[str]
- insightface
    - The insightface parameter is important because it determines the back end for facial recognition and processing. It affects the ability of nodes to accurately identify and enhance facial features.
    - Comfy dtype: STRING
    - Python dtype: Union[str]
- control_net_name
    - The control_net_name parameter is essential because it assigns a control network to guide image processing. It ensures that the output meets expectations of aesthetic or thematic constraints.
    - Comfy dtype: FILEPATH
    - Python dtype: List[str]
- cn_strength
    - cn_strength parameter adjustment control network impacts on image processing. It plays a key role in balancing the desired control with the natural appearance of the processing image.
    - Comfy dtype: FLOAT
    - Python dtype: float
- cn_soft_weights
    - cn_soft_rights parameters determine the softness of control of network applications. It affects the subtleness of changes made to images, ensuring smooth and detailed conversions.
    - Comfy dtype: FLOAT
    - Python dtype: float
- weight
    - The weight parameter affects the overall intensity of image processing. It is a key factor in controlling the degree of enhancement or modification of the image.
    - Comfy dtype: FLOAT
    - Python dtype: float
- start_at
    - Start_at parameters define the starting point for application of image-processing effects. This is important to ensure that changes are applied gradually and controlledly.
    - Comfy dtype: FLOAT
    - Python dtype: float
- end_at
    - End_at parameters specify the point where the image processing effect is fully applied. This is essential to determine the scope and extent of the conversion.
    - Comfy dtype: FLOAT
    - Python dtype: float
- noise
    - The noise parameter introduces a certain amount of randomity into image processing, which contributes to diversity and unpredictability of results. This is essential for a more natural and less uniform appearance.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- pipe
    - Pipe output is a modified version of the initial data structure and now contains the results of image processing. It is important because it covers the contribution of nodes to the entire workflow.
    - Comfy dtype: PIPE_LINE
    - Python dtype: Dict
- model
    - Model output represents the updated state of the converted image or image-processing model. It is a direct reflection of the main function of the node and the effectiveness of the application technology.
    - Comfy dtype: MODEL
    - Python dtype: torch.Tensor
- positive
    - It is important to provide feedback to the subsequent phase of the pipeline and enhances the coherence and consistency of the final output.
    - Comfy dtype: CONDITIONING
    - Python dtype: Dict
- negative
    - Negative output contains node optimized or filtered condition data. It plays a key role in shaping the final output by ensuring that unwanted elements are excluded.
    - Comfy dtype: CONDITIONING
    - Python dtype: Dict

# Usage tips
- Infra type: GPU

# Source code
```
class instantIDApplyAdvanced(instantID):

    def __init__(self):
        super().__init__()
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'pipe': ('PIPE_LINE',), 'image': ('IMAGE',), 'instantid_file': (folder_paths.get_filename_list('instantid'),), 'insightface': (['CPU', 'CUDA', 'ROCM'],), 'control_net_name': (folder_paths.get_filename_list('controlnet'),), 'cn_strength': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 10.0, 'step': 0.01}), 'cn_soft_weights': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.001}), 'weight': ('FLOAT', {'default': 0.8, 'min': 0.0, 'max': 5.0, 'step': 0.01}), 'start_at': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1.0, 'step': 0.001}), 'end_at': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.001}), 'noise': ('FLOAT', {'default': 0.35, 'min': 0.0, 'max': 1.0, 'step': 0.05})}, 'optional': {'image_kps': ('IMAGE',), 'mask': ('MASK',), 'control_net': ('CONTROL_NET',), 'positive': ('CONDITIONING',), 'negative': ('CONDITIONING',)}, 'hidden': {'prompt': 'PROMPT', 'extra_pnginfo': 'EXTRA_PNGINFO', 'my_unique_id': 'UNIQUE_ID'}}
    RETURN_TYPES = ('PIPE_LINE', 'MODEL', 'CONDITIONING', 'CONDITIONING')
    RETURN_NAMES = ('pipe', 'model', 'positive', 'negative')
    OUTPUT_NODE = True
    FUNCTION = 'apply_advanced'
    CATEGORY = 'EasyUse/Adapter'

    def apply_advanced(self, pipe, image, instantid_file, insightface, control_net_name, cn_strength, cn_soft_weights, weight, start_at, end_at, noise, image_kps=None, mask=None, control_net=None, positive=None, negative=None, prompt=None, extra_pnginfo=None, my_unique_id=None):
        positive = positive if positive is not None else pipe['positive']
        negative = negative if negative is not None else pipe['negative']
        return self.run(pipe, image, instantid_file, insightface, control_net_name, cn_strength, cn_soft_weights, weight, start_at, end_at, noise, image_kps, mask, control_net, positive, negative, prompt, extra_pnginfo, my_unique_id)
```