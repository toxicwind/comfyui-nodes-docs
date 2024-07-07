# Documentation
- Class name: VAESave
- Category: advanced/model_merging
- Output node: True
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

VAESave node is responsible for preserving the status of the VAE model. It provides the function of serializing the model's state dictionary into a file that can be used for subsequent retrieval or deployment. This node is essential for preserving the parameters of the training model and ensuring that they can be reloaded without loss of information.

# Input types
## Required
- vae
    - The 'vae' parameter is necessary because it represents the variable self-encoder model to be saved. It is necessary for node operations and the main input that determines node operations.
    - Comfy dtype: VAE
    - Python dtype: comfy.model_base.VAE
- filename_prefix
    - The 'filename_prefix' parameter is used to define prefixes to the output filename that saves the VAE model. It plays an important role in organizing and identifying the model file that is saved.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- prompt
    - The `prompt' parameter, although optional, could be used to include additional context or description of the intended use of the model, which may be useful for future reference or metadata purposes.
    - Comfy dtype: PROMPT
    - Python dtype: str
- extra_pnginfo
    - The 'extra_pnginfo' parameter allows for the inclusion of additional information that can be stored with the model. This may be useful for adding notes or other relevant data that may be required.
    - Comfy dtype: EXTRA_PNGINFO
    - Python dtype: dict

# Output types
- output_checkpoint
    - The 'output_checkpoint' parameter represents the path of the model file saved. It marks the successful completion of the preservation process and provides a location where the model can be found.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class VAESave:

    def __init__(self):
        self.output_dir = folder_paths.get_output_directory()

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'vae': ('VAE',), 'filename_prefix': ('STRING', {'default': 'vae/ComfyUI_vae'})}, 'hidden': {'prompt': 'PROMPT', 'extra_pnginfo': 'EXTRA_PNGINFO'}}
    RETURN_TYPES = ()
    FUNCTION = 'save'
    OUTPUT_NODE = True
    CATEGORY = 'advanced/model_merging'

    def save(self, vae, filename_prefix, prompt=None, extra_pnginfo=None):
        (full_output_folder, filename, counter, subfolder, filename_prefix) = folder_paths.get_save_image_path(filename_prefix, self.output_dir)
        prompt_info = ''
        if prompt is not None:
            prompt_info = json.dumps(prompt)
        metadata = {}
        if not args.disable_metadata:
            metadata['prompt'] = prompt_info
            if extra_pnginfo is not None:
                for x in extra_pnginfo:
                    metadata[x] = json.dumps(extra_pnginfo[x])
        output_checkpoint = f'{filename}_{counter:05}_.safetensors'
        output_checkpoint = os.path.join(full_output_folder, output_checkpoint)
        comfy.utils.save_torch_file(vae.get_sd(), output_checkpoint, metadata=metadata)
        return {}
```