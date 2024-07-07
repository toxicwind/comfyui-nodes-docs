# Documentation
- Class name: SeargeImageAdapterV2
- Category: UI_PROMPTING
- Output node: False
- Repo Ref: https://github.com/jobunk/SeargeSDXL.git

The SeergeImageAdapterV2 class is designed to facilitate the conversion and adaptation of image data for the purpose of user interface tips. It plays a key role in integrating source images, image masks and upload masks into a structured data stream that UI components can use efficiently.

# Input types
## Required
- source_image
    - The source_image parameter is essential to the operation of the node because it indicates the raw image data that needs to be processed. It significantly influences how the node converts and constructs the data for downstream tasks.
    - Comfy dtype: IMAGE
    - Python dtype: Union[str, bytes, io.BufferedReader]
- image_mask
    - The image_mask parameter is an optional input that defines the mask to be applied to the source image. It is important because it determines the image range that will be processed or highlighted.
    - Comfy dtype: MASK
    - Python dtype: Union[str, bytes, io.BufferedReader]
- uploaded_mask
    - The uploaded_mask parameter allows the user to upload a mask in the image processing stream. Its existence can change node behaviour by providing additional context for image operations.
    - Comfy dtype: MASK
    - Python dtype: Union[str, bytes, io.BufferedReader]
- data
    - Data parameters are used as containers for additional data that may need to be used for node operations. It is optional and can be used to transmit additional information to nodes.
    - Comfy dtype: SRG_DATA_STREAM
    - Python dtype: Dict[str, Any]

# Output types
- data
    - Data output is a structured data stream that contains processed images and mask information. It is important because it provides the necessary input for subsequent UI components or downstream processing.
    - Comfy dtype: SRG_DATA_STREAM
    - Python dtype: Dict[str, Any]
- S_IMAGE_INPUTS
    - The S_IMAGE_INPUTS output contains image input that is suitable for UI tips. It is essential for correct display and interaction within the user interface.
    - Comfy dtype: SRG_DATA_STREAM
    - Python dtype: Dict[str, Any]

# Usage tips
- Infra type: CPU

# Source code
```
class SeargeImageAdapterV2:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {}, 'optional': {'data': ('SRG_DATA_STREAM',), 'source_image': ('IMAGE',), 'image_mask': ('MASK',), 'uploaded_mask': ('MASK',)}}
    RETURN_TYPES = ('SRG_DATA_STREAM', 'SRG_DATA_STREAM')
    RETURN_NAMES = ('data', UI.S_IMAGE_INPUTS)
    FUNCTION = 'get_value'
    CATEGORY = UI.CATEGORY_UI_PROMPTING

    @staticmethod
    def create_dict(source_image, image_mask, uploaded_mask):
        return {UI.F_SOURCE_IMAGE_CHANGED: True, UI.F_SOURCE_IMAGE: source_image, UI.F_IMAGE_MASK_CHANGED: True, UI.F_IMAGE_MASK: image_mask, UI.F_UPLOADED_MASK_CHANGED: True, UI.F_UPLOADED_MASK: uploaded_mask}

    def get_value(self, source_image=None, image_mask=None, uploaded_mask=None, data=None):
        if data is None:
            data = {}
        data[UI.S_IMAGE_INPUTS] = self.create_dict(source_image, image_mask, uploaded_mask)
        return (data, data[UI.S_IMAGE_INPUTS])
```