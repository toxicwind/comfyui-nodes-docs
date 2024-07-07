# Documentation
- Class name: comfyLoader
- Category: EasyUse/Loaders
- Output node: False
- Repo Ref: https://github.com/yolain/ComfyUI-Easy-Use.git

The `adv_pipeloader'method of the `comfyLoader'class simplifys the process of loading and preparing models and data for advanced cases. It integrates components such as VAE, CLIP and LORA and creates a comprehensive processing process that allows high-quality images to be generated and operated on the basis of instructions and preferences provided by users.

# Input types
## Required
- ckpt_name
    - ckpt_name is the key to determining the specific model configuration to be used in the process. It influences the overall performance and output of the node by determining the structure of the model and the parameters learned.
    - Comfy dtype: COMBO[folder_paths.get_filename_list('checkpoints')]
    - Python dtype: Union[str, None]
- vae_name
    - The vae_name parameter is essential to the selection of an appropriate variable-based encoder model and plays an important role in the potential representation of the generation and operation of images.
    - Comfy dtype: COMBO[['Baked VAE'] + folder_paths.get_filename_list('vae')]
    - Python dtype: Union[str, None]
- clip_skip
    - The parameter `clip_skip'plays an important role in controlling interactions with the CLIP model, influencing how nodes use semantic information to enhance image generation.
    - Comfy dtype: INT
    - Python dtype: int
- lora_name
    - The lora_name parameter is essential to enable the fine-tuning of models with LORA layers, which refines the image generation process according to the user's specific preferences.
    - Comfy dtype: COMBO[['None'] + folder_paths.get_filename_list('loras')]
    - Python dtype: Union[str, None]
- lora_model_strength
    - The parameter `lora_model_strength'adjusts the influence of the LORA layer on model output, directly affecting the fine-tuning process and the image quality generated.
    - Comfy dtype: FLOAT
    - Python dtype: float
- lora_clip_strength
    - The parameter `lora_climp_strength' regulates the strength of the integration of the CLIP model with the LORA layer, which is essential for achieving a balance between semantic accuracy and visual authenticity in the images generated.
    - Comfy dtype: FLOAT
    - Python dtype: float
- resolution
    - The resolution parameters determine the size of the output image and significantly influence the level of detail and computational resources required for image generation.
    - Comfy dtype: COMBO[resolution_strings]
    - Python dtype: Union[str, None]
- empty_latent_width
    - The parameter `empty_latent_width'sets the width of the potential space, which is essential for determining the range of possible image changes that can be generated.
    - Comfy dtype: INT
    - Python dtype: int
- empty_latent_height
    - The parameter `empty_latet_height'defines the altitude of potential space and plays a key role in the diversity of image output and in the efficiency of the production process.
    - Comfy dtype: INT
    - Python dtype: int
- positive
    - The parameter `positive'contains the text of a positive reminder, which is essential for guiding the model to produce images that correspond to the desired aesthetic or thematic orientation.
    - Comfy dtype: STRING
    - Python dtype: str
- negative
    - The parameter `negative'contains negative hint text, which is essential to steer the model away from the features or styles that are not required in the creation of the image.
    - Comfy dtype: STRING
    - Python dtype: str
- batch_size
    - The parameter `batch_size'determines the number of images to be processed simultaneously, affecting the volume of throughput and the computational efficiency of the image generation process.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- ui
    - UI output provides user-friendly indications of wildcard tips, which are important for visualization to apply to both the positive and negative impacts of the image generation process.
    - Comfy dtype: DICT
    - Python dtype: Dict[str, str]
- result
    - The output is a comprehensive set of models, VAE, CLIP and other relevant data structures that are essential for further image operation and analysis.
    - Comfy dtype: TUPLE
    - Python dtype: Tuple[Dict[str, Any], ModelPatcher, VAE, CLIP, torch.Tensor]

# Usage tips
- Infra type: GPU

# Source code
```
class comfyLoader:

    @classmethod
    def INPUT_TYPES(cls):
        resolution_strings = [f'{width} x {height}' for (width, height) in BASE_RESOLUTIONS]
        return {'required': {'ckpt_name': (folder_paths.get_filename_list('checkpoints'),), 'vae_name': (['Baked VAE'] + folder_paths.get_filename_list('vae'),), 'clip_skip': ('INT', {'default': -1, 'min': -24, 'max': 0, 'step': 1}), 'lora_name': (['None'] + folder_paths.get_filename_list('loras'),), 'lora_model_strength': ('FLOAT', {'default': 1.0, 'min': -10.0, 'max': 10.0, 'step': 0.01}), 'lora_clip_strength': ('FLOAT', {'default': 1.0, 'min': -10.0, 'max': 10.0, 'step': 0.01}), 'resolution': (resolution_strings, {'default': '512 x 512'}), 'empty_latent_width': ('INT', {'default': 512, 'min': 64, 'max': MAX_RESOLUTION, 'step': 8}), 'empty_latent_height': ('INT', {'default': 512, 'min': 64, 'max': MAX_RESOLUTION, 'step': 8}), 'positive': ('STRING', {'default': 'Positive', 'multiline': True}), 'negative': ('STRING', {'default': 'Negative', 'multiline': True}), 'batch_size': ('INT', {'default': 1, 'min': 1, 'max': 64})}, 'optional': {'optional_lora_stack': ('LORA_STACK',)}, 'hidden': {'prompt': 'PROMPT', 'my_unique_id': 'UNIQUE_ID'}}
    RETURN_TYPES = ('PIPE_LINE', 'MODEL', 'VAE')
    RETURN_NAMES = ('pipe', 'model', 'vae')
    FUNCTION = 'adv_pipeloader'
    CATEGORY = 'EasyUse/Loaders'

    def adv_pipeloader(self, ckpt_name, vae_name, clip_skip, lora_name, lora_model_strength, lora_clip_strength, resolution, empty_latent_width, empty_latent_height, positive, negative, batch_size, optional_lora_stack=None, prompt=None, my_unique_id=None):
        return fullLoader.adv_pipeloader(self, ckpt_name, 'Default', vae_name, clip_skip, lora_name, lora_model_strength, lora_clip_strength, resolution, empty_latent_width, empty_latent_height, positive, 'none', 'comfy', negative, 'none', 'comfy', batch_size, None, None, None, optional_lora_stack, False, prompt, my_unique_id)
```