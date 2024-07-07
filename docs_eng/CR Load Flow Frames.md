# Documentation
- Class name: CR_LoadFlowFrames
- Category: Comfyroll/Animation/IO
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

The CR_LoadFlowFrames node is designed to load and process image sequences for animation purposes. It can sort and select frames in the directory according to user-defined criteria to ensure a flow flow of animated frame-to-frame operations.

# Input types
## Required
- input_folder
    - Input_folder parameters specify a directory containing an image sequence. It plays a key role in determining the origin of animated images.
    - Comfy dtype: STRING
    - Python dtype: str
- sort_by
    - The sort_by parameter determines how to sort the image files in the input folder. It is essential to maintain the correct sequence of frames in the animation sequence.
    - Comfy dtype: STRING
    - Python dtype: str
- current_frame
    - The current_frame parameter indicates the starting frame of the loading process of the image. It is essential to control the position where the node starts to operate in the animation sequence.
    - Comfy dtype: INT
    - Python dtype: int
- skip_start_frames
    - The skip_start_frames parameter allows the user to skip a certain number of frames at the beginning of the sequence. This is very useful to remove the initial frames that are not needed for animation.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- input_path
    - The optional input_path parameter provides a particular path to the image file, if they are not in the default input directory. It provides flexibility for the animation process to locate the file.
    - Comfy dtype: STRING
    - Python dtype: str
- file_pattern
    - The file_pattern parameter is used to define the pattern of the file selection in the folder. It helps to filter selected image files of the specific type required for the animation.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- current_image
    - The Current_image output provides the latest frame that is loaded from the image sequence. It is important for continuous animation operations and displays.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- previous_image
    - The previous_image output provides a frame before the current frame in the sequence. It can be used for comparisons or transition effects in animations.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- current_frame
    - This information is very useful for tracking progress in the animation sequence.
    - Comfy dtype: INT
    - Python dtype: int
- show_help
    - Show_help output provides a link to the document to obtain further guidance on how to use the node. This is particularly helpful for users seeking more information about node functions.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_LoadFlowFrames:

    @classmethod
    def INPUT_TYPES(s):
        sort_methods = ['Index', 'Alphabetic']
        input_dir = folder_paths.input_directory
        input_folders = [name for name in os.listdir(input_dir) if os.path.isdir(os.path.join(input_dir, name)) and len(os.listdir(os.path.join(input_dir, name))) != 0]
        return {'required': {'input_folder': (sorted(input_folders),), 'sort_by': (sort_methods,), 'current_frame': ('INT', {'default': 0, 'min': 0, 'max': 10000, 'forceInput': True}), 'skip_start_frames': ('INT', {'default': 0, 'min': 0, 'max': 10000})}, 'optional': {'input_path': ('STRING', {'default': '', 'multiline': False}), 'file_pattern': ('STRING', {'default': '*.png', 'multiline': False})}}
    CATEGORY = icons.get('Comfyroll/Animation/IO')
    RETURN_TYPES = ('IMAGE', 'IMAGE', 'INT', 'STRING')
    RETURN_NAMES = ('current_image', 'previous_image', 'current_frame', 'show_help')
    FUNCTION = 'load_images'

    def load_images(self, file_pattern, skip_start_frames, input_folder, sort_by, current_frame, input_path=''):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/IO-Nodes#cr-load-flow-frames'
        input_dir = folder_paths.input_directory
        current_frame = current_frame + skip_start_frames
        print(f'[Info] CR Load Flow Frames: current_frame {current_frame}')
        if input_path != '':
            if not os.path.exists(input_path):
                print(f'[Warning] CR Load Flow Frames: The input_path `{input_path}` does not exist')
                return ('',)
            image_path = os.path.join('', input_path)
        else:
            image_path = os.path.join(input_dir, input_folder)
        print(f'[Info] CR Load Flow Frames: ComfyUI Input directory is `{image_path}`')
        file_list = get_files(image_path, sort_by, file_pattern)
        if os.path.exists(image_path + '.DS_Store'):
            file_list.remove('.DS_Store')
        if len(file_list) == 0:
            print(f'[Warning] CR Load Flow Frames: No matching files found for loading')
            return ()
        remaining_files = len(file_list) - current_frame
        print(f'[Info] CR Load Flow Frames: {remaining_files} input files remaining for processing')
        img = Image.open(os.path.join(image_path, file_list[current_frame]))
        cur_image = img.convert('RGB')
        cur_image = np.array(cur_image).astype(np.float32) / 255.0
        cur_image = torch.from_numpy(cur_image)[None,]
        print(f'[Debug] CR Load Flow Frames: Current image {file_list[current_frame]}')
        if current_frame == 0 and skip_start_frames == 0:
            img = Image.open(os.path.join(image_path, file_list[current_frame]))
            pre_image = img.convert('RGB')
            pre_image = np.array(pre_image).astype(np.float32) / 255.0
            pre_image = torch.from_numpy(pre_image)[None,]
            print(f'[Debug] CR Load Flow Frames: Previous image {file_list[current_frame]}')
        else:
            img = Image.open(os.path.join(image_path, file_list[current_frame - 1]))
            pre_image = img.convert('RGB')
            pre_image = np.array(pre_image).astype(np.float32) / 255.0
            pre_image = torch.from_numpy(pre_image)[None,]
            print(f'[Debug] CR Load Flow Frames: Previous image {file_list[current_frame - 1]}')
        return (cur_image, pre_image, current_frame, show_help)
```