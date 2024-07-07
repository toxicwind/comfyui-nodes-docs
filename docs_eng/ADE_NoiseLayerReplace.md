# Documentation
- Class name: NoiseLayerReplaceNode
- Category: Animate Diff 🎭🅐🅓/noise layers
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved.git

NoiseLayerReplaceNode is designed to operate and generate noise layers in the model for animation purposes. It replaces existing noises with new noises based on specified parameters, allowing dynamic and diverse animation effects.

# Input types
## Required
- batch_offset
    - Batch deviation parameters are essential to manage the noise layers sequence in the animation. It determines the starting point in the data batch, which is critical to ensuring the correct operating layer.
    - Comfy dtype: INT
    - Python dtype: int
- noise_type
    - Noise type parameters determine the type of noise layer that will be created. It is a key factor in the overall noise generation process, influencing the properties of noise and the final animation effect.
    - Comfy dtype: NoiseLayerType.LIST
    - Python dtype: str
- seed_gen_override
    - Seeds generate coverage parameters that allow the process of generating seeds that customize the noise layers. This may be particularly important when the objective is to achieve specific noise patterns or effects in animations.
    - Comfy dtype: SeedNoiseGeneration.LIST_WITH_OVERRIDE
    - Python dtype: str
- seed_offset
    - Seed deviation parameters are used to adjust the value of the torrent used for noise generation. This can significantly influence the noise patterns generated and provide a way to introduce changes in animations.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- prev_noise_layers
    - Previous noise layer parameters are used to specify existing noise layers that will be replaced or modified. It plays a key role in the continuity and evolution of noise in animation.
    - Comfy dtype: NOISE_LAYERS
    - Python dtype: NoiseLayerGroup
- mask_optional
    - The masked optional parameters provide a way of selectively applying the noise layer to certain parts of the animation. They can be used to introduce targeted effects or to protect certain areas from noise applications.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor
- seed_override
    - Seed-cover parameters allow manual control of seed values for noise generation. This may be particularly useful for specific aspects of noise in micromobilization.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- noise_layers
    - Noise output contains noise layers that have been created or modified and added to animations. These layers are essential to the visual appearance and behaviour of the animation sequence.
    - Comfy dtype: NOISE_LAYERS
    - Python dtype: NoiseLayerGroup

# Usage tips
- Infra type: CPU

# Source code
```
class NoiseLayerReplaceNode:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'batch_offset': ('INT', {'default': 0, 'min': 0, 'max': BIGMAX}), 'noise_type': (NoiseLayerType.LIST,), 'seed_gen_override': (SeedNoiseGeneration.LIST_WITH_OVERRIDE,), 'seed_offset': ('INT', {'default': 0, 'min': BIGMIN, 'max': BIGMAX})}, 'optional': {'prev_noise_layers': ('NOISE_LAYERS',), 'mask_optional': ('MASK',), 'seed_override': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615, 'forceInput': True})}}
    RETURN_TYPES = ('NOISE_LAYERS',)
    CATEGORY = 'Animate Diff 🎭🅐🅓/noise layers'
    FUNCTION = 'create_layers'

    def create_layers(self, batch_offset: int, noise_type: str, seed_gen_override: str, seed_offset: int, prev_noise_layers: NoiseLayerGroup=None, mask_optional: Tensor=None, seed_override: int=None):
        if prev_noise_layers is None:
            prev_noise_layers = NoiseLayerGroup()
        prev_noise_layers = prev_noise_layers.clone()
        layer = NoiseLayerReplace(noise_type=noise_type, batch_offset=batch_offset, seed_gen_override=seed_gen_override, seed_offset=seed_offset, seed_override=seed_override, mask=mask_optional)
        prev_noise_layers.add_to_start(layer)
        return (prev_noise_layers,)
```