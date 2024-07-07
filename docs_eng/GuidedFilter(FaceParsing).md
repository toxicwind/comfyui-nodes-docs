# Documentation
- Class name: GuidedFilter
- Category: face_parsing
- Output node: False
- Repo Ref: https://github.com/Ryuukeisyou/comfyui_face_parsing

GuidedFilter nodes apply a non-linear filtering technology that uses lead images to influence the filtering process, with the aim of preserving the structure and edge of the original image while removing noise or smoothing appearances.

# Input types
## Required
- image
    - The image parameter is necessary because it provides input image data on which the guided filter operation will be performed, which has a significant impact on the quality and detail of the output.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- radius
    - The radius parameters determine the size of the local adjacent area considered by the filter, affecting the extent to which the filter smooths the image while retaining the edges.
    - Comfy dtype: INT
    - Python dtype: int
- eps
    - The eps parameter controls the sensitivity of the lead filter, with lower values leading to more radical smoothness and higher values retaining more detail.
    - Comfy dtype: FLOAT
    - Python dtype: float
## Optional
- guide
    - When guiding parameters are provided, it guides the filtering process as a reference image, allowing selective enhancement or suppression of features based on guiding content.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Output types
- output_image
    - The output image is the result of a filter operation that reflects the combination of the input image with the guidance provided by the guide image, if any.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class GuidedFilter:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'image': ('IMAGE',), 'radius': ('INT', {'default': 3, 'min': 0, 'step': 1}), 'eps': ('FLOAT', {'default': 125, 'min': 0, 'step': 1})}, 'optional': {'guide': ('IMAGE', {'default': None})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'guided_filter'
    CATEGORY = 'face_parsing'

    def guided_filter(self, image: Tensor, radius: int, eps: float, guide: Tensor | None=None):
        results = []
        for item in image:
            image_cv2 = cv2.cvtColor(item.mul(255).byte().numpy(), cv2.COLOR_RGB2BGR)
            guide_cv2 = image_cv2 if guide is None else cv2.cvtColor(guide.numpy(), cv2.COLOR_RGB2BGR)
            result_cv2 = cv2.ximgproc.guidedFilter(guide_cv2, image_cv2, radius, eps)
            result_cv2_rgb = cv2.cvtColor(result_cv2, cv2.COLOR_BGR2RGB)
            result = torch.tensor(result_cv2_rgb).float().div(255)
            results.append(result)
        return (torch.cat(results, dim=0).unsqueeze(0),)
```