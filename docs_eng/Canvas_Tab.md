# Documentation
- Class name: Canvas_Tab
- Category: image
- Output node: False
- Repo Ref: https://github.com/Lerc/canvas_tab.git

Canvas_Tab acts as an intermediary in processing and processing visual content data in a separate tab environment.

# Input types
## Required
- unique_id
    - The only identifier for the example of an image buffer zone is essential for the management and association of image data in different tab pages or sessions.
    - Comfy dtype: str
    - Python dtype: str
- mask
    - The mask parameters are essential for defining areas of interest in the image, allowing for selective processing and analysis.
    - Comfy dtype: str
    - Python dtype: str
- canvas
    - A canvas parameter represents the source image, which is the basis for all image operations and editing operations.
    - Comfy dtype: str
    - Python dtype: str
## Optional
- images
    - An optional collection of images can be used for comparison or additional processing to enhance the multifunctionality of the image buffer zone.
    - Comfy dtype: list
    - Python dtype: list

# Output types
- rgb_image
    - Processed RGB image data for further analysis or operation.
    - Comfy dtype: tensor
    - Python dtype: torch.Tensor
- mask_data
    - The extracted mask data represent areas of interest and are essential for target image analysis and editing.
    - Comfy dtype: tensor
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class Canvas_Tab:
    """
    A Image Buffer for handling an editor in another tab.
    """

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'mask': ('CANVAS',), 'canvas': ('CANVAS',)}, 'hidden': {'unique_id': 'UNIQUE_ID'}}
    RETURN_TYPES = ('IMAGE', 'MASK')
    FUNCTION = 'image_buffer'
    CATEGORY = 'image'

    def image_buffer(self, unique_id, mask, canvas, images=None):
        print(f'-----hyn debug image_buffer : unique_id = {unique_id} canvas = {canvas} images = {images} masks = {mask}')
        if canvas.startswith('http'):
            from worker.components.utils import util
            i = util.get_image_from_uri(canvas)
        else:
            image_path = folder_paths.get_annotated_filepath(canvas)
            i = Image.open(image_path)
        i = ImageOps.exif_transpose(i)
        rgb_image = i.convert('RGB')
        rgb_image = np.array(rgb_image).astype(np.float32) / 255.0
        rgb_image = torch.from_numpy(rgb_image)[None,]
        if mask.startswith('http'):
            from worker.components.utils import util
            i = util.get_image_from_uri(mask)
        else:
            mask_path = folder_paths.get_annotated_filepath(mask)
            i = Image.open(mask_path)
        i = ImageOps.exif_transpose(i)
        if 'A' in i.getbands():
            mask_data = np.array(i.getchannel('A')).astype(np.float32) / 255.0
            mask_data = torch.from_numpy(mask_data)
        else:
            mask_data = torch.zeros((64, 64), dtype=torch.float32, device='cpu')
        return (rgb_image, mask_data)
```