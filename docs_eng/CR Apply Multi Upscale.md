# Documentation
- Class name: CR_ApplyMultiUpscale
- Category: Comfyroll/Upscale
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_ApplyMultiUpscale is a node that aims to increase the resolution of images by increasing them over multiple phases. It uses a series of elevation models to fine-tune image quality in sequence. The node can adjust sampling methods and round-up models to provide users with fine control over the magnification process. The main objective is to provide high-resolution images with improved clarity and detail.

# Input types
## Required
- image
    - The input image is the primary data for node processing. It is the starting point for all magnification operations, the quality of which directly affects the final output. The image parameter is necessary because it determines the subject of enhancement.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- resampling_method
    - The re-sampling method determines how the image is plugged in during the magnification process. It is a key parameter that affects the smoothness and clarity of the magnifying image and allows users to select different algorithms for the best results.
    - Comfy dtype: COMBO[lanczos, nearest, bilinear, bicubic]
    - Python dtype: str
- supersample
    - The Supersample parameter allows the sampling to be controlled during the magnification process. It is important because it enhances the detail and clarity of the image, especially for high-resolution output.
    - Comfy dtype: COMBO[true, false]
    - Python dtype: bool
- rounding_modulus
    - The rounding module is used to determine the rounding behaviour during the magnification process. It is an important parameter to ensure that the size of the magnification image is consistent and optimized so that it can be displayed or further processed.
    - Comfy dtype: INT
    - Python dtype: int
- upscale_stack
    - The magnification stack is a collection of models and factors that define the magnification of the sequence of operations. It is essential because it determines the complexity and sequence of the models applied to the images and significantly influences the end result.
    - Comfy dtype: UPSCALE_STACK
    - Python dtype: List[Tuple[str, float]]

# Output types
- IMAGE
    - The magnified image is the main output of the node, representing the end result of the multistage magnification process. It is important because it is the direct result of the node operation and is used for further processing or displaying.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- show_help
    - Show_help output provides a document URL for further help. It is useful for users who need more information about node operations or troubleshooting instructions.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: GPU

# Source code
```
class CR_ApplyMultiUpscale:

    @classmethod
    def INPUT_TYPES(s):
        resampling_methods = ['lanczos', 'nearest', 'bilinear', 'bicubic']
        return {'required': {'image': ('IMAGE',), 'resampling_method': (resampling_methods,), 'supersample': (['true', 'false'],), 'rounding_modulus': ('INT', {'default': 8, 'min': 8, 'max': 1024, 'step': 8}), 'upscale_stack': ('UPSCALE_STACK',)}}
    RETURN_TYPES = ('IMAGE', 'STRING')
    RETURN_NAMES = ('IMAGE', 'show_help')
    FUNCTION = 'apply'
    CATEGORY = icons.get('Comfyroll/Upscale')

    def apply(self, image, resampling_method, supersample, rounding_modulus, upscale_stack):
        pil_img = tensor2pil(image)
        (original_width, original_height) = pil_img.size
        params = list()
        params.extend(upscale_stack)
        for tup in params:
            (upscale_model, rescale_factor) = tup
            print(f'[Info] CR Apply Multi Upscale: Applying {upscale_model} and rescaling by factor {rescale_factor}')
            up_model = load_model(upscale_model)
            up_image = upscale_with_model(up_model, image)
            pil_img = tensor2pil(up_image)
            (upscaled_width, upscaled_height) = pil_img.size
            if upscaled_width == original_width and rescale_factor == 1:
                image = up_image
            else:
                scaled_images = []
                mode = 'rescale'
                resize_width = 1024
                for img in up_image:
                    scaled_images.append(pil2tensor(apply_resize_image(tensor2pil(img), original_width, original_height, rounding_modulus, mode, supersample, rescale_factor, resize_width, resampling_method)))
                image = torch.cat(scaled_images, dim=0)
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Upscale-Nodes#cr-apply-multi-upscale'
        return (image, show_help)
```