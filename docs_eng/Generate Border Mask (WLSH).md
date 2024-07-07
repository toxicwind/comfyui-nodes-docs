# Documentation
- Class name: WLSH_Generate_Edge_Mask
- Category: WLSH Nodes/inpainting
- Output node: False
- Repo Ref: https://github.com/wallish77/wlsh_nodes

The WLSH_Generate_Edge_Mask node is responsible for generating a border mask based on the given direction and image. It creates a mask that can be used to repair the task and ensure that the hidden area is aligned with the given direction, such as 'up', 'down', 'left' or 'right'. The function of the node is essential for the application of image processing that requires selective cover.

# Input types
## Required
- image
    - An image parameter is essential for the node because it is the basis for generating a border mask. The node processes the image to create a mask corresponding to the given direction, which plays a key role in the overall function of the node.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- direction
    - The direction parameter determines the direction of the mask to be generated. It is a key input, because it determines how the mask will be applied to the image and influences the final outcome of the restoration process.
    - Comfy dtype: STRING
    - Python dtype: str
- pixels
    - The pixel parameter specifies the size of the edge of the mask in pixels, which is an important factor in controlling the range of the mask area. This parameter directly affects the execution of the node and the accuracy of the mask generated.
    - Comfy dtype: INT
    - Python dtype: int
- overlap
    - Overlapping parameters define the thickness of the masked edges, which is important to ensure smooth transitions between the sheltered and unshielded areas. It helps to improve the quality of repair results by preventing border mutations.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- mask
    - The output mask is the key result of node operations. It represents the area to be repaired and its quality and alignment directly influences the final image output.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class WLSH_Generate_Edge_Mask:
    directions = ['left', 'right', 'up', 'down']

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'direction': (s.directions,), 'pixels': ('INT', {'default': 128, 'min': 32, 'max': 512, 'step': 32}), 'overlap': ('INT', {'default': 64, 'min': 16, 'max': 256, 'step': 16})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'gen_second_mask'
    CATEGORY = 'WLSH Nodes/inpainting'

    def gen_second_mask(self, direction, image, pixels, overlap):
        image = tensor2pil(image)
        (new_width, new_height) = image.size
        mask2 = Image.new('RGBA', (new_width, new_height), (0, 0, 0, 255))
        mask_thickness = overlap
        if direction == 'up':
            new_mask = Image.new('RGBA', (new_width, mask_thickness), (0, 122, 0, 255))
            mask2.paste(new_mask, (0, pixels - int(mask_thickness / 2)))
        elif direction == 'down':
            new_mask = Image.new('RGBA', (new_width, mask_thickness), (0, 122, 0, 255))
            mask2.paste(new_mask, (0, new_height - pixels - int(mask_thickness / 2)))
        elif direction == 'left':
            new_mask = Image.new('RGBA', (mask_thickness, new_height), (0, 122, 0, 255))
            mask2.paste(new_mask, (pixels - int(mask_thickness / 2), 0))
        elif direction == 'right':
            new_mask = Image.new('RGBA', (mask_thickness, new_height), (0, 122, 0, 255))
            mask2.paste(new_mask, (new_width - pixels - int(mask_thickness / 2), 0))
        mask2 = mask2.filter(ImageFilter.GaussianBlur(radius=5))
        mask2 = np.array(mask2).astype(np.float32) / 255.0
        mask2 = torch.from_numpy(mask2)[None,]
        return (mask2,)
```