# Documentation
- Class name: samplerSimpleTiled
- Category: EasyUse/Sampler
- Output node: True
- Repo Ref: https://github.com/yolain/ComfyUI-Easy-Use.git

The node streamlines the sampling process by managing the layout of the image and by processing the output according to the user’s preferences. It abstractes the complexity of the sampling, allowing users to focus on creative input without worrying about the technical details of the sampling process.

# Input types
## Required
- pipe
    - Pipeline parameters are necessary because they carry the state of the entire flow line, including models and data information, to guide node execution.
    - Comfy dtype: PIPE_LINE
    - Python dtype: Dict
- tile_size
    - The flat size parameters determine the size of the flat output, which is essential for controlling the resolution and layout of the final image.
    - Comfy dtype: INT
    - Python dtype: int
- image_output
    - This parameter controls the handling of image output, whether for preview, preservation or other purposes, affecting the availability of nodes and workflows.
    - Comfy dtype: COMBO
    - Python dtype: Union[str, None]
- link_id
    - Link ID parameters are important for establishing connectivity between different parts of the system, ensuring correct data flow and communication.
    - Comfy dtype: INT
    - Python dtype: int
- save_prefix
    - This parameter specifies the prefix for saving the file, which is essential for organizing and identifying the output in the file system.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- model
    - When model parameters are provided, nodes are allowed to use specific models during the sampling process to influence the quality and properties of the images generated.
    - Comfy dtype: MODEL
    - Python dtype: Any
- prompt
    - The reminder parameters are used to guide the generation process and their content significantly influences the creative direction and results of the sampling.
    - Comfy dtype: PROMPT
    - Python dtype: Any
- extra_pnginfo
    - This parameter contains additional information relevant to the PNG image, which enhances the processing and processing of such images within the node.
    - Comfy dtype: EXTRA_PNGINFO
    - Python dtype: Any
- my_unique_id
    - The only ID parameters are used to track and manage the various examples of node operations to ensure individualization and targeted implementation.
    - Comfy dtype: UNIQUE_ID
    - Python dtype: Any

# Output types
- pipe
    - Pipe output is an integrated structure, including an updated flow line state, reflecting the changes made during the sampling process.
    - Comfy dtype: PIPE_LINE
    - Python dtype: Dict
- image
    - Image output represents the visual results of sampling and is the main creative element of node generation.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class samplerSimpleTiled:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'pipe': ('PIPE_LINE',), 'tile_size': ('INT', {'default': 512, 'min': 320, 'max': 4096, 'step': 64}), 'image_output': (['Hide', 'Preview', 'Save', 'Hide/Save', 'Sender', 'Sender/Save'], {'default': 'Preview'}), 'link_id': ('INT', {'default': 0, 'min': 0, 'max': sys.maxsize, 'step': 1}), 'save_prefix': ('STRING', {'default': 'ComfyUI'})}, 'optional': {'model': ('MODEL',)}, 'hidden': {'prompt': 'PROMPT', 'extra_pnginfo': 'EXTRA_PNGINFO', 'my_unique_id': 'UNIQUE_ID', 'embeddingsList': (folder_paths.get_filename_list('embeddings'),)}}
    RETURN_TYPES = ('PIPE_LINE', 'IMAGE')
    RETURN_NAMES = ('pipe', 'image')
    OUTPUT_NODE = True
    FUNCTION = 'run'
    CATEGORY = 'EasyUse/Sampler'

    def run(self, pipe, tile_size=512, image_output='preview', link_id=0, save_prefix='ComfyUI', model=None, prompt=None, extra_pnginfo=None, my_unique_id=None, force_full_denoise=False, disable_noise=False):
        return samplerFull().run(pipe, None, None, None, None, None, image_output, link_id, save_prefix, None, model, None, None, None, None, None, None, tile_size, prompt, extra_pnginfo, my_unique_id, force_full_denoise, disable_noise)
```