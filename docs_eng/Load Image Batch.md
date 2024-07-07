# Documentation
- Class name: WAS_Load_Image_Batch
- Category: WAS Suite/IO
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

WAS_Load_Image_Batch is designed to load and manage image file batches efficiently. It provides the functionality to load images in different modes, such as single images, incremental images, or random selection. The node ensures that images are properly directed and can handle RGBA to RGB conversions when needed. It can also remove file extensions from file names as specified.

# Input types
## Required
- path
    - The 'path' parameter specifies the directory path in which the image file is located. This is essential for node positioning and access to the image file that you need to process.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- pattern
    - The 'pattern' parameter is used to filter image files according to a given mode. It is important for selecting a subset of images that meets the given criteria in the specified directory.
    - Comfy dtype: STRING
    - Python dtype: str
- index
    - The 'index'parameter is an integer that indicates the exact location of the image in the batch to be loaded. When the mode is set to'single_image ', it plays an important role in determining the exact image to be retrieved.
    - Comfy dtype: INT
    - Python dtype: int
- mode
    - The'mode' parameter determines how to load an image. It can be'single_image' for loading a given image, 'incorporate_image' for sequential access, or 'random' for random selection.
    - Comfy dtype: COMBO['single_image', 'incremental_image', 'random']
    - Python dtype: str
- label
    - The 'label 'parameter is a string used to identify and classify image batches. It helps to organize and track different sets of images in node operations.
    - Comfy dtype: STRING
    - Python dtype: str
- allow_RGBA_output
    - The 'allow_RGBA_output' parameter decides whether to allow the output image to have an RGBA channel. If set to 'false', the node converts the image to RGB.
    - Comfy dtype: COMBO['false', 'true']
    - Python dtype: str
- filename_text_extension
    - The 'filename_text_extension' parameter indicates whether to include file extensions in the file name text output. It is useful in file names that do not require file extensions.
    - Comfy dtype: COMBO['true', 'false']
    - Python dtype: str

# Output types
- image
    - The 'image'output provides the image that is loaded in the specified batch. It is the main output of the image-processing task within the node function.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image
- filename_text
    - The 'filename_text' output returns the name of the image file loaded and can be used for reference or further processing outside the node.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Load_Image_Batch:

    def __init__(self):
        self.HDB = WASDatabase(WAS_HISTORY_DATABASE)

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'mode': (['single_image', 'incremental_image', 'random'],), 'index': ('INT', {'default': 0, 'min': 0, 'max': 150000, 'step': 1}), 'label': ('STRING', {'default': 'Batch 001', 'multiline': False}), 'path': ('STRING', {'default': '', 'multiline': False}), 'pattern': ('STRING', {'default': '*', 'multiline': False}), 'allow_RGBA_output': (['false', 'true'],)}, 'optional': {'filename_text_extension': (['true', 'false'],)}}
    RETURN_TYPES = ('IMAGE', TEXT_TYPE)
    RETURN_NAMES = ('image', 'filename_text')
    FUNCTION = 'load_batch_images'
    CATEGORY = 'WAS Suite/IO'

    def load_batch_images(self, path, pattern='*', index=0, mode='single_image', label='Batch 001', allow_RGBA_output='false', filename_text_extension='true'):
        allow_RGBA_output = allow_RGBA_output == 'true'
        if not os.path.exists(path):
            return (None,)
        fl = self.BatchImageLoader(path, label, pattern)
        new_paths = fl.image_paths
        if mode == 'single_image':
            (image, filename) = fl.get_image_by_id(index)
            if image == None:
                cstr(f'No valid image was found for the inded `{index}`').error.print()
                return (None, None)
        elif mode == 'incremental_image':
            (image, filename) = fl.get_next_image()
            if image == None:
                cstr(f'No valid image was found for the next ID. Did you remove images from the source directory?').error.print()
                return (None, None)
        else:
            newindex = int(random.random() * len(fl.image_paths))
            (image, filename) = fl.get_image_by_id(newindex)
            if image == None:
                cstr(f'No valid image was found for the next ID. Did you remove images from the source directory?').error.print()
                return (None, None)
        update_history_images(new_paths)
        if not allow_RGBA_output:
            image = image.convert('RGB')
        if filename_text_extension == 'false':
            filename = os.path.splitext(filename)[0]
        return (pil2tensor(image), filename)

    class BatchImageLoader:

        def __init__(self, directory_path, label, pattern):
            self.WDB = WDB
            self.image_paths = []
            self.load_images(directory_path, pattern)
            self.image_paths.sort()
            stored_directory_path = self.WDB.get('Batch Paths', label)
            stored_pattern = self.WDB.get('Batch Patterns', label)
            if stored_directory_path != directory_path or stored_pattern != pattern:
                self.index = 0
                self.WDB.insert('Batch Counters', label, 0)
                self.WDB.insert('Batch Paths', label, directory_path)
                self.WDB.insert('Batch Patterns', label, pattern)
            else:
                self.index = self.WDB.get('Batch Counters', label)
            self.label = label

        def load_images(self, directory_path, pattern):
            for file_name in glob.glob(os.path.join(glob.escape(directory_path), pattern), recursive=True):
                if file_name.lower().endswith(ALLOWED_EXT):
                    abs_file_path = os.path.abspath(file_name)
                    self.image_paths.append(abs_file_path)

        def get_image_by_id(self, image_id):
            if image_id < 0 or image_id >= len(self.image_paths):
                cstr(f'Invalid image index `{image_id}`').error.print()
                return
            i = Image.open(self.image_paths[image_id])
            i = ImageOps.exif_transpose(i)
            return (i, os.path.basename(self.image_paths[image_id]))

        def get_next_image(self):
            if self.index >= len(self.image_paths):
                self.index = 0
            image_path = self.image_paths[self.index]
            self.index += 1
            if self.index == len(self.image_paths):
                self.index = 0
            cstr(f'{cstr.color.YELLOW}{self.label}{cstr.color.END} Index: {self.index}').msg.print()
            self.WDB.insert('Batch Counters', self.label, self.index)
            i = Image.open(image_path)
            i = ImageOps.exif_transpose(i)
            return (i, os.path.basename(image_path))

        def get_current_image(self):
            if self.index >= len(self.image_paths):
                self.index = 0
            image_path = self.image_paths[self.index]
            return os.path.basename(image_path)

    @classmethod
    def IS_CHANGED(cls, **kwargs):
        if kwargs['mode'] != 'single_image':
            return float('NaN')
        else:
            fl = WAS_Load_Image_Batch.BatchImageLoader(kwargs['path'], kwargs['label'], kwargs['pattern'])
            filename = fl.get_current_image()
            image = os.path.join(kwargs['path'], filename)
            sha = get_sha256(image)
            return sha
```