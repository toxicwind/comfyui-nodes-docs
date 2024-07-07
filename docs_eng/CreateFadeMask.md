# Documentation
- Class name: CreateFadeMask
- Category: KJNodes/deprecated
- Output node: False
- Repo Ref: https://github.com/kijai/ComfyUI-KJNodes.git

The CreateFademask node is designed to generate a series of gradient masks that smooth the transition from one opaque to another. It uses plug-in techniques to create visually attractive gradients, especially for visual effects and image processing applications.

# Input types
## Required
- invert
    - The `invert' parameter decides whether a inverse gradient mask is needed, which is essential for some visual effects that require an inverse and non-transparent transition.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- frames
    - The `frames' parameter specifies the number of frames in the gradient mask sequence, which directly affects the duration and spacing of the gradient effect.
    - Comfy dtype: INT
    - Python dtype: int
- width
    - The `width' parameter sets the width of each frame in the gradient mask, affecting the overall size of the output.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - The `height' parameter defines the height of each frame in the gradient mask, which is essential for maintaining the horizontal and visual consistency of the output.
    - Comfy dtype: INT
    - Python dtype: int
- interpolation
    - The `interpolation' parameter selects the type of plug for the gradient effect, which can significantly change the appearance of the transition between the non-transparent levels.
    - Comfy dtype: COMBO['linear', 'ease_in', 'ease_out', 'ease_in_out']
    - Python dtype: str
- start_level
    - The `start_level' parameter sets the initial opacity level of the gradient mask, which is a key factor in determining the starting point of the gradient effect.
    - Comfy dtype: FLOAT
    - Python dtype: float
- midpoint_level
    - The `midpoint_level' parameter indicates the opacity level of the midpoint of the gradient mask sequence, which helps to control the gradient speed at the centre of the transition.
    - Comfy dtype: FLOAT
    - Python dtype: float
- end_level
    - The `end_level' parameter determines the ultimate level of opacity of the gradient mask, which determines how the gradient effect ends.
    - Comfy dtype: FLOAT
    - Python dtype: float
- midpoint_frame
    - The `midpoint_frame' parameter specifies the frame within which the midpoint of the gradient effect occurs and allows for precise control of the timing of the transition.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- mask
    - The output `mask' is a series of gradient masks that represent an opaque transition from the initial to the end level and are created on the basis of the specified parameters.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class CreateFadeMask:
    RETURN_TYPES = ('MASK',)
    FUNCTION = 'createfademask'
    CATEGORY = 'KJNodes/deprecated'

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'invert': ('BOOLEAN', {'default': False}), 'frames': ('INT', {'default': 2, 'min': 2, 'max': 255, 'step': 1}), 'width': ('INT', {'default': 256, 'min': 16, 'max': 4096, 'step': 1}), 'height': ('INT', {'default': 256, 'min': 16, 'max': 4096, 'step': 1}), 'interpolation': (['linear', 'ease_in', 'ease_out', 'ease_in_out'],), 'start_level': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'midpoint_level': ('FLOAT', {'default': 0.5, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'end_level': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'midpoint_frame': ('INT', {'default': 0, 'min': 0, 'max': 4096, 'step': 1})}}

    def createfademask(self, frames, width, height, invert, interpolation, start_level, midpoint_level, end_level, midpoint_frame):

        def ease_in(t):
            return t * t

        def ease_out(t):
            return 1 - (1 - t) * (1 - t)

        def ease_in_out(t):
            return 3 * t * t - 2 * t * t * t
        batch_size = frames
        out = []
        image_batch = np.zeros((batch_size, height, width), dtype=np.float32)
        if midpoint_frame == 0:
            midpoint_frame = batch_size // 2
        for i in range(batch_size):
            if i <= midpoint_frame:
                t = i / midpoint_frame
                if interpolation == 'ease_in':
                    t = ease_in(t)
                elif interpolation == 'ease_out':
                    t = ease_out(t)
                elif interpolation == 'ease_in_out':
                    t = ease_in_out(t)
                color = start_level - t * (start_level - midpoint_level)
            else:
                t = (i - midpoint_frame) / (batch_size - midpoint_frame)
                if interpolation == 'ease_in':
                    t = ease_in(t)
                elif interpolation == 'ease_out':
                    t = ease_out(t)
                elif interpolation == 'ease_in_out':
                    t = ease_in_out(t)
                color = midpoint_level - t * (midpoint_level - end_level)
            color = np.clip(color, 0, 255)
            image = np.full((height, width), color, dtype=np.float32)
            image_batch[i] = image
        output = torch.from_numpy(image_batch)
        mask = output
        out.append(mask)
        if invert:
            return (1.0 - torch.cat(out, dim=0),)
        return (torch.cat(out, dim=0),)
```