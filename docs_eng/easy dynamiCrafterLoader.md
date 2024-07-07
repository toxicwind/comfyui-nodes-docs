# Documentation
- Class name: dynamiCrafterLoader
- Category: EasyUse/Loaders
- Output node: False
- Repo Ref: https://github.com/yolain/ComfyUI-Easy-Use.git

The node class covers the various models and data required to load and prepare the dynamyCrafter stream. It streamlines the process of model selection, initialization and reconciliation to ensure that the necessary components are ready for the subsequent task generation.

# Input types
## Required
- model_name
    - Model name parameters are essential to specify which model will be used in the dynamiteCraftLoader. It determines the basic structure and the parameters that guide the generation process.
    - Comfy dtype: COMBO
    - Python dtype: str
- clip_skip
    - The clip_skip parameter influences the selection of layers in the CLIP model that are used for text reconciliation. It is essential to fine-tune the production process to the desired creative direction.
    - Comfy dtype: INT
    - Python dtype: int
- init_image
    - The init_image parameter is a visual input into the potential space of the initialization process. It is a key factor in setting the initial conditions for the formation of the final output.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image
- resolution
    - The resolution parameter defines the size of the output generated. It is important for matching the desired quality and level of detail with the ability of the bottom model.
    - Comfy dtype: COMBO
    - Python dtype: str

# Output types
- pipe
    - Pipe output is an integrated structure that covers all the components required for the dynamyCrafter stream. It is designed to facilitate seamless integration with downstream generation tasks.
    - Comfy dtype: PIPE_LINE
    - Python dtype: dict
- model
    - Model output represents the generation model that is loaded and prepared. It is the core element that drives the generation process and converts input into the desired creative output.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- vae
    - The vae output is a variable-based encoder component for potential space operations and image regulation. It plays a vital role in generating diverse and coherent visual content.
    - Comfy dtype: VAE
    - Python dtype: comfy.sd.VAE

# Usage tips
- Infra type: GPU

# Source code
```
class dynamiCrafterLoader(DynamiCrafter):

    def __init__(self):
        super().__init__()

    @classmethod
    def INPUT_TYPES(cls):
        resolution_strings = [f'{width} x {height}' for (width, height) in BASE_RESOLUTIONS]
        return {'required': {'model_name': (list(DYNAMICRAFTER_MODELS.keys()),), 'clip_skip': ('INT', {'default': -2, 'min': -24, 'max': 0, 'step': 1}), 'init_image': ('IMAGE',), 'resolution': (resolution_strings, {'default': '512 x 512'}), 'empty_latent_width': ('INT', {'default': 256, 'min': 16, 'max': MAX_RESOLUTION, 'step': 8}), 'empty_latent_height': ('INT', {'default': 256, 'min': 16, 'max': MAX_RESOLUTION, 'step': 8}), 'positive': ('STRING', {'default': '', 'multiline': True}), 'negative': ('STRING', {'default': '', 'multiline': True}), 'use_interpolate': ('BOOLEAN', {'default': False}), 'fps': ('INT', {'default': 15, 'min': 1, 'max': 30, 'step': 1}), 'frames': ('INT', {'default': 16}), 'scale_latents': ('BOOLEAN', {'default': False})}, 'optional': {'optional_vae': ('VAE',)}, 'hidden': {'prompt': 'PROMPT', 'my_unique_id': 'UNIQUE_ID'}}
    RETURN_TYPES = ('PIPE_LINE', 'MODEL', 'VAE')
    RETURN_NAMES = ('pipe', 'model', 'vae')
    FUNCTION = 'adv_pipeloader'
    CATEGORY = 'EasyUse/Loaders'

    def get_clip_file(self, node_name):
        clip_list = folder_paths.get_filename_list('clip')
        pattern = 'sd2-1-open-clip|model\\.(safetensors|bin)$'
        clip_files = [e for e in clip_list if re.search(pattern, e, re.IGNORECASE)]
        clip_name = clip_files[0] if len(clip_files) > 0 else None
        clip_file = folder_paths.get_full_path('clip', clip_name) if clip_name else None
        if clip_name is not None:
            log_node_info(node_name, f'Using {clip_name}')
        return (clip_file, clip_name)

    def get_clipvision_file(self, node_name):
        clipvision_list = folder_paths.get_filename_list('clip_vision')
        pattern = '(ViT.H.14.*s32B.b79K|ipadapter.*sd15|sd1.?5.*model|open_clip_pytorch_model\\.(bin|safetensors))'
        clipvision_files = [e for e in clipvision_list if re.search(pattern, e, re.IGNORECASE)]
        clipvision_name = clipvision_files[0] if len(clipvision_files) > 0 else None
        clipvision_file = folder_paths.get_full_path('clip_vision', clipvision_name) if clipvision_name else None
        if clipvision_name is not None:
            log_node_info(node_name, f'Using {clipvision_name}')
        return (clipvision_file, clipvision_name)

    def get_vae_file(self, node_name):
        vae_list = folder_paths.get_filename_list('vae')
        pattern = 'vae-ft-mse-840000-ema-pruned\\.(pt|bin|safetensors)$'
        vae_files = [e for e in vae_list if re.search(pattern, e, re.IGNORECASE)]
        vae_name = vae_files[0] if len(vae_files) > 0 else None
        vae_file = folder_paths.get_full_path('vae', vae_name) if vae_name else None
        if vae_name is not None:
            log_node_info(node_name, f'Using {vae_name}')
        return (vae_file, vae_name)

    def adv_pipeloader(self, model_name, clip_skip, init_image, resolution, empty_latent_width, empty_latent_height, positive, negative, use_interpolate, fps, frames, scale_latents, optional_vae=None, prompt=None, my_unique_id=None):
        (positive_embeddings_final, negative_embeddings_final) = (None, None)
        If resolution! = Custom x Custom:
            try:
                (width, height) = map(int, resolution.split(' x '))
                empty_latent_width = width
                empty_latent_height = height
            except ValueError:
                raise ValueError('Invalid base_resolution format.')
        easyCache.update_loaded_objects(prompt)
        models_0 = list(DYNAMICRAFTER_MODELS.keys())[0]
        if optional_vae:
            vae = optional_vae
            vae_name = None
        else:
            (vae_file, vae_name) = self.get_vae_file('easy dynamiCrafterLoader')
            if vae_file is None:
                vae_name = 'vae-ft-mse-840000-ema-pruned.safetensors'
                get_local_filepath(DYNAMICRAFTER_MODELS[models_0]['vae_url'], os.path.join(folder_paths.models_dir, 'vae'), vae_name)
            vae = easyCache.load_vae(vae_name)
        (clip_file, clip_name) = self.get_clip_file('easy dynamiCrafterLoader')
        if clip_file is None:
            clip_name = 'sd2-1-open-clip.safetensors'
            get_local_filepath(DYNAMICRAFTER_MODELS[models_0]['clip_url'], os.path.join(folder_paths.models_dir, 'clip'), clip_name)
        clip = easyCache.load_clip(clip_name)
        (clip_vision_file, clip_vision_name) = self.get_clipvision_file('easy dynamiCrafterLoader')
        if clip_vision_file is None:
            clip_vision_name = 'CLIP-ViT-H-14-laion2B-s32B-b79K.safetensors'
            clip_vision_file = get_local_filepath(DYNAMICRAFTER_MODELS[models_0]['clip_vision_url'], os.path.join(folder_paths.models_dir, 'clip_vision'), clip_vision_name)
        clip_vision = load_clip_vision(clip_vision_file)
        model_path = get_local_filepath(DYNAMICRAFTER_MODELS[model_name]['model_url'], DYNAMICRAFTER_DIR)
        (model_patcher, image_proj_model) = self.load_dynamicrafter(model_path)
        (model, empty_latent, image_latent) = self.process_image_conditioning(model_patcher, clip_vision, vae, image_proj_model, init_image, use_interpolate, fps, frames, scale_latents)
        clipped = clip.clone()
        if clip_skip != 0:
            clipped.clip_layer(clip_skip)
        if positive is not None and positive != '':
            (positive_embeddings_final,) = CLIPTextEncode().encode(clipped, positive)
        if negative is not None and negative != '':
            (negative_embeddings_final,) = CLIPTextEncode().encode(clipped, negative)
        image = easySampler.pil2tensor(Image.new('RGB', (1, 1), (0, 0, 0)))
        pipe = {'model': model, 'positive': positive_embeddings_final, 'negative': negative_embeddings_final, 'vae': vae, 'clip': clip, 'clip_vision': clip_vision, 'samples': empty_latent, 'images': image, 'seed': 0, 'loader_settings': {'ckpt_name': model_name, 'vae_name': vae_name, 'positive': positive, 'positive_l': None, 'positive_g': None, 'positive_balance': None, 'negative': negative, 'negative_l': None, 'negative_g': None, 'negative_balance': None, 'empty_latent_width': empty_latent_width, 'empty_latent_height': empty_latent_height, 'batch_size': 1, 'seed': 0, 'empty_samples': empty_latent}}
        return (pipe, model, vae)
```