# Documentation
- Class name: LoadImageMask
- Category: mask
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The LoadImageMask node is designed to load and process image files, with particular attention to extracting a particular colour channel or alpha channel to create a mask. It can handle various image formats and ensure that the output is a standardized mask load for further processing of downstream tasks.

# Input types
## Required
- image
    - The image parameter is essential for the LoadImage Mask node because it specifies the image file to be loaded. This input directly affects the operation of the node and determines the source of the mask data.
    - Comfy dtype: str
    - Python dtype: str
- channel
    - Channel parameters indicate the colour channel in which the image is used to generate the mask. It plays a key role in the function of the node by defining the particular channel to be extracted and processed.
    - Comfy dtype: str
    - Python dtype: str

# Output types
- MASK
    - The MASK output at the LoadImage Mask node represents a shield from the specified image and channel. It is a standardized load that can be used immediately for follow-up operations.
    - Comfy dtype: torch.Tensor
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class LoadImageMask:
    _color_channels = ['alpha', 'red', 'green', 'blue']

    @classmethod
    def INPUT_TYPES(s):
        input_dir = folder_paths.get_input_directory()
        files = [f for f in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, f))]
        return {'required': {'image': (sorted(files), {'image_upload': True}), 'channel': (s._color_channels,)}}
    CATEGORY = 'mask'
    RETURN_TYPES = ('MASK',)
    FUNCTION = 'load_image'

    def load_image(self, image, channel):
        image_path = folder_paths.get_annotated_filepath(image)
        i = Image.open(image_path)
        i = ImageOps.exif_transpose(i)
        if i.getbands() != ('R', 'G', 'B', 'A'):
            if i.mode == 'I':
                i = i.point(lambda i: i * (1 / 255))
            i = i.convert('RGBA')
        mask = None
        c = channel[0].upper()
        if c in i.getbands():
            mask = np.array(i.getchannel(c)).astype(np.float32) / 255.0
            mask = torch.from_numpy(mask)
            if c == 'A':
                mask = 1.0 - mask
        else:
            mask = torch.zeros((64, 64), dtype=torch.float32, device='cpu')
        return (mask.unsqueeze(0),)

    @classmethod
    def IS_CHANGED(s, image, channel):
        image_path = folder_paths.get_annotated_filepath(image)
        m = hashlib.sha256()
        with open(image_path, 'rb') as f:
            m.update(f.read())
        return m.digest().hex()

    @classmethod
    def VALIDATE_INPUTS(s, image):
        if not folder_paths.exists_annotated_filepath(image):
            return 'Invalid image file: {}'.format(image)
        return True
```