# Documentation
- Class name: CR_ModulePipeLoader
- Category: Comfyroll/Pipe/Module
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_ModulePipeLoader is a node that aims to integrate models and data types into a pipeline. It facilitates seamless processing of models, potential indications and other conditionality factors, enabling complex operations to be carried out in a structured and efficient manner.

# Input types
## Optional
- model
    - Model parameters are essential for defining the core algorithm structure for node operations. It determines the type of model to be loaded, thus significantly influencing the processing capacity and results of node operations.
    - Comfy dtype: MODEL
    - Python dtype: Union[str, Path]
- pos
    - Entering the reconciliation is essential for a node that requires directional guidance or enhancement. It provides a point of reference that will help channel the function of the node to the desired result.
    - Comfy dtype: CONDITIONING
    - Python dtype: Union[str, List[str]]
- neg
    - Negative adjustment parameters, as a balance of positive input, allow nodes to fine-tune their response and avoid undesirable effects by incorporating suppression signals.
    - Comfy dtype: CONDITIONING
    - Python dtype: Union[str, List[str]]
- latent
    - This parameter enables the node to use compressed data, and improves the efficiency of data processing.
    - Comfy dtype: LATENT
    - Python dtype: Union[torch.Tensor, List[torch.Tensor]]
- vae
    - VAE parameters are essential for using the generation model to synthesize data nodes. It allows nodes to use the capabilities of VAE to create new data examples.
    - Comfy dtype: VAE
    - Python dtype: Union[str, Path]
- clip
    - CLIP parameters are essential for nodes using multi-module learning methods, especially tasks involving visual and text data. They enable nodes to integrate CLIP models to enhance cross-module interactions.
    - Comfy dtype: CLIP
    - Python dtype: Union[str, Path]
- controlnet
    - A control network parameter is essential for a node that requires a structured flow control or condition execution path. It provides a framework for managing node operating logic based on predefined conditions.
    - Comfy dtype: CONTROL_NET
    - Python dtype: Union[str, Path]
- image
    - Image input is fundamental for processing the nodes of visual data. It allows nodes to take and operate visual content, which is essential for a wide range of image-based applications.
    - Comfy dtype: IMAGE
    - Python dtype: Union[str, Path, PIL.Image]
- seed
    - Seed parameters ensure the replicability of results by providing fixed points for random number generation. It is particularly important during random processes where consistent results are required.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- pipe
    - Pipe output represents the built pipe, which covers all inputs and settings provided to nodes. It is a key component for further processing or analysis within the system.
    - Comfy dtype: PIPE_LINE
    - Python dtype: Tuple[Any, ...]
- show_help
    - Show_help output provides links to node documents and guides users on how to use the node effectively. It is an important resource for understanding node functions and potential usages.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_ModulePipeLoader:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {}, 'optional': {'model': ('MODEL',), 'pos': ('CONDITIONING',), 'neg': ('CONDITIONING',), 'latent': ('LATENT',), 'vae': ('VAE',), 'clip': ('CLIP',), 'controlnet': ('CONTROL_NET',), 'image': ('IMAGE',), 'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615})}}
    RETURN_TYPES = ('PIPE_LINE', 'STRING')
    RETURN_NAMES = ('pipe', 'show_help')
    FUNCTION = 'pipe_input'
    CATEGORY = icons.get('Comfyroll/Pipe/Module')

    def pipe_input(self, model=0, pos=0, neg=0, latent=0, vae=0, clip=0, controlnet=0, image=0, seed=0):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Pipe-Nodes#cr-module-pipe-loader'
        pipe_line = (model, pos, neg, latent, vae, clip, controlnet, image, seed)
        return (pipe_line, show_help)
```