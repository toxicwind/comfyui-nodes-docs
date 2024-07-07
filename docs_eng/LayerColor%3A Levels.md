# Documentation
- Class name: ColorCorrectLevels
- Category: 😺dzNodes/LayerColor
- Output node: False
- Repo Ref: https://github.com/chflame163/ComfyUI_LayerStyle

Change the image colour order.

# Input types
## Required

- image
    - Enter the picture.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

- channel
    - Select the channel that you want to adjust. There is an option for RGB, red, green, blue.
    - Comfy dtype: STRING
    - Python dtype: str
    - Options:
        - RGB
        - red
        - green
        - blue

- black_point
    - Enter the black point value for the image. Value range 0-255, default value 0.
    - Comfy dtype: INT
    - Python dtype: int
    - Range: [0, 255]
    - Default: 0
    
- white_point
    - Images enter white point values. Value range 0-255, default 255.
    - Comfy dtype: INT
    - Python dtype: int
    - Range: [0, 255]
    - Default: 255

- gray_point
    - Enter the grey point value for the image. Value range 0.01-9.99, default 1.
    - Comfy dtype: FLOAT
    - Python dtype: float
    - Range: [0.01, 9.99]
    - Default: 1

- output_black_point
    - The image output black point value. Value range 0-255, default value 0.
    - Comfy dtype: INT
    - Python dtype: int
    - Range: [0, 255]
    - Default: 0

- output_white_point
    - Image output white point value. Value range 0-255, default 255.
    - Comfy dtype: INT
    - Python dtype: int
    - Range: [0, 255]
    - Default: 255

# Output types

- image
    - Output pictures.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class ColorCorrectLevels:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        channel_list = ["RGB", "red", "green", "blue"]
        return {
            "required": {
                "image": ("IMAGE", ),  #
                "channel": (channel_list,),
                "black_point": ("INT", {"default": 0, "min": 0, "max": 255, "step": 1}),
                "white_point": ("INT", {"default": 255, "min": 0, "max": 255, "step": 1}),
                "gray_point": ("FLOAT", {"default": 1, "min": 0.01, "max": 9.99, "step": 0.01}),
                "output_black_point": ("INT", {"default": 0, "min": 0, "max": 255, "step": 1}),
                "output_white_point": ("INT", {"default": 255, "min": 0, "max": 255, "step": 1}),
            },
            "optional": {
            }
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image",)
    FUNCTION = 'levels'
    CATEGORY = '😺dzNodes/LayerColor'

    def levels(self, image, channel,
                      black_point, white_point,
                      gray_point, output_black_point, output_white_point):

        l_images = []
        l_masks = []
        ret_images = []

        for l in image:
            l_images.append(torch.unsqueeze(l, 0))
            m = tensor2pil(l)
            if m.mode == 'RGBA':
                l_masks.append(m.split()[-1])
            else:
                l_masks.append(Image.new('L', m.size, 'white'))


        for i in range(len(l_images)):
            _image = l_images[i]
            _mask = l_masks[i]
            orig_image = tensor2pil(_image)


            if channel == "red":
                r, g, b, _ = image_channel_split(orig_image, 'RGB')
                r = adjust_levels(r, black_point, white_point, gray_point,
                                          output_black_point, output_white_point)
                ret_image = image_channel_merge((r.convert('L'), g, b), 'RGB')
            elif channel == "green":
                r, g, b, _ = image_channel_split(orig_image, 'RGB')
                g = adjust_levels(g, black_point, white_point, gray_point,
                                  output_black_point, output_white_point)
                ret_image = image_channel_merge((r, g.convert('L'), b), 'RGB')
            elif channel == "blue":
                r, g, b, _ = image_channel_split(orig_image, 'RGB')
                b = adjust_levels(b, black_point, white_point, gray_point,
                                  output_black_point, output_white_point)
                ret_image = image_channel_merge((r, g, b.convert('L')), 'RGB')
            else:
                ret_image = adjust_levels(orig_image, black_point, white_point, gray_point,
                                          output_black_point, output_white_point)

            if orig_image.mode == 'RGBA':
                ret_image = RGB2RGBA(ret_image, orig_image.split()[-1])

            ret_images.append(pil2tensor(ret_image))

        log(f"{NODE_NAME} Processed {len(ret_images)} image(s).", message_type='finish')
        return (torch.cat(ret_images, dim=0),)

```