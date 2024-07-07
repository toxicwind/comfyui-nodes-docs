# Documentation
- Class name: WAS_Shadow_And_Highlight_Adjustment
- Category: WAS Suite/Image/Adjustment
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

WAS_Shadow_And_Highlight_Adjustment aims to modify the contrast and colour range by adjusting the shadow and high light of the image. By enhancing the detail of the darker and brighter areas in the image, the node allows for better visual definition and more balanced exposure. It operates by applying different thresholds and factors to the shadow and high-light, respectively, and can selectively smooth the areas to obtain a more natural appearance. This node is particularly suitable for later-stage image processing, where dynamic ranges need to be optimized for better visual appeal or to meet specific technical requirements.

# Input types
## Required
- image
    - This parameter is essential because it determines the basic visual content that the node will process. The execution and results of the node depend heavily on the quality and properties of the input image.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image
## Optional
- shadow_threshold
    - The pixel value is considered a threshold for the shadow section. Adjusting this parameter affects the extent to which the shadow is modified in the image. This is an important parameter to control the strength of the shadow in the final output.
    - Comfy dtype: FLOAT
    - Python dtype: float
- shadow_factor
    - Multiplication factor to increase the intensity of the image shadow area. This is a key parameter to enhance the detail of the image darkness.
    - Comfy dtype: FLOAT
    - Python dtype: float
- shadow_smoothing
    - To apply to the smoothness of the shadow mask. Higher values lead to a smoother transition between the shadow and the non-shaded areas, which may be better suited to a more natural appearance, but may reduce the contrast in the shadow.
    - Comfy dtype: FLOAT
    - Python dtype: float
- highlight_threshold
    - The pixel value is considered a threshold for the high light segment. This parameter is essential for determining which parts of the image will be considered high light and then adjusted.
    - Comfy dtype: FLOAT
    - Python dtype: float
- highlight_factor
    - Multiplication factors to reduce the intensity of the high-light area of the image. This is a key parameter to control the burning level of the high-light and to prevent the loss of details of the brighter parts of the image.
    - Comfy dtype: FLOAT
    - Python dtype: float
- highlight_smoothing
    - To apply to the smoothness of the high-light mask. Similar to the smoothness of the shadow, it helps to achieve a more gradual transition between high-light and non-high-light regions.
    - Comfy dtype: FLOAT
    - Python dtype: float
- simplify_isolation
    - It can be used to reduce the complexity of the mask, which may be useful for performance reasons or for achieving specific visual effects.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- image
    - The final adjusted image has an enhanced shadow and high light. It represents the main output of the node and shows the cumulative effect of all the adjustments made to the input image.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image
- shadow_map
    - A shadow map that is generated as part of the adjustment process. It is a greyscale image, with darker values indicating the shadowed area that has been modified.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image
- highlight_map
    - High-light maps are generated as part of the adjustment process. It is a grey-scale image, with brighter values indicating a modified high-light area.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Shadow_And_Highlight_Adjustment:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'image': ('IMAGE',), 'shadow_threshold': ('FLOAT', {'default': 75, 'min': 0.0, 'max': 255.0, 'step': 0.1}), 'shadow_factor': ('FLOAT', {'default': 1.5, 'min': -12.0, 'max': 12.0, 'step': 0.1}), 'shadow_smoothing': ('FLOAT', {'default': 0.25, 'min': -255.0, 'max': 255.0, 'step': 0.1}), 'highlight_threshold': ('FLOAT', {'default': 175, 'min': 0.0, 'max': 255.0, 'step': 0.1}), 'highlight_factor': ('FLOAT', {'default': 0.5, 'min': -12.0, 'max': 12.0, 'step': 0.1}), 'highlight_smoothing': ('FLOAT', {'default': 0.25, 'min': -255.0, 'max': 255.0, 'step': 0.1}), 'simplify_isolation': ('FLOAT', {'default': 0, 'min': -255.0, 'max': 255.0, 'step': 0.1})}}
    RETURN_TYPES = ('IMAGE', 'IMAGE', 'IMAGE')
    RETURN_NAMES = ('image', 'shadow_map', 'highlight_map')
    FUNCTION = 'apply_shadow_and_highlight'
    CATEGORY = 'WAS Suite/Image/Adjustment'

    def apply_shadow_and_highlight(self, image, shadow_threshold=30, highlight_threshold=220, shadow_factor=1.5, highlight_factor=0.5, shadow_smoothing=0, highlight_smoothing=0, simplify_isolation=0):
        WTools = WAS_Tools_Class()
        (result, shadows, highlights) = WTools.shadows_and_highlights(tensor2pil(image), shadow_threshold, highlight_threshold, shadow_factor, highlight_factor, shadow_smoothing, highlight_smoothing, simplify_isolation)
        (result, shadows, highlights) = WTools.shadows_and_highlights(tensor2pil(image), shadow_threshold, highlight_threshold, shadow_factor, highlight_factor, shadow_smoothing, highlight_smoothing, simplify_isolation)
        return (pil2tensor(result), pil2tensor(shadows), pil2tensor(highlights))
```