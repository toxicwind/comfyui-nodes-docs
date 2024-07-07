# Documentation
- Class name: CR_HalftoneFilter
- Category: Comfyroll/Graphics/Filter
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

The CR_HalftoneFilter node uses half-colored effects for images to simulate the appearance of the printing point. It provides customisation of point shapes, sizes and resolution to create various semi-coloured styles. The node is designed to enhance the visual effects of graphic design and art applications so that users are able to perform archaic or stylistic appearances.

# Input types
## Required
- image
    - The input image that you want to apply the half-colour effect. It is the basis for node processing and determines the theme of the half-colour conversion.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image or torch.Tensor
- dot_size
    - The size of the point used for the half-colour effect affects the particle size of the final image. A larger point size leads to a rougher look, while a smaller size provides more fine detail.
    - Comfy dtype: INT
    - Python dtype: int
- dot_shape
    - Determines the shape of the point in the semi-colour pattern case. The selection between ellipse and rectangle changes the visual texture of the output image and provides a means of adjusting the half-colour effect.
    - Comfy dtype: COMBO['ellipse', 'rectangle']
    - Python dtype: str
- resolution
    - The 'hi-res' option doubles the output size and provides a higher definition of a semi-colour pattern, but at the cost of increasing processing time and resource use.
    - Comfy dtype: COMBO['normal', 'hi-res (2x output size)']
    - Python dtype: str
- angle_c
    - Specifies the angle of the cyan channel in the CMYK colour space to influence the direction of the cyan point in the semi-colour pattern case.
    - Comfy dtype: INT
    - Python dtype: int
- angle_m
    - Specifies the angle of the magenta channel in the CMYK colour space and influences the direction of the magenta point.
    - Comfy dtype: INT
    - Python dtype: int
- angle_y
    - Specifies the angle of the yellow channel in the CMYK colour space and determines the direction of the yellow point.
    - Comfy dtype: INT
    - Python dtype: int
- angle_k
    - Specifies the angle of the key (black) channel in the CMYK colour space, affecting the direction of the black point.
    - Comfy dtype: INT
    - Python dtype: int
- greyscale
    - A sign that indicates whether the input image should be processed in greyscale. When enabled, the half-colour effect is applied only to the brightness channel and the output is reduced to a monochrome.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- antialias
    - Enables or disables anti-sawing, smooths the edges of the half-colored dots and reduces visual prostheses. This makes the final image more natural and finer.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- antialias_scale
    - Controls apply to the anti-sawing level at the half-colored dots. Higher values make the appearance smoother, but may increase processing time.
    - Comfy dtype: INT
    - Python dtype: int
- border_blending
    - When enabled, the border mix smooths the transition between semi-colour palettes near the edge of the image, prevents sharp dividing lines and promotes a more uniform appearance.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- IMAGE
    - Output images with a semi-coloured effect have been applied for further processing or presentation.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image or torch.Tensor
- show_help
    - Provides a link to a document or help page to provide further guidance on how to use the node.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_HalftoneFilter:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        shapes = ['ellipse', 'rectangle']
        rez = ['normal', 'hi-res (2x output size)']
        return {'required': {'image': ('IMAGE',), 'dot_size': ('INT', {'default': 5, 'min': 1, 'max': 30, 'step': 1}), 'dot_shape': (shapes, {'default': 'ellipse'}), 'resolution': (rez, {'default': 'normal'}), 'angle_c': ('INT', {'default': 75, 'min': 0, 'max': 360, 'step': 1}), 'angle_m': ('INT', {'default': 45, 'min': 0, 'max': 360, 'step': 1}), 'angle_y': ('INT', {'default': 15, 'min': 0, 'max': 360, 'step': 1}), 'angle_k': ('INT', {'default': 0, 'min': 0, 'max': 360, 'step': 1}), 'greyscale': ('BOOLEAN', {'default': True}), 'antialias': ('BOOLEAN', {'default': True}), 'antialias_scale': ('INT', {'default': 2, 'min': 1, 'max': 4, 'step': 1}), 'border_blending': ('BOOLEAN', {'default': False})}}
    RETURN_TYPES = ('IMAGE', 'STRING')
    RETURN_NAMES = ('IMAGE', 'show_help')
    FUNCTION = 'halftone_effect'
    CATEGORY = icons.get('Comfyroll/Graphics/Filter')

    def tensor_to_pil(self, tensor):
        if tensor.ndim == 4 and tensor.shape[0] == 1:
            tensor = tensor.squeeze(0)
        if tensor.dtype == torch.float32:
            tensor = tensor.mul(255).byte()
        elif tensor.dtype != torch.uint8:
            tensor = tensor.byte()
        numpy_image = tensor.cpu().numpy()
        if tensor.ndim == 3:
            if tensor.shape[2] == 1:
                mode = 'L'
            elif tensor.shape[2] == 3:
                mode = 'RGB'
            elif tensor.shape[2] == 4:
                mode = 'RGBA'
            else:
                raise ValueError(f'Unsupported channel number: {tensor.shape[2]}')
        else:
            raise ValueError(f'Unexpected tensor shape: {tensor.shape}')
        pil_image = Image.fromarray(numpy_image, mode)
        return pil_image

    def pil_to_tensor(self, pil_image):
        numpy_image = np.array(pil_image)
        tensor = torch.from_numpy(numpy_image).float().div(255)
        tensor = tensor.unsqueeze(0)
        return tensor

    def halftone_effect(self, image, dot_size, dot_shape, resolution, angle_c, angle_m, angle_y, angle_k, greyscale, antialias, border_blending, antialias_scale):
        sample = dot_size
        shape = dot_shape
        resolution_to_scale = {'normal': 1, 'hi-res (2x output size)': 2}
        scale = resolution_to_scale.get(resolution, 1)
        if isinstance(image, torch.Tensor):
            image = self.tensor_to_pil(image)
        if not isinstance(image, Image.Image):
            raise TypeError('The provided image is neither a PIL Image nor a PyTorch tensor.')
        pil_image = image
        if greyscale:
            pil_image = pil_image.convert('L')
            channel_images = [pil_image]
            angles = [angle_k]
        else:
            pil_image = pil_image.convert('CMYK')
            channel_images = list(pil_image.split())
            angles = [angle_c, angle_m, angle_y, angle_k]
        halftone_images = self._halftone_pil(pil_image, channel_images, sample, scale, angles, antialias, border_blending, antialias_scale, shape)
        if greyscale:
            new_image = halftone_images[0].convert('RGB')
        else:
            new_image = Image.merge('CMYK', halftone_images).convert('RGB')
        result_tensor = self.pil_to_tensor(new_image)
        print('Final tensor shape:', result_tensor.shape)
        return (result_tensor, show_help)

    def _halftone_pil(self, im, cmyk, sample, scale, angles, antialias, border_blending, antialias_scale, shape):
        antialias_res = antialias_scale if antialias else 1
        scale = scale * antialias_res
        dots = []
        for (channel_index, (channel, angle)) in enumerate(zip(cmyk, angles)):
            channel = channel.rotate(angle, expand=1)
            size = (channel.size[0] * scale, channel.size[1] * scale)
            half_tone = Image.new('L', size)
            draw = ImageDraw.Draw(half_tone)
            for x in range(0, channel.size[0], sample):
                for y in range(0, channel.size[1], sample):
                    if border_blending and angle % 90 != 0 and (x < sample or y < sample or x > channel.size[0] - sample or (y > channel.size[1] - sample)):
                        neighboring_pixels = channel.crop((max(x - 1, 0), max(y - 1, 0), min(x + 2, channel.size[0]), min(y + 2, channel.size[1])))
                        pixels = list(neighboring_pixels.getdata())
                        weights = [0.5 if i in [0, len(pixels) - 1] else 1 for i in range(len(pixels))]
                        weighted_mean = sum((p * w for (p, w) in zip(pixels, weights))) / sum(weights)
                        mean = weighted_mean
                    else:
                        box = channel.crop((x, y, x + sample, y + sample))
                        mean = ImageStat.Stat(box).mean[0]
                    size = (mean / 255) ** 0.5
                    box_size = sample * scale
                    draw_size = size * box_size
                    (box_x, box_y) = (x * scale, y * scale)
                    x1 = box_x + (box_size - draw_size) / 2
                    y1 = box_y + (box_size - draw_size) / 2
                    x2 = x1 + draw_size
                    y2 = y1 + draw_size
                    draw_method = getattr(draw, shape, None)
                    if draw_method:
                        draw_method([(x1, y1), (x2, y2)], fill=255)
            half_tone = half_tone.rotate(-angle, expand=1)
            (width_half, height_half) = half_tone.size
            xx1 = (width_half - im.size[0] * scale) / 2
            yy1 = (height_half - im.size[1] * scale) / 2
            xx2 = xx1 + im.size[0] * scale
            yy2 = yy1 + im.size[1] * scale
            half_tone = half_tone.crop((xx1, yy1, xx2, yy2))
            if antialias:
                w = int((xx2 - xx1) / antialias_scale)
                h = int((yy2 - yy1) / antialias_scale)
                half_tone = half_tone.resize((w, h), resample=Image.LANCZOS)
            dots.append(half_tone)
            show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Filter-Nodes#cr-halftone-filter'
        return (dots, show_help)
```