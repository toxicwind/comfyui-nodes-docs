# Documentation
- Class name: WAS_CLIPSeg
- Category: WAS Suite/Image/Masking
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The CLIPSeg_image method is designed to divide images using text tips. It uses the CLIPSeg model to generate a mask that separates the body of the image described in the text. This method is particularly useful for applications that require precise object separation based on text descriptions.

# Input types
## Required
- image
    - The image parameter is essential for the partition process, as it is the input that the model will analyse to identify and isolate the subject that is needed. The quality and resolution of the image can significantly influence the accuracy of the mask generated.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image
## Optional
- text
    - Text parameters provide a description that guides the split process. It is optional, but the accuracy of the split can be improved by specifying what the model should focus on in the image.
    - Comfy dtype: STRING
    - Python dtype: str
- clipseg_model
    - The clipseg_model parameter allows users to provide pre-trained CLIPSeg models for splits. This may be useful for using self-defined models that have been fine-tuned for specific tasks or data sets.
    - Comfy dtype: CLIPSEG_MODEL
    - Python dtype: Tuple[str, transformers.CLIPSegForImageSegmentation]

# Output types
- MASK
    - MASK output is a binary mask that separates the separated subjects from the rest of the image according to the text description provided. It is essential for applications that require object separation or background removal.
    - Comfy dtype: MASK
    - Python dtype: np.ndarray
- MASK_IMAGE
    - MASK_IMAGE output is a reverse image of a split subject that is highlighted by mask. It can be used for visual validation or for further processing steps expressed by the image that needs to be split.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class WAS_CLIPSeg:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'image': ('IMAGE',), 'text': ('STRING', {'default': '', 'multiline': False})}, 'optional': {'clipseg_model': ('CLIPSEG_MODEL',)}}
    RETURN_TYPES = ('MASK', 'IMAGE')
    RETURN_NAMES = ('MASK', 'MASK_IMAGE')
    FUNCTION = 'CLIPSeg_image'
    CATEGORY = 'WAS Suite/Image/Masking'

    def CLIPSeg_image(self, image, text=None, clipseg_model=None):
        from transformers import CLIPSegProcessor, CLIPSegForImageSegmentation
        image = tensor2pil(image)
        cache = os.path.join(MODELS_DIR, 'clipseg')
        if clipseg_model:
            inputs = clipseg_model[0]
            model = clipseg_model[1]
        else:
            inputs = CLIPSegProcessor.from_pretrained('CIDAS/clipseg-rd64-refined', cache_dir=cache)
            model = CLIPSegForImageSegmentation.from_pretrained('CIDAS/clipseg-rd64-refined', cache_dir=cache)
        with torch.no_grad():
            result = model(**inputs(text=text, images=image, padding=True, return_tensors='pt'))
        tensor = torch.sigmoid(result[0])
        mask = 1.0 - (tensor - tensor.min()) / tensor.max()
        mask = mask.unsqueeze(0)
        mask = tensor2pil(mask).convert('L')
        mask = mask.resize(image.size)
        return (pil2mask(mask), pil2tensor(ImageOps.invert(mask.convert('RGB'))))
```