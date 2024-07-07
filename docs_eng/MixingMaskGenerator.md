# Documentation
- Class name: MixingMaskGeneratorNode
- Category: mask/generation
- Output node: False
- Repo Ref: https://github.com/ttulttul/ComfyUI-Iterative-Mixer

The node is designed to generate noise masks for the iterative mixing process and provides a flexible mechanism for creating various types of masks that improve the quality and results of the mixing.

# Input types
## Required
- mask_type
    - The mask type parameter determines the type of noise mask to be generated, such as Perlin or Random. It fundamentally affects the nature of the output mask and its applicability in different hybrid scenarios.
    - Comfy dtype: COMBO[perlin,random]
    - Python dtype: str
- seed
    - Seed parameters ensure the replicability of noise generation processes. It is essential for achieving consistent results in different operations, which is particularly important for experimental and test purposes.
    - Comfy dtype: INT
    - Python dtype: int
- width
    - The width parameter defines the horizontal dimensions of the noise mask. It affects the spatial resolution of the mask, thereby affecting its ability to capture details in the mixed output.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - Similar to the width parameters, height parameters define the vertical dimension of the noise mask, affecting its spatial resolution and the level of detail it can express.
    - Comfy dtype: INT
    - Python dtype: int
- batch_size
    - Batch size parameters determine the number of noise masks generated in an operation. It is important for processing efficiency and can affect the amount of throughput at nodes in the stream line.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- perlin_scale
    - When generating Perlin noise mask, this parameter adjusts the size of the noise, which affects the level of detail and overall appearance of the mask. It is essential to adjust the mask to a particular mixture.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- masks
    - The output mask is essential for the iterative mixing process, as a medium for mixing and combining different elements. They play a key role in determining the final result of the mixing.
    - Comfy dtype: TENSOR
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class MixingMaskGeneratorNode:
    """
    A node that can generate different kinds of noise mask batches for
    iterative mixing purposes.
    """
    MASK_TYPES = ['perlin', 'random']
    MAX_RESOLUTION = 8192

    def __init__(self):
        self.device = comfy.model_management.intermediate_device()

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'mask_type': (s.MASK_TYPES, {'default': 'perlin'}), 'perlin_scale': ('FLOAT', {'default': 10.0, 'min': 0.1, 'max': 400.0, 'step': 0.01}), 'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615}), 'width': ('INT', {'default': 512, 'min': 16, 'max': s.MAX_RESOLUTION, 'step': 8}), 'height': ('INT', {'default': 512, 'min': 16, 'max': s.MAX_RESOLUTION, 'step': 8}), 'batch_size': ('INT', {'default': 1, 'min': 1, 'max': 4096})}}
    RETURN_TYPES = ('MASK',)
    CATEGORY = 'mask/generation'
    FUNCTION = 'get_masks'

    def get_masks(self, mask_type, perlin_scale, seed, width, height, batch_size):
        mask_height = height // 8
        mask_width = width // 8
        if mask_type == 'perlin':
            perlin_tensors = perlin_masks(batch_size, mask_width, mask_height, device=self.device, seed=seed, scale=perlin_scale)
            masks = perlin_tensors.view(batch_size, 1, mask_height, mask_width)
        elif mask_type == 'random':
            masks = torch.randn([batch_size, width // 8, height // 8])
        else:
            raise ValueError('invalid mask_type')
        return (masks,)
```