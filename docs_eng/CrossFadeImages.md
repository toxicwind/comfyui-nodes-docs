# Documentation
- Class name: CrossFadeImages
- Category: KJNodes/image
- Output node: False
- Repo Ref: https://github.com/kijai/ComfyUI-KJNodes.git

CrossFadeImages nodes are designed to mix two sets of images seamlessly using cross-dipping techniques. They apply a transition effect that smooths the plug-in between start-up and end-up images, creating a visually attractive transformation sequence. This node is particularly useful when it needs to evolve from one image to another, and is suitable for creating animation transitions or visual effects.

# Input types
## Required
- images_1
    - The first group of images that will fade out during the transition period. These images form the starting point for cross-cutting desalinization effects and are essential for initial visual performance.
    - Comfy dtype: IMAGE
    - Python dtype: List[torch.Tensor]
- images_2
    - The second group of images that will gradually emerge during the transition period. These images represent the end state of cross-diplomaticization and are essential for the ultimate visual effect.
    - Comfy dtype: IMAGE
    - Python dtype: List[torch.Tensor]
## Optional
- interpolation
    - This parameter determines the rate of change between images and can significantly affect the visual dynamics of the transition.
    - Comfy dtype: COMBO['linear', 'ease_in', 'ease_out', 'ease_in_out', 'bounce', 'elastic', 'glitchy', 'exponential_ease_out']
    - Python dtype: str
- transition_start_index
    - Cross-reduces the index from which the transition begins. This parameter allows control of the starting point of the dilution process in the image sequence.
    - Comfy dtype: INT
    - Python dtype: int
- transitioning_frames
    - Cross-reduces the number of frames in which the transition occurs. This parameter defines the duration of the transition effect in the animation sequence.
    - Comfy dtype: INT
    - Python dtype: int
- start_level
    - The threshold level of cross-diplomatic alpha, which determines the initial opacity of iages_2 versus iages_1. Value of 0.0 means that iages_1 will be completely opaque, while iages_2 will be completely transparent.
    - Comfy dtype: FLOAT
    - Python dtype: float
- end_level
    - The closing alpha level of cross-cutting dilution determines the ultimate opacity of the events_2 versus the events_1. Value of 1.0 means that the events_2 will be completely opaque, while the events_1 will be completely transparent.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- crossfade_images
    - The output of the node is the image sequence that represents the transition over which the cross-reduces. Each image in the sequence is a mixture of the input images, the degree of which is determined by the specified alpha level and the buffer function.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class CrossFadeImages:
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'crossfadeimages'
    CATEGORY = 'KJNodes/image'

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'images_1': ('IMAGE',), 'images_2': ('IMAGE',), 'interpolation': (['linear', 'ease_in', 'ease_out', 'ease_in_out', 'bounce', 'elastic', 'glitchy', 'exponential_ease_out'],), 'transition_start_index': ('INT', {'default': 1, 'min': 0, 'max': 4096, 'step': 1}), 'transitioning_frames': ('INT', {'default': 1, 'min': 0, 'max': 4096, 'step': 1}), 'start_level': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'end_level': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.01})}}

    def crossfadeimages(self, images_1, images_2, transition_start_index, transitioning_frames, interpolation, start_level, end_level):

        def crossfade(images_1, images_2, alpha):
            crossfade = (1 - alpha) * images_1 + alpha * images_2
            return crossfade

        def ease_in(t):
            return t * t

        def ease_out(t):
            return 1 - (1 - t) * (1 - t)

        def ease_in_out(t):
            return 3 * t * t - 2 * t * t * t

        def bounce(t):
            if t < 0.5:
                return self.ease_out(t * 2) * 0.5
            else:
                return self.ease_in((t - 0.5) * 2) * 0.5 + 0.5

        def elastic(t):
            return math.sin(13 * math.pi / 2 * t) * math.pow(2, 10 * (t - 1))

        def glitchy(t):
            return t + 0.1 * math.sin(40 * t)

        def exponential_ease_out(t):
            return 1 - (1 - t) ** 4
        easing_functions = {'linear': lambda t: t, 'ease_in': ease_in, 'ease_out': ease_out, 'ease_in_out': ease_in_out, 'bounce': bounce, 'elastic': elastic, 'glitchy': glitchy, 'exponential_ease_out': exponential_ease_out}
        crossfade_images = []
        alphas = torch.linspace(start_level, end_level, transitioning_frames)
        for i in range(transitioning_frames):
            alpha = alphas[i]
            image1 = images_1[i + transition_start_index]
            image2 = images_2[i + transition_start_index]
            easing_function = easing_functions.get(interpolation)
            alpha = easing_function(alpha)
            crossfade_image = crossfade(image1, image2, alpha)
            crossfade_images.append(crossfade_image)
        crossfade_images = torch.stack(crossfade_images, dim=0)
        last_frame = crossfade_images[-1]
        remaining_frames = len(images_2) - (transition_start_index + transitioning_frames)
        for i in range(remaining_frames):
            alpha = alphas[-1]
            image1 = images_1[i + transition_start_index + transitioning_frames]
            image2 = images_2[i + transition_start_index + transitioning_frames]
            easing_function = easing_functions.get(interpolation)
            alpha = easing_function(alpha)
            crossfade_image = crossfade(image1, image2, alpha)
            crossfade_images = torch.cat([crossfade_images, crossfade_image.unsqueeze(0)], dim=0)
        beginning_images_1 = images_1[:transition_start_index]
        crossfade_images = torch.cat([beginning_images_1, crossfade_images], dim=0)
        return (crossfade_images,)
```