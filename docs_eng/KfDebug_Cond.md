# Documentation
- Class name: KfDebug_Cond
- Category: debugging
- Output node: True
- Repo Ref: https://github.com/dmarx/ComfyUI-Keyframed

The KfDebug_Cond node is designed to provide a way to visualize and understand the reconciliation aspects of the key frame model. It is very useful for debugging to ensure that the reconciliation data are correctly processed and thus to optimize the model more wisely.

# Input types
## Required
- conditioning_data
    - The reconciliation data (conversion_data) is essential for KfDebug_Cond node, as it represents the input data used to regulate model output. The correct handling of this parameter is essential for the normal work of the node and the validity of the debugging process.
    - Comfy dtype: torch.Tensor
    - Python dtype: torch.Tensor

# Output types
- debug_info
    - The debug_info output of the KfDebug_Cond node contains valuable information on the reconciliation process. This information can be used to identify any problems in model reconciliations and thus facilitate the debug_info process.
    - Comfy dtype: dict
    - Python dtype: Dict[str, Any]

# Usage tips
- Infra type: CPU

# Source code
```
class KfDebug_Cond(KfDebug_Passthrough):
    RETURN_TYPES = ('CONDITIONING',)
```