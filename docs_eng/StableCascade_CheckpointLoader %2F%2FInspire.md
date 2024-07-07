# Documentation
- Class name: StableCascade_CheckpointLoader
- Category: InspirePack/Backend
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Inspire-Pack.git

The node is designed to efficiently load and manage check points from designated directories, classify them to different stages, and facilitate the retrieval of models and related data. It enhances workflows by providing a cache function, which can significantly increase the speed of duplicate tasks by reloading previously loaded check points.

# Input types
## Required
- stage_b
    - The stage_b parameter specifies the name of the checkpoint file for the second phase of the cascade. It is essential for the node to identify the correct check point for loading and cache, which has a direct impact on subsequent processing and results.
    - Comfy dtype: STRING
    - Python dtype: str
- stage_c
    - The stage_c parameter represents the checkpoint document for the third stage of the cascade. It is essential for the node to properly load advanced models and related data, affecting the effectiveness of final output and model utilization.
    - Comfy dtype: STRING
    - Python dtype: str
- cache_mode
    - The cache_mode parameter controls the cache behaviour of nodes. It determines whether to load the checkpoints directly or directly from the file system and whether to store the loaded check points for future use. This parameter significantly affects the performance and efficiency of the nodes.
    - Comfy dtype: COMBO
    - Python dtype: str
## Optional
- key_opt_b
    - The key_opt_b parameter is an optional identifier for the checkpoint. It allows custom naming, which is very useful for the reference of a particular check point in the cache. If this value is provided, it will be used as a key in the cache, otherwise'stage_b' will be used.
    - Comfy dtype: STRING
    - Python dtype: str
- key_opt_c
    - The key_opt_c parameter is the backup key for the stop_c checkpoint. It allows the user to mark the checkpoint with the only name in order to better manage the cache and references. If you leave empty, use'stop_c' as the default key.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- b_model
    - b _model output represents the second stage model that is loaded from the site. It is a key component of further processing and analysis, as it contains the learning parameters and structure required for the model function.
    - Comfy dtype: MODEL
    - Python dtype: Any
- b_vae
    - b _vae output provides a variable coder (VAE) associated with phase II. It plays an important role in generating new data points or re-establishing existing data points and is critical to the tasks involved in the generation of models.
    - Comfy dtype: VAE
    - Python dtype: Any
- c_model
    - c _model output is a phase III model that is retrieved from the checkpoint. It plays a key role in the overall workflow, as it is usually more sophisticated than the phase II model and is capable of performing more advanced tasks.
    - Comfy dtype: MODEL
    - Python dtype: Any
- c_vae
    - c_vae output represents the third phase of the variable self-codifier (VAE). It is essential for tasks requiring advanced data generation and operational capability, such as feature extraction and decomposition.
    - Comfy dtype: VAE
    - Python dtype: Any
- clip_vision
    - Clip_vision output is a specialized component of the third phase of the model, focusing on visual-related tasks. It is important for applications involving image processing and understanding and provides a solid basis for visual data analysis.
    - Comfy dtype: CLIP_VISION
    - Python dtype: Any
- clip
    - Clip output represents the contextual language model (CLM) associated with the second phase. It is essential for tasks that need to be understood and generated in natural languages and provides a powerful tool for text-based applications.
    - Comfy dtype: CLIP
    - Python dtype: Any
- key_b
    - Key_b output is the identifier for the second phase of the cache. It is important for the effective management of the cache, as it allows quick retrieval and reuse of the check point during follow-up operations.
    - Comfy dtype: STRING
    - Python dtype: str
- key_c
    - Key_c output corresponds to the cache identifier at the phase III checkpoint. It plays a key role in the cache management process by ensuring efficient access to advanced models and their components.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class StableCascade_CheckpointLoader:

    @classmethod
    def INPUT_TYPES(s):
        ckpts = folder_paths.get_filename_list('checkpoints')
        default_stage_b = ''
        default_stage_c = ''
        sc_ckpts = [x for x in ckpts if 'cascade' in x.lower()]
        sc_b_ckpts = [x for x in sc_ckpts if 'stage_b' in x.lower()]
        sc_c_ckpts = [x for x in sc_ckpts if 'stage_c' in x.lower()]
        if len(sc_b_ckpts) == 0:
            sc_b_ckpts = [x for x in ckpts if 'stage_b' in x.lower()]
        if len(sc_c_ckpts) == 0:
            sc_c_ckpts = [x for x in ckpts if 'stage_c' in x.lower()]
        if len(sc_b_ckpts) == 0:
            sc_b_ckpts = ckpts
        if len(sc_c_ckpts) == 0:
            sc_c_ckpts = ckpts
        if len(sc_b_ckpts) > 0:
            default_stage_b = sc_b_ckpts[0]
        if len(sc_c_ckpts) > 0:
            default_stage_c = sc_c_ckpts[0]
        return {'required': {'stage_b': (ckpts, {'default': default_stage_b}), 'key_opt_b': ('STRING', {'multiline': False, 'placeholder': "If empty, use 'stage_b' as the key."}), 'stage_c': (ckpts, {'default': default_stage_c}), 'key_opt_c': ('STRING', {'multiline': False, 'placeholder': "If empty, use 'stage_c' as the key."}), 'cache_mode': (['none', 'stage_b', 'stage_c', 'all'], {'default': 'none'})}}
    RETURN_TYPES = ('MODEL', 'VAE', 'MODEL', 'VAE', 'CLIP_VISION', 'CLIP', 'STRING', 'STRING')
    RETURN_NAMES = ('b_model', 'b_vae', 'c_model', 'c_vae', 'c_clip_vision', 'clip', 'key_b', 'key_c')
    FUNCTION = 'doit'
    CATEGORY = 'InspirePack/Backend'

    def doit(self, stage_b, key_opt_b, stage_c, key_opt_c, cache_mode):
        if key_opt_b.strip() == '':
            key_b = stage_b
        else:
            key_b = key_opt_b.strip()
        if key_opt_c.strip() == '':
            key_c = stage_c
        else:
            key_c = key_opt_c.strip()
        if cache_mode in ['stage_b', 'all']:
            if key_b not in cache:
                res_b = nodes.CheckpointLoaderSimple().load_checkpoint(ckpt_name=stage_b)
                cache[key_b] = ('ckpt', (False, res_b))
                print(f"[Inspire Pack] StableCascade_CheckpointLoader: Ckpt '{stage_b}' is cached to '{key_b}'.")
            else:
                (_, (_, res_b)) = cache[key_b]
                print(f"[Inspire Pack] StableCascade_CheckpointLoader: Cached ckpt '{key_b}' is loaded. (Loading skip)")
            (b_model, clip, b_vae) = res_b
        else:
            (b_model, clip, b_vae) = nodes.CheckpointLoaderSimple().load_checkpoint(ckpt_name=stage_b)
        if cache_mode in ['stage_c', 'all']:
            if key_c not in cache:
                res_c = nodes.CheckpointLoaderSimple().load_checkpoint(ckpt_name=stage_c)
                cache[key_c] = ('unclip_ckpt', (False, res_c))
                print(f"[Inspire Pack] StableCascade_CheckpointLoader: Ckpt '{stage_c}' is cached to '{key_c}'.")
            else:
                (_, (_, res_c)) = cache[key_c]
                print(f"[Inspire Pack] StableCascade_CheckpointLoader: Cached ckpt '{key_c}' is loaded. (Loading skip)")
            (c_model, _, c_vae, clip_vision) = res_c
        else:
            (c_model, _, c_vae, clip_vision) = nodes.unCLIPCheckpointLoader().load_checkpoint(ckpt_name=stage_c)
        return (b_model, b_vae, c_model, c_vae, clip_vision, clip, key_b, key_c)
```