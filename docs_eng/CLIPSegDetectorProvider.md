# Documentation
- Class name: CLIPSegDetectorProvider
- Category: ImpactPack/Util
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The CLIPSegDectorProvider node is designed to create a border frame detector based on the CLIPSeg model. It processes input text and image data to generate boundary boxes around objects of interest in the image. This node is particularly suitable for applications that need to be guided by the object detection function based on texttips.

# Input types
## Required
- text
    - Text parameters are essential to guide the detection process by providing a text description of the object to be tested. They play a key role in the accuracy and relevance of the boundary frame generated.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- blur
    - Fuzzy parameters are adjusted to apply to the degree of fuzzyness of the image, which may affect the accuracy of the test. It is an optional parameter that allows fine-tuning of the detection process according to the characteristics of the image.
    - Comfy dtype: FLOAT
    - Python dtype: float
- threshold
    - The threshold parameter determines the cut-off point for the object test. It is an optional input that can be used to control the sensitivity of the test and affect which objects are identified as relevant.
    - Comfy dtype: FLOAT
    - Python dtype: float
- dilation_factor
    - The inflation factor is used to expand the boundaries of the detected object. It is an optional parameter that enhances the detection of larger or more dispersed objects in the image.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- BBOX_DETECTOR
    - The output of CLIPSegDectorProvider is a BBOX_DETECTOR object that contains logic based on the texttip provided to detect and generate the boundary box around the object in the image.
    - Comfy dtype: BBOX_DETECTOR
    - Python dtype: BBoxDetectorBasedOnCLIPSeg

# Usage tips
- Infra type: GPU

# Source code
```
class CLIPSegDetectorProvider:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'text': ('STRING', {'multiline': False}), 'blur': ('FLOAT', {'min': 0, 'max': 15, 'step': 0.1, 'default': 7}), 'threshold': ('FLOAT', {'min': 0, 'max': 1, 'step': 0.05, 'default': 0.4}), 'dilation_factor': ('INT', {'min': 0, 'max': 10, 'step': 1, 'default': 4})}}
    RETURN_TYPES = ('BBOX_DETECTOR',)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Util'

    def doit(self, text, blur, threshold, dilation_factor):
        if 'CLIPSeg' in nodes.NODE_CLASS_MAPPINGS:
            return (core.BBoxDetectorBasedOnCLIPSeg(text, blur, threshold, dilation_factor),)
        else:
            print("[ERROR] CLIPSegToBboxDetector: CLIPSeg custom node isn't installed. You must install biegert/ComfyUI-CLIPSeg extension to use this node.")
```