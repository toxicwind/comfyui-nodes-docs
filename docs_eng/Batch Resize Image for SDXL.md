# Documentation
- Class name: BatchResizeImageSDXL
- Category: Mikey/Image
- Output node: False
- Repo Ref: https://github.com/bash-j/mikey_nodes

The MatchResizeImageSDXL node is designed to process images according to the specified array of parameters and optimize them by resizing them. It supports a variety of cropping and magnification methods to ensure that images can be adjusted accurately and efficiently. This node is particularly suitable for preparing image data sets for further processing or presentation.

# Input types
## Required
- image_directory
    - The image_directory parameter specifies the location of the image storage that you want to resize. This is essential for node positioning and accessing images.
    - Comfy dtype: STRING
    - Python dtype: str
- upscale_method
    - The upperscale_method parameter determines the algorithm to be used to magnify the image. It has a significant impact on the quality and appearance of the adjusted image.
    - Comfy dtype: COMBO['nearest-exact', 'bilinear', 'area', 'bicubic']
    - Python dtype: str
- crop
    - Crop parameters indicate whether and how to crop the image after resizeing. This may be important to maintain a wide ratio or to focus on specific parts of the image.
    - Comfy dtype: COMBO['disabled', 'center']
    - Python dtype: str

# Output types
- image
    - MatchResizeImageSDXL node output is an adjusted list of images. Each image is processed according to input parameters to prepare it for the next phase of application or analysis.
    - Comfy dtype: IMAGE
    - Python dtype: List[torch.Tensor]

# Usage tips
- Infra type: CPU

# Source code
```
class BatchResizeImageSDXL(ResizeImageSDXL):
    crop_methods = ['disabled', 'center']
    upscale_methods = ['nearest-exact', 'bilinear', 'area', 'bicubic']

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image_directory': ('STRING', {'multiline': False, 'placeholder': 'Image Directory'}), 'upscale_method': (s.upscale_methods,), 'crop': (s.crop_methods,)}}
    RETURN_TYPES = ('IMAGE',)
    RETURN_NAMES = ('image',)
    FUNCTION = 'batch'
    CATEGORY = 'Mikey/Image'
    OUTPUT_IS_LIST = (True,)

    def batch(self, image_directory, upscale_method, crop):
        if not os.path.exists(image_directory):
            raise Exception(f'Image directory {image_directory} does not exist')
        images = []
        for file in os.listdir(image_directory):
            if file.endswith('.png') or file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.webp') or file.endswith('.bmp') or file.endswith('.gif'):
                img = Image.open(os.path.join(image_directory, file))
                img = pil2tensor(img)
                img = self.resize(img, upscale_method, crop)[0]
                images.append(img)
        return (images,)
```