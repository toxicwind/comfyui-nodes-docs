# Documentation
- Class name: FaceDetailer
- Category: face_detailer
- Output node: False
- Repo Ref: https://github.com/friendlymilo/DZ-FaceDetailer.git

FaceDetailer is a node that aims to enhance facial features in the image by using advanced machine learning models and image processing techniques. It focuses on fine-tuning facial details through the application of masking and noise operations, with the aim of improving the quality and clarity of facial data.

# Input types
## Required
- model
    - Model parameters are essential for the FaceDetailer node, because it determines the machine learning architecture for facial detail enhancement. This is essential for the correct function of the node and for producing accurate facial features enhancement.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- seed
    - Seed parameters are important for the FaceDetailer node because they introduce randomity in the process of enhancing facial features. It ensures that nodes generate various facial details and contribute to the diversity of output.
    - Comfy dtype: INT
    - Python dtype: int
- steps
    - The step parameter affects the number of overlaps that FaceDetailer nodes carry out in the face enhancement process. It affects the details and refinements achieved in the final output. More steps may lead to higher quality enhancements.
    - Comfy dtype: INT
    - Python dtype: int
- cfg
    - The cfg parameter is a configuration value used to adjust the intensity of the facial feature enhancement process. It plays an important role in determining node output, and higher values may lead to more obvious facial details.
    - Comfy dtype: FLOAT
    - Python dtype: float
- sampler_name
    - The sampler_name parameter is essential for the FaceDetailer node because it selects the sampling method used to generate facial details. It influences the diversity and randomness of facial features and contributes to the uniqueness of node output.
    - Comfy dtype: COMBO
    - Python dtype: str
- scheduler
    - The scheduler parameter is essential for the FaceDetailer node because it manages the process of enhancement. It influences how the node applies enhanced facial features over time to ensure smooth and efficient conversions.
    - Comfy dtype: COMBO
    - Python dtype: str
- positive
    - Positive parameters determine which facial features are enhanced as the Facial Detailer node. It plays a key role in shaping the final output, ensuring that the required features are highlighted and improved.
    - Comfy dtype: CONDITIONING
    - Python dtype: str
- negative
    - Negative parameters are used by the FaceDetailer node to identify facial features that should be reduced or reduced. It contributes to overall facial detail by ensuring that unwanted features are reduced.
    - Comfy dtype: CONDITIONING
    - Python dtype: str
- latent_image
    - The latent_image parameter is essential for the FaceDetailer node because it provides initial data on enhanced facial features. It is the basis for node construction and fine-tuning of facial details, directly affecting the quality of output.
    - Comfy dtype: LATENT
    - Python dtype: dict
- denoise
    - Noise parameters are important for the FaceDetailer node because it controls the level of noise reduction applied during facial enhancement. It contributes to a clearer and more finer detailed output of the face.
    - Comfy dtype: FLOAT
    - Python dtype: float
- vae
    - The vae parameter is essential for the FaceDetailer node, because it represents the variable coder model used to decode and generate facial images. It is a key component of the node that can produce high-quality facial detail enhancement.
    - Comfy dtype: VAE
    - Python dtype: torch.nn.Module
- mask_blur
    - The mask_blur parameter is important for the FaceDetailer node because it determines the degree of ambiguity applied to the mask. It affects the smoothness and accuracy of the mask, and thus the quality of the enhanced facial detail.
    - Comfy dtype: INT
    - Python dtype: int
- mask_type
    - The mask_type parameter is essential for the FaceDetailer node because it specifies the type of mask to be used for facial enhancement. It directly affects the effectiveness and accuracy of the facial detail enhancement process.
    - Comfy dtype: MASK_TYPE
    - Python dtype: str
- mask_control
    - The mask_control parameter is essential for the FaceDetailer node, as it manages the facial mask operation. It affects the ultimate appearance of the mask, and hence the enhanced quality of the facial signature.
    - Comfy dtype: MASK_CONTROL
    - Python dtype: str
- dilate_mask_value
    - The dilaate_mask_value parameter is important for the FaceDetailer node, because it defines the level of mask inflation that should be applied to facial masking. It affects the size and shape of the masked area, which is essential for the enhancement of precise facial features.
    - Comfy dtype: INT
    - Python dtype: int
- erode_mask_value
    - The erode_mask_value parameter is important for the FaceDetailer node because it sets the level of mask corrosion that should be applied to facial masking. It affects the definition and boundary of mask facial features and helps to enhance the accuracy of facial detail.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- latent
    - The latent parameter represents the refined and enhanced facial features extracted from the FaceDetailer node. This is a key output that contains detailed facial information for further use or analysis.
    - Comfy dtype: LATENT
    - Python dtype: dict
- mask
    - The mask parameter is an output of the FaceDetailer node, which provides the facial mask used in the enhancement process. It is an important component for any subsequent facial characterization operation or analysis.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class FaceDetailer:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615}), 'steps': ('INT', {'default': 20, 'min': 1, 'max': 10000}), 'cfg': ('FLOAT', {'default': 8.0, 'min': 0.0, 'max': 100.0, 'step': 0.1, 'round': 0.01}), 'sampler_name': (comfy.samplers.KSampler.SAMPLERS,), 'scheduler': (comfy.samplers.KSampler.SCHEDULERS,), 'positive': ('CONDITIONING',), 'negative': ('CONDITIONING',), 'latent_image': ('LATENT',), 'denoise': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'latent_image': ('LATENT',), 'vae': ('VAE',), 'mask_blur': ('INT', {'default': 0, 'min': 0, 'max': 100}), 'mask_type': (MASK_TYPE,), 'mask_control': (MASK_CONTROL,), 'dilate_mask_value': ('INT', {'default': 3, 'min': 0, 'max': 100}), 'erode_mask_value': ('INT', {'default': 3, 'min': 0, 'max': 100})}}
    RETURN_TYPES = ('LATENT', 'MASK')
    FUNCTION = 'detailer'
    CATEGORY = 'face_detailer'

    def detailer(self, model, seed, steps, cfg, sampler_name, scheduler, positive, negative, latent_image, denoise, vae, mask_blur, mask_type, mask_control, dilate_mask_value, erode_mask_value):
        tensor_img = vae.decode(latent_image['samples'])
        batch_size = tensor_img.shape[0]
        mask = Detection().detect_faces(tensor_img, batch_size, mask_type, mask_control, mask_blur, dilate_mask_value, erode_mask_value)
        latent_mask = set_mask(latent_image, mask)
        latent = nodes.common_ksampler(model, seed, steps, cfg, sampler_name, scheduler, positive, negative, latent_mask, denoise=denoise)
        return (latent[0], latent[0]['noise_mask'])
```