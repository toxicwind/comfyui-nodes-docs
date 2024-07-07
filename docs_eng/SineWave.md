# Documentation
- Class name: SineWave
- Category: postprocessing/Effects
- Output node: False
- Repo Ref: https://github.com/EllangoK/ComfyUI-post-processing-nodes

The SineWave class has introduced a method of applying the schord distortion effect to images that enhances their visual appearance by simulating wave-like patterns. This method is designed to manipulate image data in creative ways and introduce artistic changes without compromising the integrity of the original content.

# Input types
## Required
- image
    - The image parameter is essential because it is the main input for node operations. It is the medium for applying the effect of the sine wave, the properties of which directly affect the distortion of the result.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- amplitude
    - The amplitude determines the intensity of the sine wave effect and controls the distortion applied to the image. It is a key factor in shaping nodes to implement visual results.
    - Comfy dtype: FLOAT
    - Python dtype: float
- frequency
    - The frequency determines the number of sine wave cycles within the unit image space and affects the distorted particle size. It plays an important role in defining the shape of the pattern.
    - Comfy dtype: FLOAT
    - Python dtype: float
- direction
    - Direction specifies the direction, horizontal or vertical of the effect of the sine wave, which determines how the distortion is applied to the image.
    - Comfy dtype: COMBO['horizontal', 'vertical']
    - Python dtype: str

# Output types
- output_image
    - The output image is the result of the sine wave effect applied to the input image. It represents the conversion, is the main output of the node and contains creative distortions.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class SineWave:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'amplitude': ('FLOAT', {'default': 10, 'min': 0, 'max': 150, 'step': 5}), 'frequency': ('FLOAT', {'default': 5, 'min': 0, 'max': 20, 'step': 1}), 'direction': (['horizontal', 'vertical'],)}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'apply_sine_wave'
    CATEGORY = 'postprocessing/Effects'

    def apply_sine_wave(self, image: torch.Tensor, amplitude: float, frequency: float, direction: str):
        (batch_size, height, width, channels) = image.shape
        result = torch.zeros_like(image)
        for b in range(batch_size):
            tensor_image = image[b]
            result[b] = self.sine_wave_effect(tensor_image, amplitude, frequency, direction)
        return (result,)

    def sine_wave_effect(self, image: torch.Tensor, amplitude: float, frequency: float, direction: str):
        (height, width, _) = image.shape
        shifted_image = torch.zeros_like(image)
        for channel in range(3):
            if direction == 'horizontal':
                for i in range(height):
                    offset = int(amplitude * np.sin(2 * torch.pi * i * frequency / height))
                    shifted_image[i, :, channel] = torch.roll(image[i, :, channel], offset)
            elif direction == 'vertical':
                for j in range(width):
                    offset = int(amplitude * np.sin(2 * torch.pi * j * frequency / width))
                    shifted_image[:, j, channel] = torch.roll(image[:, j, channel], offset)
        return shifted_image
```