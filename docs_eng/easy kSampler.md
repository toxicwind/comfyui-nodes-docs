# Documentation
- Class name: samplerSimple
- Category: EasyUse/Sampler
- Output node: True
- Repo Ref: https://github.com/yolain/ComfyUI-Easy-Use.git

The node streamlines the sampling process through a complex configuration in the abstract, allowing users to generate images with minimal input. It focuses on ease of use and simplicity of operation, providing a direct interface to the image generation task.

# Input types
## Required
- pipe
    - The pipe parameter is the main data source and setting source for node operations. It is essential because it contains the context required for the sampling process, including model information and previous processing steps.
    - Comfy dtype: PIPE_LINE
    - Python dtype: Dict
- image_output
    - This parameter determines how the image generated should be treated. It is important in determining the output format and the subsequent action (e.g. showing, saving or sending the image).
    - Comfy dtype: COMBO
    - Python dtype: Union[str, None]
- link_id
    - Link_id parameters are essential to establish connectivity between the different components within the system and to ensure that the correct data flow to the appropriate destination.
    - Comfy dtype: INT
    - Python dtype: int
- save_prefix
    - This parameter defines the prefix for saving the file, which is important for organizing and identifying the output in a directory that may contain a large number of outputs.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- model
    - Model parameters provide a neural network structure for the sampling process. It is optional, but it can significantly influence the quality and properties of the images generated.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- tile_size
    - When a flat image is generated, the tile_size parameter is relevant, which affects how the output is divided and constructed. It plays a role in the efficiency and appearance of the final image.
    - Comfy dtype: INT
    - Python dtype: int
- prompt
    - The prompt parameter is a text description that guides the generation of images. It is important to channel the creation process to the desired results.
    - Comfy dtype: PROMPT
    - Python dtype: str
- extra_pnginfo
    - This parameter contains additional information relevant to the PNG image that can be used to refine the image generation process.
    - Comfy dtype: EXTRA_PNGINFO
    - Python dtype: Dict
- my_unique_id
    - My_unique_id parameters are used to track and manage examples of node operations to ensure that each operation is uniquely identified and referenced.
    - Comfy dtype: UNIQUE_ID
    - Python dtype: str

# Output types
- pipe
    - Pipe output is a structured collection of data, including updated models, samples and other relevant information after the sampling process. It is essential to transmit or review the system state to a subsequent node.
    - Comfy dtype: PIPE_LINE
    - Python dtype: Dict
- image
    - The image output contains the visual content generated, representing the main result of the node operation. It is important because it shows the results of the sampling process.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class samplerSimple:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'pipe': ('PIPE_LINE',), 'image_output': (['Hide', 'Preview', 'Save', 'Hide/Save', 'Sender', 'Sender/Save'], {'default': 'Preview'}), 'link_id': ('INT', {'default': 0, 'min': 0, 'max': sys.maxsize, 'step': 1}), 'save_prefix': ('STRING', {'default': 'ComfyUI'})}, 'optional': {'model': ('MODEL',)}, 'hidden': {'tile_size': 'INT', 'prompt': 'PROMPT', 'extra_pnginfo': 'EXTRA_PNGINFO', 'my_unique_id': 'UNIQUE_ID', 'embeddingsList': (folder_paths.get_filename_list('embeddings'),)}}
    RETURN_TYPES = ('PIPE_LINE', 'IMAGE')
    RETURN_NAMES = ('pipe', 'image')
    OUTPUT_NODE = True
    FUNCTION = 'run'
    CATEGORY = 'EasyUse/Sampler'

    def run(self, pipe, image_output, link_id, save_prefix, model=None, tile_size=None, prompt=None, extra_pnginfo=None, my_unique_id=None, force_full_denoise=False, disable_noise=False):
        return samplerFull().run(pipe, None, None, None, None, None, image_output, link_id, save_prefix, None, model, None, None, None, None, None, None, None, prompt, extra_pnginfo, my_unique_id, force_full_denoise, disable_noise)
```