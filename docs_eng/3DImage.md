# Documentation
- Class name: Image3D
- Category: ♾️Mixlab/Image
- Output node: True
- Repo Ref: https://github.com/shadowcz007/comfyui-mixlab-nodes.git

The Image3D node is designed to process and operate 3D images. It accepts a base64-coded image and optional material as input and converts them into a volume format suitable for further processing by the deep learning model. The node also processes the extraction of masks and background images, providing a comprehensive set of image operations.

# Input types
## Required
- upload
    - The `upload' parameter is essential for node because it contains image data and optional materials coded as Base64. It is essential for node implementation because it provides the main input for image operations.
    - Comfy dtype: Dict[str, str]
    - Python dtype: Dict[str, Union[str, torch.Tensor]]
- material
    - The `material' parameter is optional and allows for the inclusion of additional image data that can be used to enhance the main image processing process. It increases the flexibility of node functions by enabling the use of additional visual elements.
    - Comfy dtype: IMAGE
    - Python dtype: Optional[torch.Tensor]

# Output types
- IMAGE
    - The `IMAGE' output represents 3D images processed in volume form, which can be used for downstream tasks such as machine learning or computer visual applications.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- MASK
    - The `MASK' output provides a binary mask derived from the input image that can be used to divide or other image analysis tasks.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- BG_IMAGE
    - The `BG_IMAGE' output is an optional background image that complements the main image and enhances the context for some applications.
    - Comfy dtype: IMAGE
    - Python dtype: Optional[torch.Tensor]
- MATERIAL
    - The `MATERIAL' output is a processed material image that, together with the main image, can be used for more complex image processing tasks.
    - Comfy dtype: IMAGE
    - Python dtype: Optional[torch.Tensor]

# Usage tips
- Infra type: CPU

# Source code
```
class Image3D:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'upload': ('THREED',)}, 'optional': {'material': ('IMAGE',)}}
    RETURN_TYPES = ('IMAGE', 'MASK', 'IMAGE', 'IMAGE')
    RETURN_NAMES = ('IMAGE', 'MASK', 'BG_IMAGE', 'MATERIAL')
    FUNCTION = 'run'
    CATEGORY = '♾️Mixlab/Image'
    INPUT_IS_LIST = False
    OUTPUT_IS_LIST = (False, False, False, False)
    OUTPUT_NODE = True

    def run(self, upload, material=None):
        image = base64_to_image(upload['image'])
        mat = None
        if 'material' in upload and upload['material']:
            mat = base64_to_image(upload['material'])
            mat = mat.convert('RGB')
            mat = pil2tensor(mat)
        mask = image.split()[3]
        image = image.convert('RGB')
        mask = mask.convert('L')
        bg_image = None
        if 'bg_image' in upload and upload['bg_image']:
            bg_image = base64_to_image(upload['bg_image'])
            bg_image = bg_image.convert('RGB')
            bg_image = pil2tensor(bg_image)
        mask = pil2tensor(mask)
        image = pil2tensor(image)
        m = []
        if not material is None:
            m = create_temp_file(material[0])
        return {'ui': {'material': m}, 'result': (image, mask, bg_image, mat)}
```