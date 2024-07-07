# Documentation
- Class name: controlnetSimple
- Category: EasyUse/Loaders
- Output node: True
- Repo Ref: https://github.com/yolain/ComfyUI-Easy-Use.git

ContronetSimple nodes are designed to make it easier for users to use the control network to improve the output of the generation model. By receiving a set of images and a control network name, it exports an enhanced model pipe that integrates the effects of the control network. This node is very useful for users seeking to integrate control mechanisms to achieve more accurate and detailed results in the process of their generation.

# Input types
## Required
- pipe
    - The `pipe' parameter is a key input for the contralnet Simple node, which represents the entire generation model pipe. It includes models, conditional data and other relevant settings as necessary. These settings are essential for the proper functioning of the node. Pipe input directly affects the generation process and the final output, enabling the node to effectively apply the control network.
    - Comfy dtype: PIPE_LINE
    - Python dtype: Dict[str, Any]
- image
    - The 'image'parameter is the visual input of the controlnet Simple node. It is essential for the node to understand the context and desired direction of the production process. By incorporating the image into the control network, the node can produce output more in line with the user's visual intent.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- control_net_name
    - The `control_net_name' parameter is the key input to the designated node using the control network. It determines the control mechanism that will be applied to the generation of the model, affecting the quality of the final output and the degree of compliance with the user's creative vision.
    - Comfy dtype: CONTROL_NET
    - Python dtype: str
## Optional
- strength
    - The `strength' parameter is used to adjust the intensity of the influence of the control network on the generation process. This is an optional input that allows users to fine-tune the effects of the control network, balancing the level of control with the freedom of creation of the model.
    - Comfy dtype: FLOAT
    - Python dtype: float
- scale_soft_weights
    - The `scale_soft_rights' parameter is used to modify the softness of the control net weights. This input can be adjusted to achieve a smoother transition in the generation of output, providing more detailed control over the final visual result.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- pipe
    - The `pipe' output is an enhanced generation of model tubes modified by the control network application. It includes updated models and condition data, which now reflect the impact of the control network. This output is essential for the user to continue to use the modified pipe for generation.
    - Comfy dtype: PIPE_LINE
    - Python dtype: Dict[str, Any]
- positive
    - The `positive' output represents the refined condition data adjusted to the influence of the control network. It serves as a guide for the generation of models to produce outputs that are more precise and compatible with the creative intent of the user.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Tuple[Any, Dict[str, Any]]]
- negative
    - ‘negative’ output is an optimized condition data that offsets characteristics or elements that are not required during the generation process. It helps models learn from the guidance of the control network and avoids unintended outcomes.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Tuple[Any, Dict[str, Any]]]

# Usage tips
- Infra type: CPU

# Source code
```
class controlnetSimple:

    @classmethod
    def INPUT_TYPES(s):

        def get_file_list(filenames):
            return [file for file in filenames if file != 'put_models_here.txt' and 'lllite' not in file]
        return {'required': {'pipe': ('PIPE_LINE',), 'image': ('IMAGE',), 'control_net_name': (get_file_list(folder_paths.get_filename_list('controlnet')),)}, 'optional': {'control_net': ('CONTROL_NET',), 'strength': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 10.0, 'step': 0.01}), 'scale_soft_weights': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.001})}}
    RETURN_TYPES = ('PIPE_LINE', 'CONDITIONING', 'CONDITIONING')
    RETURN_NAMES = ('pipe', 'positive', 'negative')
    OUTPUT_NODE = True
    FUNCTION = 'controlnetApply'
    CATEGORY = 'EasyUse/Loaders'

    def controlnetApply(self, pipe, image, control_net_name, control_net=None, strength=1, scale_soft_weights=1):
        (positive, negative) = easyControlnet().apply(control_net_name, image, pipe['positive'], pipe['negative'], strength, 0, 1, control_net, scale_soft_weights)
        new_pipe = {'model': pipe['model'], 'positive': positive, 'negative': negative, 'vae': pipe['vae'], 'clip': pipe['clip'], 'samples': pipe['samples'], 'images': pipe['images'], 'seed': 0, 'loader_settings': pipe['loader_settings']}
        del pipe
        return (new_pipe, positive, negative)
```