# Documentation
- Class name: JagsCombineMasks
- Category: Jags_vector/CLIPSEG
- Output node: False
- Repo Ref: https://github.com/jags111/ComfyUI_Jags_VectorMagic

The node integrates multiple masks into a uniform form of representation, facilitating the integration of partitions in the given image context. It aims to simplify the process of combining binary or disaggregated data into consistent visual output and to enhance the usefulness of mask-based image processing tasks.

# Input types
## Required
- input_image
    - The role of the input image as the base layer for the consolidation and visualization mask is crucial, as it provides the spatial context required for the accurate stacking and integration of the mask.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- mask_1
    - The main mask is a key component in the integration process, defining the initial split and laying the basis for subsequent additions to the other mask.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor
- mask_2
    - Submasks improve the particle size and specificity of the final output by introducing additional partitions to perfect the merger mask.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor
## Optional
- mask_3
    - The third possible mask provides an additional dimension to the combination of the mask, allowing for more complex and detailed partitions when required.
    - Comfy dtype: MASK
    - Python dtype: Optional[torch.Tensor]

# Output types
- Combined Mask
    - The resulting merger mask contains the group partition information for the input mask as a composite of the elements for the partition in the image.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor
- Heatmap Mask
    - The thermal mask is separated by colour stacking and visualization, providing a visual and easily interpretable description of the partition result.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- BW Mask
    - The double mask provides a clear, high contrast split, highlighting the divided areas in a clear and precise manner.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class JagsCombineMasks:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'input_image': ('IMAGE',), 'mask_1': ('MASK',), 'mask_2': ('MASK',)}, 'optional': {'mask_3': ('MASK',)}}
    CATEGORY = 'Jags_vector/CLIPSEG'
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
        combined_mask = mask_1 + mask_2 + mask_3 if mask_3 is not None else mask_1 + mask_2
        image_np = tensor_to_numpy(input_image)
        heatmap = apply_colormap(combined_mask, cm.viridis)
        binary_mask = apply_colormap(combined_mask, cm.Greys_r)
        dimensions = (image_np.shape[1], image_np.shape[0])
        print('heatmap', heatmap)
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