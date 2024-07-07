# Documentation
- Class name: SplitSigmas
- Category: sampling/custom_sampling/sigmas
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

SplitSigmas nodes are designed to divide a given set of sigma values into two different subsets based on a specified step-long index. This action is essential for a self-defined sampling technique that requires the classification of sigma values for further processing at a given time. The function of the nodes is not dependent on a particular method, but rather focuses on conceptual data disaggregation, providing a basic step for a more complex sampling process.

# Input types
## Required
- sigmas
    - The parameter'sigmas' represents a set of values that are essential to the sampling process. It is important because it determines the initial conditions of the sampling algorithm and affects the quality and properties of the samples generated. The parameter plays a central role in node operations, as it is the main input for the sigma classification.
    - Comfy dtype: FLOAT
    - Python dtype: List[float]
## Optional
- step
    - The parameter'step' defines the index where the sigma value is divided. It is important because it determines the split point of the sigma value, thus influencing the structure of the output. This parameter is optional and provides some flexibility in processing the sigma value.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- sigmas1
    - Output'sigmas1' contains the first part of the sigma value up to the specified step length. It is a key component of the node output, as it represents the initial part of the sigma value and may be used for specific sampling techniques or further analysis.
    - Comfy dtype: FLOAT
    - Python dtype: List[float]
- sigmas2
    - The output'sigmas2' contains the sigma value remaining after the specified length of the step. This output is important because it represents the continuity of the sigma sequence, which can be used in subsequent sampling overlaps or for other computing purposes.
    - Comfy dtype: FLOAT
    - Python dtype: List[float]

# Usage tips
- Infra type: CPU

# Source code
```
class SplitSigmas:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'sigmas': ('SIGMAS',), 'step': ('INT', {'default': 0, 'min': 0, 'max': 10000})}}
    RETURN_TYPES = ('SIGMAS', 'SIGMAS')
    CATEGORY = 'sampling/custom_sampling/sigmas'
    FUNCTION = 'get_sigmas'

    def get_sigmas(self, sigmas, step):
        sigmas1 = sigmas[:step + 1]
        sigmas2 = sigmas[step:]
        return (sigmas1, sigmas2)
```