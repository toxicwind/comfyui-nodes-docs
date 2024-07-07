# Documentation
- Class name: LoopStart_IMAGE
- Category: DragNUWA
- Output node: False
- Repo Ref: https://github.com/chaojie/ComfyUI-DragNUWA.git

The node facilitates the start-up of the cycle structure, enabling the processing of image data in an iterative manner. Its role is crucial in a scenario that requires repeated applications for image operation or analysis.

# Input types
## Required
- first_loop
    - The first element of the cycle, which sets the initial state for subsequent overlaps, is crucial because it determines the starting point and the nature of the operation of the cycle.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image
## Optional
- loop
    - It represents the continuation of the cycle, allowing the link to be operated. It is important because it makes possible the progress of the cycle and the processing of complex image-processing tasks.
    - Comfy dtype: LOOP
    - Python dtype: None

# Output types
- IMAGE
    - The output is the result of a circular operation of image data and contains a envelope containing the cumulative effects of the iterative process.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image

# Usage tips
- Infra type: CPU

# Source code
```
class LoopStart_IMAGE:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'first_loop': ('IMAGE',), 'loop': ('LOOP',)}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'run'
    CATEGORY = 'DragNUWA'

    def run(self, first_loop, loop):
        if hasattr(loop, 'next'):
            return (loop.next,)
        return (first_loop,)

    @classmethod
    def IS_CHANGED(s, first_loop, loop):
        if hasattr(loop, 'next'):
            return id(loop.next)
        return float('NaN')
```