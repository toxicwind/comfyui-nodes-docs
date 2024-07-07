# Documentation
- Class name: WLSH_Image_Save_With_File_Info
- Category: WLSH Nodes/IO
- Output node: True
- Repo Ref: https://github.com/wallish77/wlsh_nodes

The WLSH_Image_Save_With_File_Info node is designed to save pictures to the file system and to attach file information. It provides the function to save pictures, allows custom filenames, extensions and quality settings, and can contain metadata, such as tips and model information.

# Input types
## Required
- images
    - Picture parameters are essential for the node because they define the input pictures that you want to save. Node processes and saves the images according to the other parameters provided.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
## Optional
- filename
    - The filename parameter allows the user to specify a basic name for the saved file. It plays an important role in the tissue output file because it determines the initial part of the filename.
    - Comfy dtype: STRING
    - Python dtype: str
- path
    - Path parameters determine the directory where the pictures will be saved. It is important for organizing the saved files into a specific folder.
    - Comfy dtype: STRING
    - Python dtype: str
- extension
    - The extension parameter determines the file format for which the picture will be saved. It is essential to define the file extension type to be used for the output picture.
    - Comfy dtype: COMBO['png', 'jpeg', 'tiff', 'gif']
    - Python dtype: str
- quality
    - Quality parameters are important for setting the compression level for the preservation of pictures, particularly for formats such as JPEG or WebP, which affect the balance between the quality of the picture and the size of the file.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- ui
    - The ui parameter in the output contains the path to the preservation of the picture, which provides the user with the reference for the location of the image storage.
    - Comfy dtype: DICT
    - Python dtype: Dict[str, List[Dict[str, str]]]

# Usage tips
- Infra type: CPU

# Source code
```
class WLSH_Image_Save_With_File_Info:

    def __init__(self):
        self.output_dir = folder_paths.output_directory
        self.type = 'output'

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'images': ('IMAGE',), 'filename': ('STRING', {'default': f'%time_%seed', 'multiline': False}), 'path': ('STRING', {'default': '', 'multiline': False}), 'extension': (['png', 'jpeg', 'tiff', 'gif'],), 'quality': ('INT', {'default': 100, 'min': 1, 'max': 100, 'step': 1})}, 'optional': {'positive': ('STRING', {'default': '', 'multiline': True, 'forceInput': True}), 'negative': ('STRING', {'default': '', 'multiline': True, 'forceInput': True}), 'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615, 'forceInput': True}), 'modelname': ('STRING', {'default': '', 'multiline': False, 'forceInput': True}), 'counter': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615}), 'time_format': ('STRING', {'default': '%Y-%m-%d-%H%M%S', 'multiline': False}), 'info': ('INFO',)}, 'hidden': {'prompt': 'PROMPT', 'extra_pnginfo': 'EXTRA_PNGINFO'}}
    RETURN_TYPES = ()
    FUNCTION = 'save_files'
    OUTPUT_NODE = True
    CATEGORY = 'WLSH Nodes/IO'

    def save_files(self, images, positive='unknown', negative='unknown', seed=-1, modelname='unknown', info=None, counter=0, filename='', path='', time_format='%Y-%m-%d-%H%M%S', extension='png', quality=100, prompt=None, extra_pnginfo=None):
        filename = make_filename(filename, seed, modelname, counter, time_format)
        comment = make_comment(positive, negative, modelname, seed, info)
        output_path = os.path.join(self.output_dir, path)
        if output_path.strip() != '':
            if not os.path.exists(output_path.strip()):
                print(f"The path `{output_path.strip()}` specified doesn't exist! Creating directory.")
                os.makedirs(output_path, exist_ok=True)
        paths = self.save_images(images, output_path, path, filename, comment, extension, quality, prompt, extra_pnginfo)
        self.save_text_file(filename, output_path, comment, seed, modelname)
        return {'ui': {'images': paths}}

    def save_images(self, images, output_path, path, filename_prefix='ComfyUI', comment='', extension='png', quality=100, prompt=None, extra_pnginfo=None):

        def map_filename(filename):
            prefix_len = len(filename_prefix)
            prefix = filename[:prefix_len + 1]
            try:
                digits = int(filename[prefix_len + 1:].split('_')[0])
            except:
                digits = 0
            return (digits, prefix)
        imgCount = 1
        paths = list()
        for image in images:
            i = 255.0 * image.cpu().numpy()
            img = Image.fromarray(np.clip(i, 0, 255).astype(np.uint8))
            metadata = PngInfo()
            if prompt is not None:
                metadata.add_text('prompt', json.dumps(prompt))
            if extra_pnginfo is not None:
                for x in extra_pnginfo:
                    metadata.add_text(x, json.dumps(extra_pnginfo[x]))
            metadata.add_text('parameters', comment)
            if images.size()[0] > 1:
                filename_prefix += '_{:02d}'.format(imgCount)
            file = f'{filename_prefix}.{extension}'
            if extension == 'png':
                img.save(os.path.join(output_path, file), comment=comment, pnginfo=metadata, optimize=True)
            elif extension == 'webp':
                img.save(os.path.join(output_path, file), quality=quality)
            elif extension == 'jpeg':
                img.save(os.path.join(output_path, file), quality=quality, comment=comment, optimize=True)
            elif extension == 'tiff':
                img.save(os.path.join(output_path, file), quality=quality, optimize=True)
            else:
                img.save(os.path.join(output_path, file))
            paths.append({'filename': file, 'subfolder': path, 'type': self.type})
            imgCount += 1
        return paths

    def save_text_file(self, filename, output_path, comment='', seed=0, modelname=''):
        self.writeTextFile(os.path.join(output_path, filename + '.txt'), comment)
        return

    def writeTextFile(self, file, content):
        try:
            with open(file, 'w') as f:
                f.write(content)
        except OSError:
            print('Unable to save file `{file}`')
```