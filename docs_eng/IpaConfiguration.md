# Documentation
- Class name: IpaConfigurationNode
- Category: Steerable-Motion
- Output node: False
- Repo Ref: https://github.com/banodoco/steerable-motion

The IpaConfigurationNode class covers the configuration logic of a node that manages parameters that affect the behaviour of a controlled motion model. It processes input to focus on the balance between control and natural motion, depending on the user's preference for fine-tuning model performance.

# Input types
## Required
- ipa_starts_at
    - The "ipa_starts_at" parameter sets the starting point of the movement, which is essential for defining the initial conditions for animation. It affects the overall trajectory and ensures that the movement starts at the desired level.
    - Comfy dtype: FLOAT
    - Python dtype: float
- ipa_ends_at
    - The "ipa_ends_at" parameter specifies the end point of the movement, which is essential for determining the final state of the animation. It ensures that the movement ends at the desired position and contributes to the consistency of the animation sequence.
    - Comfy dtype: FLOAT
    - Python dtype: float
- ipa_weight_type
    - The "ipa_weight_type" parameter influences the weight distribution along the motion path, affecting the smoothness and visual appeal of the animation. It is a key factor in the natural transition between different stages of the movement.
    - Comfy dtype: ENUM
    - Python dtype: str
- ipa_weight
    - The effect of the "ipa_weight" parameter adjustment weighting on the movement as a whole is important for the dynamics of the micromobilization drawings. It helps to achieve the desired balance between the different elements of the movement.
    - Comfy dtype: FLOAT
    - Python dtype: float
- ipa_embeds_scaling
    - The embedded scaling used in the "ipa_embeds_scaling" parameter control motion model is essential for adjusting the responsiveness of the model to user input. It plays an important role in the accuracy and adaptability of the movement.
    - Comfy dtype: ENUM
    - Python dtype: str
- ipa_noise_strength
    - The "ipa_noise_strength" parameter determines the noise intensity to be applied to motion, which increases the authenticity and variability of animation. It is an important aspect of creating a more dynamic and unpredictable sequence of motion.
    - Comfy dtype: FLOAT
    - Python dtype: float
- use_image_for_noise
    - The "use_image_for_noise" parameter enables the use of images as a noise source, which can introduce more complex and visually rich noise patterns into animations. It enhances the diversity of motion and aesthetic quality.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- type_of_noise
    - The "type_of_noise" parameter defines the type of noise to be applied, which significantly affects the visual features and style of animation. It is a key element in achieving desired aesthetic and style outcomes.
    - Comfy dtype: ENUM
    - Python dtype: str
- noise_blur
    - The "noise_blur" parameter adjusts the level of fuzzy application of noise, affecting the smoothness and consistency of noise patterns in animations. It plays a role in defining overall visual quality and quality.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- configuration
    - Output 'configuration' is a group of processed and optimized parameters for controlled motion models. It covers all user-defined settings to ensure that the models function according to the preferences specified.
    - Comfy dtype: DICT
    - Python dtype: Dict[str, Any]

# Usage tips
- Infra type: CPU

# Source code
```
class IpaConfigurationNode:
    WEIGHT_TYPES = ['linear', 'ease in', 'ease out', 'ease in-out', 'reverse in-out', 'weak input', 'weak output', 'weak middle', 'strong middle']
    IPA_EMBEDS_SCALING_OPTIONS = ['V only', 'K+V', 'K+V w/ C penalty', 'K+mean(V) w/ C penalty']

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'ipa_starts_at': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'ipa_ends_at': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'ipa_weight_type': (cls.WEIGHT_TYPES,), 'ipa_weight': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 2.0, 'step': 0.01}), 'ipa_embeds_scaling': (cls.IPA_EMBEDS_SCALING_OPTIONS,), 'ipa_noise_strength': ('FLOAT', {'default': 0.3, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'use_image_for_noise': ('BOOLEAN', {'default': False}), 'type_of_noise': (['fade', 'dissolve', 'gaussian', 'shuffle'],), 'noise_blur': ('INT', {'default': 0, 'min': 0, 'max': 32, 'step': 1})}, 'optional': {}}
    FUNCTION = 'process_inputs'
    RETURN_TYPES = ('ADVANCED_IPA_SETTINGS',)
    RETURN_NAMES = ('configuration',)
    CATEGORY = 'Steerable-Motion'

    @classmethod
    def process_inputs(cls, ipa_starts_at, ipa_ends_at, ipa_weight_type, ipa_weight, ipa_embeds_scaling, ipa_noise_strength, use_image_for_noise, type_of_noise, noise_blur):
        return ({'ipa_starts_at': ipa_starts_at, 'ipa_ends_at': ipa_ends_at, 'ipa_weight_type': ipa_weight_type, 'ipa_weight': ipa_weight, 'ipa_embeds_scaling': ipa_embeds_scaling, 'ipa_noise_strength': ipa_noise_strength, 'use_image_for_noise': use_image_for_noise, 'type_of_noise': type_of_noise, 'noise_blur': noise_blur},)
```