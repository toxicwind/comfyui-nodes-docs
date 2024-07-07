# Documentation
- Class name: BatchCropImage
- Category: Mikey/Image
- Output node: False
- Repo Ref: https://github.com/bash-j/mikey_nodes

The `batch'method of the CatchCropImage node is designed to process images in a directory and to keep the width ratio by cutting each image to a specified size. It can process various image formats and convert the cropped image to a volume format suitable for further processing.

# Input types
## Required
- image_directory
    - Parameter `image_directory'specifies the path to the directory containing the image to be cropped. This is a key parameter, as node execution depends on the existence and accessibility of the directory.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- crop_amount
    - The parameter `crop_amount'determines the proportion of the image to be cropped. It is important because it directly affects the size of the image as a result and influences subsequent analysis or processing.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- image
    - Output `image'consists of a list of cropped images converted to volume format. This output is important because it represents processed data ready for downstream tasks, such as machine learning or image analysis.
    - Comfy dtype: IMAGE
    - Python dtype: List[torch.Tensor]

# Usage tips
- Infra type: CPU

# Source code
```
class BatchCropImage:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image_directory': ('STRING', {'multiline': False, 'placeholder': 'Image Directory'}), 'crop_amount': ('FLOAT', {'default': 0.05})}}
    RETURN_TYPES = ('IMAGE',)
    RETURN_NAMES = ('image',)
    FUNCTION = 'batch'
    CATEGORY = 'Mikey/Image'
    OUTPUT_IS_LIST = (True,)

    def batch(self, image_directory, crop_amount):
        if not os.path.exists(image_directory):
            raise Exception(f'Image directory {image_directory} does not exist')
        images = []
        for file in os.listdir(image_directory):
            if file.endswith('.png') or file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.webp') or file.endswith('.bmp') or file.endswith('.gif'):
                img = Image.open(os.path.join(image_directory, file))
                (width, height) = img.size
                pixels = int(width * crop_amount) // 8 * 8
                left = pixels
                upper = pixels
                right = width - pixels
                lower = height - pixels
                cropped_img = img.crop((left, upper, right, lower))
                img = pil2tensor(cropped_img)
                images.append(img)
        return (images,)
```