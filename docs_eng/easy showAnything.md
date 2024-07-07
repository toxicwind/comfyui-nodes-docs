# Documentation
- Class name: showAnything
- Category: EasyUse/Logic
- Output node: True
- Repo Ref: https://github.com/yolain/ComfyUI-Easy-Use.git

ShowAnything is a multifunctional interface for recording and processing diversified input data for managing and visualizing various types of information in workflows.

# Input types
## Optional
- anything
    - The `anything' parameter is a key element in enabling nodes to adapt to a variety of input data, ensuring flexibility and adaptability in a diverse treatment landscape.
    - Comfy dtype: COMBO[*]
    - Python dtype: Union[str, int, float, list, dict, None]
- unique_id
    - The `unique_id' parameter is essential for linking input values to specific workflow nodes and allows targeted data operations and tracking within the workflow structure.
    - Comfy dtype: str
    - Python dtype: str
- extra_pnginfo
    - The `extra_pnginfo' parameter contains additional information that may be necessary for node operations to influence the processing and output of nodes according to the context of the workflow.
    - Comfy dtype: list
    - Python dtype: List[Dict[str, Any]]

# Output types
- ui
    - The `ui' output parameter is a structured expression of node results and focuses on providing clear and concise visual processing data within the user interface.
    - Comfy dtype: dict
    - Python dtype: Dict[str, Any]

# Usage tips
- Infra type: CPU

# Source code
```
class showAnything:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {}, 'optional': {'anything': (AlwaysEqualProxy('*'), {})}, 'hidden': {'unique_id': 'UNIQUE_ID', 'extra_pnginfo': 'EXTRA_PNGINFO'}}
    RETURN_TYPES = ()
    INPUT_IS_LIST = True
    OUTPUT_NODE = True
    FUNCTION = 'log_input'
    CATEGORY = 'EasyUse/Logic'

    def log_input(self, unique_id=None, extra_pnginfo=None, **kwargs):
        values = []
        if 'anything' in kwargs:
            for val in kwargs['anything']:
                try:
                    if type(val) is str:
                        values.append(val)
                    else:
                        val = json.dumps(val)
                        values.append(str(val))
                except Exception:
                    values.append(str(val))
                    pass
        if unique_id and extra_pnginfo and ('workflow' in extra_pnginfo[0]):
            workflow = extra_pnginfo[0]['workflow']
            node = next((x for x in workflow['nodes'] if str(x['id']) == unique_id[0]), None)
            if node:
                node['widgets_values'] = [values]
        return {'ui': {'text': values}}
```