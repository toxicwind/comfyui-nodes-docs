# Documentation
- Class name: IPAdapterRegionalConditioning
- Category: ipadapter/params
- Output node: False
- Repo Ref: https://github.com/cubiq/ComfyUI_IPAdapter_plus.git

The IPAdapterRegionalConditioning node is a tool for generating images on a regional basis. This node is used primarily to process the attention mask and text conditionality of the specified area during the image generation process.

# Input types

## Required
- image
    - Reference image, which is encoded and used as a condition for generating a new image. Ensures that the key parts of the reference image are located at the centre of the image, so that better results can be obtained.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- image_weight
    - Image weights are used to adjust the impact of the image. This parameter can be used to balance the relationship between the image and the text to ensure that the image is produced in line with expectations.
    - Comfy dtype: FLOAT
    - Python dtype: float
- prompt_weight
    - Text weights are used to adjust the impact of the text. This parameter can be used to balance the relationship between the text and the image to ensure that the image is produced in line with expectations.
    - Comfy dtype: FLOAT
    - Python dtype: float
- weight_type
    - weight type, the method used to calculate the weight of the assigned weight. This parameter can be used to calculate the weight of the control in order to achieve better production effects.
    - Comfy dtype: WEIGHT_TYPES
    - Python dtype: str
- start_at
    - Starts the position, which is used to specify the starting position for the creation of the conditioned image. This parameter is used to control the beginning of the creation of the image in order to achieve better results.
    - Comfy dtype: FLOAT
    - Python dtype: float
- end_at
    - End position. This parameter is used to control the end position in which the image is generated in order to achieve better results.
    - Comfy dtype: FLOAT
    - Python dtype: float
## Optional
- mask
    - The focus mask is used to specify the area of attention in which the image is generated. This parameter is used to control the area of interest in which the image is generated in order to achieve better results.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor
- positive
    - This parameter is used to control the positive conditions for the creation of the image in order to achieve better results.
    - Comfy dtype: CONDITIONING
    - Python dtype: torch.Tensor
- negative
    - Negative condition is used to specify the negative condition for generating the image. This parameter is used to control the negative condition for generating the image in order to achieve better results.
    - Comfy dtype: CONDITIONING
    - Python dtype: torch.Tensor


# Output types

- IPADAPTER_PARAMS
  - IP adapter parameters, containing the contents of all input parameters
- POSITIVE
  - Cannot initialise Evolution's mail component.
- NEGATIVE
  - Negative Conditionation, which contains the contents of all input parameters

# Usage tips
- Infra type: GPU

# Source code
```
class IPAdapterRegionalConditioning:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
            #"set_cond_area": (["default", "mask bounds"],),
            "image": ("IMAGE",),
            "image_weight": ("FLOAT", { "default": 1.0, "min": -1.0, "max": 3.0, "step": 0.05 }),
            "prompt_weight": ("FLOAT", { "default": 1.0, "min": 0.0, "max": 10.0, "step": 0.05 }),
            "weight_type": (WEIGHT_TYPES, ),
            "start_at": ("FLOAT", { "default": 0.0, "min": 0.0, "max": 1.0, "step": 0.001 }),
            "end_at": ("FLOAT", { "default": 1.0, "min": 0.0, "max": 1.0, "step": 0.001 }),
        }, "optional": {
            "mask": ("MASK",),
            "positive": ("CONDITIONING",),
            "negative": ("CONDITIONING",),
        }}

    RETURN_TYPES = ("IPADAPTER_PARAMS", "CONDITIONING", "CONDITIONING", )
    RETURN_NAMES = ("IPADAPTER_PARAMS", "POSITIVE", "NEGATIVE")
    FUNCTION = "conditioning"

    CATEGORY = "ipadapter/params"

    def conditioning(self, image, image_weight, prompt_weight, weight_type, start_at, end_at, mask=None, positive=None, negative=None):
        set_area_to_bounds = False #if set_cond_area == "default" else True

        if mask is not None:
            if positive is not None:
                positive = conditioning_set_values(positive, {"mask": mask, "set_area_to_bounds": set_area_to_bounds, "mask_strength": prompt_weight})
            if negative is not None:
                negative = conditioning_set_values(negative, {"mask": mask, "set_area_to_bounds": set_area_to_bounds, "mask_strength": prompt_weight})

        ipadapter_params = {
            "image": [image],
            "attn_mask": [mask],
            "weight": [image_weight],
            "weight_type": [weight_type],
            "start_at": [start_at],
            "end_at": [end_at],
        }

        return (ipadapter_params, positive, negative, )
```