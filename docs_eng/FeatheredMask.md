# Documentation
- Class name: FeatheredMask
- Category: ♾️Mixlab/Mask
- Output node: False
- Repo Ref: https://github.com/shadowcz007/comfyui-mixlab-nodes.git

The Feiathered Mask node is designed to integrate the masked edges more naturally and seamlessly with the surrounding image content by applying the plume effect to process and enhance the mask image. The node accepts the input mask and fine-tunes it to create a more natural and seamless mix.

# Input types
## Required
- mask
    - The `mask' parameter is the main input of the node, representing the image mask to be processed. It plays a key role in determining the final output of the node, as the plume effect is applied directly to the mask.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- start_offset
    - The `start_offset' parameter controls the initial distance from the edge of the mask to the effect of fumigation. It is important because it determines the starting point of smooth transition and thus affects the overall appearance of the mask.
    - Comfy dtype: INT
    - Python dtype: int
- feathering_weight
    - The 'feathering_weight' parameter adjusts the intensity of the plume effect. It is important because it allows fine-tuning of the softness and mixing of the edges to ensure that the results are visually pleasurable.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- masks
    - The `masks' output contains a masked image of the fumigation effect that has been applied. It is important because it represents the final product of node operations, which can be further used or displayed.
    - Comfy dtype: LIST[IMAGE]
    - Python dtype: List[torch.Tensor]

# Usage tips
- Infra type: CPU

# Source code
```
class FeatheredMask:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'mask': ('MASK',), 'start_offset': ('INT', {'default': 1, 'min': -150, 'max': 150, 'step': 1, 'display': 'slider'}), 'feathering_weight': ('FLOAT', {'default': 0.1, 'min': 0.0, 'max': 1, 'step': 0.1, 'display': 'slider'})}}
    RETURN_TYPES = ('MASK',)
    FUNCTION = 'run'
    CATEGORY = '♾️Mixlab/Mask'
    OUTPUT_IS_LIST = (True,)

    def run(self, mask, start_offset, feathering_weight):
        (num, _, _) = mask.size()
        masks = []
        for i in range(num):
            mm = mask[i]
            image = tensor2pil(mm)
            image = image.convert('L')
            if start_offset > 0:
                image = ImageOps.invert(image)
            image_np = np.array(image)
            edges = cv2.Canny(image_np, 30, 150)
            for i in range(0, abs(start_offset)):
                a = int(abs(start_offset) * 0.1 * i)
                kernel = np.ones((a, a), np.uint8)
                dilated_edges = cv2.dilate(edges, kernel, iterations=1)
                smoothed_edges = cv2.GaussianBlur(dilated_edges, (5, 5), 0)
                feathering_weight = max(0, min(feathering_weight, 1))
                image_np = cv2.addWeighted(image_np, 1, smoothed_edges, feathering_weight, feathering_weight)
            result_image = Image.fromarray(np.uint8(image_np))
            result_image = result_image.convert('L')
            if start_offset > 0:
                result_image = ImageOps.invert(result_image)
            result_image = result_image.convert('L')
            mt = pil2tensor(result_image)
            masks.append(mt)
        return (masks,)
```