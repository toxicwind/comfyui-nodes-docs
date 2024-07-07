# Documentation
- Class name: WAS_Image_History
- Category: WAS Suite/History
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Image_History node is designed to manage and retrieve historical images stored in the WASDatabase. It provides access to and displays of images in historical records and ensures that users can view past image status or data.

# Input types
## Required
- image
    - The 'image'parameter is essential to specify the historical image that the user wants to access. Node uses it to locate and retrieve the correct image from the database.
    - Comfy dtype: str
    - Python dtype: str

# Output types
- image
    - The 'image'output parameter represents a historical image retrieved in volume format and is suitable for further processing or display purposes.
    - Comfy dtype: COMBO[str, torch.Tensor]
    - Python dtype: Union[str, torch.Tensor]
- filename_text
    - The 'filename_text' output parameter provides the filename of the image retrieved, which is very useful for recording, referencing or additional metadata purposes.
    - Comfy dtype: str
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Image_History:

    def __init__(self):
        self.HDB = WASDatabase(WAS_HISTORY_DATABASE)
        self.conf = getSuiteConfig()

    @classmethod
    def INPUT_TYPES(cls):
        HDB = WASDatabase(WAS_HISTORY_DATABASE)
        conf = getSuiteConfig()
        paths = ['No History']
        if HDB.catExists('History') and HDB.keyExists('History', 'Images'):
            history_paths = HDB.get('History', 'Images')
            if conf.__contains__('history_display_limit'):
                history_paths = history_paths[-conf['history_display_limit']:]
                paths = []
            for path_ in history_paths:
                paths.append(os.path.join('...' + os.sep + os.path.basename(os.path.dirname(path_)), os.path.basename(path_)))
        return {'required': {'image': (paths,)}}
    RETURN_TYPES = ('IMAGE', TEXT_TYPE)
    RETURN_NAMES = ('image', 'filename_text')
    FUNCTION = 'image_history'
    CATEGORY = 'WAS Suite/History'

    def image_history(self, image):
        self.HDB = WASDatabase(WAS_HISTORY_DATABASE)
        paths = {}
        if self.HDB.catExists('History') and self.HDB.keyExists('History', 'Images'):
            history_paths = self.HDB.get('History', 'Images')
            for path_ in history_paths:
                paths.update({os.path.join('...' + os.sep + os.path.basename(os.path.dirname(path_)), os.path.basename(path_)): path_})
        if os.path.exists(paths[image]) and paths.__contains__(image):
            return (pil2tensor(Image.open(paths[image]).convert('RGB')), os.path.basename(paths[image]))
        else:
            cstr(f'The image `{image}` does not exist!').error.print()
            return (pil2tensor(Image.new('RGB', (512, 512), (0, 0, 0, 0))), 'null')

    @classmethod
    def IS_CHANGED(cls, **kwargs):
        return float('NaN')
```