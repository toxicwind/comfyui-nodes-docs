# Documentation
- Class name: WAS_Lucy_Sharpen
- Category: WAS Suite/Image/Filter
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Lucy_Sharpen node is designed to enhance the clarity and detail of the image by applying sharp filters. It uses an iterative process to fine-tune the image to make the edges and details clearer, without introducing significant hypotheses. This node is particularly suitable for improving the visual quality of images that may be blurred or soft enough to produce clearer and more clearly defined outputs.

# Input types
## Required
- images
    - The `images' parameter is essential for the operation of the node because it specifies input images that need to be sharpened. The quality of the sharpness effect is directly influenced by the initial state of the images, making this parameter essential for achieving the desired result.
    - Comfy dtype: IMAGE
    - Python dtype: List[PIL.Image.Image]
## Optional
- iterations
    - The `internations' parameter determines the number of times you apply acute treatments to each image channel. The more multiple iterations, the more pronounced they may be, the greater the calculated load. This is an optional parameter that allows users to control the intensity of acuteization.
    - Comfy dtype: INT
    - Python dtype: int
- kernel_size
    - The `kernel_size' parameter defines the size of the volume that is used in the sharpening process. A larger nuclear size captures more context, but may also introduce more ambiguity. This is an optional parameter that affects the balance between sharpness and smoothness in the output image.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- sharpened_images
    - The `sharpened_images' output parameters contain the results of the images that have been treated with acute application. These images are expected to have better clarity and detail than input images, with enhanced edges and textures.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Lucy_Sharpen:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'images': ('IMAGE',), 'iterations': ('INT', {'default': 2, 'min': 1, 'max': 12, 'step': 1}), 'kernel_size': ('INT', {'default': 3, 'min': 1, 'max': 16, 'step': 1})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'sharpen'
    CATEGORY = 'WAS Suite/Image/Filter'

    def sharpen(self, images, iterations, kernel_size):
        tensors = []
        if len(images) > 1:
            for img in images:
                tensors.append(pil2tensor(self.lucy_sharpen(tensor2pil(img), iterations, kernel_size)))
            tensors = torch.cat(tensors, dim=0)
        else:
            return (pil2tensor(self.lucy_sharpen(tensor2pil(images), iterations, kernel_size)),)
        return (tensors,)

    def lucy_sharpen(self, image, iterations=10, kernel_size=3):
        from scipy.signal import convolve2d
        image_array = np.array(image, dtype=np.float32) / 255.0
        kernel = np.ones((kernel_size, kernel_size), dtype=np.float32) / kernel_size ** 2
        sharpened_channels = []
        padded_image_array = np.pad(image_array, ((kernel_size, kernel_size), (kernel_size, kernel_size), (0, 0)), mode='edge')
        for channel in range(3):
            channel_array = padded_image_array[:, :, channel]
            for _ in range(iterations):
                blurred_channel = convolve2d(channel_array, kernel, mode='same')
                ratio = channel_array / (blurred_channel + 1e-06)
                channel_array *= convolve2d(ratio, kernel, mode='same')
            sharpened_channels.append(channel_array)
        cropped_sharpened_image_array = np.stack(sharpened_channels, axis=-1)[kernel_size:-kernel_size, kernel_size:-kernel_size, :]
        sharpened_image_array = np.clip(cropped_sharpened_image_array * 255.0, 0, 255).astype(np.uint8)
        sharpened_image = Image.fromarray(sharpened_image_array)
        return sharpened_image
```