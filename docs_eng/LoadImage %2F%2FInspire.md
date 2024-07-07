# Documentation
- Class name: LoadImageInspire
- Category: InspirePack/image
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Inspire-Pack.git

This node facilitates loading and pre-processing of images and converts them to formats suitable for further analysis and operation. It emphasizes the transformation of raw image data into structured arrays to prepare for downstream tasks such as feature extraction or image classification.

# Input types
## Required
- image
    - The image parameter is essential because it specifies the source image that will be processed. Its selection affects the quality and applicability of the result image data.
    - Comfy dtype: COMBO[sorted(files) + ['#DATA']]
    - Python dtype: PIL.Image
## Optional
- image_data
    - This parameter, which contains coded image data, is essential for node execution of its main function — image loading and conversion.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- image
    - The output image is an input conversion and structural expression and is prepared for further analysis or processing within the system.
    - Comfy dtype: torch.Tensor
    - Python dtype: torch.Tensor
- mask
    - The mask output provides a binary expression that can be used in a variety of image-related operations and enhances the multifunctionality of node applications.
    - Comfy dtype: torch.Tensor
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class LoadImageInspire:

    @classmethod
    def INPUT_TYPES(s):
        input_dir = folder_paths.get_input_directory()
        files = [f for f in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, f))]
        return {'required': {'image': (sorted(files) + ['#DATA'], {'image_upload': True}), 'image_data': ('STRING', {'multiline': False})}}
    CATEGORY = 'InspirePack/image'
    RETURN_TYPES = ('IMAGE', 'MASK')
    FUNCTION = 'load_image'

    def load_image(self, image, image_data):
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
```