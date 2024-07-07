# Documentation
- Class name: SaveLatent
- Category: _for_testing
- Output node: True
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The SaveLatent node is designed to save the potential expression of the sample on diskette. It processes the storage process by converting the potential load into a file format that can be easily retrieved and used for further processing or analysis. The node ensures that potential data are safely written and contains selected metadata to provide additional context.

# Input types
## Required
- samples
    - The samples parameter is essential because it contains potential expressions that need to be saved. It directly affects the operation of the nodes by identifying the data to be written into the output file.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
## Optional
- filename_prefix
    - The filename_prefix parameter defines the beginning of the file name of the potential file that is saved. It affects how the files are organized and named in the output directory.
    - Comfy dtype: STRING
    - Python dtype: str
- prompt
    - When the “prompt” parameter is provided, it adds a description to the metadata of the potential files saved, which is useful for tracking the context in which potential expressions are generated.
    - Comfy dtype: PROMPT
    - Python dtype: str
- extra_pnginfo
    - The " extra_pnginfo " parameter allows for the inclusion of additional information in the metadata of potential files. This is useful for storing any additional details that may be relevant to the analysis or use of potential data.
    - Comfy dtype: EXTRA_PNGINFO
    - Python dtype: Dict[str, Any]

# Output types
- ui
    - The " ui " parameter in the output is a dictionary that contains information about potential files saved, including filenames and subfolders, which can be used for displaying or further processing at the user interface.
    - Comfy dtype: DICT
    - Python dtype: Dict[str, Any]

# Usage tips
- Infra type: CPU

# Source code
```
class SaveLatent:

    def __init__(self):
        self.output_dir = folder_paths.get_output_directory()

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'samples': ('LATENT',), 'filename_prefix': ('STRING', {'default': 'latents/ComfyUI'})}, 'hidden': {'prompt': 'PROMPT', 'extra_pnginfo': 'EXTRA_PNGINFO'}}
    RETURN_TYPES = ()
    FUNCTION = 'save'
    OUTPUT_NODE = True
    CATEGORY = '_for_testing'

    def save(self, samples, filename_prefix='ComfyUI', prompt=None, extra_pnginfo=None):
        (full_output_folder, filename, counter, subfolder, filename_prefix) = folder_paths.get_save_image_path(filename_prefix, self.output_dir)
        prompt_info = ''
        if prompt is not None:
            prompt_info = json.dumps(prompt)
        metadata = None
        if not args.disable_metadata:
            metadata = {'prompt': prompt_info}
            if extra_pnginfo is not None:
                for x in extra_pnginfo:
                    metadata[x] = json.dumps(extra_pnginfo[x])
        file = f'{filename}_{counter:05}_.latent'
        results = list()
        results.append({'filename': file, 'subfolder': subfolder, 'type': 'output'})
        file = os.path.join(full_output_folder, file)
        output = {}
        output['latent_tensor'] = samples['samples']
        output['latent_format_version_0'] = torch.tensor([])
        comfy.utils.save_torch_file(output, file, metadata=metadata)
        return {'ui': {'latents': results}}
```