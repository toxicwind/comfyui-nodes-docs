# Documentation
- Class name: showTensorShape
- Category: EasyUse/Logic
- Output node: True
- Repo Ref: https://github.com/yolain/ComfyUI-Easy-Use.git

This node category is designed to provide an advanced overview of the size of the data through it, which helps to understand the structure of the data rather than the details of the specific method. It is a key tool for debugging and ensuring the correct dimensions in the workflow.

# Input types
## Required
- tensor
    - The `tensor' parameter is key because it carries the data to be analysed by the node. It can be a volume, a list, or a dictionary, with the shape to be reported by the node, which is essential for the operation of the node and subsequent data processing.
    - Comfy dtype: COMBO[Tensor, List, Dict]
    - Python dtype: Union[torch.Tensor, List, Dict]
## Optional
- unique_id
    - The `unique_id' parameter, although not necessary, serves as an identifier for volume-shaped information, allowing data to be tracked and managed more easily within the system.
    - Comfy dtype: str
    - Python dtype: str
- extra_pnginfo
    - If the `extra_pnginfo' parameters are provided, it will add additional context to volume shape information, which may enhance the usefulness of nodes in more complex data processing scenarios.
    - Comfy dtype: str
    - Python dtype: str

# Output types
- ui
    - `ui' output is a dictionary with text in volume shape, which is essential for visualizing data structures and ensuring that the next steps in the workflow are correctly informed.
    - Comfy dtype: Dict[str, Any]
    - Python dtype: Dict[str, Any]

# Usage tips
- Infra type: CPU

# Source code
```
class showTensorShape:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'tensor': (AlwaysEqualProxy('*'),)}, 'optional': {}, 'hidden': {'unique_id': 'UNIQUE_ID', 'extra_pnginfo': 'EXTRA_PNGINFO'}}
    RETURN_TYPES = ()
    RETURN_NAMES = ()
    OUTPUT_NODE = True
    FUNCTION = 'log_input'
    CATEGORY = 'EasyUse/Logic'

    def log_input(self, tensor, unique_id=None, extra_pnginfo=None):
        shapes = []

        def tensorShape(tensor):
            if isinstance(tensor, dict):
                for k in tensor:
                    tensorShape(tensor[k])
            elif isinstance(tensor, list):
                for i in range(len(tensor)):
                    tensorShape(tensor[i])
            elif hasattr(tensor, 'shape'):
                shapes.append(list(tensor.shape))
        tensorShape(tensor)
        return {'ui': {'text': shapes}}
```