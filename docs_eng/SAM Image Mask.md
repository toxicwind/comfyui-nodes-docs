# Documentation
- Class name: WAS_SAM_Image_Mask
- Category: WAS Suite/Image/Masking
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The `sam_image_mask'method of the WAS_SAM_Image_Mask node is designed to apply semantic sensitisation models to input images and generate the corresponding mask. It predicts partitions using the SAM (Semantitic Aware Masking) model, and then uses the partition to create mask coverage on the original image. This method is essential for the application of specific areas in the image to be identified and isolated for further analysis or operation.

# Input types
## Required
- sam_model
    - The parameter `sam_model'is essential because it indicates a semantic sense partition model that will be used to process the input image. This is a key component that determines the quality and accuracy of the mask generated.
    - Comfy dtype: SAM_MODEL
    - Python dtype: torch.nn.Module
- sam_parameters
    - The parameter `sam_parameters'contains the points and labels needed for the SAM model to perform the split. This is a key input that directly affects the results of the split process.
    - Comfy dtype: SAM_PARAMETERS
    - Python dtype: Dict[str, Any]
- image
    - The parameter `image'is the input image that will be processed by the SAM model to generate the mask. It is the main data source for node operations in a format that significantly influences the split result.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Output types
- image
    - Output `image'is the original input image with predictive mask coverage. It represents the visual results of the semantic sense partitioning process and allows direct visual examination of the mask area.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- mask
    - Output `mask'is a binary expression that divides the mask, highlighting the area identified by the SAM model. It is important for applications that require more precise handling or analysis of a given image area.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class WAS_SAM_Image_Mask:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        return {'required': {'sam_model': ('SAM_MODEL',), 'sam_parameters': ('SAM_PARAMETERS',), 'image': ('IMAGE',)}}
    RETURN_TYPES = ('IMAGE', 'MASK')
    FUNCTION = 'sam_image_mask'
    CATEGORY = 'WAS Suite/Image/Masking'

    def sam_image_mask(self, sam_model, sam_parameters, image):
        image = tensor2sam(image)
        points = sam_parameters['points']
        labels = sam_parameters['labels']
        from segment_anything import SamPredictor
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        sam_model.to(device=device)
        predictor = SamPredictor(sam_model)
        predictor.set_image(image)
        (masks, scores, logits) = predictor.predict(point_coords=points, point_labels=labels, multimask_output=False)
        sam_model.to(device='cpu')
        mask = np.expand_dims(masks, axis=-1)
        image = np.repeat(mask, 3, axis=-1)
        image = torch.from_numpy(image)
        mask = torch.from_numpy(mask)
        mask = mask.squeeze(2)
        mask = mask.squeeze().to(torch.float32)
        return (image, mask)
```