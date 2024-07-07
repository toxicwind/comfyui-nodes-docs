# Documentation
- Class name: IPAdapterNoise
- Category: ipadapter/utils
- Output node: False
- Repo Ref: https://github.com/cubiq/ComfyUI_IPAdapter_plus.git

IPAdapterNoise is designed to introduce controlled noise into images that can be used for a variety of purposes, such as data enhancement or model stamina. It provides options for multiple noise types and allows for adjustments in noise intensity, thus providing flexible solutions for different cases.

# Input types
## Required
- type
    - The "type" parameter determines the type of noise to be generated, which significantly affects the results of noise applications. This is a key decision point because different noise types have different functions and affect images in different ways.
    - Comfy dtype: COMBO[fade, dissolve, gaussian, shuffle]
    - Python dtype: str
- strength
    - The "strength" parameter adjusts the intensity of noise and directly affects the extent of changes in the image. This is an important parameter that allows users to adjust noise effects to meet their specific needs.
    - Comfy dtype: FLOAT
    - Python dtype: float
## Optional
- blur
    - "blur" parameters apply Gaussian fuzzy to noise, which can help smooth noise in some applications. It plays a role in the final visual outcome of noise and provides a means of further fine-tuning noise textures.
    - Comfy dtype: INT
    - Python dtype: int
- image_optional
    - The " image_optional " parameter allows for an optional image to be used as the basis for noise generation. This parameter is important because it allows noise to be applied to a given image rather than the default blank image, providing greater flexibility and customization.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Output types
- noise
    - The "noise" output is the main result of the IPAdapterNoise node and represents the image that introduces noise. It is a key component because it carries the noise effects of the application and is prepared for use in follow-up processes or analysis.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class IPAdapterNoise:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'type': (['fade', 'dissolve', 'gaussian', 'shuffle'],), 'strength': ('FLOAT', {'default': 1.0, 'min': 0, 'max': 1, 'step': 0.05}), 'blur': ('INT', {'default': 0, 'min': 0, 'max': 32, 'step': 1})}, 'optional': {'image_optional': ('IMAGE',)}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'make_noise'
    CATEGORY = 'ipadapter/utils'

    def make_noise(self, type, strength, blur, image_optional=None):
        if image_optional is None:
            image = torch.zeros([1, 224, 224, 3])
        else:
            transforms = T.Compose([T.CenterCrop(min(image_optional.shape[1], image_optional.shape[2])), T.Resize((224, 224), interpolation=T.InterpolationMode.BICUBIC, antialias=True)])
            image = transforms(image_optional.permute([0, 3, 1, 2])).permute([0, 2, 3, 1])
        seed = int(torch.sum(image).item()) % 1000000007
        torch.manual_seed(seed)
        if type == 'fade':
            noise = torch.rand_like(image)
            noise = image * (1 - strength) + noise * strength
        elif type == 'dissolve':
            mask = (torch.rand_like(image) < strength).float()
            noise = torch.rand_like(image)
            noise = image * (1 - mask) + noise * mask
        elif type == 'gaussian':
            noise = torch.randn_like(image) * strength
            noise = image + noise
        elif type == 'shuffle':
            transforms = T.Compose([T.ElasticTransform(alpha=75.0, sigma=(1 - strength) * 3.5), T.RandomVerticalFlip(p=1.0), T.RandomHorizontalFlip(p=1.0)])
            image = transforms(image.permute([0, 3, 1, 2])).permute([0, 2, 3, 1])
            noise = torch.randn_like(image) * (strength * 0.75)
            noise = image * (1 - noise) + noise
        del image
        noise = torch.clamp(noise, 0, 1)
        if blur > 0:
            if blur % 2 == 0:
                blur += 1
            noise = T.functional.gaussian_blur(noise.permute([0, 3, 1, 2]), blur).permute([0, 2, 3, 1])
        return (noise,)
```