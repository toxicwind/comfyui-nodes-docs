# Documentation
- Class name: WAS_Load_Image
- Category: WAS Suite/IO
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

WAS_Load_Image nodes are designed to load and process images from specified paths or URLs efficiently. It processes images to the required formatting and provides additional functions such as creating a mask from the alpha channel and extracting a filename.

# Input types
## Required
- image_path
    - The image_path parameter is essential because it determines the origin of the image to be loaded. It can be a local file path or an online image URL. This parameter directly affects the ability of nodes to access and process image data.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- RGBA
    - The RGBA parameter specifies whether you should load an image with a alpha channel. This affects the transparency of the image and may be important for some image processing tasks.
    - Comfy dtype: ['false', 'true']
    - Python dtype: str
- filename_text_extension
    - The filename_text_extension parameter decides whether to include file extensions in the file name text. This may be important for downstream processes that require a specific name agreement.
    - Comfy dtype: ['true', 'false']
    - Python dtype: str

# Output types
- image
    - Image output provides the image data that is loaded and processed. It is the basis for any subsequent image analysis or operational task.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- mask
    - The alpha channel (if any) where the mask output originates from the image is used to distinguish between transparent areas in the image.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor
- filename_text
    - The filename_text output is a text expression for the image filename. It can be used for recording, displaying or other text-based operations.
    - Comfy dtype: TEXT_TYPE
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Load_Image:

    def __init__(self):
        self.input_dir = comfy_paths.input_directory
        self.HDB = WASDatabase(WAS_HISTORY_DATABASE)

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'image_path': ('STRING', {'default': './ComfyUI/input/example.png', 'multiline': False}), 'RGBA': (['false', 'true'],)}, 'optional': {'filename_text_extension': (['true', 'false'],)}}
    RETURN_TYPES = ('IMAGE', 'MASK', TEXT_TYPE)
    RETURN_NAMES = ('image', 'mask', 'filename_text')
    FUNCTION = 'load_image'
    CATEGORY = 'WAS Suite/IO'

    def load_image(self, image_path, RGBA='false', filename_text_extension='true'):
        RGBA = RGBA == 'true'
        if image_path.startswith('http'):
            from io import BytesIO
            i = self.download_image(image_path)
        else:
            try:
                i = Image.open(image_path)
            except OSError:
                cstr(f"The image `{image_path.strip()}` specified doesn't exist!").error.print()
                i = Image.new(mode='RGB', size=(512, 512), color=(0, 0, 0))
        if not i:
            return
        update_history_images(image_path)
        image = i
        if not RGBA:
            image = image.convert('RGB')
        image = np.array(image).astype(np.float32) / 255.0
        image = torch.from_numpy(image)[None,]
        if 'A' in i.getbands():
            mask = np.array(i.getchannel('A')).astype(np.float32) / 255.0
            mask = 1.0 - torch.from_numpy(mask)
        else:
            mask = torch.zeros((64, 64), dtype=torch.float32, device='cpu')
        if filename_text_extension == 'true':
            filename = os.path.basename(image_path)
        else:
            filename = os.path.splitext(os.path.basename(image_path))[0]
        return (image, mask, filename)

    def download_image(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            img = Image.open(BytesIO(response.content))
            return img
        except requests.exceptions.HTTPError as errh:
            cstr(f'HTTP Error: ({url}): {errh}').error.print()
        except requests.exceptions.ConnectionError as errc:
            cstr(f'Connection Error: ({url}): {errc}').error.print()
        except requests.exceptions.Timeout as errt:
            cstr(f'Timeout Error: ({url}): {errt}').error.print()
        except requests.exceptions.RequestException as err:
            cstr(f'Request Exception: ({url}): {err}').error.print()

    @classmethod
    def IS_CHANGED(cls, image_path):
        if image_path.startswith('http'):
            return float('NaN')
        m = hashlib.sha256()
        with open(image_path, 'rb') as f:
            m.update(f.read())
        return m.digest().hex()
```