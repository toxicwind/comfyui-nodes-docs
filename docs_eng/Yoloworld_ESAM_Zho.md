# Documentation
- Class name: Yoloworld_ESAM_Zho
- Category: YOLOWORLD_ESAM
- Output node: False
- Repo Ref: https://github.com/ZHO-ZHO-ZHO/ComfyUI-YoloWorld-EfficientSAM.git

The Yoloworld_ESAM_Zho class encapsulates the integration of YOLO target testing with ESAM. It is designed to provide a comprehensive analysis of images by identifying and classifying objects in images, and by dividing them based on detected categories. The node contributes to the overall process by enhancing understanding of visual content, which is essential for applications that require detailed analysis of images.

# Input types
## Required
- yolo_world_model
    - The YOLO World Model is essential for the target detection process. It identifies and classifies the objects in the image. The accuracy and efficiency of the model directly influences the ability of nodes to process images and produce accurate results.
    - Comfy dtype: YOLOWORLDMODEL
    - Python dtype: YOLOWorldModel
- esam_model
    - The ESAM model is essential to the split process. It is subject to detection and further refines the understanding of their spatial distribution in the image. The performance of the model is essential for achieving detailed and precise partitioning of the mask.
    - Comfy dtype: ESAMMODEL
    - Python dtype: ESAMModel
- image
    - Images are the main input of nodes. They are the objects of the detection and partition process. The quality and resolution of images directly influence the accuracy and reliability of the results.
    - Comfy dtype: IMAGE
    - Python dtype: List[cv2.ndarray]
- categories
    - Category defines the categories that the models will identify in the image. They are essential to guide the detection and partition process, ensuring that nodes are focused on the object.
    - Comfy dtype: STRING
    - Python dtype: List[str]
## Optional
- confidence_threshold
    - The confidence threshold filters the results of a test that does not reach a certain level of confidence. It plays an important role in managing the trade-off between sensitivity and specificity, thus affecting the overall quality of the results.
    - Comfy dtype: FLOAT
    - Python dtype: float
- iou_threshold
    - The IoU threshold is used in the non-extreme inhibition (NMS) process to eliminate redundant detection. It affects the ability of nodes to produce a clean and accurate detection set by reducing the overlap area.
    - Comfy dtype: FLOAT
    - Python dtype: float
- box_thickness
    - The thickness of the border determines the visual prominence of the boundary frame around the object. It affects the beauty and clarity of the annotated image, which is important for visual analysis and interpretation.
    - Comfy dtype: INT
    - Python dtype: int
- text_thickness
    - Text thickness affects the visibility of class labels drawn on the annotated image. It is important to ensure that the labels are easy to read and contribute to a comprehensive understanding of the image content.
    - Comfy dtype: INT
    - Python dtype: int
- text_scale
    - Text zooms to adjust the size of the category label to affect the readability and visual balance of the annotated image. It is a key factor in creating both informative and visually attractive notes.
    - Comfy dtype: FLOAT
    - Python dtype: float
- with_confidence
    - When this parameter is enabled, a confidence score is added to the category label to provide an additional layer of information on the reliability of the results. This is essential for the decision-making process that relies on the certainty of the results.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- with_class_agnostic_nms
    - Activate this parameter by applying an unknown non-extreme inhibition (NMS) of the type of test result, which helps to reduce the overlap box between the different categories. It improves the overall presentation of the test results by ensuring that the boundary frame is cleaner and more organized.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- with_segmentation
    - When this parameter is enabled, the node divides the detected object to provide a detailed visual description of its shape and boundary. This enhances understanding of the image content and is particularly useful for applications that require precise object drawings.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- mask_combined
    - This parameter controls whether the partition mask is merged into a single mask that represents all the objects detected. This is useful for the collective spatial distribution of objects in visualized images.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- mask_extracted
    - Enable this parameter to allow the extraction of a separate partition mask for each detected object, providing a fine control for the individual operation or analysis of each object, which is particularly useful for applications requiring individual processing or analysis of each object.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- mask_extracted_index
    - This parameter specifies an index of the split mask that is extracted when a separate mask is required. It is essential for the object to be concentrated for further processing or analysis.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- processed_images
    - The processed images are the output of the application target detection and partitioning nodes. They include notes such as boundary frames and labels, which provide visual indications of the detection and separation of objects. These images are essential for visual analysis and validation of the performance of the nodes.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- processed_masks
    - The treated mask is a split output that outlines the precise boundaries of the object detected. They are important for applications that require detailed spatial information about the object in the image, for example, in medical imaging or autopilot vehicle navigation.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class Yoloworld_ESAM_Zho:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'yolo_world_model': ('YOLOWORLDMODEL',), 'esam_model': ('ESAMMODEL',), 'image': ('IMAGE',), 'categories': ('STRING', {'default': 'person, bicycle, car, motorcycle, airplane, bus, train, truck, boat', 'multiline': True}), 'confidence_threshold': ('FLOAT', {'default': 0.1, 'min': 0, 'max': 1, 'step': 0.01}), 'iou_threshold': ('FLOAT', {'default': 0.1, 'min': 0, 'max': 1, 'step': 0.01}), 'box_thickness': ('INT', {'default': 2, 'min': 1, 'max': 5}), 'text_thickness': ('INT', {'default': 2, 'min': 1, 'max': 5}), 'text_scale': ('FLOAT', {'default': 1.0, 'min': 0, 'max': 1, 'step': 0.01}), 'with_confidence': ('BOOLEAN', {'default': True}), 'with_class_agnostic_nms': ('BOOLEAN', {'default': False}), 'with_segmentation': ('BOOLEAN', {'default': True}), 'mask_combined': ('BOOLEAN', {'default': True}), 'mask_extracted': ('BOOLEAN', {'default': True}), 'mask_extracted_index': ('INT', {'default': 0, 'min': 0, 'max': 1000})}}
    RETURN_TYPES = ('IMAGE', 'MASK')
    FUNCTION = 'yoloworld_esam_image'
    CATEGORY = 'YOLOWORLD_ESAM'

    def yoloworld_esam_image(self, image, yolo_world_model, esam_model, categories, confidence_threshold, iou_threshold, box_thickness, text_thickness, text_scale, with_segmentation, mask_combined, with_confidence, with_class_agnostic_nms, mask_extracted, mask_extracted_index):
        categories = process_categories(categories)
        processed_images = []
        processed_masks = []
        for img in image:
            img = np.clip(255.0 * img.cpu().numpy().squeeze(), 0, 255).astype(np.uint8)
            YOLO_WORLD_MODEL = yolo_world_model
            YOLO_WORLD_MODEL.set_classes(categories)
            results = YOLO_WORLD_MODEL.infer(img, confidence=confidence_threshold)
            detections = sv.Detections.from_inference(results)
            detections = detections.with_nms(class_agnostic=with_class_agnostic_nms, threshold=iou_threshold)
            combined_mask = None
            if with_segmentation:
                detections.mask = inference_with_boxes(image=img, xyxy=detections.xyxy, model=esam_model, device=DEVICE)
                if mask_combined:
                    combined_mask = np.zeros(img.shape[:2], dtype=np.uint8)
                    det_mask = detections.mask
                    for mask in det_mask:
                        combined_mask = np.logical_or(combined_mask, mask).astype(np.uint8)
                    masks_tensor = torch.tensor(combined_mask, dtype=torch.float32)
                    processed_masks.append(masks_tensor)
                else:
                    det_mask = detections.mask
                    if mask_extracted:
                        mask_index = mask_extracted_index
                        selected_mask = det_mask[mask_index]
                        masks_tensor = torch.tensor(selected_mask, dtype=torch.float32)
                    else:
                        masks_tensor = torch.tensor(det_mask, dtype=torch.float32)
                    processed_masks.append(masks_tensor)
            output_image = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
            output_image = annotate_image(input_image=output_image, detections=detections, categories=categories, with_confidence=with_confidence, thickness=box_thickness, text_thickness=text_thickness, text_scale=text_scale)
            output_image = cv2.cvtColor(output_image, cv2.COLOR_BGR2RGB)
            output_image = torch.from_numpy(output_image.astype(np.float32) / 255.0).unsqueeze(0)
            processed_images.append(output_image)
        new_ims = torch.cat(processed_images, dim=0)
        if processed_masks:
            new_masks = torch.stack(processed_masks, dim=0)
        else:
            new_masks = torch.empty(0)
        return (new_ims, new_masks)
```