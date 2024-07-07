# Documentation
- Class name: ImageCropByAlpha
- Category: ♾️Mixlab/Image
- Output node: False
- Repo Ref: https://github.com/shadowcz007/comfyui-mixlab-nodes.git

The ImageCropBy Alpha node is designed to effectively segregate the opaque area of the image by using image-based alpha-channel smart cutting. It enhances the image processing workflow by providing a precise and automated content extraction method, especially for applications involving complex image combinations or requiring a clear separation of image elements.

# Input types
## Required
- image
    - The 'image 'parameter is the main input of the node, which represents the original image to be processed. The significance of this is that it is the source from which the alpha channel is knitted. The execution of the node and the image generated depends heavily on the content and quality of the input image.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- RGBA
    - The 'RGBA'parameter is a necessary input that provides the alpha channel information that is necessary during the cropping process. This parameter directly affects how nodes identify and isolate the opaque areas of the image, and thus plays a key role in determining the final cutting of the image.
    - Comfy dtype: RGBA
    - Python dtype: torch.Tensor

# Output types
- IMAGE
    - The 'IMAGE'output is the result of a crop operation that provides users with image content based on the isolation of the alpha channel. It is important because it represents the main elements of the node function and shows the validity of the image processing task.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- MASK
    - The 'MASK'output is a binary mask that corresponds to the non-transparent area of the original image, as a visual guide to the crop operation. It is important for applications that require accurate space information.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor
- AREA_MASK
    - The `AREA_MASK' output is a mask that paints an image area that is identified as non-transparent. This is very useful for the possible need to understand further image analysis or processing steps in a particular area of the image.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor
- x
    - The 'x' output provides the x-coordinate at the top left corner of the crop area, which is essential to understand the spatial location of the clipping content in the original image.
    - Comfy dtype: INT
    - Python dtype: int
- y
    - The 'y'output provides the coordinates of y in the upper left corner of the crop area, further defining the spatial location of the clipping content.
    - Comfy dtype: INT
    - Python dtype: int
- width
    - The 'width' output represents the width of the crop area, which is the key measure for understanding the dimensions of the isolated image content.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - The 'height'output represents the height of the crop area, which complements the width and provides a complete description of the size of the extracted image segment.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class ImageCropByAlpha:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'RGBA': ('RGBA',)}}
    RETURN_TYPES = ('IMAGE', 'MASK', 'MASK', 'INT', 'INT', 'INT', 'INT')
    RETURN_NAMES = ('IMAGE', 'MASK', 'AREA_MASK', 'x', 'y', 'width', 'height')
    FUNCTION = 'run'
    CATEGORY = '♾️Mixlab/Image'
    INPUT_IS_LIST = True
    OUTPUT_IS_LIST = (True, True, True, True, True, True, True)

    def run(self, image, RGBA):
        image = image[0]
        RGBA = RGBA[0]
        bf_im = tensor2pil(image)
        im = tensor2pil(RGBA)
        im = im.convert('RGBA')
        (red, green, blue, alpha) = im.split()
        im = naive_cutout(bf_im, alpha)
        (x, y, w, h) = get_not_transparent_area(im)
        x = min(x, image.shape[2] - 1)
        y = min(y, image.shape[1] - 1)
        to_x = w + x
        to_y = h + y
        x_1 = x
        y_1 = y
        width_1 = w
        height_1 = h
        img = image[:, y:to_y, x:to_x, :]
        ori = RGBA[:, y:to_y, x:to_x, :]
        ori = tensor2pil(ori)
        new_image = Image.new('RGBA', ori.size)
        pixel_data = ori.load()
        new_pixel_data = new_image.load()
        for y in range(ori.size[1]):
            for x in range(ori.size[0]):
                (r, g, b, a) = pixel_data[x, y]
                if a != 0:
                    new_pixel_data[x, y] = (255, 255, 255, 255)
                else:
                    new_pixel_data[x, y] = (0, 0, 0, 0)
        ori = new_image.convert('L')
        ori = pil2tensor(ori)
        b_image = AreaToMask_run(RGBA)
        return ([img], [ori], [b_image], [x_1], [y_1], [width_1], [height_1])
```