# Documentation
- Class name: WAS_SAM_Combine_Parameters
- Category: WAS Suite/Image/Masking
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The method `sam_combine_parameters'is designed to combine two sets of parameters related to SAM. Its function is to integrate multiple parameters into a unified structure, which is essential for the operation of data that need to be integrated across the different SAM examples. The node plays a key role in ensuring seamless integration of points and labels, facilitating the implementation of complex images and cover tasks in the WAS package.

# Input types
## Required
- sam_parameters_a
    - The first set of SAM parameters is essential for the integration process. It contains the initial data points and labels that will be combined with another set. This parameter significantly influences the structure and content of the final set of parameters, influencing the image and the next steps in the masking workflow.
    - Comfy dtype: SAM_PARAMETERS
    - Python dtype: Dict[str, Union[np.ndarray, List[str]]]
- sam_parameters_b
    - The second set of SAM parameters, which is to be combined with the first set of parameters, is as important as the first set of parameters, providing additional data points and labels that contribute to the comprehensiveness of the combined parameters.
    - Comfy dtype: SAM_PARAMETERS
    - Python dtype: Dict[str, Union[np.ndarray, List[str]]]

# Output types
- parameters
    - The output of the `sam_combine_parameters'method is a single set of parameters, which contains a combination of data from two input SM parameters. This output is important because it is the basis for further processing and analysis of the image and cover field.
    - Comfy dtype: SAM_PARAMETERS
    - Python dtype: Dict[str, Union[np.ndarray, List[str]]]

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_SAM_Combine_Parameters:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        return {'required': {'sam_parameters_a': ('SAM_PARAMETERS',), 'sam_parameters_b': ('SAM_PARAMETERS',)}}
    RETURN_TYPES = ('SAM_PARAMETERS',)
    FUNCTION = 'sam_combine_parameters'
    CATEGORY = 'WAS Suite/Image/Masking'

    def sam_combine_parameters(self, sam_parameters_a, sam_parameters_b):
        parameters = {'points': np.concatenate((sam_parameters_a['points'], sam_parameters_b['points']), axis=0), 'labels': np.concatenate((sam_parameters_a['labels'], sam_parameters_b['labels']))}
        return (parameters,)
```