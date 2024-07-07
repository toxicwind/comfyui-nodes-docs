# Documentation
- Class name: WAS_Image_Filters
- Category: WAS Suite/Image/Filter
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Image_Filters node is designed to enhance or modify the visual features of the image by applying a comprehensive set of image-processing filters to input images. It provides functions such as adjusting brightness, contrast and saturation, and applying sharpness, ambiguity, edge enhancement and detail enhancement. The node is designed to provide a multifunctional image-processing tool that can be used for applications ranging from simple adaptation to more complex visual transformation.

# Input types
## Required
- image
    - The 'image'parameter is the main input of the node, which represents the image data that will be filtered. It is vital because it determines the basic content of all subsequent enhancements and modifications that will be applied. The quality and format of the input image directly influences the execution of the node and the appearance of the final output.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
## Optional
- brightness
    - The " Brightness " parameter allows the user to adjust the overall brightness of the image. It is important because it enhances visibility or creates style effects in conditions where light is insufficient. The value of this parameter directly influences the output of the node. The higher the value, the brightness increases; the lower the value, the lighter the brightness.
    - Comfy dtype: FLOAT
    - Python dtype: float
- contrast
    - The " Contrast" parameter is used to modify the colour or colour differences between parts of the image. It plays an important role in making the image look more dynamic or less coloured in order to reach a softer look. This adjustment can significantly change the visual impact of the final image.
    - Comfy dtype: FLOAT
    - Python dtype: float
- saturation
    - The'saturation' parameter controls the intensity of colours in the image. It is essential to create a more colourful and rich image or to produce a more saturated, retrograde visual effect. The level of saturation can greatly influence the emotional response to the image and the aesthetic appeal of the image as a whole.
    - Comfy dtype: FLOAT
    - Python dtype: float
- sharpness
    - The " sharpness" parameter is responsible for increasing the edges of the image and making it clearer. It is important for improving the clarity of the image, especially when the image appears to be blurred or the focus is not clear. Adding sharpness can make the details more visible.
    - Comfy dtype: FLOAT
    - Python dtype: float
- blur
    - The " fuzzy" parameter applies fuzzy effects to images, which can be used to create deep senses or deliberately soften images. In a scenario that requires less sharp appearances, it is important, for example, for aesthetic purposes or to reduce image noise.
    - Comfy dtype: INT
    - Python dtype: int
- gaussian_blur
    - The Gaussian Blur parameter applies Gaussian blurry to images, which is a smoothing technique that reduces detail and noise. It is particularly suitable for creating smooth, blurred appearances, and is controlled by the radius of the fuzzy effect.
    - Comfy dtype: FLOAT
    - Python dtype: float
- edge_enhance
    - The'marginal enhancement' parameter is used to highlight the edges of the image, making them more visible. It plays an important role in highlighting the details and can be creatively used to change the visual style of the image.
    - Comfy dtype: FLOAT
    - Python dtype: float
- detail_enhance
    - The 'Friends Up' parameter, when set to True, uses the image details to enhance filters. This makes the delicate details more visible, especially for images that require greater clarity and definition.
    - Comfy dtype: COMBO['false', 'true']
    - Python dtype: Union[str, Literal['false', 'true']]

# Output types
- output_image
    - The 'output_image'parameter represents the application of all treated images after a given filter. It is the highest performance of the node function and contains the results of the image processing process. This output is important because it is the node's main deliverer, reflecting the collective impact of all adjustments.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Image_Filters:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'image': ('IMAGE',), 'brightness': ('FLOAT', {'default': 0.0, 'min': -1.0, 'max': 1.0, 'step': 0.01}), 'contrast': ('FLOAT', {'default': 1.0, 'min': -1.0, 'max': 2.0, 'step': 0.01}), 'saturation': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 5.0, 'step': 0.01}), 'sharpness': ('FLOAT', {'default': 1.0, 'min': -5.0, 'max': 5.0, 'step': 0.01}), 'blur': ('INT', {'default': 0, 'min': 0, 'max': 16, 'step': 1}), 'gaussian_blur': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1024.0, 'step': 0.1}), 'edge_enhance': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'detail_enhance': (['false', 'true'],)}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'image_filters'
    CATEGORY = 'WAS Suite/Image/Filter'

    def image_filters(self, image, brightness, contrast, saturation, sharpness, blur, gaussian_blur, edge_enhance, detail_enhance):
        tensors = []
        if len(image) > 1:
            for img in image:
                pil_image = None
                if brightness > 0.0 or brightness < 0.0:
                    img = np.clip(img + brightness, 0.0, 1.0)
                if contrast > 1.0 or contrast < 1.0:
                    img = np.clip(img * contrast, 0.0, 1.0)
                if saturation > 1.0 or saturation < 1.0:
                    pil_image = tensor2pil(img)
                    pil_image = ImageEnhance.Color(pil_image).enhance(saturation)
                if sharpness > 1.0 or sharpness < 1.0:
                    pil_image = pil_image if pil_image else tensor2pil(img)
                    pil_image = ImageEnhance.Sharpness(pil_image).enhance(sharpness)
                if blur > 0:
                    pil_image = pil_image if pil_image else tensor2pil(img)
                    for _ in range(blur):
                        pil_image = pil_image.filter(ImageFilter.BLUR)
                if gaussian_blur > 0.0:
                    pil_image = pil_image if pil_image else tensor2pil(img)
                    pil_image = pil_image.filter(ImageFilter.GaussianBlur(radius=gaussian_blur))
                if edge_enhance > 0.0:
                    pil_image = pil_image if pil_image else tensor2pil(img)
                    edge_enhanced_img = pil_image.filter(ImageFilter.EDGE_ENHANCE_MORE)
                    blend_mask = Image.new(mode='L', size=pil_image.size, color=round(edge_enhance * 255))
                    pil_image = Image.composite(edge_enhanced_img, pil_image, blend_mask)
                    del blend_mask, edge_enhanced_img
                if detail_enhance == 'true':
                    pil_image = pil_image if pil_image else tensor2pil(img)
                    pil_image = pil_image.filter(ImageFilter.DETAIL)
                out_image = pil2tensor(pil_image) if pil_image else img
                tensors.append(out_image)
            tensors = torch.cat(tensors, dim=0)
        else:
            pil_image = None
            img = image
            if brightness > 0.0 or brightness < 0.0:
                img = np.clip(img + brightness, 0.0, 1.0)
            if contrast > 1.0 or contrast < 1.0:
                img = np.clip(img * contrast, 0.0, 1.0)
            if saturation > 1.0 or saturation < 1.0:
                pil_image = tensor2pil(img)
                pil_image = ImageEnhance.Color(pil_image).enhance(saturation)
            if sharpness > 1.0 or sharpness < 1.0:
                pil_image = pil_image if pil_image else tensor2pil(img)
                pil_image = ImageEnhance.Sharpness(pil_image).enhance(sharpness)
            if blur > 0:
                pil_image = pil_image if pil_image else tensor2pil(img)
                for _ in range(blur):
                    pil_image = pil_image.filter(ImageFilter.BLUR)
            if gaussian_blur > 0.0:
                pil_image = pil_image if pil_image else tensor2pil(img)
                pil_image = pil_image.filter(ImageFilter.GaussianBlur(radius=gaussian_blur))
            if edge_enhance > 0.0:
                pil_image = pil_image if pil_image else tensor2pil(img)
                edge_enhanced_img = pil_image.filter(ImageFilter.EDGE_ENHANCE_MORE)
                blend_mask = Image.new(mode='L', size=pil_image.size, color=round(edge_enhance * 255))
                pil_image = Image.composite(edge_enhanced_img, pil_image, blend_mask)
                del blend_mask, edge_enhanced_img
            if detail_enhance == 'true':
                pil_image = pil_image if pil_image else tensor2pil(img)
                pil_image = pil_image.filter(ImageFilter.DETAIL)
            out_image = pil2tensor(pil_image) if pil_image else img
            tensors = out_image
        return (tensors,)
```