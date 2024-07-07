# Documentation
- Class name: VAEEncodeBatched
- Category: Video Helper Suite 🎥🅥🅗🅢/batched nodes
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite.git

The VAEEncodeBatched node is designed to efficiently encode video frames into potential spaces using VAEs. It uses the specified batch-size processing frames to optimize the amount of resources and throughput and make them suitable for processing large amounts of video data.

# Input types
## Required
- pixels
    - The `pixels' parameter is the key input to the VAEEncodeBatched node, as it represents the original video frame that needs to be coded. Its efficient processing is essential for the quality of the node performance and the potential spatial expression generated.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- vae
    - The `vae' parameter specifies the node that will be used to encode the video frames as a variable self-encoder model. It is essential for determining the structure and properties of the potential space of the frame code.
    - Comfy dtype: VAE
    - Python dtype: torch.nn.Module
## Optional
- per_batch
    - The `per_batch' parameter defines the size of each pixel batch to be handled by the node. It is important for managing memory use and computing efficiency, especially when processing high-resolution or large video frames.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- samples
    - The `samples' output of the VAEncodeBatched node contains a potential coding space for entering video frames. This output is important because it forms the basis for further analysis or processing in downstream tasks.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class VAEEncodeBatched:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'pixels': ('IMAGE',), 'vae': ('VAE',), 'per_batch': ('INT', {'default': 16, 'min': 1})}}
    CATEGORY = 'Video Helper Suite 🎥🅥🅗🅢/batched nodes'
    RETURN_TYPES = ('LATENT',)
    FUNCTION = 'encode'

    def encode(self, vae, pixels, per_batch):
        t = []
        for start_idx in range(0, pixels.shape[0], per_batch):
            try:
                sub_pixels = vae.vae_encode_crop_pixels(pixels[start_idx:start_idx + per_batch])
            except:
                sub_pixels = VAEEncode.vae_encode_crop_pixels(pixels[start_idx:start_idx + per_batch])
            t.append(vae.encode(sub_pixels[:, :, :, :3]))
        return ({'samples': torch.cat(t, dim=0)},)
```