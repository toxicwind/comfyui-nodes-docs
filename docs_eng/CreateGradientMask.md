# Documentation
- Class name: CreateGradientMask
- Category: KJNodes/masking/generate
- Output node: False
- Repo Ref: https://github.com/kijai/ComfyUI-KJNodes.git

The CreateGradient Mask node is designed to generate a gradient mask that can be used for various image processing tasks. It creates a mask by calculating linear gradients on image width and then adjusts the gradient to the current frame in the frame sequence. This allows for dynamic masking effects that can change over time or in different parts of the image.

# Input types
## Required
- invert
    - The 'invert'parameter determines whether a gradient mask is needed to reverse it. This is very useful for creating a complementary mask or for applying different effects in a shadow-based direction.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- frames
    - The 'frames'parameter specifies the number of frames to generate the masked version. It directly affects the batch size of the output and is essential for creating animated or time-changing effects.
    - Comfy dtype: INT
    - Python dtype: int
- width
    - The 'width' parameter sets the width of the gradient mask in pixels. It is essential to define the spatial resolution of the mask and the particle size of the effect gradient.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - The 'height' parameter sets the height of the gradient mask in pixels. It works with the 'width' parameter to determine the overall size of the mask.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- MASK
    - The output MASK is the volume of the gradient mask. It is the key component for the subsequent image operation and effect application.
    - Comfy dtype: TORCH.TENSOR
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class CreateGradientMask:
    RETURN_TYPES = ('MASK',)
    FUNCTION = 'createmask'
    CATEGORY = 'KJNodes/masking/generate'

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'invert': ('BOOLEAN', {'default': False}), 'frames': ('INT', {'default': 0, 'min': 0, 'max': 255, 'step': 1}), 'width': ('INT', {'default': 256, 'min': 16, 'max': 4096, 'step': 1}), 'height': ('INT', {'default': 256, 'min': 16, 'max': 4096, 'step': 1})}}

    def createmask(self, frames, width, height, invert):
        batch_size = frames
        out = []
        image_batch = np.zeros((batch_size, height, width), dtype=np.float32)
        for i in range(batch_size):
            gradient = np.linspace(1.0, 0.0, width, dtype=np.float32)
            time = i / frames
            offset_gradient = gradient - time
            image_batch[i] = offset_gradient.reshape(1, -1)
        output = torch.from_numpy(image_batch)
        mask = output
        out.append(mask)
        if invert:
            return (1.0 - torch.cat(out, dim=0),)
        return (torch.cat(out, dim=0),)
```