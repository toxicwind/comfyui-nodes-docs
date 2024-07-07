# Documentation
- Class name: SeargeImageSave
- Category: Searge/_deprecated_/Files
- Output node: True
- Repo Ref: https://github.com/jobunk/SeargeSDXL.git

The node is intended to facilitate the preservation of image data and to ensure that images are stored correctly with relevant metadata and naming.

# Input types
## Required
- images
    - Input images that need to be saved by nodes. These images are the primary data for node operations, and their quality and format directly influence the output results.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- filename_prefix
    - The prefix string used to construct the saved image filename. This parameter is essential because it determines the identity and organization of the saved file.
    - Comfy dtype: STRING
    - Python dtype: str
- state
    - A state parameter that affects the execution of the node. It determines whether the node performs the saving operation.
    - Comfy dtype: ENABLE_STATE
    - Python dtype: int
- save_to
    - This parameter specifies the destination folder for which the image is stored. It is essential for organizing the output and ensuring that the image is accessible after processing.
    - Comfy dtype: SAVE_FOLDER
    - Python dtype: int
## Optional
- prompt
    - This is an optional parameter, which, when available, will contain a hint text in the image metadata. This adds context to the image, which may be useful for subsequent reference.
    - Comfy dtype: PROMPT
    - Python dtype: str
- extra_pnginfo
    - Additional metadata to be saved with the image. This parameter allows for additional information that enriches the context and utility of saving the image.
    - Comfy dtype: EXTRA_PNGINFO
    - Python dtype: Dict[str, str]

# Output types

# Usage tips
- Infra type: CPU

# Source code
```
class SeargeImageSave:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'images': ('IMAGE',), 'filename_prefix': ('STRING', {'default': 'SeargeSDXL-%date%/Image'}), 'state': ('ENABLE_STATE', {'default': SeargeParameterProcessor.STATES[1]}), 'save_to': ('SAVE_FOLDER', {'default': SeargeParameterProcessor.SAVE_TO[0]})}, 'hidden': {'prompt': 'PROMPT', 'extra_pnginfo': 'EXTRA_PNGINFO'}}
    RETURN_TYPES = ()
    FUNCTION = 'save_images'
    OUTPUT_NODE = True
    CATEGORY = 'Searge/_deprecated_/Files'

    def save_images(self, images, filename_prefix, state, save_to, prompt=None, extra_pnginfo=None):
        if state == SeargeParameterProcessor.STATES[0]:
            return {}
        if save_to == SeargeParameterProcessor.SAVE_TO[1]:
            output_dir = folder_paths.get_input_directory()
            filename_prefix = 'output-%date%'
        else:
            output_dir = folder_paths.get_output_directory()
        filename_prefix = filename_prefix.replace('%date%', datetime.now().strftime('%Y-%m-%d'))
        (full_output_folder, filename, counter, subfolder, filename_prefix) = folder_paths.get_save_image_path(filename_prefix, output_dir, images[0].shape[1], images[0].shape[0])
        for image in images:
            i = 255.0 * image.cpu().numpy()
            img = Image.fromarray(np.clip(i, 0, 255).astype(np.uint8))
            metadata = None
            if args.disable_metadata is None or not args.disable_metadata:
                metadata = PngInfo()
                if prompt is not None:
                    metadata.add_text('prompt', json.dumps(prompt))
                if extra_pnginfo is not None:
                    for x in extra_pnginfo:
                        metadata.add_text(x, json.dumps(extra_pnginfo[x]))
            file = f'{filename}_{counter:05}_.png'
            img.save(os.path.join(full_output_folder, file), pnginfo=metadata, compress_level=4)
            counter += 1
        return {}
```