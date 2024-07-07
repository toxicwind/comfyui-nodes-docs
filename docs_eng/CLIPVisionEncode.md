# Documentation
- Class name: CLIPVisionEncode
- Category: conditioning
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

Encodes the visual information of the image into a format suitable for downstream tasks such as text-image matching or image classification. The node abstractes the complexity of the bottom model structure and focuses on converting raw image data into semantic expressions.

# Input types
## Required
- clip_vision
    - The CLIP visual model used to encode images. It plays a key role in the operation of nodes, providing the model architecture and parameters required for image coding.
    - Comfy dtype: CLIP_VISION
    - Python dtype: torch.nn.Module
- image
    - The input image that you want to encode. It is the key to the node because it is the raw data that will be converted into semantic expressions.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Output types
- CLIP_VISION_OUTPUT
    - The CLAIP visual model code output, including the final hidden state, image embedding and penultimate hidden state. This output is important because it provides the basis for further analysis or processing in various applications.
    - Comfy dtype: CLIP_VISION_OUTPUT
    - Python dtype: Dict[str, torch.Tensor]

# Usage tips
- Infra type: GPU

# Source code
```
class CLIPVisionEncode:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'clip_vision': ('CLIP_VISION',), 'image': ('IMAGE',)}}
    RETURN_TYPES = ('CLIP_VISION_OUTPUT',)
    FUNCTION = 'encode'
    CATEGORY = 'conditioning'

    def encode(self, clip_vision, image):
        output = clip_vision.encode_image(image)
        return (output,)
```