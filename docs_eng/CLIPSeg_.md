# Documentation
- Class name: CLIPSeg
- Category: ♾️Mixlab/Mask
- Output node: False
- Repo Ref: https://github.com/shadowcz007/comfyui-CLIPSeg

CLIPSeg is designed to divide images using text tips and image input. It uses the power of the CLIPSeg model to create partition masks consistent with the text description provided. The node is good at generating masks that can be further processed for various applications, such as object identification, image editing and data analysis.

# Input types
## Required
- image
    - The image parameter is essential for the operation of the node, as it is the main input to the split. It determines the content to be analysed and divided according to the texttips provided.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- text
    - Text parameters are necessary because they provide descriptive tips to guide the split process. It allows nodes to focus on specific elements of the image that are relevant to the description of the text.
    - Comfy dtype: STRING
    - Python dtype: str
- blur
    - Fuzzy parameters allow the smoothness of the partition mask to be adjusted. It helps to fine-tune the edge of the mask and improves the overall quality of the partition.
    - Comfy dtype: FLOAT
    - Python dtype: float
- threshold
    - The threshold parameter is used to convert a continuous split mask to a binary mask. It determines the cut-off point between the split object and the background.
    - Comfy dtype: FLOAT
    - Python dtype: float
- dilation_factor
    - The inflation factor is important to extend the boundary that divides the mask. It can be used to ensure that the area covers all the objects.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- Mask
    - The mask output provides a binary partition mask from the image partitioning process. This is a key output for applications that require object identification or separation from background.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- Heatmap Mask
    - The thermal mask output is the visual expression of the partition mask, in which the intensity of the colour corresponds to the confidence level of the partition. It applies to visual analysis and debugging purposes.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- BW Mask
    - Black and white mask output is a binary version of the partition mask, which provides a direct distinction between the object and the background of the split. It is usually used for further processing or as a simplified expression of the split.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class CLIPSeg:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        """
            Return a dictionary which contains config for all input fields.
            Some types (string): "MODEL", "VAE", "CLIP", "CONDITIONING", "LATENT", "IMAGE", "INT", "STRING", "FLOAT".
            Input types "INT", "STRING" or "FLOAT" are special values for fields on the node.
            The type can be a list for selection.

            Returns: `dict`:
                - Key input_fields_group (`string`): Can be either required, hidden or optional. A node class must have property `required`
                - Value input_fields (`dict`): Contains input fields config:
                    * Key field_name (`string`): Name of a entry-point method's argument
                    * Value field_config (`tuple`):
                        + First value is a string indicate the type of field or a list for selection.
                        + Secound value is a config for type "INT", "STRING" or "FLOAT".
        """
        return {'required': {'image': ('IMAGE',), 'text': ('STRING', {'multiline': False, 'dynamicPrompts': False})}, 'optional': {'blur': ('FLOAT', {'min': 0, 'max': 15, 'step': 0.1, 'default': 3}), 'threshold': ('FLOAT', {'min': 0, 'max': 1, 'step': 0.05, 'default': 0.3}), 'dilation_factor': ('INT', {'min': 0, 'max': 10, 'step': 1, 'default': 4})}}
    CATEGORY = '♾️Mixlab/Mask'
    RETURN_TYPES = ('MASK', 'IMAGE', 'IMAGE')
    RETURN_NAMES = ('Mask', 'Heatmap Mask', 'BW Mask')
    OUTPUT_IS_LIST = (False, False, False)
    FUNCTION = 'segment_image'

    def segment_image(self, image: torch.Tensor, text: str, blur: float, threshold: float, dilation_factor: int) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
        """Create a segmentation mask from an image and a text prompt using CLIPSeg.

        Args:
            image (torch.Tensor): The image to segment.
            text (str): The text prompt to use for segmentation.
            blur (float): How much to blur the segmentation mask.
            threshold (float): The threshold to use for binarizing the segmentation mask.
            dilation_factor (int): How much to dilate the segmentation mask.

        Returns:
            Tuple[torch.Tensor, torch.Tensor, torch.Tensor]: The segmentation mask, the heatmap mask, and the binarized mask.
        """
        image_np = image.numpy().squeeze()
        image_np = (image_np * 255).astype(np.uint8)
        i = Image.fromarray(image_np, mode='RGB')
        processor = CLIPSegProcessor.from_pretrained(clipseg_model_dir)
        model = CLIPSegForImageSegmentation.from_pretrained(clipseg_model_dir)
        prompt = text
        input_prc = processor(text=prompt, images=i, padding='max_length', return_tensors='pt')
        with torch.no_grad():
            outputs = model(**input_prc)
        tensor = torch.sigmoid(outputs[0])
        thresh = threshold
        tensor_thresholded = torch.where(tensor > thresh, tensor, torch.tensor(0, dtype=torch.float))
        sigma = blur
        tensor_smoothed = gaussian_filter(tensor_thresholded.numpy(), sigma=sigma)
        tensor_smoothed = torch.from_numpy(tensor_smoothed)
        mask_normalized = (tensor_smoothed - tensor_smoothed.min()) / (tensor_smoothed.max() - tensor_smoothed.min())
        mask_dilated = dilate_mask(mask_normalized, dilation_factor)
        heatmap = apply_colormap(mask_dilated, cm.viridis)
        binary_mask = apply_colormap(mask_dilated, cm.Greys_r)
        dimensions = (image_np.shape[1], image_np.shape[0])
        heatmap_resized = resize_image(heatmap, dimensions)
        binary_mask_resized = resize_image(binary_mask, dimensions)
        (alpha_heatmap, alpha_binary) = (0.5, 1)
        overlay_heatmap = overlay_image(image_np, heatmap_resized, alpha_heatmap)
        overlay_binary = overlay_image(image_np, binary_mask_resized, alpha_binary)
        image_out_heatmap = numpy_to_tensor(overlay_heatmap)
        image_out_binary = numpy_to_tensor(overlay_binary)
        binary_mask_image = Image.fromarray(binary_mask_resized[..., 0])
        tensor_bw = binary_mask_image.convert('L')
        tensor_bw = pil2tensor(tensor_bw)
        return (tensor_bw, image_out_heatmap, image_out_binary)
```