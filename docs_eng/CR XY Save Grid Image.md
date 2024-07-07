# Documentation
- Class name: CR_XYSaveGridImage
- Category: Comfyroll/XY Grid
- Output node: True
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_XYSaveGridImage is a node designed to save a grid image to the specified output directory. It handles different modes of saving or previewing images and supports multiple file formats. This node ensures that each saved image is based on a prefix and the sole name of a digital counter, so that the image can be organized and retrieved.

# Input types
## Required
- mode
    - Model parameters determine whether the node is in the'save' mode to save the image permanently or the'preview' mode to save the image temporarily for review. This selects the destination that affects the behaviour of the node and the preservation of the image.
    - Comfy dtype: COMBO['Save', 'Preview']
    - Python dtype: str
- output_folder
    - Output folder parameters specify the directory in the output directory where the image will be saved. This is essential to ensure that the images saved by the organization are stored in the right location.
    - Comfy dtype: STRING
    - Python dtype: str
- image
    - The image parameter is the actual image data that the node will process and save. It is the central input to the node operation, because the node's main purpose is to process the preservation of the image.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- file_format
    - The file format parameter defines the format in which the image will be saved. It supports the various formats and allows flexibility in the way the image is stored and used.
    - Comfy dtype: COMBO['webp', 'jpg', 'png', 'tif']
    - Python dtype: str
## Optional
- filename_prefix
    - The prefix parameter provides the basis for preserving the image file name. It is used in conjunction with the digital counter to ensure the uniqueness of the filename, which is important to prevent the document from covering and maintaining the file tissue.
    - Comfy dtype: STRING
    - Python dtype: str
- output_path
    - Output path parameters allow a custom path to be specified to save the image, overwrite the default output directory. It provides additional control over the location of the image.
    - Comfy dtype: STRING
    - Python dtype: str
- trigger
    - The trigger parameter is a boolean symbol that starts the image preservation process when set as True. It serves as a control mechanism to determine when node should perform its primary function.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- preview
    - Preview output provides a structured expression for saving the image, including its filename and location. This output is useful for displaying the image in the user interface for review.
    - Comfy dtype: DICT
    - Python dtype: Dict[str, Any]

# Usage tips
- Infra type: CPU

# Source code
```
class CR_XYSaveGridImage:

    def __init__(self):
        self.type = 'output'

    @classmethod
    def INPUT_TYPES(cls):
        output_dir = folder_paths.output_directory
        output_folders = [name for name in os.listdir(output_dir) if os.path.isdir(os.path.join(output_dir, name))]
        return {'required': {'mode': (['Save', 'Preview'],), 'output_folder': (sorted(output_folders),), 'image': ('IMAGE',), 'filename_prefix': ('STRING', {'default': 'CR'}), 'file_format': (['webp', 'jpg', 'png', 'tif'],)}, 'optional': {'output_path': ('STRING', {'default': '', 'multiline': False}), 'trigger': ('BOOLEAN', {'default': False})}}
    RETURN_TYPES = ()
    FUNCTION = 'save_image'
    OUTPUT_NODE = True
    CATEGORY = icons.get('Comfyroll/XY Grid')

    def save_image(self, mode, output_folder, image, file_format, output_path='', filename_prefix='CR', trigger=False):
        if trigger == False:
            return ()
        output_dir = folder_paths.get_output_directory()
        out_folder = os.path.join(output_dir, output_folder)
        if output_path != '':
            if not os.path.exists(output_path):
                print(f'[Warning] CR Save XY Grid Image: The input_path `{output_path}` does not exist')
                return ('',)
            out_path = output_path
        else:
            out_path = os.path.join(output_dir, out_folder)
        if mode == 'Preview':
            out_path = folder_paths.temp_directory
        print(f'[Info] CR Save XY Grid Image: Output path is `{out_path}`')
        counter = find_highest_numeric_value(out_path, filename_prefix) + 1
        output_image = image[0].cpu().numpy()
        img = Image.fromarray(np.clip(output_image * 255.0, 0, 255).astype(np.uint8))
        output_filename = f'{filename_prefix}_{counter:05}'
        img_params = {'png': {'compress_level': 4}, 'webp': {'method': 6, 'lossless': False, 'quality': 80}, 'jpg': {'format': 'JPEG'}, 'tif': {'format': 'TIFF'}}
        self.type = 'output' if mode == 'Save' else 'temp'
        resolved_image_path = os.path.join(out_path, f'{output_filename}.{file_format}')
        img.save(resolved_image_path, **img_params[file_format])
        print(f'[Info] CR Save XY Grid Image: Saved to {output_filename}.{file_format}')
        out_filename = f'{output_filename}.{file_format}'
        preview = {'ui': {'images': [{'filename': out_filename, 'subfolder': out_path, 'type': self.type}]}}
        return preview
```