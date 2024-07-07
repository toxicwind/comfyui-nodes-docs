# Documentation
- Class name: samplerCascadeFull
- Category: EasyUse/Sampler
- Output node: True
- Repo Ref: https://github.com/yolain/ComfyUI-Easy-Use.git

The samplerCascadeFull node is designed to perform the sampling process in the frame that produces the model. It coordinates the coding, sampling and decoding phases to produce a series of images or potential expressions. This node is essential for generating new image content based on the seeds and models provided, and provides users with seamless interfaces using advanced sampling techniques.

# Input types
## Required
- pipe
    - The `pipe' parameter is a key input that carries the pipe settings and data required for the sampling process. It includes the information necessary for loader settings, model references and other guiding nodes to operate.
    - Comfy dtype: PIPE_LINE
    - Python dtype: Dict[str, Any]
- encode_vae_name
    - The `encode_vae_name' parameter specifies the name of the VAE model that is used to encode the input image to potential space. It is an optional parameter that allows customization of the encoding process.
    - Comfy dtype: STRING
    - Python dtype: Union[str, None]
- decode_vae_name
    - `decode_vae_name' parameters determine the VAE model used to decode potential expressions back to images. It provides users with the flexibility to select decoding models according to their needs.
    - Comfy dtype: STRING
    - Python dtype: Union[str, None]
- steps
    - The'steps' parameter defines the number of sampling steps to be performed during the sampling process. It directly affects the quality and detail of the images generated.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- pipe
    - The 'pipe'output contains the updated piping settings and results of the sampling process. It is a comprehensive output that covers the state after the node is executed.
    - Comfy dtype: PIPE_LINE
    - Python dtype: Dict[str, Any]
- model_b
    - The `model_b' output represents the model used during the decoding phase of the sampling process. It is important for users who need to quote specific models used in their operations.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- latent_b
    - The `latent_b' output provides a potential indication from the sampling process. These potential codes are essential for users wishing to further operate or analyse the content generated.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class samplerCascadeFull:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'pipe': ('PIPE_LINE',), 'encode_vae_name': (['None'] + folder_paths.get_filename_list('vae'),), 'decode_vae_name': (['None'] + folder_paths.get_filename_list('vae'),), 'steps': ('INT', {'default': 20, 'min': 1, 'max': 10000}), 'cfg': ('FLOAT', {'default': 4.0, 'min': 0.0, 'max': 100.0}), 'sampler_name': (comfy.samplers.KSampler.SAMPLERS, {'default': 'euler_ancestral'}), 'scheduler': (comfy.samplers.KSampler.SCHEDULERS, {'default': 'simple'}), 'denoise': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'image_output': (['Hide', 'Preview', 'Save', 'Hide/Save', 'Sender', 'Sender/Save'],), 'link_id': ('INT', {'default': 0, 'min': 0, 'max': sys.maxsize, 'step': 1}), 'save_prefix': ('STRING', {'default': 'ComfyUI'}), 'seed': ('INT', {'default': 0, 'min': 0, 'max': MAX_SEED_NUM})}, 'optional': {'image_to_latent_c': ('IMAGE',), 'latent_c': ('LATENT',), 'model_c': ('MODEL',)}, 'hidden': {'tile_size': 'INT', 'prompt': 'PROMPT', 'extra_pnginfo': 'EXTRA_PNGINFO', 'my_unique_id': 'UNIQUE_ID', 'embeddingsList': (folder_paths.get_filename_list('embeddings'),)}}
    RETURN_TYPES = ('PIPE_LINE', 'MODEL', 'LATENT')
    RETURN_NAMES = ('pipe', 'model_b', 'latent_b')
    OUTPUT_NODE = True
    FUNCTION = 'run'
    CATEGORY = 'EasyUse/Sampler'

    def run(self, pipe, encode_vae_name, decode_vae_name, steps, cfg, sampler_name, scheduler, denoise, image_output, link_id, save_prefix, seed, image_to_latent_c=None, latent_c=None, model_c=None, tile_size=None, prompt=None, extra_pnginfo=None, my_unique_id=None, force_full_denoise=False, disable_noise=False):
        encode_vae_name = encode_vae_name if encode_vae_name is not None else pipe['loader_settings']['encode_vae_name']
        decode_vae_name = decode_vae_name if decode_vae_name is not None else pipe['loader_settings']['decode_vae_name']
        batch_size = pipe['loader_settings']['batch_size'] if 'batch_size' in pipe['loader_settings'] else 1
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
            latent_c = encode_vae.encode(s[:, :, :, :3])
            latent_b = torch.zeros([latent_c.shape[0], 4, height // 4, width // 4])
            samples_c = {'samples': latent_c}
            samples_c = RepeatLatentBatch().repeat(samples_c, batch_size)[0]
            samples_b = {'samples': latent_b}
            samples_b = RepeatLatentBatch().repeat(samples_b, batch_size)[0]
            images = image_to_latent_c
        elif latent_c is not None:
            samples_c = latent_c
            samples_b = pipe['samples'][1]
            images = pipe['images']
        else:
            samples_c = pipe['samples'][0]
            samples_b = pipe['samples'][1]
            images = pipe['images']
        easyCache.update_loaded_objects(prompt)
        samp_model = model_c if model_c else pipe['model'][0]
        samp_positive = pipe['positive']
        samp_negative = pipe['negative']
        samp_samples = samples_c
        samp_seed = seed if seed is not None else pipe['seed']
        steps = steps if steps is not None else pipe['loader_settings']['steps']
        start_step = pipe['loader_settings']['start_step'] if 'start_step' in pipe['loader_settings'] else 0
        last_step = pipe['loader_settings']['last_step'] if 'last_step' in pipe['loader_settings'] else 10000
        cfg = cfg if cfg is not None else pipe['loader_settings']['cfg']
        sampler_name = sampler_name if sampler_name is not None else pipe['loader_settings']['sampler_name']
        scheduler = scheduler if scheduler is not None else pipe['loader_settings']['scheduler']
        denoise = denoise if denoise is not None else pipe['loader_settings']['denoise']
        start_time = int(time.time() * 1000)
        samp_samples = sampler.common_ksampler(samp_model, samp_seed, steps, cfg, sampler_name, scheduler, samp_positive, samp_negative, samp_samples, denoise=denoise, preview_latent=False, start_step=start_step, last_step=last_step, force_full_denoise=False, disable_noise=False)
        end_time = int(time.time() * 1000)
        stage_c = samp_samples['samples']
        results = None
        if image_output not in ['Hide', 'Hide/Save']:
            if decode_vae_name != 'None':
                decode_vae = easyCache.load_vae(decode_vae_name)
            else:
                decode_vae = pipe['vae'][0]
            samp_images = decode_vae.decode(stage_c).cpu()
            results = easySave(samp_images, save_prefix, image_output, prompt, extra_pnginfo)
            sampler.update_value_by_id('results', my_unique_id, results)
        end_decode_time = int(time.time() * 1000)
        Spent_time = 'proliferation:'+str (end_time - start_time) / 1000 seconds, decoding:'+str (end_decode_time - end_time) / 1000) +'s
        easyCache.update_loaded_objects(prompt)
        c1 = []
        for t in samp_positive:
            d = t[1].copy()
            if 'pooled_output' in d:
                d['pooled_output'] = torch.zeros_like(d['pooled_output'])
            n = [torch.zeros_like(t[0]), d]
            c1.append(n)
        c2 = []
        for t in c1:
            d = t[1].copy()
            d['stable_cascade_prior'] = stage_c
            n = [t[0], d]
            c2.append(n)
        new_pipe = {'model': pipe['model'][1], 'positive': c2, 'negative': c1, 'vae': pipe['vae'][1], 'clip': pipe['clip'], 'samples': samples_b, 'images': images, 'seed': seed, 'loader_settings': {**pipe['loader_settings'], 'spent_time': spent_time}}
        sampler.update_value_by_id('pipe_line', my_unique_id, new_pipe)
        del pipe
        if image_output in ('Hide', 'Hide/Save'):
            return {'ui': {}, 'result': sampler.get_output(new_pipe)}
        if image_output in ('Sender', 'Sender/Save') and results is not None:
            PromptServer.instance.send_sync('img-send', {'link_id': link_id, 'images': results})
        return {'ui': {'images': results}, 'result': (new_pipe, new_pipe['model'], new_pipe['samples'])}
```