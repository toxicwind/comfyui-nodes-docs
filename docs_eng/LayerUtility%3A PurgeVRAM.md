# Documentation
- Class name: PurgeVRAM
- Category: 😺dzNodes/LayerUtility/SystemIO
- Output node: True
- Repo Ref: https://github.com/chflame163/ComfyUI_LayerStyle

Cleans up the GPU visible. You can access any type of input, and when you go to this node, you will clear the VRAM and the RAM objects. They are usually placed after the node of the reasoned task, such as the VAE Decode node.

# Input types

## Required

- anything
    - Any input.
    - Comfy dtype: any
    - Python dtype: any

- purge_cache
    - Clear the cache.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

- purge_models
    - Clear the model.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

## Optional

- None

# Output types

- None

# Usage tips
- Infra type: CPU

# Source code
```python
class PurgeVRAM:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "anything": (any, {}),
                "purge_cache": ("BOOLEAN", {"default": True}),
                "purge_models": ("BOOLEAN", {"default": True}),
            },
            "optional": {
            }
        }

    RETURN_TYPES = ()
    FUNCTION = "purge_vram"
    CATEGORY = '😺dzNodes/LayerUtility/SystemIO'
    OUTPUT_NODE = True

    def purge_vram(self, anything, purge_cache, purge_models):
        import torch.cuda
        import gc
        import comfy.model_management
        if purge_cache:
            if torch.cuda.is_available():
                gc.collect()
                torch.cuda.empty_cache()
                torch.cuda.ipc_collect()
        if purge_models:
            comfy.model_management.unload_all_models()

        return (None,)