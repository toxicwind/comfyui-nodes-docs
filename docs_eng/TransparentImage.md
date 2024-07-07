# Documentation
- Class name: TransparentImage
- Category: ♾️Mixlab/Image
- Output node: True
- Repo Ref: https://github.com/shadowcz007/comfyui-mixlab-nodes.git

TransparentImage is designed to process and operate transparent images, providing the function of creating and managing masks. It allows colour inverting, saving processed images and processing image formats. The node plays a key role in enhancing visual content by applying masks to images, allowing for innovative visual effects and modifications.

# Input types
## Required
- images
    - The `images' parameter is essential for the operation of the node because it is an input image to be processed. It is a key element that directly influences the output of the node and determines the visual content to be converted and operated.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- masks
    - The `masks' parameter defines the mask that will be applied to the input image. It is an essential part of the node function because it determines the area in which the image will be affected by the mask treatment.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor
- invert
    - The `invert' parameter allows the inverse colour of the image after processing. This is an optional feature that can significantly change the visual result and provide a means of creating a comparison effect within the image.
    - Comfy dtype: COMBO['yes', 'no']
    - Python dtype: str
- save
    - The `save' parameter determines whether the processed image will be saved on disk. This is a key decision point for the node because it affects the persistence of visual changes to the image.
    - Comfy dtype: COMBO['yes', 'no']
    - Python dtype: str
- filename_prefix
    - The 'filename_prefix' parameter is used to specify the prefix for the saved image file. It provides a more efficient way to organize and identify the output file and enhances the management of the stored visual content.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- file_path
    - The 'file_path' output provides the path to the saved image file. It is important because it allows users to locate and access processed images for further use or distribution.
    - Comfy dtype: STRING
    - Python dtype: str
- IMAGE
    - The `IMAGE' output represents the image processed in RGB format. It is the direct result of node operations and is essential for visualization of changes made to input images.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- RGBA
    - The ‘RGBA’ output contains processed images with transparency information. This is an important aspect of the application that needs to be kept in the alpha channel of the original image for further editing or synthesis.
    - Comfy dtype: RGBA
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class TransparentImage:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'images': ('IMAGE',), 'masks': ('MASK',), 'invert': (['yes', 'no'],), 'save': (['yes', 'no'],)}, 'optional': {'filename_prefix': ('STRING', {'multiline': False, 'default': 'Mixlab_save'})}, 'hidden': {'prompt': 'PROMPT', 'extra_pnginfo': 'EXTRA_PNGINFO'}}
    RETURN_TYPES = ('STRING', 'IMAGE', 'RGBA')
    RETURN_NAMES = ('file_path', 'IMAGE', 'RGBA')
    OUTPUT_NODE = True
    FUNCTION = 'run'
    CATEGORY = '♾️Mixlab/Image'
    OUTPUT_IS_LIST = (True, True, True)

    def run(self, images, masks, invert, save, filename_prefix, prompt=None, extra_pnginfo=None):
        ui_images = []
        image_paths = []
        count = images.shape[0]
        masks_new = []
        nh = masks.shape[0] // count
        masks_new = masks
        if images.shape[0] == masks.shape[0] and images.shape[1] == masks.shape[1] and (images.shape[2] == masks.shape[2]):
            print('TransparentImage', images.shape, images.size(), masks.shape, masks.size())
        elif nh * count == masks.shape[0]:
            masks_new = split_mask_by_new_height(masks, nh)
        else:
            masks_new = split_mask_by_new_height(masks, masks.shape[0])
        is_save = True if save == 'yes' else False
        images_rgb = []
        images_rgba = []
        for i in range(len(images)):
            image = images[i]
            mask = masks_new[i]
            result = doMask(image, mask, is_save, filename_prefix, invert, not is_save, prompt, extra_pnginfo)
            for item in result['result']:
                ui_images.append(item)
            image_paths.append(result['image_path'])
            images_rgb.append(result['im_tensor'])
            images_rgba.append(result['im_rgba_tensor'])
        return {'ui': {'images': ui_images, 'image_paths': image_paths}, 'result': (image_paths, images_rgb, images_rgba)}
```