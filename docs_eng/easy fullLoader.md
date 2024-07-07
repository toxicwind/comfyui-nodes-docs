# Documentation
- Class name: fullLoader
- Category: EasyUse/Loaders
- Output node: False
- Repo Ref: https://github.com/yolain/ComfyUI-Easy-Use.git

Full Loader class covers the various models and components needed to load and prepare the pipe. It streamlines the integration check point, VAE, CLIP, and condition data, providing a coherent interface for the initialization and configuration of the model.

# Input types
## Required
- ckpt_name
    - The name of the check point is essential to identify the specific models to be loaded and used in the pipeline. It guides the loader to find the correct preservation status of the model, which is essential for consistency and accuracy in the next step of processing.
    - Comfy dtype: FILE
    - Python dtype: List[str]
- config_name
    - The configuration name plays a key role in determining the model's settings and hyper-parameters. It ensures that the model operates within the desired parameters, affecting overall performance and output quality.
    - Comfy dtype: ENUM
    - Python dtype: Enum
- vae_name
    - The VAE name is essential for selecting an appropriate variable-based encoder model. It affects the capacity of the pipeline to generate and the quality of the potential spatial expression.
    - Comfy dtype: FILE
    - Python dtype: List[str]
- clip_skip
    - The clip_skip parameter is important for controlling the level of application of the CLIP model in the pipe. It affects the particle size of the text condition and the responsiveness of the model to the texttip.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- pipe
    - The pipe output represents the results of the full Loader work and provides an integrated conduit setting containing model, VAE, CLIP and condition data. It is the backbone of the generation process and ensures seamless integration of all components.
    - Comfy dtype: PIPE_LINE
    - Python dtype: Dict

# Usage tips
- Infra type: CPU

# Source code
```
class fullLoader:

    @classmethod
    def INPUT_TYPES(cls):
        resolution_strings = [f'{width} x {height}' for (width, height) in BASE_RESOLUTIONS]
        a1111_prompt_style_default = False
        return {'required': {'ckpt_name': (folder_paths.get_filename_list('checkpoints'),), 'config_name': (['Default'] + folder_paths.get_filename_list('configs'), {'default': 'Default'}), 'vae_name': (['Baked VAE'] + folder_paths.get_filename_list('vae'),), 'clip_skip': ('INT', {'default': -1, 'min': -24, 'max': 0, 'step': 1}), 'lora_name': (['None'] + folder_paths.get_filename_list('loras'),), 'lora_model_strength': ('FLOAT', {'default': 1.0, 'min': -10.0, 'max': 10.0, 'step': 0.01}), 'lora_clip_strength': ('FLOAT', {'default': 1.0, 'min': -10.0, 'max': 10.0, 'step': 0.01}), 'resolution': (resolution_strings,), 'empty_latent_width': ('INT', {'default': 512, 'min': 64, 'max': MAX_RESOLUTION, 'step': 8}), 'empty_latent_height': ('INT', {'default': 512, 'min': 64, 'max': MAX_RESOLUTION, 'step': 8}), 'positive': ('STRING', {'default': 'Positive', 'multiline': True}), 'positive_token_normalization': (['none', 'mean', 'length', 'length+mean'],), 'positive_weight_interpretation': (['comfy', 'A1111', 'comfy++', 'compel', 'fixed attention'],), 'negative': ('STRING', {'default': 'Negative', 'multiline': True}), 'negative_token_normalization': (['none', 'mean', 'length', 'length+mean'],), 'negative_weight_interpretation': (['comfy', 'A1111', 'comfy++', 'compel', 'fixed attention'],), 'batch_size': ('INT', {'default': 1, 'min': 1, 'max': 64})}, 'optional': {'model_override': ('MODEL',), 'clip_override': ('CLIP',), 'vae_override': ('VAE',), 'optional_lora_stack': ('LORA_STACK',), 'a1111_prompt_style': ('BOOLEAN', {'default': a1111_prompt_style_default})}, 'hidden': {'prompt': 'PROMPT', 'my_unique_id': 'UNIQUE_ID'}}
    RETURN_TYPES = ('PIPE_LINE', 'MODEL', 'VAE', 'CLIP', 'CONDITIONING', 'CONDITIONING', 'LATENT')
    RETURN_NAMES = ('pipe', 'model', 'vae', 'clip', 'positive', 'negative', 'latent')
    FUNCTION = 'adv_pipeloader'
    CATEGORY = 'EasyUse/Loaders'

    def adv_pipeloader(self, ckpt_name, config_name, vae_name, clip_skip, lora_name, lora_model_strength, lora_clip_strength, resolution, empty_latent_width, empty_latent_height, positive, positive_token_normalization, positive_weight_interpretation, negative, negative_token_normalization, negative_weight_interpretation, batch_size, model_override=None, clip_override=None, vae_override=None, optional_lora_stack=None, a1111_prompt_style=False, prompt=None, my_unique_id=None):
        model: ModelPatcher | None = None
        clip: CLIP | None = None
        vae: VAE | None = None
        can_load_lora = True
        pipe_lora_stack = []
        If resolution! = Custom x Custom:
            try:
                (width, height) = map(int, resolution.split(' x '))
                empty_latent_width = width
                empty_latent_height = height
            except ValueError:
                raise ValueError('Invalid base_resolution format.')
        latent = torch.zeros([batch_size, 4, empty_latent_height // 8, empty_latent_width // 8]).cpu()
        samples = {'samples': latent}
        easyCache.update_loaded_objects(prompt)
        log_node_warn
        xy_model_id = next((x for x in prompt if str(prompt[x]['class_type']) in ['easy XYInputs: ModelMergeBlocks', 'easy XYInputs: Checkpoint']), None)
        xy_lora_id = next((x for x in prompt if str(prompt[x]['class_type']) == 'easy XYInputs: Lora'), None)
        if xy_lora_id is not None:
            can_load_lora = False
        if xy_model_id is not None:
            node = prompt[xy_model_id]
            if 'ckpt_name_1' in node['inputs']:
                ckpt_name_1 = node['inputs']['ckpt_name_1']
                (model, clip, vae, clip_vision) = easyCache.load_checkpoint(ckpt_name_1)
                can_load_lora = False
        elif model_override is not None and clip_override is not None and (vae_override is not None):
            model = model_override
            clip = clip_override
            vae = vae_override
        elif model_override is not None:
            raise Exception(f'[ERROR] clip or vae is missing')
        elif vae_override is not None:
            raise Exception(f'[ERROR] model or clip is missing')
        elif clip_override is not None:
            raise Exception(f'[ERROR] model or vae is missing')
        else:
            (model, clip, vae, clip_vision) = easyCache.load_checkpoint(ckpt_name, config_name)
        if optional_lora_stack is not None and can_load_lora:
            for lora in optional_lora_stack:
                lora = {'lora_name': lora[0], 'model': model, 'clip': clip, 'model_strength': lora[1], 'clip_strength': lora[2]}
                (model, clip) = easyCache.load_lora(lora)
                lora['model'] = model
                lora['clip'] = clip
                pipe_lora_stack.append(lora)
        if lora_name != 'None' and can_load_lora:
            lora = {'lora_name': lora_name, 'model': model, 'clip': clip, 'model_strength': lora_model_strength, 'clip_strength': lora_clip_strength}
            (model, clip) = easyCache.load_lora(lora)
            pipe_lora_stack.append(lora)
        if vae_name not in ['Baked VAE', 'Baked-VAE']:
            vae = easyCache.load_vae(vae_name)
        if not clip:
            raise Exception('No CLIP found')
        (positive_embeddings_final, positive_wildcard_prompt, model, clip) = prompt_to_cond('positive', model, clip, clip_skip, pipe_lora_stack, positive, positive_token_normalization, positive_weight_interpretation, a1111_prompt_style, my_unique_id, prompt, easyCache)
        (negative_embeddings_final, negative_wildcard_prompt, model, clip) = prompt_to_cond('negative', model, clip, clip_skip, pipe_lora_stack, negative, negative_token_normalization, negative_weight_interpretation, a1111_prompt_style, my_unique_id, prompt, easyCache)
        image = easySampler.pil2tensor(Image.new('RGB', (1, 1), (0, 0, 0)))
        Blog_node_warn
        pipe = {'model': model, 'positive': positive_embeddings_final, 'negative': negative_embeddings_final, 'vae': vae, 'clip': clip, 'samples': samples, 'images': image, 'seed': 0, 'loader_settings': {'ckpt_name': ckpt_name, 'vae_name': vae_name, 'lora_name': lora_name, 'lora_model_strength': lora_model_strength, 'lora_clip_strength': lora_clip_strength, 'lora_stack': pipe_lora_stack, 'refiner_ckpt_name': None, 'refiner_vae_name': None, 'refiner_lora_name': None, 'refiner_lora_model_strength': None, 'refiner_lora_clip_strength': None, 'clip_skip': clip_skip, 'a1111_prompt_style': a1111_prompt_style, 'positive': positive, 'positive_l': None, 'positive_g': None, 'positive_token_normalization': positive_token_normalization, 'positive_weight_interpretation': positive_weight_interpretation, 'positive_balance': None, 'negative': negative, 'negative_l': None, 'negative_g': None, 'negative_token_normalization': negative_token_normalization, 'negative_weight_interpretation': negative_weight_interpretation, 'negative_balance': None, 'empty_latent_width': empty_latent_width, 'empty_latent_height': empty_latent_height, 'batch_size': batch_size, 'seed': 0, 'empty_samples': samples}}
        return {'ui': {'positive': positive_wildcard_prompt, 'negative': negative_wildcard_prompt}, 'result': (pipe, model, vae, clip, positive_embeddings_final, negative_embeddings_final, samples)}
```