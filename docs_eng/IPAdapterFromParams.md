# Documentation
- Class name: IPAdapterFromParams
- Category: ipadapter/params
- Output node: False
- Repo Ref: https://github.com/cubiq/ComfyUI_IPAdapter_plus.git

The main function of the IPAdapterFromParams node is to create an IP adaptor object from the parameters provided by the user

# Input types

## Required
- model
    - model, which specifies the model that produces the image. This parameter is used to control the model that produces the image in order to achieve better results.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- ipadapter
    - IP adapter, which specifies the IP adapter for generating the image. This parameter is used to control the IP adapter for generating the image for better results.
    - Comfy dtype: IPADAPTER
    - Python dtype: torch.nn.Module
- ipadapter_params
    - IP adapter parameters that specify the IP adapter parameters that generate the image. This parameter is used to control the IP adapter parameters that generate the image for better effect.
    - Comfy dtype: IPADAPTER_PARAMS
    - Python dtype: torch.Tensor
- combine_embeds
    - The cobine_embeds parameter determines how embedding is combined. It is vital because it determines the mathematical operation to be applied to embedded input, significantly influencing the function of the node and the nature of the output.
    - Comfy dtype: ['concat', 'add', 'subtract', 'average', 'norm average']
    - Python dtype: str
- embeds_scaling
    - The embeds_scaling parameter determines how the embedding is scaled. It is vital because it decides to apply to the mathematical operation of the embedded input and significantly affects the function of the node and the nature of the output.
    - Comfy dtype: ['V only', 'K+V', 'K+V w/ C penalty', 'K+mean(V) w/ C penalty']
    - Python dtype: str

## Optional

- image_negative
    - A negative image is used to specify the negative direction in which the image is generated. This parameter is used to control the negative direction in which the image is generated in order to achieve better results.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- clip_vision
    - This parameter is used to control the clip_vision that produces the image for better results.
    - Comfy dtype: CLIP_VISION
    - Python dtype: torch.Tensor


# Output types
- model
    - Model to generate an image that contains the contents of all input parameters

# Usage tips
- Infra type: GPU

# Source code
```
class IPAdapterFromParams(IPAdapterAdvanced):
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "model": ("MODEL", ),
                "ipadapter": ("IPADAPTER", ),
                "ipadapter_params": ("IPADAPTER_PARAMS", ),
                "combine_embeds": (["concat", "add", "subtract", "average", "norm average"],),
                "embeds_scaling": (['V only', 'K+V', 'K+V w/ C penalty', 'K+mean(V) w/ C penalty'], ),
            },
            "optional": {
                "image_negative": ("IMAGE",),
                "clip_vision": ("CLIP_VISION",),
            }
        }

    CATEGORY = "ipadapter/params"
```