# Documentation
- Class name: ResizeImage
- Category: ♾️Mixlab/Image
- Output node: False
- Repo Ref: https://github.com/shadowcz007/comfyui-mixlab-nodes.git

The ResizeImage node is designed to adjust the size of the image to the specified requirements. It is able to finely adjust the image to the required width and height, while maintaining the integrity of the visual content. The node also provides an option to scale the image according to any dimension, or to zoom in to a given size while maintaining the width ratio, or to zoom in. In addition, it can generate an average colour expression of the image and convert it to a hexadecimal code, providing a multifunctional tool for pre-processing and operation of the image.

# Input types
## Required
- width
    - The `width' parameter is essential to define the new width of the adjusted-size image. It plays a key role in determining the final size of the image, which may significantly influence visual output and width ratios.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - The `height' parameter specifies a new height for the adjusted size of the image. It is essential to control the vertical dimensions of the image and to work with the `width' parameter to maintain the expected width ratio.
    - Comfy dtype: INT
    - Python dtype: int
- scale_option
    - The `scale_option' parameter indicates how the image should be resized. It allows for scaling according to width, height, overall size, or in the middle of a new size, and provides flexibility in maintaining or changing the image width ratio.
    - Comfy dtype: COMBO['width', 'height', 'overall', 'center']
    - Python dtype: str
- image
    - The 'image'parameter is used to enter images that need to be resized. It is the core of node operations because this is the actual content that will be operated and converted.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image
- average_color
    - The `average_color' parameter determines whether to calculate and return the average colour of the image. This is very useful for creating simplified expressions or colour-based design decisions.
    - Comfy dtype: COMBO['on', 'off']
    - Python dtype: str
- fill_color
    - The `fill_color' parameter specifies the colour to be used to fill any blank space after adjusting the image to a greater size than its original size. It ensures a consistent background appearance.
    - Comfy dtype: STRING
    - Python dtype: str
- mask
    - The `mask' parameter is used to apply a mask to the image during the resizeing process. This is important for keeping the image visible or hidden in a specific area as required.
    - Comfy dtype: MASK
    - Python dtype: PIL.Image.Image

# Output types
- image
    - The 'image'output provides an adjusted-size image. This is the main result of the node operation and reflects the conversion applied according to the input parameter.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- average_image
    - The `average_image' output is an image of the average colour calculated from the input image. It is a visual summary of the color composition of the image.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- average_hex
    - The 'average_hex' output returns the hexadecimal expression of the average colour of the image, which can be used for various design and colour-related applications.
    - Comfy dtype: STRING
    - Python dtype: str
- mask
    - The `mask' output provides an adjusted-size mask image. It is particularly useful when nodes are used to operate and improve the visibility of specific areas in the image.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class ResizeImage:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'width': ('INT', {'default': 512, 'min': 1, 'max': 8192, 'step': 8, 'display': 'number'}), 'height': ('INT', {'default': 512, 'min': 1, 'max': 8192, 'step': 8, 'display': 'number'}), 'scale_option': (['width', 'height', 'overall', 'center'],)}, 'optional': {'image': ('IMAGE',), 'average_color': (['on', 'off'],), 'fill_color': ('STRING', {'multiline': False, 'default': '#FFFFFF', 'dynamicPrompts': False}), 'mask': ('MASK',)}}
    RETURN_TYPES = ('IMAGE', 'IMAGE', 'STRING', 'MASK')
    RETURN_NAMES = ('image', 'average_image', 'average_hex', 'mask')
    FUNCTION = 'run'
    CATEGORY = '♾️Mixlab/Image'
    INPUT_IS_LIST = True
    OUTPUT_IS_LIST = (True, True, True, True)

    def run(self, width, height, scale_option, image=None, average_color=['on'], fill_color=['#FFFFFF'], mask=None):
        w = width[0]
        h = height[0]
        scale_option = scale_option[0]
        average_color = average_color[0]
        fill_color = fill_color[0]
        imgs = []
        masks = []
        average_images = []
        hexs = []
        if image == None:
            im = create_noisy_image(w, h, 'RGB')
            (a_im, hex) = get_average_color_image(im)
            im = pil2tensor(im)
            imgs.append(im)
            a_im = pil2tensor(a_im)
            average_images.append(a_im)
            hexs.append(hex)
        else:
            for ims in image:
                for im in ims:
                    im = tensor2pil(im)
                    im = resize_image(im, scale_option, w, h, fill_color)
                    im = im.convert('RGB')
                    (a_im, hex) = get_average_color_image(im)
                    im = pil2tensor(im)
                    imgs.append(im)
                    a_im = pil2tensor(a_im)
                    average_images.append(a_im)
                    hexs.append(hex)
            try:
                for mas in mask:
                    for ma in mas:
                        ma = tensor2pil(ma)
                        ma = ma.convert('RGB')
                        ma = resize_image(ma, scale_option, w, h, fill_color)
                        ma = ma.convert('L')
                        ma = pil2tensor(ma)
                        masks.append(ma)
            except:
                print('')
        return (imgs, average_images, hexs, masks)
```