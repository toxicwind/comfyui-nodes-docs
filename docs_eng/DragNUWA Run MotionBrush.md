# Documentation
- Class name: DragNUWARunMotionBrush
- Category: DragNUWA
- Output node: False
- Repo Ref: https://github.com/chaojie/ComfyUI-DragNUWA.git

The node is applied to static images through campaigns extrapolated from brush input, simulated dynamic effects aimed at enhancing the visual performance of motion in images, and made possible the creation of dynamic or interactive visual content by integrating the movement data provided by users.

# Input types
## Required
- model
    - Model parameters are essential for the operation of nodes, as they define the basic architecture and parameters used to process images and apply motion effects.
    - Comfy dtype: DragNUWA
    - Python dtype: DragNUWA
- image
    - The image parameter is necessary because it provides the basic visual content that the node will operate to simulate the motion. Its properties directly affect the quality of the output and the effectiveness of the motion simulation.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image
- motion_brush
    - The motion_brush parameter is essential for the function of the node, as it provides the movement data that will be applied to the image. Its structure and content directly influence the ultimate exercise effect.
    - Comfy dtype: MotionBrush
    - Python dtype: MotionBrush
- inference_batch_size
    - This parameter optimizes the processing of nodes by controlling the volume of batch processing during the reasoning process and influences the computational efficiency and speed of motion simulations.
    - Comfy dtype: INT
    - Python dtype: int
- motion_bucket_id
    - The motion_bucket_id parameter is important because it identifies the specific movement data to be used in the sports drums for simulation purposes and guides the visual results required for node creation.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- output
    - The output of the node is an enhanced image or a series of images that visualize the motion effect applied to the input image and demonstrate the ability of the node to simulate dynamic visual content.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image

# Usage tips
- Infra type: GPU

# Source code
```
class DragNUWARunMotionBrush:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'model': ('DragNUWA',), 'image': ('IMAGE',), 'motion_brush': ('MotionBrush',), 'inference_batch_size': ('INT', {'default': 1, 'min': 1, 'max': 1}), 'motion_bucket_id': ('INT', {'default': 4, 'min': 1, 'max': 100})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'run_inference'
    CATEGORY = 'DragNUWA'

    def run_inference(self, model, image, motion_brush, inference_batch_size, motion_bucket_id):
        image = 255.0 * image[0].cpu().numpy()
        image_pil = Image.fromarray(np.clip(image, 0, 255).astype(np.uint8))
        (raw_w, raw_h) = image_pil.size
        resize_ratio = max(model.width / raw_w, model.height / raw_h)
        image_pil = image_pil.resize((int(raw_w * resize_ratio), int(raw_h * resize_ratio)), Image.BILINEAR)
        image_pil = transforms.CenterCrop((model.height, model.width))(image_pil.convert('RGB'))
        return model.run_brush(image_pil, motion_brush, inference_batch_size, motion_bucket_id)
```