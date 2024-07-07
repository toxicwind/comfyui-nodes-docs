# Documentation
- Class name: ChangeImageBatchSize
- Category: InspirePack/image
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Inspire-Pack.git

This node is intended to adjust the volume size of the given image set to ensure that the output meets the specified batch size requirements. It does so by copying the last image to fill the batch or to cut the batch as necessary, depending on the input. This node is essential for pre-processing image data to meet input requirements for subsequent processing steps.

# Input types
## Required
- image
    - Image parameters represent a group of images that need to be resized or adjusted to meet the size of a given batch. This is a key input, because the entire operation of the node revolves around the manipulation of the image data to achieve the desired output batch size.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- batch_size
    - Batch size parameters specify the number of images expected in the output batch. This is a key factor that determines the treatment of the input image, whether by copying or cutting, to the specified size.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- mode
    - The mode parameters determine the method used to resize the batch. In this case, the'simple' mode is the only supported option that outlines the process by which the volume size requirement is met by copying the last image or intercepting a batch.
    - Comfy dtype: COMBO[simple]
    - Python dtype: str

# Output types
- image
    - Output image parameters are the result of a batch size adjustment process. It contains an adjusted set of images that now corresponds to the specified batch size and is prepared for further processing or analysis.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class ChangeImageBatchSize:

    @classmethod
    def INPUT_TYPES(s):
        input_dir = folder_paths.get_input_directory()
        files = [f for f in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, f))]
        return {'required': {'image': ('IMAGE',), 'batch_size': ('INT', {'default': 1, 'min': 1, 'max': 4096, 'step': 1}), 'mode': (['simple'],)}}
    CATEGORY = 'InspirePack/image'
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'load_image'

    def load_image(self, image, batch_size, mode):
        if mode == 'simple':
            if len(image) < batch_size:
                last_frame = image[-1].unsqueeze(0).expand(batch_size - len(image), -1, -1, -1)
                image = torch.concat((image, last_frame), dim=0)
            else:
                image = image[:batch_size, :, :, :]
            return (image,)
        else:
            print(f'[WARN] ChangeImageBatchSize: Unknown mode `{mode}` - ignored')
            return (image,)
```