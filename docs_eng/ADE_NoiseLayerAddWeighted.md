# Documentation
- Class name: NoiseLayerAddWeightedNode
- Category: Animate Diff 🎭🅐🅓/noise layers
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved.git

The NoiseLayerAddWeightedNode class is designed to operate and introduce noise into the system in a weighted manner. It is a key component of the animation process, allowing for fine-tuning of noise features. The primary function of the node is to add noise layers to the existing group, ensuring that new noise elements are balanced with existing ones, thereby enhancing the overall diversity and complexity of animations.

# Input types
## Required
- batch_offset
    - Match_offset parameters are essential to manage the sequence of noise layers. It affects the overall structure and organization of noise layers in animations and ensures that each layer is correctly positioned in the sequence.
    - Comfy dtype: INT
    - Python dtype: int
- noise_type
    - The noise_type parameter defines the type of noise that you want to add to the animation. It plays an important role in determining the visual and structural aspects of the noise, thus influencing the final output of the animation.
    - Comfy dtype: NoiseLayerType.LIST
    - Python dtype: str
- seed_gen_override
    - Seed_gen_override parameters allow customise noise generation processes. It is important to create unique noise patterns and to ensure the randomity required to animate random elements.
    - Comfy dtype: SeedNoiseGeneration.LIST_WITH_OVERRIDE
    - Python dtype: str
- seed_offset
    - Seed_offset parameters are essential to control randomity in noise generation. It ensures that each noise layer has a unique and unpredictable quality that helps to increase the diversity of animations.
    - Comfy dtype: INT
    - Python dtype: int
- noise_weight
    - The noise_weight parameter adjusts the noise intensity added to the animation. It is a key factor in achieving the desired visual effect and ensures a balance between the noise and the basic elements of the animation.
    - Comfy dtype: FLOAT
    - Python dtype: float
- balance_multiplier
    - The balance_multiplier parameter is used to fine-tune the balance between the existing noise and the new noise. It ensures that the overall noise effect is harmonious and integrated into the animation.
    - Comfy dtype: FLOAT
    - Python dtype: float
## Optional
- prev_noise_layers
    - The prev_noise_layers parameter is an optional group of previously generated noise layers. It allows for continuation and construction of existing noise structures to maintain the consistency and consistency of animations.
    - Comfy dtype: NOISE_LAYERS
    - Python dtype: Optional[NoiseLayerGroup]
- mask_optional
    - The mask_optional parameter is an optional volume that can be used to selectively apply noise to specific areas of animation. It provides control over the most prominent location of noise effects.
    - Comfy dtype: MASK
    - Python dtype: Optional[torch.Tensor]
- seed_override
    - Seed_override parameters provide an optional overlay for seeds used in noise generation. They can be used to ensure repeatability or to introduce specific noise patterns into animations.
    - Comfy dtype: INT
    - Python dtype: Optional[int]

# Output types
- noise_layers
    - The output of NoiseLayerAddWeightedNode is a modified group of noise layers, including the newly added weighted noise layers. This output is important because it forms the basis for further processing and animation development.
    - Comfy dtype: NOISE_LAYERS
    - Python dtype: NoiseLayerGroup

# Usage tips
- Infra type: CPU

# Source code
```
class NoiseLayerAddWeightedNode:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'batch_offset': ('INT', {'default': 0, 'min': 0, 'max': BIGMAX}), 'noise_type': (NoiseLayerType.LIST,), 'seed_gen_override': (SeedNoiseGeneration.LIST_WITH_OVERRIDE,), 'seed_offset': ('INT', {'default': 0, 'min': BIGMIN, 'max': BIGMAX}), 'noise_weight': ('FLOAT', {'default': 0.5, 'min': 0.0, 'max': 10.0, 'step': 0.001}), 'balance_multiplier': ('FLOAT', {'default': 1.0, 'min': 0.0, 'step': 0.001})}, 'optional': {'prev_noise_layers': ('NOISE_LAYERS',), 'mask_optional': ('MASK',), 'seed_override': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615, 'forceInput': True})}}
    RETURN_TYPES = ('NOISE_LAYERS',)
    CATEGORY = 'Animate Diff 🎭🅐🅓/noise layers'
    FUNCTION = 'create_layers'

    def create_layers(self, batch_offset: int, noise_type: str, seed_gen_override: str, seed_offset: int, noise_weight: float, balance_multiplier: float, prev_noise_layers: NoiseLayerGroup=None, mask_optional: Tensor=None, seed_override: int=None):
        if prev_noise_layers is None:
            prev_noise_layers = NoiseLayerGroup()
        prev_noise_layers = prev_noise_layers.clone()
        layer = NoiseLayerAddWeighted(noise_type=noise_type, batch_offset=batch_offset, seed_gen_override=seed_gen_override, seed_offset=seed_offset, seed_override=seed_override, mask=mask_optional, noise_weight=noise_weight, balance_multiplier=balance_multiplier)
        prev_noise_layers.add_to_start(layer)
        return (prev_noise_layers,)
```