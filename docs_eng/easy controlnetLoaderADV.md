# Documentation
- Class name: controlnetAdvanced
- Category: EasyUse/Loaders
- Output node: True
- Repo Ref: https://github.com/yolain/ComfyUI-Easy-Use.git

The controlnetAdvanced node is designed to facilitate the application of the control network to modify and enhance image data according to the specified conditions. It functions by integrating the control signal into the image processing process, allowing fine-tuning and conditional conversions.

# Input types
## Required
- pipe
    - The `pipe' parameter is essential because it carries the entire image treatment flow line data, including models and samples. This is essential for the proper functioning of nodes and for generating the desired output.
    - Comfy dtype: PIPE_LINE
    - Python dtype: Dict[str, Any]
- image
    - The 'image'parameter is the input image that will be processed by the node. It is the basis for the operation and provides the basis for all conversions and enhancements.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- control_net_name
    - The 'control_net_name' parameter specifies the control network for image processing. It is important because it determines the type of control applied to the image and affects the end result.
    - Comfy dtype: CONTROL_NET
    - Python dtype: str
## Optional
- control_net
    - The `control_net' parameter is an optional control network input that can be provided directly by the user. It provides a method of customizing the control network for processing without the need to load it from a file.
    - Comfy dtype: CONTROL_NET
    - Python dtype: Optional[torch.nn.Module]
- strength
    - The `strength' parameter adjusts the intensity of the network's influence on the image. It is important for fine-tuning the conversion of the image.
    - Comfy dtype: FLOAT
    - Python dtype: float
- start_percent
    - The `start_percent' parameter defines the starting point of the control network for image effects. It is important because it determines when the control will be applied in the processing of the flow line.
    - Comfy dtype: FLOAT
    - Python dtype: float
- end_percent
    - The `end_percent' parameter sets the end point for controlling the impact of the network, and affects how the effects of the network fade when the image is processed.
    - Comfy dtype: FLOAT
    - Python dtype: float
- scale_soft_weights
    - The `scale_soft_rights' parameter adjusts the softness of network weight control, which helps to achieve smoother transitions and less abrupt changes in images.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- pipe
    - The `pipe' output is an updated image treatment stream that has been adapted to the control network. It is important because it represents the final state of the control network's waterline after application.
    - Comfy dtype: PIPE_LINE
    - Python dtype: Dict[str, Any]
- positive
    - The `positive' output contains images of positive conditions obtained after the application of the control network. It is essential to assess the effectiveness of the control network in achieving the desired visual enhancement.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Tuple[Any, Dict[str, Any]]]
- negative
    - The `negative' output consists of negative condition images as a comparison of `positive' output. It is important to understand the range of controls that the control network can impose on the image.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Tuple[Any, Dict[str, Any]]]

# Usage tips
- Infra type: CPU

# Source code
```
class controlnetAdvanced:

    @classmethod
    def INPUT_TYPES(s):

        def get_file_list(filenames):
            return [file for file in filenames if file != 'put_models_here.txt' and 'lllite' not in file]
        return {'required': {'pipe': ('PIPE_LINE',), 'image': ('IMAGE',), 'control_net_name': (get_file_list(folder_paths.get_filename_list('controlnet')),)}, 'optional': {'control_net': ('CONTROL_NET',), 'strength': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 10.0, 'step': 0.01}), 'start_percent': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1.0, 'step': 0.001}), 'end_percent': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.001}), 'scale_soft_weights': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.001})}}
    RETURN_TYPES = ('PIPE_LINE', 'CONDITIONING', 'CONDITIONING')
    RETURN_NAMES = ('pipe', 'positive', 'negative')
    OUTPUT_NODE = True
    FUNCTION = 'controlnetApply'
    CATEGORY = 'EasyUse/Loaders'

    def controlnetApply(self, pipe, image, control_net_name, control_net=None, strength=1, start_percent=0, end_percent=1, scale_soft_weights=1):
        (positive, negative) = easyControlnet().apply(control_net_name, image, pipe['positive'], pipe['negative'], strength, start_percent, end_percent, control_net, scale_soft_weights)
        new_pipe = {'model': pipe['model'], 'positive': positive, 'negative': negative, 'vae': pipe['vae'], 'clip': pipe['clip'], 'samples': pipe['samples'], 'images': pipe['images'], 'seed': 0, 'loader_settings': pipe['loader_settings']}
        del pipe
        return (new_pipe, positive, negative)
```