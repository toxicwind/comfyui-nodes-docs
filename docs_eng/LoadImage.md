# Documentation
- Class name: LoadImage
- Category: image
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The LoadImage node is designed to take image files from the specified directory, process them, and output the image and its corresponding mask. It can process the image sequence and convert it into a format suitable for further processing, emphasizing its role in preparing data for the image-related task.

# Input types
## Required
- image
    - The 'image'parameter is the path of the image file that you want to process. It is essential for the operation of the node because it determines the particular image that you want to load and operate.
    - Comfy dtype: str
    - Python dtype: str

# Output types
- IMAGE
    - The 'IMAGE' output, which represents the volume of processed image data, has been converted to floating point format and has been normalized. This output is important because it is the main data structure used for follow-up image analysis or operational tasks.
    - Comfy dtype: torch.Tensor
    - Python dtype: torch.Tensor
- MASK
    - The `MASK' output is a volume of binary masks associated with the image to distinguish between different areas or objects in the image. It is essential for tasks that need to be split or identified by the object.
    - Comfy dtype: torch.Tensor
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class LoadImage:

    @classmethod
    def INPUT_TYPES(s):
        input_dir = folder_paths.get_input_directory()
        files = [f for f in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, f))]
        return {'required': {'image': (sorted(files), {'image_upload': True})}}
    CATEGORY = 'image'
    RETURN_TYPES = ('IMAGE', 'MASK')
    FUNCTION = 'load_image'

    def load_image(self, image):
        image_path = folder_paths.get_annotated_filepath(image)
        img = Image.open(image_path)
        output_images = []
        output_masks = []
        for i in ImageSequence.Iterator(img):
            i = ImageOps.exif_transpose(i)
            if i.mode == 'I':
                i = i.point(lambda i: i * (1 / 255))
            image = i.convert('RGB')
            image = np.array(image).astype(np.float32) / 255.0
            image = torch.from_numpy(image)[None,]
            if 'A' in i.getbands():
                mask = np.array(i.getchannel('A')).astype(np.float32) / 255.0
                mask = 1.0 - torch.from_numpy(mask)
            else:
                mask = torch.zeros((64, 64), dtype=torch.float32, device='cpu')
            output_images.append(image)
            output_masks.append(mask.unsqueeze(0))
        if len(output_images) > 1:
            output_image = torch.cat(output_images, dim=0)
            output_mask = torch.cat(output_masks, dim=0)
        else:
            output_image = output_images[0]
            output_mask = output_masks[0]
        return (output_image, output_mask)

    @classmethod
    def IS_CHANGED(s, image):
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