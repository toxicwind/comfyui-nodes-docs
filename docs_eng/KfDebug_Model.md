# Documentation
- Class name: KfDebug_Model
- Category: Debugging
- Output node: True
- Repo Ref: https://github.com/dmarx/ComfyUI-Keyframed

The node facilitates the examination and analysis of the internal state and output of the model and provides a means of understanding and debugging the behaviour of the model in the reasoning process.

# Input types
## Required
- input_data
    - The input data are critical, and it represents a sample or sample batch processed by the model. It directly influences the output of the model and the insights obtained from debugging.
    - Comfy dtype: COMBO[numpy.ndarray, torch.Tensor]
    - Python dtype: Union[numpy.ndarray, torch.Tensor]
- model
    - Model parameters are essential and define the neural network structure of the behavior being debuggered. The configuration and parameters of the model determine the debugging process.
    - Comfy dtype: torch.nn.Module
    - Python dtype: torch.nn.Module

# Output types
- debug_info
    - Debug information is important because it provides a detailed overview of the internal work of the model and helps to identify potential problems and areas for improvement.
    - Comfy dtype: Dict[str, Any]
    - Python dtype: Dict[str, Any]

# Usage tips
- Infra type: GPU

# Source code
```
class KfDebug_Model(KfDebug_Passthrough):
    RETURN_TYPES = ('MODEL',)
```