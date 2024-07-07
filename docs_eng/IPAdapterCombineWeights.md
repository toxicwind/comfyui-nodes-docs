# Documentation
- Class name: IPAdapterCombineWeights
- Category: ipadapter/weights
- Output node: False
- Repo Ref: https://github.com/cubiq/ComfyUI_IPAdapter_plus.git

IPAdapterCombineWeights supports weighting schedules that allow users to adjust the impact of images over different time periods to achieve smooth transitions and animation effects. This method is lighter and more efficient than using the gradient mask.

# Output types
- weights
    - The output of weights represents the results of the application of the specified method to input weights. It contains the essence of node purposes and provides a composite form of input data that can be used for further analysis or model training.
    - Comfy dtype: FLOAT
    - Python dtype: float
- count
    - Count output represents the number of input weights. It is an important attribute of the node that describes the size and scope of the input data.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: GPU

# Source code
```
class IPAdapterCombineWeights:
    @classmethod
    def INPUT_TYPES(s):
        return {
        "required": {
            "weights_1": ("FLOAT", { "default": 0.0, "min": 0.0, "max": 1.0, "step": 0.05 }),
            "weights_2": ("FLOAT", { "default": 0.0, "min": 0.0, "max": 1.0, "step": 0.05 }),
        }}
    RETURN_TYPES = ("FLOAT", "INT")
    RETURN_NAMES = ("weights", "count")
    FUNCTION = "combine"
    CATEGORY = "ipadapter/utils"

    def combine(self, weights_1, weights_2):
        if not isinstance(weights_1, list):
            weights_1 = [weights_1]
        if not isinstance(weights_2, list):
            weights_2 = [weights_2]
        weights = weights_1 + weights_2

        return (weights, len(weights), )
```