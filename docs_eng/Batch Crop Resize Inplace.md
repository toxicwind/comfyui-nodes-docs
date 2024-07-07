# Documentation
- Class name: BatchCropResizeInplace
- Category: Mikey/Image
- Output node: False
- Repo Ref: https://github.com/bash-j/mikey_nodes

The CatchCropResizeInplace node is designed to process a group of image files by applying tailoring, resizing, and upsampling operations. It efficiently processes image conversions in the directory, provides a flow-lined method to enhance image quality and dimensions, while choosing to replace the original file.

# Input types
## Required
- image_directory
    - Image_directory parameters specify the path to the directory containing the image files that you need to process.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- subdirectories
    - The subdirectories parameters determine whether to include the image files in the specified image_directory subdirectories. This affects the range of batch processing.
    - Comfy dtype: COMBO[true, false]
    - Python dtype: str
- replace_original
    - Replace_original parameters indicate whether the original image file should be replaced with a processed image. This has important implications for the permanent nature of the changes made.
    - Comfy dtype: COMBO[true, false]
    - Python dtype: str
- replace_suffix
    - Replace_suffix parameters define the suffix that is attached to the image filename when the processed image does not replace the original file. This is important for distinguishing the original image from the processed image.
    - Comfy dtype: STRING
    - Python dtype: str
- upscale_method
    - Upscale_method parameters select the algorithm used to magnify the image. The choice of method significantly affects the mass of the magnified image.
    - Comfy dtype: COMBO[nearest-exact, bilinear, area, bicubic]
    - Python dtype: str
- crop
    - The crop parameter determines the method of cropping that you want to apply to the image. It can disable cropping or cropping according to the designated crop_amount application centre.
    - Comfy dtype: COMBO[disabled, center]
    - Python dtype: str
- crop_amount
    - Crop_amount parameters specify the proportion of images that you want to crop from each side. It is a key factor in controlling the scope of the crop operation.
    - Comfy dtype: FLOAT
    - Python dtype: float
- prompt
    - The prompt parameter is used for additional instructions or context that may be required for certain image processing tasks. It can influence how nodes interpret and process images.
    - Comfy dtype: STRING
    - Python dtype: str
- extra_pnginfo
    - Extra_pnginfo parameters provide additional information that can be used to customize the PNG image processing process. It is particularly useful when specific metadata or attributes need to be considered.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- job_done
    - Job_done parameters represent the completion of batch processing and provide a summary of the number of images processed.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class BatchCropResizeInplace:
    crop_methods = ['disabled', 'center']
    upscale_methods = ['nearest-exact', 'bilinear', 'area', 'bicubic']

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image_directory': ('STRING', {'multiline': False, 'placeholder': 'Image Directory'}), 'subdirectories': (['true', 'false'], {'default': 'false'}), 'replace_original': (['true', 'false'], {'default': 'false'}), 'replace_suffix': ('STRING', {'default': '_cropped_resized'}), 'upscale_method': (s.upscale_methods,), 'crop': (s.crop_methods,), 'crop_amount': ('FLOAT', {'default': 0.05})}, 'hidden': {'prompt': 'PROMPT', 'extra_pnginfo': 'EXTRA_PNGINFO'}}
    RETURN_TYPES = ('STRING',)
    RETURN_NAMES = ('job_done',)
    FUNCTION = 'batch'
    CATEGORY = 'Mikey/Image'

    def crop(self, image, crop_amount):
        (width, height) = image.size
        pixels = int(width * crop_amount) // 8 * 8
        left = pixels
        upper = pixels
        right = width - pixels
        lower = height - pixels
        cropped_img = image.crop((left, upper, right, lower))
        return cropped_img

    def upscale(self, image, upscale_method, width, height, crop):
        samples = image.movedim(-1, 1)
        s = comfy.utils.common_upscale(samples, width, height, upscale_method, crop)
        s = s.movedim(1, -1)
        return (s,)

    def resize(self, image, upscale_method, crop):
        image = pil2tensor(image)
        (w, h) = find_latent_size(image.shape[2], image.shape[1])
        img = self.upscale(image, upscale_method, w, h, crop)[0]
        img = tensor2pil(img)
        return img

    def get_files_from_directory(self, image_directory, subdirectories):
        if subdirectories == 'true':
            files = [os.path.join(root, name) for (root, dirs, files) in os.walk(image_directory) for name in files if name.endswith(('.png', '.jpg', '.jpeg', '.webp', '.bmp', '.gif'))]
        else:
            files = [os.path.join(image_directory, f) for f in os.listdir(image_directory) if os.path.isfile(os.path.join(image_directory, f)) and f.endswith(('.png', '.jpg', '.jpeg', '.webp', '.bmp', '.gif'))]
        return files

    def batch(self, image_directory, subdirectories, replace_original, replace_suffix, upscale_method, crop, crop_amount, prompt, extra_pnginfo):
        if not os.path.exists(image_directory):
            raise Exception(f'Image directory {image_directory} does not exist')
        files = self.get_files_from_directory(image_directory, subdirectories)
        for file in tqdm(files, desc='Processing images'):
            img = Image.open(file)
            if crop != 'disabled':
                img = self.crop(img, crop_amount)
            img = self.resize(img, upscale_method, crop)
            if replace_original == 'true':
                img.save(file)
            else:
                replace_suffix = search_and_replace(replace_suffix, extra_pnginfo, prompt)
                (filename, file_extension) = os.path.splitext(file)
                img.save(filename + replace_suffix + file_extension)
        return (f'Job done, {len(files)} images processed',)
```