# Documentation
- Class name: ReencodeLatentPipe
- Category: ImpactPack/Util
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

ReencodeLatentPipe is a node used to facilitate the conversion of potential space expressions. It operates by recoding samples in potential space using a variable self-codifier (VAE). This node is essential for tasks that require operation or comparison of potential expressions between different VAE models.

# Input types
## Required
- samples
    - The “samples” parameter is essential because it indicates potential spatial data that needs to be recoded. It is the main input of nodes and has a direct impact on the processing and output of nodes.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
- tile_mode
    - The tile_mode parameter determines the treatment of pixel flattens during the recoding process. It is essential to control the behavior of nodes with regard to pixel data structures.
    - Comfy dtype: COMBO['None', 'Both', 'Decode(input) only', 'Encode(output) only']
    - Python dtype: str
- input_basic_pipe
    - The "input_basic_pipe" parameter is a composite input, including the initial VAE model used to decode potential samples. It plays an important role in the initial stages of the recoding process.
    - Comfy dtype: BASIC_PIPE
    - Python dtype: Tuple[Any, ...]
- output_basic_pipe
    - The "output_basic_pipe " parameter includes the ultimate VAE model that encodes the potential recoded samples. It is a key component of the final output of the node.
    - Comfy dtype: BASIC_PIPE
    - Python dtype: Tuple[Any, ...]

# Output types
- latent_samples
    - The “latet_samples” output represents potential space data that have been recoded. It is the result of node operations and is important for further analysis or processing in the follow-up task.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class ReencodeLatentPipe:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'samples': ('LATENT',), 'tile_mode': (['None', 'Both', 'Decode(input) only', 'Encode(output) only'],), 'input_basic_pipe': ('BASIC_PIPE',), 'output_basic_pipe': ('BASIC_PIPE',)}}
    CATEGORY = 'ImpactPack/Util'
    RETURN_TYPES = ('LATENT',)
    FUNCTION = 'doit'

    def doit(self, samples, tile_mode, input_basic_pipe, output_basic_pipe):
        (_, _, input_vae, _, _) = input_basic_pipe
        (_, _, output_vae, _, _) = output_basic_pipe
        return ReencodeLatent().doit(samples, tile_mode, input_vae, output_vae)
```