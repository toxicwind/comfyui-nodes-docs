# Documentation
- Class name: CR_ModuleInput
- Category: Comfyroll/Pipe/Module
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_ModuleInput is a node for processing and processing module input data. It plays a key role in initializing and managing data flows through the system to ensure that the necessary components are entered into the follow-up phase of the module operation.

# Input types
## Required
- pipe
    - The “pipe” parameter is necessary because it represents the main data structure of the node operation. It is through this parameter that the node receives input data, which are then processed and used in the work flow of the module.
    - Comfy dtype: PIPE_LINE
    - Python dtype: Tuple[Any, ...]

# Output types
- pipe
    - The " pipe " output is a continuation of the data stream and covers all processing information during the input phase. It serves as a channel for the transmission of data to subsequent nodes or modular components.
    - Comfy dtype: PIPE_LINE
    - Python dtype: Tuple[Any, ...]
- model
    - "model" output means the machine learning or AI model that the node may use in the operation of the module. It is a key component of any prediction or analysis task that the module design performs.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- pos
    - The “pos” output represents data on positive conditions that can be used to guide the generation or processing within the module towards more favourable outcomes.
    - Comfy dtype: CONDITIONING
    - Python dtype: torch.Tensor
- neg
    - The "neg" output represents the negative condition data, which is used to guide the operation of the module away from the desired result.
    - Comfy dtype: CONDITIONING
    - Python dtype: torch.Tensor
- latent
    - The “latent” output refers to the potential spatial expression of the data, which is a key concept in many machine learning models, especially in the context in which the models are generated.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
- vae
    - The "vae" output is associated with the transformational encoder component of the module, which plays an important role in the information in the potential space for coding and decoding.
    - Comfy dtype: VAE
    - Python dtype: torch.nn.Module
- clip
    - The "clip" output relates to the integration of the CLIP model in the module, which helps to align the generated content with the text description.
    - Comfy dtype: CLIP
    - Python dtype: torch.nn.Module
- controlnet
    - The “controlnet” output represents the control network within the module, which manages the direction and focus of the generation process.
    - Comfy dtype: CONTROL_NET
    - Python dtype: torch.nn.Module
- image
    - The "image" output is the visual expression of the data and is usually the end result of a module image generation or processing task.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image
- seed
    - The “seed” output provides random numbers or seeds for initialization of random number generators to ensure repeatability during the process.
    - Comfy dtype: INT
    - Python dtype: int
- show_help
    - The'show_help'output refers to the URL link to the node document, which provides additional information and guidance to users on how to use the node effectively.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_ModuleInput:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'pipe': ('PIPE_LINE',)}}
    RETURN_TYPES = ('PIPE_LINE', 'MODEL', 'CONDITIONING', 'CONDITIONING', 'LATENT', 'VAE', 'CLIP', 'CONTROL_NET', 'IMAGE', 'INT', 'STRING')
    RETURN_NAMES = ('pipe', 'model', 'pos', 'neg', 'latent', 'vae', 'clip', 'controlnet', 'image', 'seed', 'show_help')
    FUNCTION = 'flush'
    CATEGORY = icons.get('Comfyroll/Pipe/Module')

    def flush(self, pipe):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Pipe-Nodes#cr-module-input'
        (model, pos, neg, latent, vae, clip, controlnet, image, seed) = pipe
        return (pipe, model, pos, neg, latent, vae, clip, controlnet, image, seed, show_help)
```