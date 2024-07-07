# Documentation
- Class name: ToBasicPipe
- Category: ImpactPack/Pipe
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The TobasicPipe node is designed to simplify the assembly process of the basic flow lines for model operations. It efficiently combines components such as models, clips, VAEs and condition input into a coherent structure to facilitate follow-up tasks.

# Input types
## Required
- model
    - Model parameters are essential for the function of the node, as they represent the core algorithm components used to process input data. They are essential for the node to produce meaningful results.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- clip
    - The clip parameter plays an important role in the operation of the node, which defines the visual context for the treatment of the model. It is an integral part of the node's ability to interpret and operate visual data.
    - Comfy dtype: CLIP
    - Python dtype: torch.Tensor
- vae
    - The VAE parameter is essential for the node, as it relates to the conversion of the encoder component, which is essential for the potential expression of the generation or processing of data.
    - Comfy dtype: VAE
    - Python dtype: torch.nn.Module
- positive
    - The positive parameter is important for the node because it provides a positive input for guiding model behaviour towards the desired result.
    - Comfy dtype: CONDITIONING
    - Python dtype: torch.Tensor
- negative
    - Negative parameters are essential for the node because they provide a negative condition input that helps to fine-tune model output by directing the model away from desired results.
    - Comfy dtype: CONDITIONING
    - Python dtype: torch.Tensor

# Output types
- basic_pipe
    - Basic_pipe output is the main result of the node, which encapsulates the combined components into a single, coherent flow line for further processing or analysis.
    - Comfy dtype: BASIC_PIPE
    - Python dtype: Tuple[torch.nn.Module, torch.Tensor, torch.nn.Module, torch.Tensor, torch.Tensor]

# Usage tips
- Infra type: CPU

# Source code
```
class ToBasicPipe:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'clip': ('CLIP',), 'vae': ('VAE',), 'positive': ('CONDITIONING',), 'negative': ('CONDITIONING',)}}
    RETURN_TYPES = ('BASIC_PIPE',)
    RETURN_NAMES = ('basic_pipe',)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Pipe'

    def doit(self, model, clip, vae, positive, negative):
        pipe = (model, clip, vae, positive, negative)
        return (pipe,)
```