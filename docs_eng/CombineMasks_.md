# Documentation
- Class name: CombineMasks
- Category: ♾️Mixlab/Mask
- Output node: False
- Repo Ref: https://github.com/shadowcz007/comfyui-CLIPSeg

Combine Masks is a node designed to integrate multiple mask loads into a comprehensive mask, which enhances the representation of bottom data. The node not only consolidates the mask, but also generates visual expressions such as heat maps and double-value stacks, providing a more detailed analysis of the mask content.

# Input types
## Required
- input_image
    - Entering the image parameter is essential because it serves as the base layer for the masking process. It provides the spatial context that is needed for the node to rightly add and visualize the mask.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- mask_1
    - The first mask is an integral part of the integration process, representing the initial segmentation of the information layer that will be enhanced with the follow-up mask.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor
- mask_2
    - The second mask adds additional compartments and contributes to the complexity and detail of the combination mask.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor
## Optional
- mask_3
    - An optional third mask enhances the expression of the overall mask by introducing more detail on the finer particle size.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Output types
- Combined Mask
    - The combination mask is the main output of the node and represents the result of all input mask integration into a single, uniform expression.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor
- Heatmap Mask
    - The thermal mask visualizes the group split, provides colour representation and enhances the interpretability and analysis of the split results.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- BW Mask
    - A two-value mask provides a simplified black and white view that emphasizes core elements and provides a clear and direct analytical tool.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class CombineMasks:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'input_image': ('IMAGE',), 'mask_1': ('MASK',), 'mask_2': ('MASK',)}, 'optional': {'mask_3': ('MASK',)}}
    CATEGORY = '♾️Mixlab/Mask'
    RETURN_TYPES = ('MASK', 'IMAGE', 'IMAGE')
    RETURN_NAMES = ('Combined Mask', 'Heatmap Mask', 'BW Mask')
    FUNCTION = 'combine_masks'

    def combine_masks(self, input_image: torch.Tensor, mask_1: torch.Tensor, mask_2: torch.Tensor, mask_3: Optional[torch.Tensor]=None) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
        """A method that combines two or three masks into one mask. Takes in tensors and returns the mask as a tensor, as well as the heatmap and binary mask as tensors."""
        if mask_1 is not None:
            mask_1 = mask_1.squeeze()
        if mask_2 is not None:
            mask_2 = mask_2.squeeze()
        if mask_3 is not None:
            mask_3 = mask_3.squeeze()
        print(mask_1.shape, mask_2.shape, mask_3.shape)
        combined_mask = mask_1 + mask_2 + mask_3 if mask_3 is not None else mask_1 + mask_2
        image_np = tensor_to_numpy(input_image)
        heatmap = apply_colormap(combined_mask, cm.viridis)
        binary_mask = apply_colormap(combined_mask, cm.Greys_r)
        dimensions = (image_np.shape[1], image_np.shape[0])
        if dimensions is None or dimensions[0] == 0 or dimensions[1] == 0:
            raise ValueError('Invalid dimensions')
        heatmap_resized = resize_image(heatmap, dimensions)
        binary_mask_resized = resize_image(binary_mask, dimensions)
        (alpha_heatmap, alpha_binary) = (0.5, 1)
        overlay_heatmap = overlay_image(image_np, heatmap_resized, alpha_heatmap)
        overlay_binary = overlay_image(image_np, binary_mask_resized, alpha_binary)
        image_out_heatmap = numpy_to_tensor(overlay_heatmap)
        image_out_binary = numpy_to_tensor(overlay_binary)
        return (combined_mask, image_out_heatmap, image_out_binary)
```