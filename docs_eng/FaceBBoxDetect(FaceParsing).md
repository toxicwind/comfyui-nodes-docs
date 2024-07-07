# Documentation
- Class name: FaceBBoxDetect
- Category: face_parsing
- Output node: False
- Repo Ref: https://github.com/Ryuukeisyou/comfyui_face_parsing

FaceBoxDetec node is designed to identify and locate the face in the image using a pre-trained border frame detector. It processes the input image to detect the face and adjusts the boundary frame to ensure that they are within the image boundary, thus providing a list of refined facial boundary frames.

# Input types
## Required
- bbox_detector
    - The bbox_detector parameter is a pre-training model used to detect the surface boundary frame in the input image. It is essential for the function of the node, as it directly affects the accuracy and reliability of the facial testing process.
    - Comfy dtype: BBOX_DETECTOR
    - Python dtype: YOLO
- image
    - The image parameter indicates that the input image data will be performed for facial testing. It is critical because it is the primary source of information for node identification of facials.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- threshold
    - The xreshold parameter is used to set the confidence level of the facial test. It affects the decision whether the node is included in the final result, thus affecting the accuracy of the test.
    - Comfy dtype: FLOAT
    - Python dtype: float
- dilation
    - The dilation parameter is used to adjust the size of the detected border box. It is important because it helps to fine-tune the accuracy of the border frame coordinates to better fit the actual size of the face.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- bbox_list
    - The bbox_list output contains a list of refined boundary frames around the detected face. It is important because it represents the direct result of the facial testing process and provides valuable data for further analysis or processing.
    - Comfy dtype: BBOX_LIST
    - Python dtype: List[Tuple[int, int, int, int]]

# Usage tips
- Infra type: CPU

# Source code
```
class FaceBBoxDetect:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'bbox_detector': ('BBOX_DETECTOR', {}), 'image': ('IMAGE', {}), 'threshold': ('FLOAT', {'default': 0.3, 'min': 0, 'max': 1, 'step': 0.01}), 'dilation': ('INT', {'default': 8, 'min': -512, 'max': 512, 'step': 1})}}
    RETURN_TYPES = ('BBOX_LIST',)
    FUNCTION = 'main'
    CATEGORY = 'face_parsing'

    def main(self, bbox_detector: YOLO, image: Tensor, threshold: float, dilation: int):
        results = []
        transform = T.ToPILImage()
        for item in image:
            image_pil = transform(item.permute(2, 0, 1))
            pred = bbox_detector(image_pil, conf=threshold)
            bboxes = pred[0].boxes.xyxy.cpu()
            for bbox in bboxes:
                bbox[0] = bbox[0] - dilation
                bbox[1] = bbox[1] - dilation
                bbox[2] = bbox[2] + dilation
                bbox[3] = bbox[3] + dilation
                bbox[0] = bbox[0] if bbox[0] > 0 else 0
                bbox[1] = bbox[1] if bbox[1] > 0 else 0
                bbox[2] = bbox[2] if bbox[2] < item.shape[1] else item.shape[1]
                bbox[3] = bbox[3] if bbox[3] < item.shape[0] else item.shape[0]
                results.append(bbox)
        return (results,)
```