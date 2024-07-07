# Documentation
- Class name: WAS_CLIPSeg_Batch
- Category: WAS Suite/Image/Masking
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The CLAIPSeg_images method of the SAS_CLIPSeg_Batch node is designed to divide images according to text tips. It uses the CLAIPSeg model to generate masks corresponding to the entity described in the image. This node can handle multiple images and text, providing powerful solutions to complex split tasks that require understanding the semantic content of visual and text input.

# Input types
## Required
- image_a
    - The image_a parameter is the main image input required to divide the process. It is essential because it directly affects the ability of the model to understand and divide the elements required in the image.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image or torch.Tensor
- text_a
    - The text_a parameter provides a texttip to guide the partition model to identify and divide specific parts of the image. It is important that it can fine-tune the split process by focusing on the text description provided.
    - Comfy dtype: STRING
    - Python dtype: str
- image_b
    - The Image_b parameter is a secondary image input used with Image_a, which can be used for more complex partition scenarios. It allows additional visual context to be considered, thus enhancing the partition result.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image or torch.Tensor
- text_b
    - The text_b parameter is another texttip that supplements text_a and provides alternative or additional guidance to the partition model. It enhances the flexibility of nodes to deal with diverse split tasks.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- image_c
    - The optional image_c parameter allows for another image to be included in the split. In order for the model to be properly processed, it should be of the same size as the image_a.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image or torch.Tensor
- text_c
    - The optional text_c parameter expands the text guidance of the split model and provides further descriptions that can help with more complex split tasks.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- IMAGES_BATCH
    - IMAGES_BATCH output contains a batch of input images processed by nodes. It is important because it allows the original images to be reviewed and further analysed after partitioning.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- MASKS_BATCH
    - MASKS_BATCH output provides a generation mask corresponding to the area of interest in the input image. These masks are essential to isolate and further process specific parts of the texttip description.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor
- MASK_IMAGES_BATCH
    - MASK_IMAGES_BATCH output includes images that have been masked, highlighting the partition area according to the texttip. It is an important output of the results of the visible partitioning process.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class WAS_CLIPSeg_Batch:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'image_a': ('IMAGE',), 'image_b': ('IMAGE',), 'text_a': ('STRING', {'default': '', 'multiline': False}), 'text_b': ('STRING', {'default': '', 'multiline': False})}, 'optional': {'image_c': ('IMAGE',), 'image_d': ('IMAGE',), 'image_e': ('IMAGE',), 'image_f': ('IMAGE',), 'text_c': ('STRING', {'default': '', 'multiline': False}), 'text_d': ('STRING', {'default': '', 'multiline': False}), 'text_e': ('STRING', {'default': '', 'multiline': False}), 'text_f': ('STRING', {'default': '', 'multiline': False})}}
    RETURN_TYPES = ('IMAGE', 'MASK', 'IMAGE')
    RETURN_NAMES = ('IMAGES_BATCH', 'MASKS_BATCH', 'MASK_IMAGES_BATCH')
    FUNCTION = 'CLIPSeg_images'
    CATEGORY = 'WAS Suite/Image/Masking'

    def CLIPSeg_images(self, image_a, image_b, text_a, text_b, image_c=None, image_d=None, image_e=None, image_f=None, text_c=None, text_d=None, text_e=None, text_f=None):
        from transformers import CLIPSegProcessor, CLIPSegForImageSegmentation
        import torch.nn.functional as F
        images_pil = [tensor2pil(image_a), tensor2pil(image_b)]
        if image_c is not None:
            if image_c.shape[-2:] != image_a.shape[-2:]:
                cstr('Size of image_c is different from image_a.').error.print()
                return
            images_pil.append(tensor2pil(image_c))
        if image_d is not None:
            if image_d.shape[-2:] != image_a.shape[-2:]:
                cstr('Size of image_d is different from image_a.').error.print()
                return
            images_pil.append(tensor2pil(image_d))
        if image_e is not None:
            if image_e.shape[-2:] != image_a.shape[-2:]:
                cstr('Size of image_e is different from image_a.').error.print()
                return
            images_pil.append(tensor2pil(image_e))
        if image_f is not None:
            if image_f.shape[-2:] != image_a.shape[-2:]:
                cstr('Size of image_f is different from image_a.').error.print()
                return
            images_pil.append(tensor2pil(image_f))
        images_tensor = [torch.from_numpy(np.array(img.convert('RGB')).astype(np.float32) / 255.0).unsqueeze(0) for img in images_pil]
        images_tensor = torch.cat(images_tensor, dim=0)
        prompts = [text_a, text_b]
        if text_c:
            prompts.append(text_c)
        if text_d:
            prompts.append(text_d)
        if text_e:
            prompts.append(text_e)
        if text_f:
            prompts.append(text_f)
        cache = os.path.join(MODELS_DIR, 'clipseg')
        inputs = CLIPSegProcessor.from_pretrained('CIDAS/clipseg-rd64-refined', cache_dir=cache)
        model = CLIPSegForImageSegmentation.from_pretrained('CIDAS/clipseg-rd64-refined', cache_dir=cache)
        with torch.no_grad():
            result = model(**inputs(text=prompts, images=images_pil, padding=True, return_tensors='pt'))
        masks = []
        mask_images = []
        for (i, res) in enumerate(result.logits):
            tensor = torch.sigmoid(res)
            mask = 1.0 - (tensor - tensor.min()) / tensor.max()
            mask = mask.unsqueeze(0)
            mask = tensor2pil(mask).convert('L')
            mask = mask.resize(images_pil[0].size)
            mask_batch = pil2mask(mask)
            masks.append(mask_batch.unsqueeze(0).unsqueeze(1))
            mask_images.append(pil2tensor(ImageOps.invert(mask.convert('RGB'))).squeeze(0))
        masks_tensor = torch.cat(masks, dim=0)
        mask_images_tensor = torch.stack(mask_images, dim=0)
        del inputs, model, result, tensor, masks, mask_images, images_pil
        return (images_tensor, masks_tensor, mask_images_tensor)
```