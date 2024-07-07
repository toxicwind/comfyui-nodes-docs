# Documentation
- Class name: KfDebug_Clip
- Category: Debugging
- Output node: True
- Repo Ref: https://github.com/dmarx/ComfyUI-Keyframed

It is designed to provide insight into data flows and to ensure that the information being processed meets the required standards and specifications.

# Input types
## Required
- input
    - The input parameter is essential for the node because it carries data that need to be debuggered and checked. It directly affects the running of the node and the quality of debugging output.
    - Comfy dtype: CLIP
    - Python dtype: Any

# Output types
- output
    - The output of the node represents the result of the debugging process. It is important because it provides a comprehensive overview of the status of the data after debugging nodes have been processed.
    - Comfy dtype: CLIP
    - Python dtype: Any

# Usage tips
- Infra type: CPU

# Source code
```
class KfDebug_Clip(KfDebug_Passthrough):
    RETURN_TYPES = ('CLIP',)
```