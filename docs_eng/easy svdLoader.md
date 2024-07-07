# Documentation
- Class name: svdLoader
- Category: EasyUse/Loaders
- Output node: False
- Repo Ref: https://github.com/yolain/ComfyUI-Easy-Use.git

The svdLoader node, as a key component of the loading and processing model checkpoint, VAE and CLIP models, facilitates the initialization and setting up of complex generation pipelines. It streamlines the integration of models into workflows and ensures efficient and seamless data processing and conversion.

# Input types
## Required
- ckpt_name
    - The check point name parameter is essential to specify the model check point to be loaded, which forms the basis of the production process. It determines the quality and properties of the output generated.
    - Comfy dtype: COMBO
    - Python dtype: str
- vae_name
    - The VAE name parameter, which is essential for the selection of an appropriate variable-based encoder, plays an important role in the creation of a model for peacekeeping potential spatial formation.
    - Comfy dtype: COMBO
    - Python dtype: str
- clip_name
    - The CLIP name parameter is essential for the selection of the correct CLIP model and is responsible for providing text-conditional capability for the generation process.
    - Comfy dtype: COMBO
    - Python dtype: str
- init_image
    - The init_image parameter is essential because it provides the initial visual input that informs the generation of the model and significantly influences the direction and quality of the content generated.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image
- resolution
    - Resolution parameters are essential in determining the size and proportion of the image generated, directly impacting the details and clarity level of the output.
    - Comfy dtype: COMBO
    - Python dtype: str
- empty_latent_width
    - The empty_latent_width parameter is important for defining the width of potential space, which affects the diversity and variability in the generation of images.
    - Comfy dtype: INT
    - Python dtype: int
- empty_latent_height
    - The empty_latent_height parameter is important for setting the altitude of potential space, which affects the structural consistency and configuration of the image generation.
    - Comfy dtype: INT
    - Python dtype: int
- video_frames
    - The video_frames parameter is essential for defining the number of frames in the video, and it directly affects the time and sequence in which the video content is generated.
    - Comfy dtype: INT
    - Python dtype: int
- motion_bucket_id
    - The movement_bucket_id parameter is essential to control the movement and dynamics in the generation of video frames, which influences the fluidity and nature of the movement.
    - Comfy dtype: INT
    - Python dtype: int
- fps
    - The fps parameter is critical in determining the frame rate for generating the video, and it directly affects the flow and speed of the video content.
    - Comfy dtype: INT
    - Python dtype: int
- augmentation_level
    - Reference_level parameters are important for introducing random changes in the image generation process, which enhances the diversity and probity of output generation.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- pipe
    - Pipe output is an integrated structure that contains all the necessary components for the generation of pipelines, including models, VAE and CLIP, which are essential for subsequent processing and generation tasks.
    - Comfy dtype: PIPE_LINE
    - Python dtype: dict
- model
    - Model output represents the production model loaded, which creates the core component of the final output based on input data and definition parameters.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- vae
    - The vae output is a variable-based encoder model that plays an important role in generating and operating potential space and is essential for generating diversity and quality of content.
    - Comfy dtype: VAE
    - Python dtype: torch.nn.Module

# Usage tips
- Infra type: CPU

# Source code
```
class svdLoader:

    @classmethod
    def INPUT_TYPES(cls):
        resolution_strings = [f'{width} x {height}' for (width, height) in BASE_RESOLUTIONS]

        def get_file_list(filenames):
            return [file for file in filenames if file != 'put_models_here.txt' and 'svd' in file.lower()]
        return {'required': {'ckpt_name': (list(['svd.safetensors', 'svd_xt.safetensors', 'svd_image_decoder.safetensors', 'svd_xt_image_decoder.safetensors', 'svd-fp16.safetensors', 'svd_xt-fp16.safetensors', 'svd_image_decoder-fp16.safetensors', 'svd_xt_image_decoder-fp16.safetensors', 'svd_xt_1_1.safetensors']),), 'vae_name': (['Baked VAE'] + folder_paths.get_filename_list('vae'),), 'clip_name': (['None'] + folder_paths.get_filename_list('clip'),), 'init_image': ('IMAGE',), 'resolution': (resolution_strings, {'default': '1024 x 576'}), 'empty_latent_width': ('INT', {'default': 256, 'min': 16, 'max': MAX_RESOLUTION, 'step': 8}), 'empty_latent_height': ('INT', {'default': 256, 'min': 16, 'max': MAX_RESOLUTION, 'step': 8}), 'video_frames': ('INT', {'default': 14, 'min': 1, 'max': 4096}), 'motion_bucket_id': ('INT', {'default': 127, 'min': 1, 'max': 1023}), 'fps': ('INT', {'default': 6, 'min': 1, 'max': 1024}), 'augmentation_level': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 10.0, 'step': 0.01})}, 'optional': {'optional_positive': ('STRING', {'default': '', 'multiline': True}), 'optional_negative': ('STRING', {'default': '', 'multiline': True})}, 'hidden': {'prompt': 'PROMPT', 'my_unique_id': 'UNIQUE_ID'}}
    RETURN_TYPES = ('PIPE_LINE', 'MODEL', 'VAE')
    RETURN_NAMES = ('pipe', 'model', 'vae')
    FUNCTION = 'adv_pipeloader'
    CATEGORY = 'EasyUse/Loaders'

    def adv_pipeloader(self, ckpt_name, vae_name, clip_name, init_image, resolution, empty_latent_width, empty_latent_height, video_frames, motion_bucket_id, fps, augmentation_level, optional_positive=None, optional_negative=None, prompt=None, my_unique_id=None):
        model: ModelPatcher | None = None
        vae: VAE | None = None
        clip: CLIP | None = None
        clip_vision = None
        If resolution! = Custom x Custom:
            try:
                (width, height) = map(int, resolution.split(' x '))
                empty_latent_width = width
                empty_latent_height = height
            except ValueError:
                raise ValueError('Invalid base_resolution format.')
        easyCache.update_loaded_objects(prompt)
        (model, clip, vae, clip_vision) = easyCache.load_checkpoint(ckpt_name, 'Default', True)
        output = clip_vision.encode_image(init_image)
        pooled = output.image_embeds.unsqueeze(0)
        pixels = comfy.utils.common_upscale(init_image.movedim(-1, 1), empty_latent_width, empty_latent_height, 'bilinear', 'center').movedim(1, -1)
        encode_pixels = pixels[:, :, :, :3]
        if augmentation_level > 0:
            encode_pixels += torch.randn_like(pixels) * augmentation_level
        t = vae.encode(encode_pixels)
        positive = [[pooled, {'motion_bucket_id': motion_bucket_id, 'fps': fps, 'augmentation_level': augmentation_level, 'concat_latent_image': t}]]
        negative = [[torch.zeros_like(pooled), {'motion_bucket_id': motion_bucket_id, 'fps': fps, 'augmentation_level': augmentation_level, 'concat_latent_image': torch.zeros_like(t)}]]
        if optional_positive is not None and optional_positive != '':
            if clip_name == 'None':
                raise Exception('You need choose a open_clip model when positive is not empty')
            clip = easyCache.load_clip(clip_name)
            (positive_embeddings_final,) = CLIPTextEncode().encode(clip, optional_positive)
            (positive,) = ConditioningConcat().concat(positive, positive_embeddings_final)
        if optional_negative is not None and optional_negative != '':
            if clip_name == 'None':
                raise Exception('You need choose a open_clip model when negative is not empty')
            (negative_embeddings_final,) = CLIPTextEncode().encode(clip, optional_negative)
            (negative,) = ConditioningConcat().concat(negative, negative_embeddings_final)
        latent = torch.zeros([video_frames, 4, empty_latent_height // 8, empty_latent_width // 8])
        samples = {'samples': latent}
        image = easySampler.pil2tensor(Image.new('RGB', (1, 1), (0, 0, 0)))
        pipe = {'model': model, 'positive': positive, 'negative': negative, 'vae': vae, 'clip': clip, 'samples': samples, 'images': image, 'seed': 0, 'loader_settings': {'ckpt_name': ckpt_name, 'vae_name': vae_name, 'positive': positive, 'positive_l': None, 'positive_g': None, 'positive_balance': None, 'negative': negative, 'negative_l': None, 'negative_g': None, 'negative_balance': None, 'empty_latent_width': empty_latent_width, 'empty_latent_height': empty_latent_height, 'batch_size': 1, 'seed': 0, 'empty_samples': samples}}
        return (pipe, model, vae)
```