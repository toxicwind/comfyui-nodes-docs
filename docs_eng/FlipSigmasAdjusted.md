# Documentation
- Class name: FlipSigmasAdjusted
- Category: KJNodes/noise
- Output node: False
- Repo Ref: https://github.com/kijai/ComfyUI-KJNodes.git

‘FlipSigmasAdjusted’ node is designed to process and adjust a set of Sigma values. It reverses the order into which Sigma is entered, divides it by the last Sigma value and adjusts each Sigma by the amount of deviation and the assigned divide. The node also ensures that there is no Sigma value to zero and, if necessary, replaces it with a minimum positive value. The result is a set of converted Sigma values and a string for visual purposes.

# Input types
## Required
- sigmas
    - The `sigmas' parameter is the value sequence that represents the standard difference in the noise distribution. It is essential for the operation of nodes, as it determines the underlying data to be operated. The reversal and adjustment process directly affects the results of the node execution.
    - Comfy dtype: FLOAT
    - Python dtype: torch.Tensor
## Optional
- divide_by_last_sigma
    - The `divide_by_last_sigma' parameter is a boolean symbol that, when set as true, will result in dividing each Sigma in the sequence by the last Sigma. This operation has been normalized to Sigma and may be very important in some noise reduction or image processing tasks.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- divide_by
    - The `divide_by' parameter is a floating point number used to scale the adjusted Sigma value. It plays a key role in controlling the size of the Sigma adjustment, especially when it is produced for a specific application.
    - Comfy dtype: FLOAT
    - Python dtype: float
- offset_by
    - The `offset_by' parameter is an integer that moves each Sigma index to the given number. This can introduce a variation or distortion into the Sigma sequence, which may be useful for some types of data analysis or signal processing.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- SIGMAS
    - The `SIGMAS' output provides a node to adjust the Sigma value after all operations have been applied. This is a key output for subsequent processing steps that rely on these conversion values.
    - Comfy dtype: FLOAT
    - Python dtype: torch.Tensor
- sigmas_string
    - The `sigmas_string' output is a string for the adjusted Sigma value. It is useful for visualizing or recording purposes and provides a human readable format for the data.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class FlipSigmasAdjusted:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'sigmas': ('SIGMAS',), 'divide_by_last_sigma': ('BOOLEAN', {'default': False}), 'divide_by': ('FLOAT', {'default': 1, 'min': 1, 'max': 255, 'step': 0.01}), 'offset_by': ('INT', {'default': 1, 'min': -100, 'max': 100, 'step': 1})}}
    RETURN_TYPES = ('SIGMAS', 'STRING')
    RETURN_NAMES = ('SIGMAS', 'sigmas_string')
    CATEGORY = 'KJNodes/noise'
    FUNCTION = 'get_sigmas_adjusted'

    def get_sigmas_adjusted(self, sigmas, divide_by_last_sigma, divide_by, offset_by):
        sigmas = sigmas.flip(0)
        if sigmas[0] == 0:
            sigmas[0] = 0.0001
        adjusted_sigmas = sigmas.clone()
        for i in range(1, len(sigmas)):
            offset_index = i - offset_by
            if 0 <= offset_index < len(sigmas):
                adjusted_sigmas[i] = sigmas[offset_index]
            else:
                adjusted_sigmas[i] = 0.0001
        if adjusted_sigmas[0] == 0:
            adjusted_sigmas[0] = 0.0001
        if divide_by_last_sigma:
            adjusted_sigmas = adjusted_sigmas / adjusted_sigmas[-1]
        sigma_np_array = adjusted_sigmas.numpy()
        array_string = np.array2string(sigma_np_array, precision=2, separator=', ', threshold=np.inf)
        adjusted_sigmas = adjusted_sigmas / divide_by
        return (adjusted_sigmas, array_string)
```