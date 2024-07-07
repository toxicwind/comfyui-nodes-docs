# Documentation
- Class name: Send_To_Editor
- Category: image
- Output node: True
- Repo Ref: https://github.com/Lerc/canvas_tab.git

The node is designed to process and collect image data and convert them to formats suitable for further use in the editing environment. It emphasizes converting original images into structured output so that they can be integrated seamlessly into various editing tools.

# Input types
## Required
- unique_id
    - The only identifier for an image batch ensures that each group of images can be tracked and managed separately during the editing process.
    - Comfy dtype: str
    - Python dtype: str
## Optional
- images
    - Enter images that will be processed by nodes. These images are vital because they form the basis for output and directly affect the quality and availability of data sent to the editor.
    - Comfy dtype: COMBO[Image]
    - Python dtype: List[PIL.Image.Image]

# Output types
- collected_images
    - is a list of data URLs for the images collected, to be used in the edit interface.
    - Comfy dtype: List[str]
    - Python dtype: List[str]

# Usage tips
- Infra type: CPU

# Source code
```
class Send_To_Editor:

    def __init__(self):
        self.updateTick = 1
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {}, 'hidden': {'unique_id': 'UNIQUE_ID'}, 'optional': {'images': ('IMAGE',)}}
    RETURN_TYPES = ()
    FUNCTION = 'collect_images'
    OUTPUT_NODE = True
    CATEGORY = 'image'

    def IS_CHANGED(self, unique_id, images):
        self.updateTick += 1
        return hex(self.updateTick)

    def collect_images(self, unique_id, images=None):
        collected_images = list()
        if images is not None:
            for image in images:
                i = 255.0 * image.cpu().numpy()
                img = Image.fromarray(np.clip(i, 0, 255).astype(np.uint8))
                collected_images.append(image_to_data_url(img))
        return {'ui': {'collected_images': collected_images}}
```