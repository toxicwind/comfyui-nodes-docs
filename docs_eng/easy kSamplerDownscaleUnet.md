# Documentation
- Class name: samplerSimpleDownscaleUnet
- Category: EasyUse/Sampler
- Output node: True
- Repo Ref: https://github.com/yolain/ComfyUI-Easy-Use.git

This node is particularly suitable for optimizing the image processing workflow to ensure that the image is effectively scaled without loss of detail or clarity.

# Input types
## Required
- pipe
    - The pipe parameter is necessary because it represents a conduit containing image data to be processed. It is through this parameter that node accesss the image and performs subsequent zoom operations.
    - Comfy dtype: PIPE_LINE
    - Python dtype: Dict[str, Any]
- downscale_mode
    - The downscale_mode parameter determines the method to be used to narrow the image. It can be set to 'Auto' for automatic selection or 'Custom' for manual configuration, which is essential to control the scaling process.
    - Comfy dtype: COMBO[None, Auto, Custom]
    - Python dtype: str
- block_number
    - Block_number parameters specify the number of blocks to be used in the downsizing process. It is an important factor affecting the efficiency and results of scaling operations.
    - Comfy dtype: INT
    - Python dtype: int
- downscale_factor
    - The downscale_factor parameter defines the zoom factor used to reduce the size of the image. It plays an important role in the downsizing process and directly affects the final size of the image.
    - Comfy dtype: FLOAT
    - Python dtype: float
- start_percent
    - The start_percent parameter establishes the starting percentage of the scaling process. It is an important parameter that helps to determine the initial state of the image scaling.
    - Comfy dtype: FLOAT
    - Python dtype: float
- end_percent
    - End_percent parameters set the end percentage of the scaling process. It is a key factor in controlling the final appearance of the image after scaling.
    - Comfy dtype: FLOAT
    - Python dtype: float
- downscale_after_skip
    - This may affect the quality of the image after the reduction.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- downscale_method
    - The downscale_method parameter selects the algorithm to be used to narrow the image. This is a key option that can significantly influence the quality of the result image.
    - Comfy dtype: COMBO[bicubic, nearest-exact, bilinear, area, bislerp]
    - Python dtype: str
- upscale_method
    - Upscale_method parameters determine the algorithm to be used to magnify the image after the image has shrunk. It is important to improve the quality of the image during the magnification phase.
    - Comfy dtype: COMBO[bicubic, nearest-exact, bilinear, area, bislerp]
    - Python dtype: str
- image_output
    - The image_output parameter indicates how to handle the image generated. It can be set to hide the image, preview the image, save the image or a combination of these options, which is essential for managing the output of the node.
    - Comfy dtype: COMBO[Hide, Preview, Save, Hide/Save, Sender, Sender/Save]
    - Python dtype: str
- link_id
    - Link_id parameters are used to link the output of nodes to specific links or processes. It is important to track and manage the output of nodes in larger workflows.
    - Comfy dtype: INT
    - Python dtype: int
- save_prefix
    - The save_prefix parameter is a prefix for saving the image file. It is a useful parameter for organizing and identifying the saved image file.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- pipe
    - Pipe output provides a processed image pipeline, including scaled images and other relevant data. It is important because it allows further processing or analysis of images in subsequent nodes.
    - Comfy dtype: PIPE_LINE
    - Python dtype: Dict[str, Any]
- image
    - The image output represents the zoom image obtained after processing the node. It is the key output for visual screening and further operation of the image.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class samplerSimpleDownscaleUnet:

    def __init__(self):
        pass
    upscale_methods = ['bicubic', 'nearest-exact', 'bilinear', 'area', 'bislerp']

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'pipe': ('PIPE_LINE',), 'downscale_mode': (['None', 'Auto', 'Custom'], {'default': 'Auto'}), 'block_number': ('INT', {'default': 3, 'min': 1, 'max': 32, 'step': 1}), 'downscale_factor': ('FLOAT', {'default': 2.0, 'min': 0.1, 'max': 9.0, 'step': 0.001}), 'start_percent': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1.0, 'step': 0.001}), 'end_percent': ('FLOAT', {'default': 0.35, 'min': 0.0, 'max': 1.0, 'step': 0.001}), 'downscale_after_skip': ('BOOLEAN', {'default': True}), 'downscale_method': (s.upscale_methods,), 'upscale_method': (s.upscale_methods,), 'image_output': (['Hide', 'Preview', 'Save', 'Hide/Save', 'Sender', 'Sender/Save'], {'default': 'Preview'}), 'link_id': ('INT', {'default': 0, 'min': 0, 'max': sys.maxsize, 'step': 1}), 'save_prefix': ('STRING', {'default': 'ComfyUI'})}, 'optional': {'model': ('MODEL',)}, 'hidden': {'tile_size': 'INT', 'prompt': 'PROMPT', 'extra_pnginfo': 'EXTRA_PNGINFO', 'my_unique_id': 'UNIQUE_ID', 'embeddingsList': (folder_paths.get_filename_list('embeddings'),)}}
    RETURN_TYPES = ('PIPE_LINE', 'IMAGE')
    RETURN_NAMES = ('pipe', 'image')
    OUTPUT_NODE = True
    FUNCTION = 'run'
    CATEGORY = 'EasyUse/Sampler'

    def run(self, pipe, downscale_mode, block_number, downscale_factor, start_percent, end_percent, downscale_after_skip, downscale_method, upscale_method, image_output, link_id, save_prefix, model=None, tile_size=None, prompt=None, extra_pnginfo=None, my_unique_id=None, force_full_denoise=False, disable_noise=False):
        downscale_options = None
        if downscale_mode == 'Auto':
            downscale_options = {'block_number': block_number, 'downscale_factor': None, 'start_percent': 0, 'end_percent': 0.35, 'downscale_after_skip': True, 'downscale_method': 'bicubic', 'upscale_method': 'bicubic'}
        elif downscale_mode == 'Custom':
            downscale_options = {'block_number': block_number, 'downscale_factor': downscale_factor, 'start_percent': start_percent, 'end_percent': end_percent, 'downscale_after_skip': downscale_after_skip, 'downscale_method': downscale_method, 'upscale_method': upscale_method}
        return samplerFull().run(pipe, None, None, None, None, None, image_output, link_id, save_prefix, None, model, None, None, None, None, None, None, tile_size, prompt, extra_pnginfo, my_unique_id, force_full_denoise, disable_noise, downscale_options)
```