# Documentation
- Class name: ImageUpscaleWithModel
- Category: image/upscaling
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The ImageUpscaleWithModel node is designed to use the specified magnification model to enhance the resolution of the input image. It is smart to manage memory to prevent memory errors and ensure smooth magnification processes. Node functions are focused on improving image quality without sacrificing performance.

# Input types
## Required
- upscale_model
    - The upscale_model parameter is essential for the node because it defines the model used to magnify the image. It directly affects the sampling process and the quality of the image generated.
    - Comfy dtype: torch.nn.Module
    - Python dtype: torch.nn.Module
- image
    - The image parameter is necessary because it represents the input image data that the node will process. Its structure and content are key to the success of the sampling operation.
    - Comfy dtype: torch.Tensor
    - Python dtype: torch.Tensor

# Output types
- IMAGE
    - The output parameter IMAGE represents a magnified image of the node. It marks the successful completion of the sampling process and is the main result of the node function.
    - Comfy dtype: torch.Tensor
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class ImageUpscaleWithModel:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'upscale_model': ('UPSCALE_MODEL',), 'image': ('IMAGE',)}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'upscale'
    CATEGORY = 'image/upscaling'

    def upscale(self, upscale_model, image):
        device = model_management.get_torch_device()
        upscale_model.to(device)
        in_img = image.movedim(-1, -3).to(device)
        free_memory = model_management.get_free_memory(device)
        tile = 512
        overlap = 32
        oom = True
        while oom:
            try:
                steps = in_img.shape[0] * comfy.utils.get_tiled_scale_steps(in_img.shape[3], in_img.shape[2], tile_x=tile, tile_y=tile, overlap=overlap)
                pbar = comfy.utils.ProgressBar(steps)
                s = comfy.utils.tiled_scale(in_img, lambda a: upscale_model(a), tile_x=tile, tile_y=tile, overlap=overlap, upscale_amount=upscale_model.scale, pbar=pbar)
                oom = False
            except model_management.OOM_EXCEPTION as e:
                tile //= 2
                if tile < 128:
                    raise e
        upscale_model.cpu()
        s = torch.clamp(s.movedim(-3, -1), min=0, max=1.0)
        return (s,)
```