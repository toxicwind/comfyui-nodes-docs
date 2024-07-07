# Documentation
- Class name: ImpactLogger
- Category: ImpactPack/Debug
- Output node: True
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The ImpactLogger node is designed to provide log-recording functions for capturing and exporting data information that is being processed. It is particularly suitable for debugging purposes and allows developers to check the shape and content of data at different stages of the workflow.

# Input types
## Required
- data
    - The `data' parameter is essential to the log-recording process because it represents the core data that the ImpactLogger node is designed to record. It is through this parameter that the node captures and prints the shape and content of the data for debugging.
    - Comfy dtype: any_typ
    - Python dtype: Any
## Optional
- prompt
    - `prompt' parameters, as an optional descriptor, can be used to provide additional context or specific identifiers for the data being recorded. This may be particularly useful when tracking multiple data points or log output for further analysis.
    - Comfy dtype: str
    - Python dtype: str
- extra_pnginfo
    - The ‘extra_pnginfo’ parameter allows for the inclusion of additional information that may be relevant to the log-recording process. This may include metadata or any other supporting details that are not directly relevant to the core ‘data’ being recorded but that are still important for the debugging process.
    - Comfy dtype: str
    - Python dtype: str

# Output types
- output
    - The `output' of the ImpactLogger node is an empty dictionary that shows that the primary function of the node is to record information rather than produce an important output that will be transmitted to a subsequent node.
    - Comfy dtype: Dict[str, Any]
    - Python dtype: Dict[str, Any]

# Usage tips
- Infra type: CPU

# Source code
```
class ImpactLogger:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'data': (any_typ, '')}, 'hidden': {'prompt': 'PROMPT', 'extra_pnginfo': 'EXTRA_PNGINFO'}}
    CATEGORY = 'ImpactPack/Debug'
    OUTPUT_NODE = True
    RETURN_TYPES = ()
    FUNCTION = 'doit'

    def doit(self, data, prompt, extra_pnginfo):
        shape = ''
        if hasattr(data, 'shape'):
            shape = f'{data.shape} / '
        print(f'[IMPACT LOGGER]: {shape}{data}')
        print(f'         PROMPT: {prompt}')
        return {}
```