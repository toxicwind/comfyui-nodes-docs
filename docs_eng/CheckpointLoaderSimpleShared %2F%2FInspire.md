# Documentation
- Class name: CheckpointLoaderSimpleShared
- Category: InspirePack/Backend
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Inspire-Pack.git

The node facilitates retrieval and cache model check points, ensuring efficient access to the model while minimizing unnecessary loading operations. It simplifys the process of using the model through intelligent management of caches based on the provision of keys and check point names.

# Input types
## Required
- ckpt_name
    - The name of the check point is essential to identify the particular model that you want to load. It allows node to retrieve or store the corresponding model data as the only reference in the cache system.
    - Comfy dtype: COMBO[folder_paths.get_filename_list('checkpoints'),]
    - Python dtype: Union[str, None]
## Optional
- key_opt
    - This optional parameter allows the user to specify a custom key to cache the checkpoint. If not provided, default use of the checkpoint name provides flexibility for the cache organization and access.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- model
    - Model output represents a loaded machine learning or in-depth learning model for further processing or reasoning. It is a core component of the node function, making downstream tasks possible.
    - Comfy dtype: ANY
    - Python dtype: Any
- clip
    - The clip output is associated with a specific model component and is usually used to support tasks or additional processes. It complements the main model output and enhances the overall capability of the node.
    - Comfy dtype: ANY
    - Python dtype: Any
- vae
    - VAE, the variable-to-codifier, is a generation model that may be loaded by the node. It plays an important role in generating new data points or features based on the distribution it learns.
    - Comfy dtype: ANY
    - Python dtype: Any
- cache_key
    - Cache keys are the only identifiers for checkpoints that are used to quote caches in the system. They are essential for the management and retrieval of checkpoints in the cache mechanism.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CheckpointLoaderSimpleShared(nodes.CheckpointLoaderSimple):

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'ckpt_name': (folder_paths.get_filename_list('checkpoints'),), 'key_opt': ('STRING', {'multiline': False, 'placeholder': "If empty, use 'ckpt_name' as the key."})}}
    RETURN_TYPES = ('MODEL', 'CLIP', 'VAE', 'STRING')
    RETURN_NAMES = ('model', 'clip', 'vae', 'cache key')
    FUNCTION = 'doit'
    CATEGORY = 'InspirePack/Backend'

    def doit(self, ckpt_name, key_opt):
        if key_opt.strip() == '':
            key = ckpt_name
        else:
            key = key_opt.strip()
        if key not in cache:
            res = self.load_checkpoint(ckpt_name)
            cache[key] = ('ckpt', (False, res))
            print(f"[Inspire Pack] CheckpointLoaderSimpleShared: Ckpt '{ckpt_name}' is cached to '{key}'.")
        else:
            (_, (_, res)) = cache[key]
            print(f"[Inspire Pack] CheckpointLoaderSimpleShared: Cached ckpt '{key}' is loaded. (Loading skip)")
        (model, clip, vae) = res
        return (model, clip, vae, key)
```