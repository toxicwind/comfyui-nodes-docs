# Documentation
- Class name: CR_SeamlessChecker
- Category: Comfyroll/Graphics/Template
- Output node: True
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

The CR_SeamlessChecker node is used to check the seamless integration of images. The node enables users to recognize and assess the mass of images by resizing images, generating grid layouts and displaying scalding versions of multiple images. It is widely applied in graphic design and image processing to ensure that final visual effects are seamlessly connected.

# Input types
## Required
- image
    - The image parameter is the main object of node processing, which directly influences the execution and inspection results of nodes and is the source data for seamless collation checks.
    - Comfy dtype: IMAGE
    - Python type: PIL.Image. Image or toch. Tensor
- rescale_factor
    - The zoom factor parameter is used to adjust the size of the image, which is critical for assessing the seamless collage effect of the image. Users can control the zooming of the image by using this parameter to see more precisely the details of the puzzle.
    - Comfy dtype: FLOAT
    - Python dtype: float
- grid_options
    - The grid option parameter is used to define the layout of the image in the grid, which determines the number of images to be displayed during a seamless collage check. This parameter is important for displaying a scaling version of multiple images and for assessing the integration effect of the entire grid.
    - Comfy dtype: COMBO['2x2', '3x3', '4x4', '5x5', '6x6']
    - Python dtype: str

# Output types
- show_help
    - Helping information provides node use guides and further resource links to enable users to understand and operate nodes more effectively.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_SeamlessChecker:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'rescale_factor': ('FLOAT', {'default': 0.25, 'min': 0.1, 'max': 1.0, 'step': 0.01}), 'grid_options': (['2x2', '3x3', '4x4', '5x5', '6x6'],)}}
    RETURN_TYPES = ('STRING',)
    RETURN_NAMES = ('show_help',)
    OUTPUT_NODE = True
    FUNCTION = 'thumbnail'
    CATEGORY = icons.get('Comfyroll/Graphics/Template')

    def thumbnail(self, image, rescale_factor, grid_options):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Other-Nodes#cr-seamless-checker'
        outline_thickness = 0
        pil_img = tensor2pil(image)
        (original_width, original_height) = pil_img.size
        rescaled_img = apply_resize_image(tensor2pil(image), original_width, original_height, 8, 'rescale', 'false', rescale_factor, 256, 'lanczos')
        outlined_img = ImageOps.expand(rescaled_img, outline_thickness, fill='black')
        max_columns = int(grid_options[0])
        repeat_images = [outlined_img] * max_columns ** 2
        combined_image = make_grid_panel(repeat_images, max_columns)
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