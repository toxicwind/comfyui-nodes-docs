# Documentation
- Class name: DetailerPipeToBasicPipe
- Category: ImpactPack/Pipe
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The Detailer Pipeto Basic Pipe node is designed to transform detailed plumbing structures into more basic forms. It plays a key role in simplifying complex data processing workflows by extracting the basic components of detailed pipelines and reforming them into standard, more manageable structures.

# Input types
## Required
- detailer_pipe
    - The detailer_pipe parameter is essential for the operation of the node because it provides a detailed pipeline structure that needs to be converted. It is the main input parameter, which determines the processing and output of the node.
    - Comfy dtype: DETAILER_PIPE
    - Python dtype: Tuple[torch.nn.Module, torch.Tensor, torch.nn.Module, torch.Tensor, torch.Tensor]

# Output types
- base_basic_pipe
    - Base_basic_pipe is a simplified version of the pipeline that focuses on the core elements required for basic operations. It is important because it allows process processing and easier integration into the wider system.
    - Comfy dtype: BASIC_PIPE
    - Python dtype: Tuple[torch.nn.Module, torch.Tensor, torch.nn.Module, torch.Tensor, torch.Tensor]
- refiner_basic_pipe
    - Another output, refiener_basic_pipe, is a basic pipeline derived from a detailed structure. It is essential to focus more on and optimize the application of the pipeline.
    - Comfy dtype: BASIC_PIPE
    - Python dtype: Tuple[torch.nn.Module, torch.Tensor, torch.nn.Module, torch.Tensor, torch.Tensor]

# Usage tips
- Infra type: CPU

# Source code
```
class DetailerPipeToBasicPipe:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'detailer_pipe': ('DETAILER_PIPE',)}}
    RETURN_TYPES = ('BASIC_PIPE', 'BASIC_PIPE')
    RETURN_NAMES = ('base_basic_pipe', 'refiner_basic_pipe')
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Pipe'

    def doit(self, detailer_pipe):
        (model, clip, vae, positive, negative, _, _, _, _, _, refiner_model, refiner_clip, refiner_positive, refiner_negative) = detailer_pipe
        pipe = (model, clip, vae, positive, negative)
        refiner_pipe = (refiner_model, refiner_clip, vae, refiner_positive, refiner_negative)
        return (pipe, refiner_pipe)
```