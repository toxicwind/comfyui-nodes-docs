# Documentation
- Class name: samplerCascadeSimple
- Category: EasyUse/Sampler
- Output node: True
- Repo Ref: https://github.com/yolain/ComfyUI-Easy-Use.git

The samplerCascadeSimple node is designed to simplify the image sampling process by providing a simplified interface to make it easier for users to use. It abstractes the complexity of the bottom sampling process and allows users to generate images with minimal configurations. The node focuses on ease of use and efficiency, ensuring that users can quickly obtain the required output without having to go into the details of the sampling algorithm.

# Input types
## Required
- pipe
    - The `pipe' parameter is essential for the operation of the node because it represents a conduit containing the settings and data required for image sampling. It is through this parameter that the node receives input to generate the output image required.
    - Comfy dtype: PIPE_LINE
    - Python dtype: Dict[str, Any]
- image_output
    - The `image_output' parameter determines how the node produces the images. It determines whether the image is previewed, saved or sent, and thus plays a key role in the execution process of the node.
    - Comfy dtype: COMBO['Hide', 'Preview', 'Save', 'Hide/Save', 'Sender', 'Sender/Save']
    - Python dtype: str
- link_id
    - The `link_id' parameter is used to create the only link or reference to the image generated. This may be important for tracking or linking output to specific user requests or processes.
    - Comfy dtype: INT
    - Python dtype: int
- save_prefix
    - The'save_prefix' parameter specifies the prefix to be used to save the images generated. This affects the naming protocol for saving files, making it easier for users to identify and organize their output.
    - Comfy dtype: STRING
    - Python dtype: str
- model_c
    - The optional `model_c' parameter allows the user to provide a specific model to be used in the sampling process. This may be particularly useful when the user has a preference for a particular model or needs to apply a specific model setting.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module

# Output types
- pipe
    - The `pipe' output provides an up-to-date pipeline after the sampling process, including the images generated and any other relevant data. This output is important because it may be used for further processing or analysis.
    - Comfy dtype: PIPE_LINE
    - Python dtype: Dict[str, Any]
- image
    - The 'image'output represents the image generated during the sampling process. This is the main output most interested to most users because it is a visual result of node operations.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class samplerCascadeSimple:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'pipe': ('PIPE_LINE',), 'image_output': (['Hide', 'Preview', 'Save', 'Hide/Save', 'Sender', 'Sender/Save'], {'default': 'Preview'}), 'link_id': ('INT', {'default': 0, 'min': 0, 'max': sys.maxsize, 'step': 1}), 'save_prefix': ('STRING', {'default': 'ComfyUI'})}, 'optional': {'model_c': ('MODEL',)}, 'hidden': {'tile_size': 'INT', 'prompt': 'PROMPT', 'extra_pnginfo': 'EXTRA_PNGINFO', 'my_unique_id': 'UNIQUE_ID', 'embeddingsList': (folder_paths.get_filename_list('embeddings'),)}}
    RETURN_TYPES = ('PIPE_LINE', 'IMAGE')
    RETURN_NAMES = ('pipe', 'image')
    OUTPUT_NODE = True
    FUNCTION = 'run'
    CATEGORY = 'EasyUse/Sampler'

    def run(self, pipe, image_output, link_id, save_prefix, model_c=None, tile_size=None, prompt=None, extra_pnginfo=None, my_unique_id=None, force_full_denoise=False, disable_noise=False):
        return samplerCascadeFull().run(pipe, None, None, None, None, None, None, None, image_output, link_id, save_prefix, None, None, None, model_c, tile_size, prompt, extra_pnginfo, my_unique_id, force_full_denoise, disable_noise)
```