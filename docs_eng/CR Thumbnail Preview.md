# Documentation
- Class name: CR_ThumbnailPreview
- Category: Comfyroll/Graphics/Template
- Output node: True
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

The CR_ThumbnailPreview node is designed to process and display a series of images as thumbnails. It narrows the image to a specified size, adds borders to make visual distinctions, and arranges them in grid format for easy review. This node is particularly suitable for applications that require a compact display of multiple images, such as previews or galleries.

# Input types
## Required
- image
    - The 'image'parameter is the input length of the image that you want to process. It is the basis for node operations, as it is the raw data that will be converted into a thumbnail preview.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
## Optional
- rescale_factor
    - The'rescale_factor' parameter determines the scale of the image. It is essential to control the size of the thumbnail and allows users to adjust the preview size as needed.
    - Comfy dtype: FLOAT
    - Python dtype: float
- max_columns
    - The'max_columns' parameter specifies the maximum number of columns in the grid layout of the thumbnail. It affects the way the image is arranged, and it is important for the overall grid to be displayed.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- ui
    - The 'ui'output parameter is a dictionary containing images arranged in grids. It is important because it provides the ultimate visual representation of thumbnails for display purposes.
    - Comfy dtype: DICT
    - Python dtype: Dict[str, List[Dict[str, Union[str, torch.Tensor]]]]
- result
    - The 'Result' output parameter is a widget that contains the help document URL. It is useful for users who need additional guidance or information about node functions.
    - Comfy dtype: TUPLE
    - Python dtype: Tuple[str,]

# Usage tips
- Infra type: CPU

# Source code
```
class CR_ThumbnailPreview:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'rescale_factor': ('FLOAT', {'default': 0.25, 'min': 0.1, 'max': 1.0, 'step': 0.01}), 'max_columns': ('INT', {'default': 5, 'min': 0, 'max': 256})}}
    RETURN_TYPES = ('STRING',)
    RETURN_NAMES = ('show_help',)
    OUTPUT_NODE = True
    FUNCTION = 'thumbnail'
    CATEGORY = icons.get('Comfyroll/Graphics/Template')

    def thumbnail(self, image, rescale_factor, max_columns):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Template-Nodes#cr-thumbnail-preview'
        result_images = []
        outline_thickness = 1
        for img in image:
            pil_img = tensor2pil(img)
            (original_width, original_height) = pil_img.size
            rescaled_img = apply_resize_image(tensor2pil(img), original_width, original_height, 8, 'rescale', 'false', rescale_factor, 256, 'lanczos')
            outlined_img = ImageOps.expand(rescaled_img, outline_thickness, fill='black')
            result_images.append(outlined_img)
        combined_image = make_grid_panel(result_images, max_columns)
        images_out = pil2tensor(combined_image)
        results = []
        for tensor in images_out:
            array = 255.0 * tensor.cpu().numpy()
            image = Image.fromarray(np.clip(array, 0, 255).astype(np.uint8))
            server = PromptServer.instance
            server.send_sync(BinaryEventTypes.UNENCODED_PREVIEW_IMAGE, ['PNG', image, None], server.client_id)
            results.append({'source': 'websocket', 'content-type': 'image/png', 'type': 'output'})
        return {'ui': {'images': results}, 'result': (show_help,)}
```