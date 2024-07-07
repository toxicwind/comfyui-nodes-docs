# Documentation
- Class name: CR_ModuleOutput
- Category: Comfyroll/Pipe/Module
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_ModuleOutput is a node designed to manage and modify the output of the current line to ensure that the flow of data is guided and optimized according to specific conditions and inputs.

# Input types
## Required
- pipe
    - The pipe parameter is necessary because it represents the main data stream that is being processed and converted by nodes.
    - Comfy dtype: PIPE_LINE
    - Python dtype: Tuple
## Optional
- model
    - Model parameters allow for the adaptation of the bottom model in the current line to influence the processing capacity of nodes.
    - Comfy dtype: MODEL
    - Python dtype: Any
- pos
    - poss parameters are used as a reconciliation input to refine output based on positive enhancements or expected results.
    - Comfy dtype: CONDITIONING
    - Python dtype: Any
- neg
    - The neg parameter introduces negative regulation that allows nodes to avoid unintended outcomes in the output.
    - Comfy dtype: CONDITIONING
    - Python dtype: Any
- latent
    - The latent parameter is used in the operation of incorporating the submersible variable into the node, adding complexity and nuances to the output.
    - Comfy dtype: LATENT
    - Python dtype: Any
- vae
    - The vae parameter is used to integrate the variable encoder function and enhance the ability of nodes to handle unsupervised learning tasks.
    - Comfy dtype: VAE
    - Python dtype: Any
- clip
    - The clip parameter enables the node to apply the CLIP model properties to improve contextual understanding and generation in the output.
    - Comfy dtype: CLIP
    - Python dtype: Any
- controlnet
    - The contronet parameter is used to introduce control mechanisms that can guide the behaviour of nodes and refine their output.
    - Comfy dtype: CONTROL_NET
    - Python dtype: Any
- image
    - Image parameters allow nodes to incorporate visual data and enhance the multi-module capability of the output.
    - Comfy dtype: IMAGE
    - Python dtype: Any
- seed
    - Seed parameters are essential to ensure the replicability and consistency of random operations at nodes.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- pipe
    - The output pipe is an input modification that is optimized and customized to meet the specific requirements and conditions set by the node.
    - Comfy dtype: PIPE_LINE
    - Python dtype: Tuple
- show_help
    - Show_help output provides a reference link to the document to further understand and guide the use of the node.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_ModuleOutput:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'pipe': ('PIPE_LINE',)}, 'optional': {'model': ('MODEL',), 'pos': ('CONDITIONING',), 'neg': ('CONDITIONING',), 'latent': ('LATENT',), 'vae': ('VAE',), 'clip': ('CLIP',), 'controlnet': ('CONTROL_NET',), 'image': ('IMAGE',), 'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615})}}
    RETURN_TYPES = ('PIPE_LINE', 'STRING')
    RETURN_NAMES = ('pipe', 'show_help')
    FUNCTION = 'pipe_output'
    CATEGORY = icons.get('Comfyroll/Pipe/Module')

    def pipe_output(self, pipe, model=None, pos=None, neg=None, latent=None, vae=None, clip=None, controlnet=None, image=None, seed=None):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Pipe-Nodes#cr-module-output'
        (new_model, new_pos, new_neg, new_latent, new_vae, new_clip, new_controlnet, new_image, new_seed) = pipe
        if model is not None:
            new_model = model
        if pos is not None:
            new_pos = pos
        if neg is not None:
            new_neg = neg
        if latent is not None:
            new_latent = latent
        if vae is not None:
            new_vae = vae
        if clip is not None:
            new_clip = clip
        if controlnet is not None:
            new_controlnet = controlnet
        if image is not None:
            new_image = image
        if seed is not None:
            new_seed = seed
        pipe = (new_model, new_pos, new_neg, new_latent, new_vae, new_clip, new_controlnet, new_image, new_seed)
        return (pipe, show_help)
```