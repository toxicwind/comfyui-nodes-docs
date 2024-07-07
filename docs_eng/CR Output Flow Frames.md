# Documentation
- Class name: CR_OutputFlowFrames
- Category: Comfyroll/Animation/IO
- Output node: True
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

The CR_OutputFlowFrames node is designed to manage the output process of the image frame and to facilitate the preservation of the image to the specified directory. It supports direct image output and plug-in images to ensure a smooth transition between frames. The node plays a key role in the final phase of the image processing stream, focusing on the framework for efficient storage and organizational generation.

# Input types
## Required
- output_folder
    - The output_folder parameter specifies the directory that you want to save the frame. This is essential for organizing the output and ensuring that the frame is stored in the right location.
    - Comfy dtype: STRING
    - Python dtype: str
- current_image
    - The Current_image parameter represents the current frame image to be saved. It is the basic input for node operations, as it is the actual content to be written into the file system.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- current_frame
    - The Current_frame parameter indicates the frame number that is currently being processed. It is essential for the image to be named and sorted according to the sequence that reflects the processing order.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- filename_prefix
    - The filename_prefix parameter is used to define the initial part of the filename that saves the image. It helps to create a consistent naming protocol for the output file, which may be useful for subsequent identification and processing.
    - Comfy dtype: STRING
    - Python dtype: str
- interpolated_img
    - The interpolated_img parameter provides the option to include a plug-in image in the output. This enhances the visual transition between frames and provides a more fluid animation effect.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- output_path
    - The output_path parameter allows you to specify an alternative path to save the image and to overwrite the default output directory. It provides flexibility in managing the storage location of the output image.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- ui
    - The ui parameter in the output contains information about the images saved, including their filename, subfolder location and type of output. The data can be used for displaying or further processing at the user interface.
    - Comfy dtype: COMBO[Dict[str, List[Dict[str, Union[str, Dict[str, str]]]]]]
    - Python dtype: Dict[str, List[Dict[str, Union[str, Dict[str, str]]]]

# Usage tips
- Infra type: CPU

# Source code
```
class CR_OutputFlowFrames:

    def __init__(self):
        self.type = 'output'

    @classmethod
    def INPUT_TYPES(cls):
        output_dir = folder_paths.output_directory
        output_folders = [name for name in os.listdir(output_dir) if os.path.isdir(os.path.join(output_dir, name)) and len(os.listdir(os.path.join(output_dir, name))) != 0]
        return {'required': {'output_folder': (sorted(output_folders),), 'current_image': ('IMAGE',), 'filename_prefix': ('STRING', {'default': 'CR'}), 'current_frame': ('INT', {'default': 0, 'min': 0, 'max': 9999999, 'forceInput': True})}, 'optional': {'interpolated_img': ('IMAGE',), 'output_path': ('STRING', {'default': '', 'multiline': False})}}
    RETURN_TYPES = ()
    FUNCTION = 'save_images'
    OUTPUT_NODE = True
    CATEGORY = icons.get('Comfyroll/Animation/IO')

    def save_images(self, output_folder, current_image, current_frame, output_path='', filename_prefix='CR', interpolated_img=None):
        output_dir = folder_paths.get_output_directory()
        out_folder = os.path.join(output_dir, output_folder)
        if output_path != '':
            if not os.path.exists(output_path):
                print(f'[Warning] CR Output Flow Frames: The input_path `{output_path}` does not exist')
                return ('',)
            out_path = output_path
        else:
            out_path = os.path.join(output_dir, out_folder)
        print(f'[Info] CR Output Flow Frames: Output path is `{out_path}`')
        if interpolated_img is not None:
            output_image0 = current_image[0].cpu().numpy()
            output_image1 = interpolated_img[0].cpu().numpy()
            img0 = Image.fromarray(np.clip(output_image0 * 255.0, 0, 255).astype(np.uint8))
            img1 = Image.fromarray(np.clip(output_image1 * 255.0, 0, 255).astype(np.uint8))
            output_filename0 = f'{filename_prefix}_{current_frame:05}_0.png'
            output_filename1 = f'{filename_prefix}_{current_frame:05}_1.png'
            print(f'[Warning] CR Output Flow Frames: Saved {filename_prefix}_{current_frame:05}_0.png')
            print(f'[Warning] CR Output Flow Frames: Saved {filename_prefix}_{current_frame:05}_1.png')
            resolved_image_path0 = out_path + '/' + output_filename0
            resolved_image_path1 = out_path + '/' + output_filename1
            img0.save(resolved_image_path0, pnginfo='', compress_level=4)
            img1.save(resolved_image_path1, pnginfo='', compress_level=4)
        else:
            output_image0 = current_image[0].cpu().numpy()
            img0 = Image.fromarray(np.clip(output_image0 * 255.0, 0, 255).astype(np.uint8))
            output_filename0 = f'{filename_prefix}_{current_frame:05}.png'
            resolved_image_path0 = out_path + '/' + output_filename0
            img0.save(resolved_image_path0, pnginfo='', compress_level=4)
            print(f'[Info] CR Output Flow Frames: Saved {filename_prefix}_{current_frame:05}.png')
        result = {'ui': {'images': [{'filename': output_filename0, 'subfolder': out_path, 'type': self.type}]}}
        return result
```