# Documentation
- Class name: MergeLayers
- Category: ♾️Mixlab/Layer
- Output node: False
- Repo Ref: https://github.com/shadowcz007/comfyui-mixlab-nodes.git

The MergeLayes node is designed to integrate multiple layers into the base image. It handles a series of images and corresponding layers, applies each layer to the base image, and the position is specified to be scalable and to generate a composite image and a mask that depicts a layered area.

# Input types
## Required
- layers
    - The 'layers' parameters are a list of dictionaries, each of which represents a layer that you want to merge into the underlying image. Each dictionary contains a layer of images, masks, and position properties that are essential for determining the ultimate combination of layered images.
    - Comfy dtype: COMBO[str]
    - Python dtype: List[Dict[str, Union[str, torch.Tensor]]]
- images
    - The 'images' parameter is to merge the base image list of the layer. Each image should be in a volume format, indicating the original pixel data that will be drawn as a layered process.
    - Comfy dtype: COMBO[torch.Tensor]
    - Python dtype: List[torch.Tensor]

# Output types
- IMAGE
    - The 'IMAGE' output is a volume that represents the final synthetic image formed by combining the input layer into the underlying image. It contains the visual results of the tiered process.
    - Comfy dtype: torch.Tensor
    - Python dtype: torch.Tensor
- MASK
    - The MASK output is a volume that represents the mask used in the stratification process. It is used to identify the stratification of the image, with clear layers.
    - Comfy dtype: torch.Tensor
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class MergeLayers:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'layers': ('LAYER',), 'images': ('IMAGE',)}}
    RETURN_TYPES = ('IMAGE', 'MASK')
    RETURN_NAMES = ('IMAGE', 'MASK')
    FUNCTION = 'run'
    CATEGORY = '♾️Mixlab/Layer'
    INPUT_IS_LIST = True

    def run(self, layers, images):
        bg_images = []
        masks = []
        for img in images:
            for bg_image in img:
                bg_image = tensor2pil(bg_image)
                layers_new = sorted(layers, key=lambda x: x['z_index'])
                (width, height) = bg_image.size
                final_mask = Image.new('L', (width, height), 0)
                for layer in layers_new:
                    image = layer['image']
                    mask = layer['mask']
                    if 'type' in layer and layer['type'] == 'base64' and (type(image) == str):
                        im = base64_to_image(image)
                        im = im.convert('RGB')
                        image = pil2tensor(im)
                        mask = base64_to_image(mask)
                        mask = mask.convert('L')
                        mask = pil2tensor(mask)
                    layer_image = tensor2pil(image)
                    layer_mask = tensor2pil(mask)
                    bg_image = merge_images(bg_image, layer_image, layer_mask, layer['x'], layer['y'], layer['width'], layer['height'], layer['scale_option'])
                    final_mask = merge_images(final_mask, layer_mask.convert('RGB'), layer_mask, layer['x'], layer['y'], layer['width'], layer['height'], layer['scale_option'])
                    final_mask = final_mask.convert('L')
                final_mask = pil2tensor(final_mask)
                bg_image = bg_image.convert('RGB')
                bg_image = pil2tensor(bg_image)
                bg_images.append(bg_image)
                masks.append(final_mask)
        bg_images = torch.cat(bg_images, dim=0)
        masks = torch.cat(masks, dim=0)
        return (bg_images, masks)
```