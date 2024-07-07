# Documentation
- Class name: YoloSEGdetectionNode
- Category: Jags_vector/yoloSEG
- Output node: False
- Repo Ref: https://github.com/jags111/ComfyUI_Jags_VectorMagic

The node uses an in-depth learning model to semanticly divide images and identify and classify areas of interest. It draws on the power of the YOLO (YouOnly Look Once) architecture, known for its real-time object detection capability, to divide and classify objects in the image. The main objective of the node is to achieve a more complex image analysis task by mapping the boundaries of different objects and providing a detailed understanding of their contents.

# Input types
## Required
- image
    - An image parameter is essential to the operation of the node, which is the main input. It is the medium through which the node partition capability is realized. The quality and resolution of the image has a significant impact on the accuracy and detail of the split result.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image or torch.Tensor
- model_name
    - The model name parameter determines the configuration of the YOLO model that will be used to divide the process. It is important because different models can provide different levels of accuracy and performance. The selection of models directly affects the quality of the split and the ability of nodes to correctly identify and classify objects in the image.
    - Comfy dtype: COMBO
    - Python dtype: str

# Output types
- SEG_IMAGE
    - The output image, which is now divided, provides a visual indication of the object categories executed by the node. This is a key result because it demonstrates the effectiveness of the node in understanding and processing the input images and allows for further analysis and application.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class YoloSEGdetectionNode:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'image': ('IMAGE',), 'model_name': (folder_paths.get_filename_list('yolov8'),)}}
    RETURN_TYPES = ('IMAGE',)
    RETURN_NAMES = ('SEG_IMAGE',)
    FUNCTION = 'detect'
    CATEGORY = 'Jags_vector/yoloSEG'

    def detect(self, image, model_name):
        image_tensor = image
        image_np = image_tensor.cpu().numpy()
        image = Image.fromarray((image_np.squeeze(0) * 255).astype(np.uint8))
        print(f"model_path: {os.path.join(folder_paths.models_dir, 'yolov8')}/{model_name}")
        model = YOLO(f"{os.path.join(folder_paths.models_dir, 'yolov8')}/{model_name}")
        results = model(image)
        im_array = results[0].plot()
        im = Image.fromarray(im_array[..., ::-1])
        image_tensor_out = torch.tensor(np.array(im).astype(np.float32) / 255.0)
        image_tensor_out = torch.unsqueeze(image_tensor_out, 0)
        return (image_tensor_out,)
```