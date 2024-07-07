# Documentation
- Class name: samplerSDTurbo
- Category: EasyUse/Sampler
- Output node: True
- Repo Ref: https://github.com/yolain/ComfyUI-Easy-Use.git

The samplerSDTurbo node is designed to produce high-quality images efficiently through advanced sampling techniques. It operates through a series of conversions of input data to optimize both speed and visual authenticity. This node is particularly suitable for applications that require the creation of images from complex data concentrations, providing a balance between performance and output quality.

# Input types
## Required
- pipe
    - The `pipe' parameter is the main input that provides the necessary data and settings for the sampling process. It includes model information, positive and negative examples, and other relevant configurations that guide nodes to generate the output required.
    - Comfy dtype: PIPE_LINE
    - Python dtype: Dict[str, Any]
- image_output
    - The `image_output' parameter determines how to handle the image generated. Options include hiding, previewing, saving or a combination of them, allowing flexibility in the way results are displayed or stored.
    - Comfy dtype: COMBO
    - Python dtype: str
- link_id
    - The `link_id' parameter is essential to link the image generated to the corresponding request or process. It ensures that the correct image is associated with the right task, simplifies the workflow and reduces the likelihood of error.
    - Comfy dtype: INT
    - Python dtype: int
- save_prefix
    - The'save_prefix' parameter sets the prefix for saving the image file, which is essential for organizing and identifying the output. This prefix serves as the only identifier for the image and helps them retrieve and manage it.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- model
    - The `model' parameter allows the specification of a specific model to be used in the sampling process. It provides a means of adjusting nodes to specific requirements or preferences, which enhances the multifunctionality and adaptability of nodes.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- tile_size
    - The `tile_size' parameter influences the levelling policy of the image decoding process, influencing the resolution and layout of the image generation. This is an optional setup that can be adjusted to the desired output characteristics.
    - Comfy dtype: INT
    - Python dtype: Optional[int]
- prompt
    - The `prompt' parameter provides a text description that guides the image generation process. It is a key element in controlling the creative direction and ensuring that the output is consistent with the intended theme or concept.
    - Comfy dtype: PROMPT
    - Python dtype: str
- extra_pnginfo
    - The `extra_pnginfo' parameter contains additional information related to the PNG image that can be used to refine image processing and enhance the final result.
    - Comfy dtype: EXTRA_PNGINFO
    - Python dtype: Dict[str, Any]
- my_unique_id
    - The `my_unique_id' parameter is an identifier for tracking unique requests or processes associated with image generation. It plays an important role in managing and linking outputs to their respective tasks or workflows.
    - Comfy dtype: UNIQUE_ID
    - Python dtype: Union[str, int]

# Output types
- pipe
    - ‘pipe’ output is an integrated structure that contains the results of the sampling process, including the images generated and the relevant metadata. It serves as a conduit for the transmission of data between the different components of the system and promotes further processing or analysis.
    - Comfy dtype: PIPE_LINE
    - Python dtype: Dict[str, Any]
- image
    - The 'image'output contains the images generated, which are the main result of the sampling process. These images are ready for use and represent the top of the node function and the validity of the sampling techniques applied.
    - Comfy dtype: IMAGE
    - Python dtype: List[PIL.Image.Image]

# Usage tips
- Infra type: GPU

# Source code
```
class samplerSDTurbo:

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

    def run(self, pipe, image_output, link_id, save_prefix, model=None, tile_size=None, prompt=None, extra_pnginfo=None, my_unique_id=None):
        easyCache.update_loaded_objects(prompt)
        my_unique_id = int(my_unique_id)
        samp_model = pipe['model'] if model is None else model
        samp_positive = pipe['positive']
        samp_negative = pipe['negative']
        samp_samples = pipe['samples']
        samp_vae = pipe['vae']
        samp_clip = pipe['clip']
        samp_seed = pipe['seed']
        samp_sampler = pipe['loader_settings']['sampler']
        sigmas = pipe['loader_settings']['sigmas']
        cfg = pipe['loader_settings']['cfg']
        steps = pipe['loader_settings']['steps']
        disable_noise = False
        preview_latent = True
        if image_output in ('Hide', 'Hide/Save'):
            preview_latent = False
        start_time = int(time.time() * 1000)
        samp_samples = sampler.custom_ksampler(samp_model, samp_seed, steps, cfg, samp_sampler, sigmas, samp_positive, samp_negative, samp_samples, disable_noise, preview_latent)
        end_time = int(time.time() * 1000)
        latent = samp_samples['samples']
        if tile_size is not None:
            samp_images = samp_vae.decode_tiled(latent, tile_x=tile_size // 8, tile_y=tile_size // 8)
        else:
            samp_images = samp_vae.decode(latent).cpu()
        end_decode_time = int(time.time() * 1000)
        Spent_time = 'proliferation:'+str (end_time - start_time) / 1000 seconds, decoding:'+str (end_decode_time - end_time) / 1000) +'s
        easyCache.update_loaded_objects(prompt)
        results = easySave(samp_images, save_prefix, image_output, prompt, extra_pnginfo)
        sampler.update_value_by_id('results', my_unique_id, results)
        new_pipe = {'model': samp_model, 'positive': samp_positive, 'negative': samp_negative, 'vae': samp_vae, 'clip': samp_clip, 'samples': samp_samples, 'images': samp_images, 'seed': samp_seed, 'loader_settings': {**pipe['loader_settings'], 'spent_time': spent_time}}
        sampler.update_value_by_id('pipe_line', my_unique_id, new_pipe)
        del pipe
        if image_output in ('Hide', 'Hide/Save'):
            return {'ui': {}, 'result': sampler.get_output(new_pipe)}
        if image_output in ('Sender', 'Sender/Save'):
            PromptServer.instance.send_sync('img-send', {'link_id': link_id, 'images': results})
        return {'ui': {'images': results}, 'result': sampler.get_output(new_pipe)}
```