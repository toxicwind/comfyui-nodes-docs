# Documentation
- Class name: FaceParse
- Category: face_parsing
- Output node: False
- Repo Ref: https://github.com/Ryuukeisyou/comfyui_face_parsing

The FaceParse node is designed to analyse and deconstruct facial features from imported images. It uses pre-trained models to identify and separate elements of the face, such as eyes, nose and mouth. The main function of the node is to convert the input image into a detailed facial profile map, which can be used for further analysis or visualization. This process enhances understanding of face structures and is very useful for applications such as facial facial recognition or facial characterization.

# Input types
## Required
- model
    - Model parameters are essential for the FaceParse node because it defines pre-trained neural network structures for facial resolution. It is the basis for node functions that allow facial features to be identified and separated. Node cannot perform its intended task without a model.
    - Comfy dtype: FACE_PARSING_MODEL
    - Python dtype: torch.nn.Module
- processor
    - Processor parameters are essential for pre-processing the image input in compatible model format. It ensures that the image format is correct and prepares the model for facial resolution. The processor is the key component that enables the model to process input effectively.
    - Comfy dtype: FACE_PARSING_PROCESSOR
    - Python dtype: object
- image
    - The image parameter is the main input to the FaceParse node. It contains the facial image that needs to be analysed. The quality and resolution of the image directly influences the accuracy and detail of the facial resolution results.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Output types
- IMAGE
    - The output image is visualized by facial resolution results, with different facial features highlighted in different colours. This provides a visual understanding of the accuracy of facial structure and model predictions.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- FACE_PARSING_RESULT
    - The facial resolution results in a partition of the input image, in which each pixel is assigned a label corresponding to a particular facial feature. This output is essential for further analysis and can be used for various applications, such as facial facial profiling or facial characterization tracking.
    - Comfy dtype: FACE_PARSING_RESULT
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class FaceParse:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'model': ('FACE_PARSING_MODEL', {}), 'processor': ('FACE_PARSING_PROCESSOR', {}), 'image': ('IMAGE', {})}}
    RETURN_TYPES = ('IMAGE', 'FACE_PARSING_RESULT')
    FUNCTION = 'main'
    CATEGORY = 'face_parsing'

    def main(self, model, processor, image: Tensor):
        images = []
        results = []
        transform = T.ToPILImage()
        colormap = cm.get_cmap('viridis', 19)
        for item in image:
            size = item.shape[:2]
            inputs = processor(images=transform(item.permute(2, 0, 1)), return_tensors='pt')
            outputs = model(**inputs)
            logits = outputs.logits.cpu()
            upsampled_logits = nn.functional.interpolate(logits, size=size, mode='bilinear', align_corners=False)
            pred_seg = upsampled_logits.argmax(dim=1)[0]
            pred_seg_np = pred_seg.detach().numpy().astype(np.uint8)
            results.append(torch.tensor(pred_seg_np))
            colored = colormap(pred_seg_np)
            colored_sliced = colored[:, :, :3]
            images.append(torch.tensor(colored_sliced))
        return (torch.cat(images, dim=0).unsqueeze(0), torch.cat(results, dim=0).unsqueeze(0))
```