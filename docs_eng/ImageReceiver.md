# Documentation
- Class name: ImageReceiver
- Category: ImpactPack/Util
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The ImageReceiver node is designed to process and receive image data and to provide decoding, conversion and preparation of image data for further analysis or processing in workflows. It emphasizes the processing of different image formats and ensures that image data are correctly converted to formats suitable for downstream tasks.

# Input types
## Required
- image
    - The 'image'parameter is essential for the node because it specifies the source of the image data. It can be a file path or a reference to the image stored elsewhere. This parameter directly affects the ability of the node to retrieve and process the image.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- link_id
    - The 'link_id'parameter is used as an identifier to link or associate image data with other elements in the workflow. Its values range from zero to maximum integer values, providing flexibility in how to link or refer to the image.
    - Comfy dtype: INT
    - Python dtype: int
- save_to_workflow
    - The'save_to_workflow' parameter determines whether image data should be saved as part of the workflow for future use. This is very useful for sustaining data at different stages of the workflow without having to be reprocessed.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- image_data
    - The 'image_data'parameter contains coded image data, which are decoded and processed by nodes. It should be a string that represents base64 coded image contents and then converts them to available image formats.
    - Comfy dtype: STRING
    - Python dtype: str
- trigger_always
    - The 'trigger_always' parameter is a boolean symbol that, when set to True, means that node should process the image unconditionally. This can be used to ensure that the image is always processed, even if other parameters indicate that it may not need to be processed.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- IMAGE
    - The 'IMAGE' output provides image data processed in volume format for further analysis or processing in workflows. It represents the main output of the ImageReceiver node after the image data has been successfully decoded and converted.
    - Comfy dtype: TENSOR
    - Python dtype: torch.Tensor
- MASK
    - The MASK output is an optional volume, representing a mask derived from image data. It can be used to divide or identify specific areas of interest in the image.
    - Comfy dtype: TENSOR
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class ImageReceiver:

    @classmethod
    def INPUT_TYPES(s):
        input_dir = folder_paths.get_input_directory()
        files = [f for f in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, f))]
        return {'required': {'image': (sorted(files),), 'link_id': ('INT', {'default': 0, 'min': 0, 'max': sys.maxsize, 'step': 1}), 'save_to_workflow': ('BOOLEAN', {'default': False}), 'image_data': ('STRING', {'multiline': False}), 'trigger_always': ('BOOLEAN', {'default': False, 'label_on': 'enable', 'label_off': 'disable'})}}
    FUNCTION = 'doit'
    RETURN_TYPES = ('IMAGE', 'MASK')
    CATEGORY = 'ImpactPack/Util'

    def doit(self, image, link_id, save_to_workflow, image_data, trigger_always):
        if save_to_workflow:
            try:
                image_data = base64.b64decode(image_data.split(',')[1])
                i = Image.open(BytesIO(image_data))
                i = ImageOps.exif_transpose(i)
                image = i.convert('RGB')
                image = np.array(image).astype(np.float32) / 255.0
                image = torch.from_numpy(image)[None,]
                if 'A' in i.getbands():
                    mask = np.array(i.getchannel('A')).astype(np.float32) / 255.0
                    mask = 1.0 - torch.from_numpy(mask)
                else:
                    mask = torch.zeros((64, 64), dtype=torch.float32, device='cpu')
                return (image, mask.unsqueeze(0))
            except Exception as e:
                print(f"[WARN] ComfyUI-Impact-Pack: ImageReceiver - invalid 'image_data'")
                mask = torch.zeros((64, 64), dtype=torch.float32, device='cpu')
                return (empty_pil_tensor(64, 64), mask)
        else:
            return nodes.LoadImage().load_image(image)

    @classmethod
    def VALIDATE_INPUTS(s, image, link_id, save_to_workflow, image_data, trigger_always):
        if image != '#DATA' and (not folder_paths.exists_annotated_filepath(image)) or image.startswith('/') or '..' in image:
            return 'Invalid image file: {}'.format(image)
        return True

    @classmethod
    def IS_CHANGED(s, image, link_id, save_to_workflow, image_data, trigger_always):
        if trigger_always:
            return float('NaN')
        elif save_to_workflow:
            return hash(image_data)
        else:
            return hash(image)
```