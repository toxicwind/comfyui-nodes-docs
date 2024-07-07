# Documentation
- Class name: WAS_SAM_Parameters
- Category: WAS Suite/Image/Masking
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_SAM_Parameters node is designed to process and format input data for image masking operations in the WAS package. It accepts points and labels to generate parameters that are essential for the subsequent masking process. The node plays a key role in preparing the basis for an accurate and efficient image-separation task.

# Input types
## Required
- points
    - The " points " parameter is essential for defining the coordinates used to hide in the image. It is a string that contains a series of points, each of which is represented by their x and y coordinates. This parameter directly influences the accuracy of the cover process by identifying the areas in the image that require attention.
    - Comfy dtype: STRING
    - Python dtype: str
- labels
    - The Labels parameter assigns a classification label to the points provided, which is essential for distinguishing different types of areas in the image in the mask operation. It is a string that contains a tab list corresponding to each point. This parameter is essential for classifying and organizing the image segments during the masking process.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- parameters
    - The " parameters " output is a structured expression of input points and labels and is formatted as a dictionary compatible with the requirements of the image cover process. It covers the processed data and prepares them for downstream cover operations.
    - Comfy dtype: SAM_PARAMETERS
    - Python dtype: Dict[str, Union[np.ndarray, List[int]]]

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_SAM_Parameters:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        return {'required': {'points': ('STRING', {'default': '[128, 128]; [0, 0]', 'multiline': False}), 'labels': ('STRING', {'default': '[1, 0]', 'multiline': False})}}
    RETURN_TYPES = ('SAM_PARAMETERS',)
    FUNCTION = 'sam_parameters'
    CATEGORY = 'WAS Suite/Image/Masking'

    def sam_parameters(self, points, labels):
        parameters = {'points': np.asarray(np.matrix(points)), 'labels': np.array(np.matrix(labels))[0]}
        return (parameters,)
```