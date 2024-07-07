# Documentation
- Class name: GroundingDinoSAMSegment
- Category: segment_anything
- Output node: False
- Repo Ref: https://github.com/storyicon/comfyui_segment_anything

The GroundingDinoSAMSegment node is designed to treat images by dividing images based on text tips. It uses the capabilities of the SAM (Segment Anything Model) and GroupingDino models to identify and isolate objects in images, providing a partitioned image and its corresponding mask. This node is particularly suitable for applications that need to understand object levels from visual and text input.

# Input types
## Required
- sam_model
    - The SAM model is essential to the split process, providing the core function of identifying and separating objects in the image. It plays a key role in the ability to perform precise partitions based on input images and tips.
    - Comfy dtype: SAM_MODEL
    - Python dtype: torch.nn.Module
- grounding_dino_model
    - The GroundingDino model is used to predict the boundary box of the object in the image based on a texttip. It is a key component of the initial object detection step and provides the basis for the subsequent split process.
    - Comfy dtype: GROUNDING_DINO_MODEL
    - Python dtype: torch.nn.Module
- image
    - Enter the image as the main data source for node operations. It is the object of the split process, and the node is designed to identify and separate the objects in question according to the tips provided.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- prompt
    - A reminder as a text description guides the node to identify objects of interest in the image. It is an important input that helps the node to focus its split on the relevant parts of the image.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- threshold
    - The threshold parameter is used to determine the confidence level of the object's detection. It affects the node to determine which objects are to be separated based on the grounding prediction and allows control of the objects included in the final output.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- IMAGE
    - The output image is the result of the partition process, which shows the objects that are separated from the input image. It represents the main visual output of the node, highlighting the success of the partition based on the tips and modelling capabilities provided.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- MASK
    - The mask output provides a split binary representation that outlines the precise areas in the image that correspond to the split object. It is a key component for an application that requires detailed object drawings.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class GroundingDinoSAMSegment:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'sam_model': ('SAM_MODEL', {}), 'grounding_dino_model': ('GROUNDING_DINO_MODEL', {}), 'image': ('IMAGE', {}), 'prompt': ('STRING', {}), 'threshold': ('FLOAT', {'default': 0.3, 'min': 0, 'max': 1.0, 'step': 0.01})}}
    CATEGORY = 'segment_anything'
    FUNCTION = 'main'
    RETURN_TYPES = ('IMAGE', 'MASK')

    def main(self, grounding_dino_model, sam_model, image, prompt, threshold):
        res_images = []
        res_masks = []
        for item in image:
            item = Image.fromarray(np.clip(255.0 * item.cpu().numpy(), 0, 255).astype(np.uint8)).convert('RGBA')
            boxes = groundingdino_predict(grounding_dino_model, item, prompt, threshold)
            if boxes.shape[0] == 0:
                break
            (images, masks) = sam_segment(sam_model, item, boxes)
            res_images.extend(images)
            res_masks.extend(masks)
        if len(res_images) == 0:
            (_, height, width, _) = image.size()
            empty_mask = torch.zeros((1, height, width), dtype=torch.uint8, device='cpu')
            return (empty_mask, empty_mask)
        return (torch.cat(res_images, dim=0), torch.cat(res_masks, dim=0))
```