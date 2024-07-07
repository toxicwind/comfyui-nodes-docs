# Documentation
- Class name: SaveImage
- Category: image
- Output node: True
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The node is intended to perpetuate the images generated into the file system, to ensure that the results of the image creation process are stored and organized in the directory structure specified by the user.

# Input types
## Required
- images
    - An image parameter is necessary because it provides nodes with raw image data that need to be saved. It directly affects the primary function of the node to save the image.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
## Optional
- filename_prefix
    - This parameter allows the user to assign prefixes to the saved image filename, which is essential for organizing and identifying the image in the output directory.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- ui
    - The output provides a structured summary of the images saved, including filenames and subfolders, which are important for the user to track and manage the content generated.
    - Comfy dtype: DICT
    - Python dtype: Dict[str, List[Dict[str, Union[str, int]]]

# Usage tips
- Infra type: CPU

# Source code
```
class SaveImage:

    def __init__(self):
        self.output_dir = folder_paths.get_output_directory()
        self.type = 'output'
        self.prefix_append = ''
        self.compress_level = 4

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'images': ('IMAGE',), 'filename_prefix': ('STRING', {'default': 'ComfyUI'})}, 'hidden': {'prompt': 'PROMPT', 'extra_pnginfo': 'EXTRA_PNGINFO'}}
    RETURN_TYPES = ()
    FUNCTION = 'save_images'
    OUTPUT_NODE = True
    CATEGORY = 'image'

    def save_images(self, images, filename_prefix='ComfyUI', prompt=None, extra_pnginfo=None):
        filename_prefix += self.prefix_append
        (full_output_folder, filename, counter, subfolder, filename_prefix) = folder_paths.get_save_image_path(filename_prefix, self.output_dir, images[0].shape[1], images[0].shape[0])
        results = list()
        for (batch_number, image) in enumerate(images):
            i = 255.0 * image.cpu().numpy()
            img = Image.fromarray(np.clip(i, 0, 255).astype(np.uint8))
            metadata = None
            if not args.disable_metadata:
                metadata = PngInfo()
                if prompt is not None:
                    metadata.add_text('prompt', json.dumps(prompt))
                if extra_pnginfo is not None:
                    for x in extra_pnginfo:
                        metadata.add_text(x, json.dumps(extra_pnginfo[x]))
            filename_with_batch_num = filename.replace('%batch_num%', str(batch_number))
            file = f'{filename_with_batch_num}_{counter:05}_.png'
            img.save(os.path.join(full_output_folder, file), pnginfo=metadata, compress_level=self.compress_level)
            results.append({'filename': file, 'subfolder': subfolder, 'type': self.type})
            counter += 1
        return {'ui': {'images': results}}
```