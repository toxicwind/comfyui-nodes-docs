# Documentation
- Class name: GetLatentCount
- Category: Video Helper Suite 🎥🅥🅗🅢/latent
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite.git

The GetLentCount node is designed to determine the number of potential samples that exist in the given input. It plays a key role in video processing workflows by providing basic counts that can be used for further analysis or operation of video data.

# Input types
## Required
- latents
    - The 'latents' parameter is a dictionary containing potential samples for video processing. It is essential for the operation of nodes, as it directly affects the number of samples to be returned.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]

# Output types
- count
    - The 'count' output provides the total number of potential samples processed at nodes. This count is important because it can be used to make decisions about the next steps of the video processing stream.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class GetLatentCount:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'latents': ('LATENT',)}}
    CATEGORY = 'Video Helper Suite 🎥🅥🅗🅢/latent'
    RETURN_TYPES = ('INT',)
    RETURN_NAMES = ('count',)
    FUNCTION = 'count_input'

    def count_input(self, latents: dict):
        return (latents['samples'].size(0),)
```