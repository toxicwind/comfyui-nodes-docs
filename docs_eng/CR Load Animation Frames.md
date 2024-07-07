# Documentation
- Class name: CR_LoadAnimationFrames
- Category: Comfyroll/Animation/IO
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_LoadAnimationFrames is a node used to load and process image sequences from specified directories, which allows frame data to be manipulated and analysed in workflows. It facilitates the conversion of image files to fit them for further processing, such as animation or video editing tasks.

# Input types
## Required
- image_sequence_folder
    - The image_security_folder parameter specifies a directory containing the image sequences that you want to load. For nodes, positioning and accessing the correct image sequence for processing is essential.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- start_index
    - Start_index parameters determine the starting point of the image sequence to be loaded. It is important to control the starting frame of the sequence and allows the frame in the sequence to be loaded selectively.
    - Comfy dtype: INT
    - Python dtype: int
- max_frames
    - The max_frames parameter sets the maximum number of frames to be loaded from the image sequence. It plays an important role in limiting the amount of data processed, which is essential to optimize resource use and workflow efficiency.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- IMAGE
    - The IMAGE output provides a loading image sequence as a frame stack that allows downstream processing and analysis in the workflow.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- show_help
    - Show_help output provides a link to a document to obtain further guidance on using nodes and understanding their functionality.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_LoadAnimationFrames:
    input_dir = folder_paths.input_directory

    @classmethod
    def INPUT_TYPES(s):
        image_folder = [name for name in os.listdir(s.input_dir) if os.path.isdir(os.path.join(s.input_dir, name)) and len(os.listdir(os.path.join(s.input_dir, name))) != 0]
        return {'required': {'image_sequence_folder': (sorted(image_folder),), 'start_index': ('INT', {'default': 1, 'min': 1, 'max': 10000}), 'max_frames': ('INT', {'default': 1, 'min': 1, 'max': 10000})}}
    RETURN_TYPES = ('IMAGE', 'STRING')
    RETURN_NAMES = ('IMAGE', 'show_help')
    FUNCTION = 'load_image_sequence'
    CATEGORY = icons.get('Comfyroll/Animation/IO')

    def load_image_sequence(self, image_sequence_folder, start_index, max_frames):
        image_path = os.path.join(self.input_dir, image_sequence_folder)
        file_list = sorted(os.listdir(image_path), key=lambda s: sum(((s, int(n)) for (s, n) in re.findall('(\\D+)(\\d+)', 'a%s0' % s)), ()))
        sample_frames = []
        sample_frames_mask = []
        sample_index = list(range(start_index - 1, len(file_list), 1))[:max_frames]
        for num in sample_index:
            i = Image.open(os.path.join(image_path, file_list[num]))
            image = i.convert('RGB')
            image = np.array(image).astype(np.float32) / 255.0
            image = torch.from_numpy(image)[None,]
            image = image.squeeze()
            sample_frames.append(image)
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/IO-Nodes#cr-load-animation-frames'
        return (torch.stack(sample_frames), show_help)
```