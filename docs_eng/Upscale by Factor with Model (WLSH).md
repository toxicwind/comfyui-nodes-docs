# Documentation
- Class name: WLSH_Upscale_By_Factor_With_Model
- Category: WLSH Nodes/upscaling
- Output node: False
- Repo Ref: https://github.com/wallish77/wlsh_nodes

The `upscale'method of WLSH_Upscale_By_Factor_With_Model node is designed to enhance the resolution of input images by using specified zoom factors. It performs sampling using pre-training models and provides selection of methods such as 'nearest-exact', `bilinear' or `area' to perform the sampling process. The function of the node is focused on improving the visual quality and detail of the image, making it an important tool in the image enhancement task.

# Input types
## Required
- upscale_model
    - The parameter `upscale_model'is essential for the operation of the node, as it designates a pre-training model for the sampling of images. The selection of the model can significantly affect the quality of the sampling and the efficiency of the node implementation.
    - Comfy dtype: UPSCALE_MODEL
    - Python dtype: torch.nn.Module
- image
    - The parameter `image'represents the input image that the node will process. This is a basic input, as all operations of the node revolve around enhancing the resolution of the image.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- upscale_method
    - Parameters `upscale_method'determine the algorithm to be used for upsampling the image. Different methods may result in different details and quality levels of the image being sampled, affecting the appearance of the final output.
    - Comfy dtype: COMBO['nearest-exact', 'bilinear', 'area']
    - Python dtype: str
- factor
    - The parameter `factor'defines the zoom factor in which the input image will be sampled. It is essential to control the final size of the image and directly influences the output of nodes.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- upscaled_image
    - Output `upscaled_image'represents the processed image with an enhanced resolution. It is the main result of node operations and demonstrates the validity of the selected sampling models and methods.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class WLSH_Upscale_By_Factor_With_Model:
    upscale_methods = ['nearest-exact', 'bilinear', 'area']

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'upscale_model': ('UPSCALE_MODEL',), 'image': ('IMAGE',), 'upscale_method': (s.upscale_methods,), 'factor': ('FLOAT', {'default': 2.0, 'min': 0.1, 'max': 8.0, 'step': 0.1})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'upscale'
    CATEGORY = 'WLSH Nodes/upscaling'

    def upscale(self, image, upscale_model, upscale_method, factor):
        device = model_management.get_torch_device()
        upscale_model.to(device)
        in_img = image.movedim(-1, -3).to(device)
        s = comfy.utils.tiled_scale(in_img, lambda a: upscale_model(a), tile_x=128 + 64, tile_y=128 + 64, overlap=8, upscale_amount=upscale_model.scale)
        upscale_model.cpu()
        upscaled = torch.clamp(s.movedim(-3, -1), min=0, max=1.0)
        old_width = image.shape[2]
        old_height = image.shape[1]
        new_width = int(old_width * factor)
        new_height = int(old_height * factor)
        print('Processing image with shape: ', old_width, 'x', old_height, 'to ', new_width, 'x', new_height)
        samples = upscaled.movedim(-1, 1)
        s = comfy.utils.common_upscale(samples, new_width, new_height, upscale_method, crop='disabled')
        s = s.movedim(1, -1)
        return (s,)
```