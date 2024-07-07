# Documentation
- Class name: Quantize
- Category: postprocessing/Color Adjustments
- Output node: False
- Repo Ref: https://github.com/EllangoK/ComfyUI-post-processing-nodes

The Quantize node is designed to reduce the number of colours in the image, a process called colour quantification. It does this by mapping the colour of the image to a specified number of colours, which is very useful for creating a more stylish or retrograde appearance. The node also offers options for applying shaking, which helps smooth the transition between colours and reduces the appearance of colour stripes.

# Input types
## Required
- image
    - The image parameter is the input length of the image that you want to quantify. It plays a vital role in the operation of the node, because the entire process of quantification is applied to the image. The quality and characteristics of the quantified image depend to a large extent on the input image.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
## Optional
- colors
    - Colour parameters specify the number of colours that will reduce the image. This is an important setting because it directly affects the level of detail and the appearance of the quantitative image. The more the colours are, the more details are kept, but the larger the file will be.
    - Comfy dtype: INT
    - Python dtype: int
- dither
    - The shaking parameters determine whether to apply a shaking algorithm to the image in the quantification process. The shaking can help create a more visually attractive result by reducing the visibility of the colour stripes. The choice between 'one' and 'floyd-steinberg' affects the quality of the final image.
    - Comfy dtype: COMBO[none, floyd-steinberg]
    - Python dtype: str

# Output types
- quantized_image
    - Quantified image output is the result of a colour-quantified process. It is a volume that represents an image with a reduced number of colours. This output is important because it is a direct result of node operations and can be used for further processing or displaying.
    - Comfy dtype: IMAGE
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
        return {'required': {'image': ('IMAGE',), 'colors': ('INT', {'default': 256, 'min': 1, 'max': 256, 'step': 1}), 'dither': (['none', 'floyd-steinberg'],)}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'quantize'
    CATEGORY = 'postprocessing/Color Adjustments'

    def quantize(self, image: torch.Tensor, colors: int=256, dither: str='FLOYDSTEINBERG'):
        (batch_size, height, width, _) = image.shape
        result = torch.zeros_like(image)
        dither_option = Image.Dither.FLOYDSTEINBERG if dither == 'floyd-steinberg' else Image.Dither.NONE
        for b in range(batch_size):
            tensor_image = image[b]
            img = (tensor_image * 255).to(torch.uint8).numpy()
            pil_image = Image.fromarray(img, mode='RGB')
            palette = pil_image.quantize(colors=colors)
            quantized_image = pil_image.quantize(colors=colors, palette=palette, dither=dither_option)
            quantized_array = torch.tensor(np.array(quantized_image.convert('RGB'))).float() / 255
            result[b] = quantized_array
        return (result,)
```