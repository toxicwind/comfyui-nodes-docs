# Documentation
- Class name: ColorCorrectLevels
- Category: 😺dzNodes/LayerColor
- Output node: False
- Repo Ref: https://github.com/chflame163/ComfyUI_LayerStyle

Applys LUT to images. Only LUT files in.cube format are supported.

# Input types
## Required

- image
    - Enter the picture.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

- LUT
    - The list of available.cube files in the LUT folder is given here, and the selected LUT file will be applied to the image. *LUT folder is defined in the source_dir.ini, which is located under the plugin root directory with the default name resource_dir.ini.example. The initial use of this file requires the postfixing of the file to.ini. Open with the text editing software, find this line at the beginning of the "LUT_dir=" and edit the custom folder path after "=". All of the.cube files in this folder will be collected and displayed in the list of nodes at the time of the initialization of ComfyUI. If the folder set in the inini is not valid, the plugin will be enabled from the LUT folder.
    - Comfy dtype: LUT_LIST
    - Python dtype: str

- color_space
    - Please select a picture of the linear, log colour space, and choose a log.
    - Comfy dtype: str
    - Python dtype: str
    - Options: ['linear', 'log']

# Output types

- image
    - Output pictures.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class ColorCorrectLUTapply:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        color_space_list = ['linear', 'log']
        return {
            "required": {
                "image": ("IMAGE", ),  #
                "LUT": (LUT_LIST,), #LUT file
                "color_space":  (color_space_list,),
            },
            "optional": {
            }
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image",)
    FUNCTION = 'color_correct_LUTapply'
    CATEGORY = '😺dzNodes/LayerColor'

    def color_correct_LUTapply(self, image, LUT, color_space):
        ret_images = []
        for i in image:
            i = torch.unsqueeze(i, 0)
            _image = tensor2pil(i)

            lut_file = LUT_DICT[LUT]
            ret_image = apply_lut(_image, lut_file, log=(color_space == 'log'))

            if _image.mode == 'RGBA':
                ret_image = RGB2RGBA(ret_image, _image.split()[-1])
            ret_images.append(pil2tensor(ret_image))

        log(f"{NODE_NAME} Processed {len(ret_images)} image(s).", message_type='finish')
        return (torch.cat(ret_images, dim=0),)

```