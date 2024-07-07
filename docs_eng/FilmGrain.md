# Documentation
- Class name: FilmGrain
- Category: postprocessing/Effects
- Output node: False
- Repo Ref: https://github.com/EllangoK/ComfyUI-post-processing-nodes

The FilmGrain node introduces random noise patterns into the image, simulating the texture of film particles. This process enhances visual aesthetics by increasing depth and texture, often for artistic and stylistic lateral processing.

# Input types
## Required
- image
    - The image parameter is essential because it is the basic medium that will apply the particle effect of the film. It determines the visual quality of the output and is the basis of the whole operation.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- intensity
    - Strength control applies to the size of the noise in the image. It affects the visibility of the particle effect, and higher values lead to a more obvious pattern of the particle.
    - Comfy dtype: FLOAT
    - Python dtype: float
- scale
    - The scale adjusts the size of the noise pattern relative to the image. A larger proportion leads to a more visible noise feature, which can add a more dramatic effect to the image of the film particle.
    - Comfy dtype: FLOAT
    - Python dtype: float
- temperature
    - Temperature adjusts the colour balance of the image to increase warmness or coolness for the final output. This parameter changes the emotional and overall sense of the image in a subtle way.
    - Comfy dtype: FLOAT
    - Python dtype: float
- vignette
    - It controls the intensity of the bleaching on the edge of the image, creating a more focused and dramatic visual effect. It guides the audience's attention to the centre of the image.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- output_image
    - The output image is the result of the application of film particle effects, including adjusted strength, scale, temperature and dizziness parameters. It represents the final creative output of nodes.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class FilmGrain:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'intensity': ('FLOAT', {'default': 0.2, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'scale': ('FLOAT', {'default': 10, 'min': 1, 'max': 100, 'step': 1}), 'temperature': ('FLOAT', {'default': 0.0, 'min': -100, 'max': 100, 'step': 1}), 'vignette': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 10.0, 'step': 1.0})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'film_grain'
    CATEGORY = 'postprocessing/Effects'

    def film_grain(self, image: torch.Tensor, intensity: float, scale: float, temperature: float, vignette: float):
        (batch_size, height, width, _) = image.shape
        result = torch.zeros_like(image)
        for b in range(batch_size):
            tensor_image = image[b].numpy()
            noise = self.generate_perlin_noise((height, width), scale)
            noise = (noise - np.min(noise)) / (np.max(noise) - np.min(noise))
            noise = (noise * 2 - 1) * intensity
            grain_image = np.clip(tensor_image + noise[:, :, np.newaxis], 0, 1)
            grain_image = self.apply_temperature(grain_image, temperature)
            grain_image = self.apply_vignette(grain_image, vignette)
            tensor = torch.from_numpy(grain_image).unsqueeze(0)
            result[b] = tensor
        return (result,)

    def generate_perlin_noise(self, shape, scale, octaves=4, persistence=0.5, lacunarity=2):

        def smoothstep(t):
            return t * t * (3.0 - 2.0 * t)

        def lerp(t, a, b):
            return a + t * (b - a)

        def gradient(h, x, y):
            vectors = np.array([[1, 1], [-1, 1], [1, -1], [-1, -1]])
            g = vectors[h % 4]
            return g[:, :, 0] * x + g[:, :, 1] * y
        (height, width) = shape
        noise = np.zeros(shape)
        for octave in range(octaves):
            octave_scale = scale * lacunarity ** octave
            x = np.linspace(0, 1, width, endpoint=False)
            y = np.linspace(0, 1, height, endpoint=False)
            (X, Y) = np.meshgrid(x, y)
            (X, Y) = (X * octave_scale, Y * octave_scale)
            xi = X.astype(int)
            yi = Y.astype(int)
            xf = X - xi
            yf = Y - yi
            u = smoothstep(xf)
            v = smoothstep(yf)
            n00 = gradient(np.random.randint(0, 4, (height, width)), xf, yf)
            n01 = gradient(np.random.randint(0, 4, (height, width)), xf, yf - 1)
            n10 = gradient(np.random.randint(0, 4, (height, width)), xf - 1, yf)
            n11 = gradient(np.random.randint(0, 4, (height, width)), xf - 1, yf - 1)
            x1 = lerp(u, n00, n10)
            x2 = lerp(u, n01, n11)
            y1 = lerp(v, x1, x2)
            noise += y1 * persistence ** octave
        return noise / (1 - persistence ** octaves)

    def apply_temperature(self, image, temperature):
        if temperature == 0:
            return image
        temperature /= 100
        new_image = image.copy()
        if temperature > 0:
            new_image[:, :, 0] *= 1 + temperature
            new_image[:, :, 1] *= 1 + temperature * 0.4
        else:
            new_image[:, :, 2] *= 1 - temperature
        return np.clip(new_image, 0, 1)

    def apply_vignette(self, image, vignette_strength):
        if vignette_strength == 0:
            return image
        (height, width, _) = image.shape
        x = np.linspace(-1, 1, width)
        y = np.linspace(-1, 1, height)
        (X, Y) = np.meshgrid(x, y)
        radius = np.sqrt(X ** 2 + Y ** 2)
        mapped_vignette_strength = 1.8 - (vignette_strength - 1) * 0.1
        vignette = 1 - np.clip(radius / mapped_vignette_strength, 0, 1)
        return np.clip(image * vignette[..., np.newaxis], 0, 1)
```