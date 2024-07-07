# Documentation
- Class name: WAS_Image_Save
- Category: WAS Suite/IO
- Output node: True
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

WAS_Image_Save is responsible for saving pictures to the specified output directory. It handles all file formats and provides options for naming and organizing the preservation of pictures, ensuring the flow of image output management.

# Input types
## Required
- images
    - A picture parameter is necessary, which defines the input picture that needs to be saved. It plays a key role in the execution of the node because it directly affects the output.
    - Comfy dtype: IMAGE
    - Python dtype: List[PIL.Image.Image]
## Optional
- output_path
    - The output_path parameter specifies a directory for the preservation of pictures. It is very important when determining the final location of the files in the file system.
    - Comfy dtype: STRING
    - Python dtype: str
- filename_prefix
    - The filename_prefix is used to create a consistent naming protocol for preserved images, which is very useful for organizing and identifying documents.
    - Comfy dtype: STRING
    - Python dtype: str
- filename_delimiter
    - Filename_delimiter is a character used to separate prefixes and digital identifiers from saved image filenames.
    - Comfy dtype: STRING
    - Python dtype: str
- filename_number_padding
    - The filename_number_padding parameter determines the number of digits to be used for digital identifiers in the filename and ensures the consistency of the file naming scheme.
    - Comfy dtype: INT
    - Python dtype: int
- extension
    - Extension parameters indicate that pictures will be saved in file format, allowing different types of photo files to be generated.
    - Comfy dtype: COMBO['png', 'jpg', 'jpeg', 'gif', 'tiff', 'webp', 'bmp']
    - Python dtype: str
- quality
    - Quality parameters are used to set the compression level for the preservation of pictures, which may affect the balance between file size and image quality.
    - Comfy dtype: INT
    - Python dtype: int
- lossless_webp
    - The lossless_webp parameter specifies whether WEBP images should be saved using lossless compression, which preserves more image data, but at the expense of a larger file size.
    - Comfy dtype: COMBO[false, true]
    - Python dtype: bool
- overwrite_mode
    - Overwrite_mode parameters determine how to deal with existing files with the same name at nodes, which can be covered, or use the filename prefix as part of the new filename.
    - Comfy dtype: COMBO[false, prefix_as_filename]
    - Python dtype: str
- show_history
    - Show_history parameters control whether to display historical records for the preservation of pictures, which is very useful for viewing past outputs.
    - Comfy dtype: COMBO[false, true]
    - Python dtype: bool
- show_history_by_prefix
    - When the show_history_by_prefix parameter is True, it filters the image history to show only pictures with the same filename prefix, thereby enhancing organizationality.
    - Comfy dtype: COMBO[true, false]
    - Python dtype: bool
- embed_workflow
    - Embed_workflow parameters indicate whether workflow metadata should be included in the image file, providing additional context and information about the image creation process.
    - Comfy dtype: COMBO[true, false]
    - Python dtype: bool
- show_previews
    - Show_previews parameters determine whether to display a picture preview after saving, providing a quick view of the results of the operation.
    - Comfy dtype: COMBO[true, false]
    - Python dtype: bool

# Output types
- ui
    - ui parameters include user interface elements, including previews and history records (if these options are enabled) that are displayed after the preservation of the picture.
    - Comfy dtype: Dict[str, Any]
    - Python dtype: Dict[str, Union[List[Dict[str, Union[str, pathlib.Path]]], List[]]]

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Image_Save:

    def __init__(self):
        self.output_dir = comfy_paths.output_directory
        self.type = 'output'

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'images': ('IMAGE',), 'output_path': ('STRING', {'default': '[time(%Y-%m-%d)]', 'multiline': False}), 'filename_prefix': ('STRING', {'default': 'ComfyUI'}), 'filename_delimiter': ('STRING', {'default': '_'}), 'filename_number_padding': ('INT', {'default': 4, 'min': 1, 'max': 9, 'step': 1}), 'filename_number_start': (['false', 'true'],), 'extension': (['png', 'jpg', 'jpeg', 'gif', 'tiff', 'webp', 'bmp'],), 'quality': ('INT', {'default': 100, 'min': 1, 'max': 100, 'step': 1}), 'lossless_webp': (['false', 'true'],), 'overwrite_mode': (['false', 'prefix_as_filename'],), 'show_history': (['false', 'true'],), 'show_history_by_prefix': (['true', 'false'],), 'embed_workflow': (['true', 'false'],), 'show_previews': (['true', 'false'],)}, 'hidden': {'prompt': 'PROMPT', 'extra_pnginfo': 'EXTRA_PNGINFO'}}
    RETURN_TYPES = ()
    FUNCTION = 'was_save_images'
    OUTPUT_NODE = True
    CATEGORY = 'WAS Suite/IO'

    def was_save_images(self, images, output_path='', filename_prefix='ComfyUI', filename_delimiter='_', extension='png', quality=100, lossless_webp='false', prompt=None, extra_pnginfo=None, overwrite_mode='false', filename_number_padding=4, filename_number_start='false', show_history='false', show_history_by_prefix='true', embed_workflow='true', show_previews='true'):
        delimiter = filename_delimiter
        number_padding = filename_number_padding
        lossless_webp = lossless_webp == 'true'
        tokens = TextTokens()
        original_output = self.output_dir
        filename_prefix = tokens.parseTokens(filename_prefix)
        if output_path in [None, '', 'none', '.']:
            output_path = self.output_dir
        else:
            output_path = tokens.parseTokens(output_path)
        if not os.path.isabs(output_path):
            output_path = os.path.join(self.output_dir, output_path)
        base_output = os.path.basename(output_path)
        if output_path.endswith('ComfyUI/output') or output_path.endswith('ComfyUI\\output'):
            base_output = ''
        if output_path.strip() != '':
            if not os.path.isabs(output_path):
                output_path = os.path.join(comfy_paths.output_directory, output_path)
            if not os.path.exists(output_path.strip()):
                cstr(f"The path `{output_path.strip()}` specified doesn't exist! Creating directory.").warning.print()
                os.makedirs(output_path, exist_ok=True)
        if filename_number_start == 'true':
            pattern = f'(\\d+){re.escape(delimiter)}{re.escape(filename_prefix)}'
        else:
            pattern = f'{re.escape(filename_prefix)}{re.escape(delimiter)}(\\d+)'
        existing_counters = [int(re.search(pattern, filename).group(1)) for filename in os.listdir(output_path) if re.match(pattern, os.path.basename(filename))]
        existing_counters.sort(reverse=True)
        if existing_counters:
            counter = existing_counters[0] + 1
        else:
            counter = 1
        if existing_counters:
            counter = existing_counters[0] + 1
        else:
            counter = 1
        file_extension = '.' + extension
        if file_extension not in ALLOWED_EXT:
            cstr(f"The extension `{extension}` is not valid. The valid formats are: {', '.join(sorted(ALLOWED_EXT))}").error.print()
            file_extension = 'png'
        results = list()
        for image in images:
            i = 255.0 * image.cpu().numpy()
            img = Image.fromarray(np.clip(i, 0, 255).astype(np.uint8))
            if extension == 'webp':
                img_exif = img.getexif()
                workflow_metadata = ''
                prompt_str = ''
                if prompt is not None:
                    prompt_str = json.dumps(prompt)
                    img_exif[271] = 'Prompt:' + prompt_str
                if extra_pnginfo is not None:
                    for x in extra_pnginfo:
                        workflow_metadata += json.dumps(extra_pnginfo[x])
                img_exif[270] = 'Workflow:' + workflow_metadata
                exif_data = img_exif.tobytes()
            else:
                metadata = PngInfo()
                if embed_workflow == 'true':
                    if prompt is not None:
                        metadata.add_text('prompt', json.dumps(prompt))
                    if extra_pnginfo is not None:
                        for x in extra_pnginfo:
                            metadata.add_text(x, json.dumps(extra_pnginfo[x]))
                exif_data = metadata
            if overwrite_mode == 'prefix_as_filename':
                file = f'{filename_prefix}{file_extension}'
            else:
                if filename_number_start == 'true':
                    file = f'{counter:0{number_padding}}{delimiter}{filename_prefix}{file_extension}'
                else:
                    file = f'{filename_prefix}{delimiter}{counter:0{number_padding}}{file_extension}'
                if os.path.exists(os.path.join(output_path, file)):
                    counter += 1
            try:
                output_file = os.path.abspath(os.path.join(output_path, file))
                if extension in ['jpg', 'jpeg']:
                    img.save(output_file, quality=quality, optimize=True)
                elif extension == 'webp':
                    img.save(output_file, quality=quality, lossless=lossless_webp, exif=exif_data)
                elif extension == 'png':
                    img.save(output_file, pnginfo=exif_data, optimize=True)
                elif extension == 'bmp':
                    img.save(output_file)
                elif extension == 'tiff':
                    img.save(output_file, quality=quality, optimize=True)
                else:
                    img.save(output_file, pnginfo=exif_data, optimize=True)
                cstr(f'Image file saved to: {output_file}').msg.print()
                if show_history != 'true' and show_previews == 'true':
                    subfolder = self.get_subfolder_path(output_file, original_output)
                    results.append({'filename': file, 'subfolder': subfolder, 'type': self.type})
                update_history_output_images(output_file)
            except OSError as e:
                cstr(f'Unable to save file to: {output_file}').error.print()
                print(e)
            except Exception as e:
                cstr('Unable to save file due to the to the following error:').error.print()
                print(e)
            if overwrite_mode == 'false':
                counter += 1
        filtered_paths = []
        if show_history == 'true' and show_previews == 'true':
            HDB = WASDatabase(WAS_HISTORY_DATABASE)
            conf = getSuiteConfig()
            if HDB.catExists('History') and HDB.keyExists('History', 'Output_Images'):
                history_paths = HDB.get('History', 'Output_Images')
            else:
                history_paths = None
            if history_paths:
                for image_path in history_paths:
                    image_subdir = self.get_subfolder_path(image_path, self.output_dir)
                    current_subdir = self.get_subfolder_path(output_file, self.output_dir)
                    if not os.path.exists(image_path):
                        continue
                    if show_history_by_prefix == 'true' and image_subdir != current_subdir:
                        continue
                    if show_history_by_prefix == 'true' and (not os.path.basename(image_path).startswith(filename_prefix)):
                        continue
                    filtered_paths.append(image_path)
                if conf.__contains__('history_display_limit'):
                    filtered_paths = filtered_paths[-conf['history_display_limit']:]
                filtered_paths.reverse()
        if filtered_paths:
            for image_path in filtered_paths:
                subfolder = self.get_subfolder_path(image_path, self.output_dir)
                image_data = {'filename': os.path.basename(image_path), 'subfolder': subfolder, 'type': self.type}
                results.append(image_data)
        if show_previews == 'true':
            return {'ui': {'images': results}}
        else:
            return {'ui': {'images': []}}

    def get_subfolder_path(self, image_path, output_path):
        output_parts = output_path.strip(os.sep).split(os.sep)
        image_parts = image_path.strip(os.sep).split(os.sep)
        common_parts = os.path.commonprefix([output_parts, image_parts])
        subfolder_parts = image_parts[len(common_parts):]
        subfolder_path = os.sep.join(subfolder_parts[:-1])
        return subfolder_path
```