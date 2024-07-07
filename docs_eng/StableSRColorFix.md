# Documentation
- Class name: StableSRColorFix
- Category: image
- Output node: False
- Repo Ref: https://github.com/Arthurzhangsheng/Comfyui-StableSR.git

The StableSRColorFix node is designed to enhance the colour quality of the image by applying advanced colour correction techniques. It uses the ability of the deep learning model to intelligently adjust the colour palettes of the input image to match the reference colour map to produce a visually consistent and beautiful output.

# Input types
## Required
- image
    - Enter the image is the key parameter for the StableSRColorFix node, as it is the main data that will be subject to color correction. The node processes the image to keep its colour distribution consistent with the color_map_image to ensure that the final output is visually consistent.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image or torch.Tensor
- color_map_image
    - color_map_image is the reference for the colour adjustment. It is essential to guide the colour correction process in order to achieve harmony in the output image.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image or torch.Tensor
- color_fix
    - The color_fix parameter determines the type of color correction algorithm to be used for the node. It can be 'Wavelet' or 'AdaIN', and all methods provide different colour adjustment methods, which significantly affect the final appearance of the corrected image.
    - Comfy dtype: COMBO['Wavelet', 'AdaIN']
    - Python dtype: str

# Output types
- refined_image
    - Refined_image is the output of the colour correction process, representing an enhanced version of the input image with improved colour authenticity. It is the top of the node function and shows the validity of the selected color_fix algorithm.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class StableSRColorFix:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'color_map_image': ('IMAGE',), 'color_fix': (['Wavelet', 'AdaIN'],)}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'fix_color'
    CATEGORY = 'image'

    def fix_color(self, image, color_map_image, color_fix):
        print(f'[StableSR] fix_color')
        try:
            color_fix_func = wavelet_color_fix if color_fix == 'Wavelet' else adain_color_fix
            result_image = color_fix_func(tensor2pil(image), tensor2pil(color_map_image))
            refined_image = pil2tensor(result_image)
            return (refined_image,)
        except Exception as e:
            print(f'[StableSR] Error fix_color: {e}')
```