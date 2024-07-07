# Documentation
- Class name: a1111Loader
- Category: EasyUse/Loaders
- Output node: False
- Repo Ref: https://github.com/yolain/ComfyUI-Easy-Use.git

The node facilitates the loading and integration of various model components, including checkpoints, VAE and LORA stacks, in order to establish a comprehensive pipeline for processing and generating images based on the tips and parameters provided.

# Input types
## Required
- ckpt_name
    - The name of the check point is essential to specify the model state to be loaded, and it directly affects the ability of the node to generate the image according to the configuration required.
    - Comfy dtype: COMBO
    - Python dtype: str
- vae_name
    - VAE name parameters are essential for the selection of appropriate variable self-encoder models and play an important role in the image generation process.
    - Comfy dtype: COMBO
    - Python dtype: str
- clip_skip
    - Clip_skip parameters are important for controlling the interaction between CLIP and the model, affecting the efficiency of nodes and the quality of the images generated.
    - Comfy dtype: INT
    - Python dtype: int
- lora_name
    - LORA name parameters are essential for applying specific enhancements to the model, which can significantly improve the performance of nodes in the image generation task.
    - Comfy dtype: COMBO
    - Python dtype: str
- lora_model_strength
    - The lora_model_strength parameter adjusts the impact of LORA enhancements on the model to affect the ability of nodes to fine-tune image generation according to specific requirements.
    - Comfy dtype: FLOAT
    - Python dtype: float
- lora_clip_strength
    - The lora_clip_strength parameter changes the intensity of the integration of CLIP with LORA, which is essential for achieving a balanced and coordinated image-generation process.
    - Comfy dtype: FLOAT
    - Python dtype: float
- resolution
    - The resolution parameter defines the size of the output image, which is a key factor in determining the high-quality visual effect of the node.
    - Comfy dtype: COMBO
    - Python dtype: str
- empty_latent_width
    - Empty_latent_width parameters set the width of potential space, which is critical to the ability of nodes to generate diverse and complex image patterns.
    - Comfy dtype: INT
    - Python dtype: int
- empty_latent_height
    - Empty_latent_height parameters create potential space heights, affecting the ability of nodes to create detailed and nuanced images.
    - Comfy dtype: INT
    - Python dtype: int
- positive
    - The positionive parameter provides a positive hint to guide the image generation process and significantly influences the output quality and relevance of the node.
    - Comfy dtype: STRING
    - Python dtype: str
- negative
    - Negative parameters provide negative hints to improve image generation, focusing on the ability of nodes to avoid unwanted features in their output.
    - Comfy dtype: STRING
    - Python dtype: str
- batch_size
    - Match_size parameters determine the number of images to be processed at the same time, which affects node throughput and efficiency.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- pipe
    - Pipe output covers loaded models and settings and provides the basis for subsequent image generation and processing tasks.
    - Comfy dtype: PIPE_LINE
    - Python dtype: dict
- model
    - Model output provides a loaded model, which is essential for image generation based on input tips and parameters.
    - Comfy dtype: MODEL
    - Python dtype: ModelPatcher
- vae
    - The vae output contains the loaded VAE model, which is essential for generating and processing potential space and images.
    - Comfy dtype: VAE
    - Python dtype: VAE

# Usage tips
- Infra type: CPU

# Source code
```
class a1111Loader:

    @classmethod
    def INPUT_TYPES(cls):
        resolution_strings = [f'{width} x {height}' for (width, height) in BASE_RESOLUTIONS]
        a1111_prompt_style_default = False
        checkpoints = folder_paths.get_filename_list('checkpoints')
        loras = ['None'] + folder_paths.get_filename_list('loras')
        return {'required': {'ckpt_name': (checkpoints,), 'vae_name': (['Baked VAE'] + folder_paths.get_filename_list('vae'),), 'clip_skip': ('INT', {'default': -1, 'min': -24, 'max': 0, 'step': 1}), 'lora_name': (loras,), 'lora_model_strength': ('FLOAT', {'default': 1.0, 'min': -10.0, 'max': 10.0, 'step': 0.01}), 'lora_clip_strength': ('FLOAT', {'default': 1.0, 'min': -10.0, 'max': 10.0, 'step': 0.01}), 'resolution': (resolution_strings, {'default': '512 x 512'}), 'empty_latent_width': ('INT', {'default': 512, 'min': 64, 'max': MAX_RESOLUTION, 'step': 8}), 'empty_latent_height': ('INT', {'default': 512, 'min': 64, 'max': MAX_RESOLUTION, 'step': 8}), 'positive': ('STRING', {'default': 'Positive', 'multiline': True}), 'negative': ('STRING', {'default': 'Negative', 'multiline': True}), 'batch_size': ('INT', {'default': 1, 'min': 1, 'max': 64})}, 'optional': {'optional_lora_stack': ('LORA_STACK',), 'a1111_prompt_style': ('BOOLEAN', {'default': a1111_prompt_style_default})}, 'hidden': {'prompt': 'PROMPT', 'my_unique_id': 'UNIQUE_ID'}}
    RETURN_TYPES = ('PIPE_LINE', 'MODEL', 'VAE')
    RETURN_NAMES = ('pipe', 'model', 'vae')
    FUNCTION = 'adv_pipeloader'
    CATEGORY = 'EasyUse/Loaders'

    def adv_pipeloader(self, ckpt_name, vae_name, clip_skip, lora_name, lora_model_strength, lora_clip_strength, resolution, empty_latent_width, empty_latent_height, positive, negative, batch_size, optional_lora_stack=None, a1111_prompt_style=False, prompt=None, my_unique_id=None):
        return fullLoader.adv_pipeloader(self, ckpt_name, 'Default', vae_name, clip_skip, lora_name, lora_model_strength, lora_clip_strength, resolution, empty_latent_width, empty_latent_height, positive, 'mean', 'A1111', negative, 'mean', 'A1111', batch_size, None, None, None, optional_lora_stack, a1111_prompt_style, prompt, my_unique_id)
```