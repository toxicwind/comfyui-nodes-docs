# Documentation
- Class name: CR_LoadImageList
- Category: Comfyroll/List/IO
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_LoadImageList is a node for loading and processing the list of image files from the specified directory. It provides a function for searching subsets of images based on the initial index and the maximum number of images to load, ensuring efficient operations and meeting user needs. The main objective of this node is to simplify the loading of images within the ComfyUI framework in order to perform further operations or analyses.

# Input types
## Required
- input_folder
    - The input_folder parameter specifies the directory that contains the image to be loaded. It plays a key role in determining the range of images that the node will operate in, thus directly influencing the execution of the node and the list of images that you generate.
    - Comfy dtype: STRING
    - Python dtype: str
- start_index
    - Start_index parameters indicate the location of the sorted image list from which the image will start to be loaded. It is essential to control the image subsets to be processed and allows accurate operation of the image sequence.
    - Comfy dtype: INT
    - Python dtype: int
- max_images
    - The max_images parameter setting node will be the maximum number of images to be loaded from the specified start_index. It is a key parameter to limit the size of the image list and to ensure that node operational targeting and resource management are optimized.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- input_path
    - The optional input_path parameter allows the user to specify a custom path to the image directory to overwrite the default input directory. This provides flexibility in selecting the image list source and can be used to integrate images from different locations.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- IMAGE
    - The IMAGE output, which provides loaded image data, can be further processed or analysed within the ComfyUI framework. It represents the main output of the CR_LoadImageList node and reflects the core function of loading and preparing the image.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- show_help
    - Show_help output provides a URL link to the document page for further guidance and help. It is a useful resource for users seeking more information on how to use nodes effectively.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_LoadImageList:

    @classmethod
    def INPUT_TYPES(s):
        input_dir = folder_paths.input_directory
        image_folder = [name for name in os.listdir(input_dir) if os.path.isdir(os.path.join(input_dir, name))]
        return {'required': {'input_folder': (sorted(image_folder),), 'start_index': ('INT', {'default': 0, 'min': 0, 'max': 9999}), 'max_images': ('INT', {'default': 1, 'min': 1, 'max': 9999})}, 'optional': {'input_path': ('STRING', {'default': '', 'multiline': False})}}
    RETURN_TYPES = ('IMAGE', 'STRING')
    RETURN_NAMES = ('IMAGE', 'show_help')
    OUTPUT_IS_LIST = (True, False)
    FUNCTION = 'make_list'
    CATEGORY = icons.get('Comfyroll/List/IO')

    def make_list(self, start_index, max_images, input_folder, input_path=None):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/List-Nodes#cr-image-list'
        if input_path != '' and input_path is not None:
            if not os.path.exists(input_path):
                print(f'[Warning] CR Image List: The input_path `{input_path}` does not exist')
                return ('',)
            in_path = input_path
        else:
            input_dir = folder_paths.input_directory
            in_path = os.path.join(input_dir, input_folder)
        if not os.listdir(in_path):
            print(f'[Warning] CR Image List: The folder `{in_path}` is empty')
            return None
        file_list = sorted(os.listdir(in_path), key=lambda s: sum(((s, int(n)) for (s, n) in re.findall('(\\D+)(\\d+)', 'a%s0' % s)), ()))
        image_list = []
        start_index = max(0, min(start_index, len(file_list) - 1))
        end_index = min(start_index + max_images, len(file_list) - 1)
        for num in range(start_index, end_index):
            img = Image.open(os.path.join(in_path, file_list[num]))
            image = img.convert('RGB')
            image_list.append(pil2tensor(image))
        if not image_list:
            print('CR Load Image List: No images found.')
            return None
        images = torch.cat(image_list, dim=0)
        images_out = [images[i:i + 1, ...] for i in range(images.shape[0])]
        return (images_out, show_help)
```