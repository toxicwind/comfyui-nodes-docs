# Documentation
- Class name: IPAdapterWeightsFromStrategy
- Category: ipadapter/weights
- Output node: False
- Repo Ref: https://github.com/cubiq/ComfyUI_IPAdapter_plus.git

The primary function of the node is to generate the weight of the IP adaptor based on a predefined strategy.
These weights can be applied at different stages of image processing to achieve specific effects or optimize processing processes

# Input types

## Required

- weights_strategy
    - The weight policy is used to specify the weight policy for generating the image. This parameter is used to control the weight policy for generating the image in order to achieve better results.
    - Comfy dtype: WEIGHTS_STRATEGY
    - Python dtype: str

## Optional

- image
  - image, which specifies the image that produces the image. This parameter is used to control the image that produces the image in order to achieve better results.
  - Comfy dtype: IMAGE
  - Python dtype: torch.Tensor

# Output types
- weights
  - The output of weights represents the results of the application of the specified method to input weights. It contains the essence of node purposes and provides a composite form of input data that can be used for further analysis or model training.
  - Comfy dtype: FLOAT
  - Python dtype: float

- weights_invert
  - Reverses the weight to specify the weight to be reversed to produce the image. This parameter is used to control the weight to be reversed to produce the image in order to achieve better results.
  - Comfy dtype: FLOAT
  - Python dtype: float

- total_frames
  - The total frame number is used to specify the total frame number to generate the image. This parameter is used to control the total frame number to generate the image for better results.
  - Comfy dtype: INT
  - Python dtype: int

- image1
  - Image1
  - Comfy dtype: IMAGE
  - Python dtype: torch.Tensor

- image2
  - Image 2
  - Comfy dtype: IMAGE
  - Python dtype: torch.Tensor

- weight_strategy
  - Strength strategy
  - Comfy dtype: WEIGHTS_STRATEGY
  - Python dtype: str

# Usage tips
- Infra type: GPU

# Source code
```
class IPAdapterWeightsFromStrategy(IPAdapterWeights):
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
            "weights_strategy": ("WEIGHTS_STRATEGY",),
            }, "optional": {
                "image": ("IMAGE",),
            }
        }
```