# Documentation
- Class name: LoadImagePathWithMetadata
- Category: image
- Output node: False
- Repo Ref: https://github.com/Jordach/comfy-plasma.git

LoadImagePathWest Metadata node is designed to load image files and their associated metadata. It handles local and remote image paths, extracts tips and negative hints from various image formats, and returns image data arrays, masks, hints, negative hints, width and height.

# Input types
## Required
- image
    - The 'image'parameter is the path of the image file that you want to process. This is a key input, because the function of the node revolves around loading and operating image data from this path. Images can be local file paths or URLs of remote images.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- image
    - The 'image'output is a processed version of the input image, converted to a format suitable for further analysis or operation. It is a key component of node output and provides the necessary visual data for downstream tasks.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- mask
    - If available, the'mask' output is a alpha channel extracted from the image, which can be used for partition purposes. It represents transparency information about the image, especially for applications that need to be isolated from the background.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor
- prompt
    - The 'prompt' output contains any active or creative instructions embedded in image metadata. This information can be used to guide subsequent image processing or generation tasks and to provide context for the intended use of the image.
    - Comfy dtype: STRING
    - Python dtype: str
- negative
    - The `negative' output includes any instructions designed to guide you away from certain image features or attributes. This is particularly useful for fine-tuning the output of the algorithm for image generation by specifying what should be avoided.
    - Comfy dtype: STRING
    - Python dtype: str
- width
    - The `width' output provides the width of the loaded image in pixels, which is the basic information on the size and vertical ratio of the image.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - The 'height' output gives the height of the image loaded in pixels and complements the width in order to obtain a full picture of the size of the image.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class LoadImagePathWithMetadata:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('STRING', {'default': ''})}}
    CATEGORY = 'image'
    RETURN_TYPES = ('IMAGE', 'MASK', 'STRING', 'STRING', 'INT', 'INT')
    RETURN_NAMES = ('image', 'mask', 'PROMPT', 'NEGATIVE', 'WIDTH', 'HEIGHT')
    FUNCTION = 'load_image'

    def load_image(self, image):
        image_path = str(image)
        image_path = image_path.replace('"', '')
        i = None
        if image_path.startswith('http'):
            response = requests.get(image_path)
            i = Image.open(BytesIO(response.content)).convert('RGB')
        else:
            i = Image.open(image_path)
        prompt = ''
        negative = ''
        width = i.width
        height = i.height
        if i.format == 'PNG':
            if 'parameters' in i.info:
                params = i.info.get('parameters')
                (prompt, negative) = handle_auto1111(params)
            elif 'negative_prompt' in i.info or 'Negative Prompt' in i.info:
                params = str(i.info).replace("'", '"')
                (prompt, negative) = handle_ezdiff(params)
            elif 'sd-metadata' in i.info:
                (prompt, negative) = handle_invoke_modern(i.info)
            elif 'Dream' in i.info:
                (prompt, negative) = handle_invoke_legacy(i.info)
            elif i.info.get('Software') == 'NovelAI':
                (prompt, negative) = handle_novelai(i.info)
            elif 'XML:com.adobe.xmp' in i.info:
                (prompt, negative) = handle_drawthings(i.info)
        i = ImageOps.exif_transpose(i)
        image = i.convert('RGB')
        image = np.array(image).astype(np.float32) / 255.0
        image = torch.from_numpy(image)[None,]
        if 'A' in i.getbands():
            mask = np.array(i.getchannel('A')).astype(np.float32) / 255.0
            mask = 1.0 - torch.from_numpy(mask)
        else:
            mask = torch.zeros((64, 64), dtype=torch.float32, device='cpu')
        return (image, mask, prompt, negative, width, height)

    @classmethod
    def IS_CHANGED(s, image):
        image_path = str(image)
        image_path = image_path.replace('"', '')
        m = hashlib.sha256()
        if not image_path.startswith('http'):
            with open(image_path, 'rb') as f:
                m.update(f.read())
            return m.digest().hex()
        else:
            m.update(image.encode('utf-8'))
            return m.digest().hex()

    @classmethod
    def VALIDATE_INPUTS(s, image):
        image_path = str(image)
        image_path = image_path.replace('"', '')
        if image_path.startswith('http'):
            return True
        if not os.path.isfile(image_path):
            return 'No file found: {}'.format(image_path)
        return True
```