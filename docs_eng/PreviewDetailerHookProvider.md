# Documentation
- Class name: PreviewDetailerHookProvider
- Category: ImpactPack/Util
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The PreviewDetailerHookProvider node is designed to promote image enhancement and detailed previews. It adjusts image quality by applying hooks to ensure that output is both detailed and optimizes visual clarity. The node plays a key role in the pre-processing phase of image-processing tasks, focusing on quality to meet specific requirements.

# Input types
## Required
- quality
    - The `quality' parameter is essential for determining the level of detail of the output image. It directly affects the visual authenticity of the image and the file size, allowing for a balance between quality and performance.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- unique_id
    - The `unique_id' parameter is the only identifier for the operation to ensure that each process can be tracked and managed separately. It is particularly important for asymptomatic operations that may run simultaneously with multiple tasks.
    - Comfy dtype: UNIQUE_ID
    - Python dtype: str

# Output types
- DETAILER_HOOK
    - The `DETAILER_HOOK' output provides a mechanism for further processing and enhancement of image details. It is important for the task of requiring complex operation and fine-tuning of image quality.
    - Comfy dtype: DETAILER_HOOK
    - Python dtype: PreviewDetailerHook
- UPSCALER_HOOK
    - The `UPSCALER_HOOK' output is used to magnify images, increase their resolution without compromising clarity. It is essential for applications that require high visibility visual effects.
    - Comfy dtype: UPSCALER_HOOK
    - Python dtype: PreviewDetailerHook

# Usage tips
- Infra type: CPU

# Source code
```
class PreviewDetailerHookProvider:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'quality': ('INT', {'default': 95, 'min': 20, 'max': 100})}, 'hidden': {'unique_id': 'UNIQUE_ID'}}
    RETURN_TYPES = ('DETAILER_HOOK', 'UPSCALER_HOOK')
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Util'

    def doit(self, quality, unique_id):
        hook = hooks.PreviewDetailerHook(unique_id, quality)
        return (hook, hook)
```