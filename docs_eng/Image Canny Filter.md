# Documentation
- Class name: WAS_Canny_Filter
- Category: WAS Suite/Image/Filter
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Canny_Filter node is designed to enhance the visibility of the edges of the image data by applying the Canny margin detection algorithm to input images. It treats each image by using multi-stage algorithms that include Gaussian fuzzy, gradient calculations and threshold processing to identify and highlight important edges.

# Input types
## Required
- images
    - The `images' parameter is essential because it is an input into the process of detection of the edge of Canny. It is a node that will process the original image data to identify and enhance the edge.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
## Optional
- enable_threshold
    - The `enable_threshold' parameter decides whether to apply the threshold step in the Canny algorithm. This is important for controlling the sensitivity of margin detection.
    - Comfy dtype: COMBO['false', 'true']
    - Python dtype: str
- threshold_low
    - The `threshold_low' parameter sets the threshold threshold for the margin detection. It is a key factor in determining which edges are strong enough to be included in the final output.
    - Comfy dtype: FLOAT
    - Python dtype: float
- threshold_high
    - The `threshold_high' parameter sets a ceiling threshold for margin detection. It works with the lower threshold to fine-tune the margin detection process.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- images
    - The `images' output parameter contains the use of the Canny filter to highlight the treated image of the edge. This output is important because it represents the final result of the margin detection operation.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Canny_Filter:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'images': ('IMAGE',), 'enable_threshold': (['false', 'true'],), 'threshold_low': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'threshold_high': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.01})}}
    RETURN_TYPES = ('IMAGE',)
    RETURN_NAMES = ('images',)
    FUNCTION = 'canny_filter'
    CATEGORY = 'WAS Suite/Image/Filter'

    def canny_filter(self, images, threshold_low, threshold_high, enable_threshold):
        if enable_threshold == 'false':
            threshold_low = None
            threshold_high = None
        batch_tensor = []
        for image in images:
            image_canny = Image.fromarray(self.Canny_detector(255.0 * image.cpu().numpy().squeeze(), threshold_low, threshold_high)).convert('RGB')
            batch_tensor.append(pil2tensor(image_canny))
        batch_tensor = torch.cat(batch_tensor, dim=0)
        return (pil2tensor(image_canny),)

    def Canny_detector(self, img, weak_th=None, strong_th=None):
        import cv2
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.GaussianBlur(img, (5, 5), 1.4)
        gx = cv2.Sobel(np.float32(img), cv2.CV_64F, 1, 0, 3)
        gy = cv2.Sobel(np.float32(img), cv2.CV_64F, 0, 1, 3)
        (mag, ang) = cv2.cartToPolar(gx, gy, angleInDegrees=True)
        mag_max = np.max(mag)
        if not weak_th:
            weak_th = mag_max * 0.1
        if not strong_th:
            strong_th = mag_max * 0.5
        (height, width) = img.shape
        for i_x in range(width):
            for i_y in range(height):
                grad_ang = ang[i_y, i_x]
                grad_ang = abs(grad_ang - 180) if abs(grad_ang) > 180 else abs(grad_ang)
                (neighb_1_x, neighb_1_y) = (-1, -1)
                (neighb_2_x, neighb_2_y) = (-1, -1)
                if grad_ang <= 22.5:
                    (neighb_1_x, neighb_1_y) = (i_x - 1, i_y)
                    (neighb_2_x, neighb_2_y) = (i_x + 1, i_y)
                elif grad_ang > 22.5 and grad_ang <= 22.5 + 45:
                    (neighb_1_x, neighb_1_y) = (i_x - 1, i_y - 1)
                    (neighb_2_x, neighb_2_y) = (i_x + 1, i_y + 1)
                elif grad_ang > 22.5 + 45 and grad_ang <= 22.5 + 90:
                    (neighb_1_x, neighb_1_y) = (i_x, i_y - 1)
                    (neighb_2_x, neighb_2_y) = (i_x, i_y + 1)
                elif grad_ang > 22.5 + 90 and grad_ang <= 22.5 + 135:
                    (neighb_1_x, neighb_1_y) = (i_x - 1, i_y + 1)
                    (neighb_2_x, neighb_2_y) = (i_x + 1, i_y - 1)
                elif grad_ang > 22.5 + 135 and grad_ang <= 22.5 + 180:
                    (neighb_1_x, neighb_1_y) = (i_x - 1, i_y)
                    (neighb_2_x, neighb_2_y) = (i_x + 1, i_y)
                if width > neighb_1_x >= 0 and height > neighb_1_y >= 0:
                    if mag[i_y, i_x] < mag[neighb_1_y, neighb_1_x]:
                        mag[i_y, i_x] = 0
                        continue
                if width > neighb_2_x >= 0 and height > neighb_2_y >= 0:
                    if mag[i_y, i_x] < mag[neighb_2_y, neighb_2_x]:
                        mag[i_y, i_x] = 0
        weak_ids = np.zeros_like(img)
        strong_ids = np.zeros_like(img)
        ids = np.zeros_like(img)
        for i_x in range(width):
            for i_y in range(height):
                grad_mag = mag[i_y, i_x]
                if grad_mag < weak_th:
                    mag[i_y, i_x] = 0
                elif strong_th > grad_mag >= weak_th:
                    ids[i_y, i_x] = 1
                else:
                    ids[i_y, i_x] = 2
        return mag
```