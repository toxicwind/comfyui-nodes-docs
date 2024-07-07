# Documentation
- Class name: WAS_Image_Nova_Filter
- Category: WAS Suite/Image/Filter
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Image_Nova_Filter type `nova_sine'method applies sine-fine to images that enhances their visual features through wave-like patterns. This method is designed to introduce a creative and artistic effect to image-processing workflows, allowing for the control of the intensity and scale of the loss by adjusting the amplitude and frequency.

# Input types
## Required
- image
    - The 'image'parameter is essential for the operation of the node, because it is the input image to be processed. It directly influences the execution and final result of the node and determines the object for which the sine wave is lost.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image
## Optional
- amplitude
    - The 'amplitude 'parameter controls the intensity of the loss of the sine wave applied to the image. It is a key factor in determining visual effects and allows users to fine-tune effects according to their preferences.
    - Comfy dtype: FLOAT
    - Python dtype: float
- frequency
    - The 'frequency' parameter determines the scale of the sine-wave mode applied to the image. It is essential for adjusting the wave cycle, which in turn affects the whole image.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- output_image
    - 'output_image' is the result of using the chord wave to input the image. It represents the image that has been altered in the end with the creative effect expected by the node function.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Image_Nova_Filter:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'image': ('IMAGE',), 'amplitude': ('FLOAT', {'default': 0.1, 'min': 0.0, 'max': 1.0, 'step': 0.001}), 'frequency': ('FLOAT', {'default': 3.14, 'min': 0.0, 'max': 100.0, 'step': 0.001})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'nova_sine'
    CATEGORY = 'WAS Suite/Image/Filter'

    def nova_sine(self, image, amplitude, frequency):
        img = tensor2pil(image)
        img_array = np.array(img)

        def sine(x, freq, amp):
            return amp * np.sin(2 * np.pi * freq * x)
        resolution = img.info.get('dpi')
        physical_size = img.size
        if resolution is not None:
            ppm = 25.4 / resolution
            physical_size = tuple((int(pix * ppm) for pix in physical_size))
        max_freq = img.width / 2
        if frequency > max_freq:
            frequency = max_freq
        for i in range(img_array.shape[0]):
            for j in range(img_array.shape[1]):
                for k in range(img_array.shape[2]):
                    img_array[i, j, k] = int(sine(img_array[i, j, k] / 255, frequency, amplitude) * 255)
        return (torch.from_numpy(img_array.astype(np.float32) / 255.0).unsqueeze(0),)
```