# Documentation
- Class name: SaveImageToLocal
- Category: ♾️Mixlab/Image
- Output node: True
- Repo Ref: https://github.com/shadowcz007/comfyui-mixlab-nodes.git

The "SaveImageToLocal" node is designed to save image data to local filesystems. It provides a simple mechanism for sustaining images to ensure that they are stored in the specified output directory. This node is particularly useful in scenarios that require visualization or further processing of images outside the computing environment.

# Input types
## Required
- images
    - The “images” parameter is essential for the operation of the node, as it represents the raw image data to be saved. Its successful implementation depends on the correct formatting and completeness of the image data provided.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- file_path
    - The " file_path " parameter indicates that the image will be stored in the location of the local system. It is essential for guiding the output of nodes and systematically organizing the files saved.
    - Comfy dtype: STRING
    - Python dtype: str
- prompt
    - The 'prompt' parameter, although optional, can be used to add context to the saved image by embedding descriptive text in image metadata. This is particularly useful for sorting and searching image pools.
    - Comfy dtype: PROMPT
    - Python dtype: str
- extra_pnginfo
    - The “extra_pnginfo” parameter allows for the inclusion of additional metadata in each saved image, enhances the ability to describe the image and promotes more complex search or organization options.
    - Comfy dtype: EXTRA_PNGINFO
    - Python dtype: Dict[str, str]

# Output types

# Usage tips
- Infra type: CPU

# Source code
```
class SaveImageToLocal:

    def __init__(self):
        self.output_dir = folder_paths.get_output_directory()
        self.type = 'output'
        self.compress_level = 4

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'images': ('IMAGE',), 'file_path': ('STRING', {'multiline': True, 'default': '', 'dynamicPrompts': False})}, 'hidden': {'prompt': 'PROMPT', 'extra_pnginfo': 'EXTRA_PNGINFO'}}
    RETURN_TYPES = ()
    FUNCTION = 'save_images'
    OUTPUT_NODE = True
    CATEGORY = '♾️Mixlab/Image'

    def save_images(self, images, file_path, prompt=None, extra_pnginfo=None):
        filename_prefix = os.path.basename(file_path)
        if file_path == '':
            filename_prefix = 'ComfyUI'
        (filename_prefix, _) = os.path.splitext(filename_prefix)
        (_, extension) = os.path.splitext(file_path)
        if extension:
            file_path = os.path.dirname(file_path)
        (full_output_folder, filename, counter, subfolder, filename_prefix) = folder_paths.get_save_image_path(filename_prefix, self.output_dir, images[0].shape[1], images[0].shape[0])
        if not os.path.exists(file_path):
            os.makedirs(file_path)
            print ('dir created')
        else:
            print ( 'The Directory Exists')
        if file_path == '':
            files = glob.glob(full_output_folder + '/*')
        else:
            files = glob.glob(file_path + '/*')
        file_count = len(files)
        counter += file_count
        Point('Statistical Number', file_count, count)
        results = list()
        for image in images:
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
            file = f'{filename}_{counter:05}_.png'
            if file_path == '':
                fp = os.path.join(full_output_folder, file)
                if os.path.exists(fp):
                    file = f'{filename}_{counter:05}_{generate_random_string(8)}.png'
                    fp = os.path.join(full_output_folder, file)
                img.save(fp, pnginfo=metadata, compress_level=self.compress_level)
                results.append({'filename': file, 'subfolder': subfolder, 'type': self.type})
            else:
                fp = os.path.join(file_path, file)
                if os.path.exists(fp):
                    file = f'{filename}_{counter:05}_{generate_random_string(8)}.png'
                    fp = os.path.join(file_path, file)
                img.save(os.path.join(file_path, file), pnginfo=metadata, compress_level=self.compress_level)
                results.append({'filename': file, 'subfolder': file_path, 'type': self.type})
            counter += 1
        return ()
```