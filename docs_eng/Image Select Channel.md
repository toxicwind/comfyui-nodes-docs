# Documentation
- Class name: WAS_Image_Select_Channel
- Category: WAS Suite/Image/Process
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Image_Select_Channel node is designed to separate a particular colour channel from the image for further processing or analysis. It allows users to select the'red', 'green' or 'blue' channel and convert the image to a single channel indicating that by copying the selected channel into all three colour channels.

# Input types
## Required
- image
    - Entering the image is the main data that the node will process. It is essential for the operation of the node, as it determines the content of the channel that will be selected and processed.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image
## Optional
- channel
    - Channel parameters specify which colour channel to extract from the image. It is important because it determines the final result of the node operation and determines the colour information that is kept in the output image.
    - Comfy dtype: COMBO['red', 'green', 'blue']
    - Python dtype: str

# Output types
- selected_image
    - Output is a processed image that contains a selected monochrome channel. This image can be used in applications that require only one colour channel, or in further image processing tasks.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Image_Select_Channel:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'image': ('IMAGE',), 'channel': (['red', 'green', 'blue'],)}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'select_channel'
    CATEGORY = 'WAS Suite/Image/Process'

    def select_channel(self, image, channel='red'):
        image = self.convert_to_single_channel(tensor2pil(image), channel)
        return (pil2tensor(image),)

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
```