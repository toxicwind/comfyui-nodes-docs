# Documentation
- Class name: cascadeSettings
- Category: EasyUse/PreSampling
- Output node: True
- Repo Ref: https://github.com/yolain/ComfyUI-Easy-Use.git

The cascadeSettings node is designed to simplify the configuration process for the configuration and management of model flow lines. It covers the parameters necessary for model coding and decoding, as well as sampling strategies to create high-quality visual output. The node emphasizes usability and efficiency, allowing users to focus on the creative aspects of the project without being disturbed by complex technical details.

# Input types
## Required
- pipe
    - The `pipe' parameter is essential because it carries the full context, including model settings and data samples, for the generation of the model flow line. It is essential for the proper operation of the cascadeSettings nodes and for the integrity of the generation process.
    - Comfy dtype: PIPE_LINE
    - Python dtype: Dict
- encode_vae_name
    - The `encode_vae_name' parameter specifies the name of the VAE model used in the process of generation. It is important for setting the basis for potential spatial expressions and directly affects the quality of the images generated.
    - Comfy dtype: COMBO
    - Python dtype: Union[str, None]
- decode_vae_name
    - The `decode_vae_name' parameter determines the decoder VAE model used to reconstruct images from potential space. It selects the authenticity and visual consistency that influences the final output.
    - Comfy dtype: COMBO
    - Python dtype: Union[str, None]
- steps
    - The'steps' parameter defines the number of turns or steps during the sampling process. It is a key factor in controlling the level of detail and refinement of the image generated.
    - Comfy dtype: INT
    - Python dtype: int
- cfg
    - The `cfg' parameter adjusts the configuration of the generation model to affect the overall behaviour and performance of the flow line. This is a key setup that can significantly change the end result.
    - Comfy dtype: FLOAT
    - Python dtype: float
- sampler_name
    - The'sampler_name' parameter selects the sampling method used to generate the image. It is critical in determining the diversity and uniqueness of visual output.
    - Comfy dtype: COMBO
    - Python dtype: str
- scheduler
    - The `scheduler' parameter management sampling plan is essential for balancing quality and calculating efficiency. It plays an important role in optimizing generation.
    - Comfy dtype: COMBO
    - Python dtype: str
- denoise
    - The `denoise' parameter controls the level of noise reduction applied during image generation. It affects the clarity and smoothness of the final image.
    - Comfy dtype: FLOAT
    - Python dtype: float
- seed
    - The `seed' parameter ensures the replicability of the generation process by setting fixed random seeds. It is important for achieving consistent results in different operations.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- image_to_latent_c
    - The `image_to_latet_c' parameter allows the input of an image that will be encoded to potential space. This allows the user to specify a starting point for the generation process that affects the direction and style of the output.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image
- latent_c
    - The `latent_c' parameter provides direct input of potential vectors, providing users with the ability to control the generation process with greater precision. This can lead to more detailed and targeted visual output.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
- prompt
    - The `prompt' parameter introduces text guidance into the generation process, allowing users to direct the content and themes that generate images. It is an important tool for achieving specific creative visions.
    - Comfy dtype: PROMPT
    - Python dtype: str
- extra_pnginfo
    - The `extra_pnginfo' parameter contains additional information relevant to the input image that can be used to refine the generation process and increase the relevance of the output to the expected context.
    - Comfy dtype: EXTRA_PNGINFO
    - Python dtype: Dict[str, Any]
- my_unique_id
    - The `my_unique_id' parameter is the only identifier for tracking and managing each example of the generation process. It is essential for maintaining the integrity and organization of multiple parallel or sequential operations.
    - Comfy dtype: UNIQUE_ID
    - Python dtype: Any

# Output types
- pipe_line
    - The 'pipe_line' output is an updated version of the input 'pipe' that has been applied to all settings. It serves as the basis for generating the follow-up phase of the current line, ensuring that the parameters of the configuration are correctly disseminated and used during the image generation process.
    - Comfy dtype: PIPE_LINE
    - Python dtype: Dict

# Usage tips
- Infra type: CPU

# Source code
```
class cascadeSettings:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'pipe': ('PIPE_LINE',), 'encode_vae_name': (['None'] + folder_paths.get_filename_list('vae'),), 'decode_vae_name': (['None'] + folder_paths.get_filename_list('vae'),), 'steps': ('INT', {'default': 20, 'min': 1, 'max': 10000}), 'cfg': ('FLOAT', {'default': 4.0, 'min': 0.0, 'max': 100.0}), 'sampler_name': (comfy.samplers.KSampler.SAMPLERS, {'default': 'euler_ancestral'}), 'scheduler': (comfy.samplers.KSampler.SCHEDULERS, {'default': 'simple'}), 'denoise': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'seed': ('INT', {'default': 0, 'min': 0, 'max': MAX_SEED_NUM})}, 'optional': {'image_to_latent_c': ('IMAGE',), 'latent_c': ('LATENT',)}, 'hidden': {'prompt': 'PROMPT', 'extra_pnginfo': 'EXTRA_PNGINFO', 'my_unique_id': 'UNIQUE_ID'}}
    RETURN_TYPES = ('PIPE_LINE',)
    RETURN_NAMES = ('pipe',)
    OUTPUT_NODE = True
    FUNCTION = 'settings'
    CATEGORY = 'EasyUse/PreSampling'

    def settings(self, pipe, encode_vae_name, decode_vae_name, steps, cfg, sampler_name, scheduler, denoise, seed, model=None, image_to_latent_c=None, latent_c=None, prompt=None, extra_pnginfo=None, my_unique_id=None):
        (images, samples_c) = (None, None)
        samples = pipe['samples']
        batch_size = pipe['loader_settings']['batch_size'] if 'batch_size' in pipe['loader_settings'] else 1
        encode_vae_name = encode_vae_name if encode_vae_name is not None else pipe['loader_settings']['encode_vae_name']
        decode_vae_name = decode_vae_name if decode_vae_name is not None else pipe['loader_settings']['decode_vae_name']
        if image_to_latent_c is not None:
            if encode_vae_name != 'None':
                encode_vae = easyCache.load_vae(encode_vae_name)
            else:
                encode_vae = pipe['vae'][0]
            if 'compression' not in pipe['loader_settings']:
                raise Exception('compression is not found')
            compression = pipe['loader_settings']['compression']
            width = image_to_latent_c.shape[-2]
            height = image_to_latent_c.shape[-3]
            out_width = width // compression * encode_vae.downscale_ratio
            out_height = height // compression * encode_vae.downscale_ratio
            s = comfy.utils.common_upscale(image_to_latent_c.movedim(-1, 1), out_width, out_height, 'bicubic', 'center').movedim(1, -1)
            c_latent = encode_vae.encode(s[:, :, :, :3])
            b_latent = torch.zeros([c_latent.shape[0], 4, height // 4, width // 4])
            samples_c = {'samples': c_latent}
            samples_c = RepeatLatentBatch().repeat(samples_c, batch_size)[0]
            samples_b = {'samples': b_latent}
            samples_b = RepeatLatentBatch().repeat(samples_b, batch_size)[0]
            samples = (samples_c, samples_b)
            images = image_to_latent_c
        elif latent_c is not None:
            samples_c = latent_c
            samples = (samples_c, samples[1])
            images = pipe['images']
        if samples_c is not None:
            samples = (samples_c, samples[1])
        new_pipe = {'model': pipe['model'], 'positive': pipe['positive'], 'negative': pipe['negative'], 'vae': pipe['vae'], 'clip': pipe['clip'], 'samples': samples, 'images': images, 'seed': seed, 'loader_settings': {**pipe['loader_settings'], 'encode_vae_name': encode_vae_name, 'decode_vae_name': decode_vae_name, 'steps': steps, 'cfg': cfg, 'sampler_name': sampler_name, 'scheduler': scheduler, 'denoise': denoise, 'add_noise': 'enabled'}}
        sampler.update_value_by_id('pipe_line', my_unique_id, new_pipe)
        del pipe
        return {'ui': {'value': [seed]}, 'result': (new_pipe,)}
```