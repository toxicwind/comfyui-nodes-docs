# Documentation
- Class name: Quantize
- Category: image/postprocessing
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The Quantize node is designed to reduce the number of colours used in the image, a process called colour quantification. It does this by mapping the continuous colour range in the given image to a specified palette of a limited number of colours. The node supports a variety of shaking techniques to improve the visual quality of quantitative images, such as the floyd-Steinberg shaking and the bell shaking of different scales. The function of the node is essential to the application of the desired reduction in colour depth, for example, when creating smaller image files or compatible with certain display techniques.

# Input types
## Required
- image
    - The image parameter is the input length of the image that you want to quantify. It is a key part of the process, because the process revolves around reducing the colour palette of the image. The image length should be in RGB format and is expected to be represented by a floating point between 0 and 1.
    - Comfy dtype: torch.Tensor
    - Python dtype: torch.Tensor
- colors
    - Colour parameters specify the number of colours that reduce the image palette. It plays an important role in determining the final quality of the quantitative image and the size of the file. A smaller number of colours will result in a significant reduction in the size of the file, but it may also result in a loss of image details.
    - Comfy dtype: int
    - Python dtype: int
## Optional
- dither
    - The shaking parameters determine the technology to be applied in the quantification process. The shaking can help create more pleasant visual effects by dispersing quantitative errors. The options available include 'one', 'floyd-steinberg', and 'bayer' shakes of various orders.
    - Comfy dtype: str
    - Python dtype: str

# Output types
- quantized_image
    - Quantified image output is the result of a colour-quantified process. It is a volume that represents an image with a reduced colour palette. This volume is essential for further processing or for saving the image in formats that support a reduction in colour depth.
    - Comfy dtype: torch.Tensor
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class Quantize:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'colors': ('INT', {'default': 256, 'min': 1, 'max': 256, 'step': 1}), 'dither': (['none', 'floyd-steinberg', 'bayer-2', 'bayer-4', 'bayer-8', 'bayer-16'],)}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'quantize'
    CATEGORY = 'image/postprocessing'

    def bayer(im, pal_im, order):

        def normalized_bayer_matrix(n):
            if n == 0:
                return np.zeros((1, 1), 'float32')
            else:
                q = 4 ** n
                m = q * normalized_bayer_matrix(n - 1)
                return np.bmat(((m - 1.5, m + 0.5), (m + 1.5, m - 0.5))) / q
        num_colors = len(pal_im.getpalette()) // 3
        spread = 2 * 256 / num_colors
        bayer_n = int(math.log2(order))
        bayer_matrix = torch.from_numpy(spread * normalized_bayer_matrix(bayer_n) + 0.5)
        result = torch.from_numpy(np.array(im).astype(np.float32))
        tw = math.ceil(result.shape[0] / bayer_matrix.shape[0])
        th = math.ceil(result.shape[1] / bayer_matrix.shape[1])
        tiled_matrix = bayer_matrix.tile(tw, th).unsqueeze(-1)
        result.add_(tiled_matrix[:result.shape[0], :result.shape[1]]).clamp_(0, 255)
        result = result.to(dtype=torch.uint8)
        im = Image.fromarray(result.cpu().numpy())
        im = im.quantize(palette=pal_im, dither=Image.Dither.NONE)
        return im

    def quantize(self, image: torch.Tensor, colors: int, dither: str):
        (batch_size, height, width, _) = image.shape
        result = torch.zeros_like(image)
        for b in range(batch_size):
            im = Image.fromarray((image[b] * 255).to(torch.uint8).numpy(), mode='RGB')
            pal_im = im.quantize(colors=colors)
            if dither == 'none':
                quantized_image = im.quantize(palette=pal_im, dither=Image.Dither.NONE)
            elif dither == 'floyd-steinberg':
                quantized_image = im.quantize(palette=pal_im, dither=Image.Dither.FLOYDSTEINBERG)
            elif dither.startswith('bayer'):
                order = int(dither.split('-')[-1])
                quantized_image = Quantize.bayer(im, pal_im, order)
            quantized_array = torch.tensor(np.array(quantized_image.convert('RGB'))).float() / 255
            result[b] = quantized_array
        return (result,)
```