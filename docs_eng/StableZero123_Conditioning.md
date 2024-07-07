# Documentation
- Class name: StableZero123_Conditioning
- Category: conditioning/3d_models
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The `encode'method of the Stable Zero123_Conditioning class is designed to convert visual and spatial information into forms that can be used to generate 3D models. It encodes the initial image, integrates the camera direction and prepares potential indications of positive and negative conditions during the 3D model generation process.

# Input types
## Required
- clip_vision
    - The parameter `clip_vision'is essential for the coding process because it provides a visual model for understanding and processing the initial images. It plays a key role in converting visual data into a form that can be used for the 3D model conditions.
    - Comfy dtype: CLIP_VISION
    - Python dtype: Any
- init_image
    - The parameter `init_image'is necessary because it is the node used to generate the initial image of the potential expression. It directly influences the visual output of the 3D model by providing the basic visual context for the coding process.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- vae
    - The parameter `vae'is a variable self-encoder that encodes visual data into potential space. It is a key component that converts image pixels to a 3D model format.
    - Comfy dtype: VAE
    - Python dtype: torch.nn.Module
## Optional
- width
    - The parameter `width' specifies the width of the magnified image, which is important for determining the resolution to analyse image characteristics. It affects the level of detail captured during the encoding process.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - The parameter `height'sets the height of the magnified image, which is important for the resolution and the structural integrity of the encoded image. It ensures that the image maintains its horizontal ratio and quality during the encoding process.
    - Comfy dtype: INT
    - Python dtype: int
- batch_size
    - The parameter `batch_size' defines the number of samples processed in an iterative process, which is essential for managing memory use and computing efficiency in the coding process.
    - Comfy dtype: INT
    - Python dtype: int
- elevation
    - The parameter `elevation'represents the vertical angle of the camera, which is essential for the spatial conditions of the 3D model. It influences the observational perspective of the model, and thus influences the final rendering effect.
    - Comfy dtype: FLOAT
    - Python dtype: float
- azimuth
    - The parameter `azimuth'represents the horizontal angle of the camera, which plays a key role in the spatial conditions of the 3D model. It determines the direction of the model on the horizontal plane and influences its overall appearance.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- positive
    - The output `positive'provides a coded image feature and camera direction as a positive condition of the 3D model generation process. It is a key component that guides the model to produce images consistent with the input image and camera perspective.
    - Comfy dtype: CONDITIONING
    - Python dtype: Tuple[torch.Tensor, Dict[str, torch.Tensor]]
- negative
    - The output `negative'is a negative condition by providing a baseline of zero characteristics, in contrast to the positive condition. It helps to refine model formation by highlighting the difference between the required image and the zero state.
    - Comfy dtype: CONDITIONING
    - Python dtype: Tuple[torch.Tensor, Dict[str, torch.Tensor]]
- latent
    - Output `latent'contains potential samples of images that are coded by the representative in compressed form. These samples are used as the basis for 3D models to capture basic visual and spatial information in a concise manner.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]

# Usage tips
- Infra type: GPU

# Source code
```
class StableZero123_Conditioning:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'clip_vision': ('CLIP_VISION',), 'init_image': ('IMAGE',), 'vae': ('VAE',), 'width': ('INT', {'default': 256, 'min': 16, 'max': nodes.MAX_RESOLUTION, 'step': 8}), 'height': ('INT', {'default': 256, 'min': 16, 'max': nodes.MAX_RESOLUTION, 'step': 8}), 'batch_size': ('INT', {'default': 1, 'min': 1, 'max': 4096}), 'elevation': ('FLOAT', {'default': 0.0, 'min': -180.0, 'max': 180.0, 'step': 0.1, 'round': False}), 'azimuth': ('FLOAT', {'default': 0.0, 'min': -180.0, 'max': 180.0, 'step': 0.1, 'round': False})}}
    RETURN_TYPES = ('CONDITIONING', 'CONDITIONING', 'LATENT')
    RETURN_NAMES = ('positive', 'negative', 'latent')
    FUNCTION = 'encode'
    CATEGORY = 'conditioning/3d_models'

    def encode(self, clip_vision, init_image, vae, width, height, batch_size, elevation, azimuth):
        output = clip_vision.encode_image(init_image)
        pooled = output.image_embeds.unsqueeze(0)
        pixels = comfy.utils.common_upscale(init_image.movedim(-1, 1), width, height, 'bilinear', 'center').movedim(1, -1)
        encode_pixels = pixels[:, :, :, :3]
        t = vae.encode(encode_pixels)
        cam_embeds = camera_embeddings(elevation, azimuth)
        cond = torch.cat([pooled, cam_embeds.to(pooled.device).repeat((pooled.shape[0], 1, 1))], dim=-1)
        positive = [[cond, {'concat_latent_image': t}]]
        negative = [[torch.zeros_like(pooled), {'concat_latent_image': torch.zeros_like(t)}]]
        latent = torch.zeros([batch_size, 4, height // 8, width // 8])
        return (positive, negative, {'samples': latent})
```