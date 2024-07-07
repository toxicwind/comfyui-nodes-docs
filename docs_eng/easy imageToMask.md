# Documentation
- Class name: imageToMask
- Category: EasyUse/Image
- Output node: False
- Repo Ref: https://github.com/yolain/ComfyUI-Easy-Use.git

The ImageToMask node is intended to extract a single colour channel from the input image and convert it to a greyscale, which can be used for further image processing tasks.

# Input types
## Required
- image
    - Entering the image is essential for the operation of the node, as it is the source of the colour channel required for extraction.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image
## Optional
- channel
    - Channel parameters determine which colour channel is extracted from the image, affecting the end result of the greyscale conversion.
    - Comfy dtype: COMBO['red', 'green', 'blue']
    - Python dtype: str

# Output types
- MASK
    - The output is a volume representing the greyscale image derived from the selected colour channel, which is essential for the subsequent image analysis process.
    - Comfy dtype: TENSOR
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class imageToMask:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'channel': (['red', 'green', 'blue'],)}}
    RETURN_TYPES = ('MASK',)
    FUNCTION = 'convert'
    CATEGORY = 'EasyUse/Image'

    def convert_to_single_channel(self, image, channel='red'):
        image = image.convert('RGB')
        if channel == 'red':
            channel_img = image.split()[0].convert('L')
        elif channel == 'green':
            channel_img = image.split()[1].convert('L')
        elif channel == 'blue':
            channel_img = image.split()[2].convert('L')
        else:
            raise ValueError("Invalid channel option. Please choose 'red', 'green', or 'blue'.")
        channel_img = Image.merge('RGB', (channel_img, channel_img, channel_img))
        return channel_img

    def convert(self, image, channel='red'):
        image = self.convert_to_single_channel(tensor2pil(image), channel)
        image = pil2tensor(image)
        return (image.squeeze().mean(2),)
```