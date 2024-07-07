# Documentation
- Class name: YoloSegNode
- Category: Jags_vector/yoloSEG
- Output node: False
- Repo Ref: https://github.com/jags111/ComfyUI_Jags_VectorMagic

The node is designed to implement semantic partitions using models based on YOLO that identify and block examples of specific categories in the image. It processes the images that are entered to identify the categories required, and produces a split image and a corresponding mask that highlights the identified examples.

# Input types
## Required
- image
    - Entering images is essential for the partitioning of nodes. It is the primary data source for model analysis and identification of the specified categories.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image
- model_name
    - This parameter determines the specific YOLO model used for partitioning. It is vital because it determines the accuracy and validity of the partitioning process.
    - Comfy dtype: COMBO
    - Python dtype: str
## Optional
- class_id
    - Category ID parameters allow the user to specify the categories in which the image should be divided, affecting the output of the node and focusing it on the required categories.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- SEG_IMAGE
    - Split images represent input images, highlight recognized category examples, and provide visual output from the split process.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image
- SEG_MASK
    - The mask output is a binary expression for examples of split categories as an accurate tool for further analysis or operation of the categories identified in the image.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class YoloSegNode:

    def __init__(self) -> None:
        ...

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'image': ('IMAGE',), 'model_name': (folder_paths.get_filename_list('yolov8'),), 'class_id': ('INT', {'default': 0})}}
    RETURN_TYPES = ('IMAGE', 'MASK')
    RETURN_NAMES = ('SEG_IMAGE', 'SEG_MASK')
    FUNCTION = 'seg'
    CATEGORY = 'Jags_vector/yoloSEG'

    def seg(self, image, model_name, class_id):
        image_tensor = image
        image_np = image_tensor.cpu().numpy()
        image = Image.fromarray((image_np.squeeze(0) * 255).astype(np.uint8))
        print(f"model_path: {os.path.join(folder_paths.models_dir, 'yolov8')}/{model_name}")
        model = YOLO(f"{os.path.join(folder_paths.models_dir, 'yolov8')}/{model_name}")
        results = model(image)
        masks = results[0].masks.data
        boxes = results[0].boxes.data
        clss = boxes[:, 5]
        people_indices = torch.where(clss == class_id)
        people_masks = masks[people_indices]
        people_mask = torch.any(people_masks, dim=0).int() * 255
        im_array = results[0].plot()
        im = Image.fromarray(im_array[..., ::-1])
        image_tensor_out = torch.tensor(np.array(im).astype(np.float32) / 255.0)
        image_tensor_out = torch.unsqueeze(image_tensor_out, 0)
        return (image_tensor_out, people_mask)
```