# Documentation
- Class name: SeargeSeparator
- Category: UI
- Output node: False
- Repo Ref: https://github.com/jobunk/SeargeSDXL.git

SeergeSeparator is designed as a placeholder in a workflow that provides a means of separating and organizing different process segments without performing any active computing or data operations. As a structural component, it allows for a clear and logical layout of the workflow.

# Input types
## Required
- required
    - This parameter is the key component in the SeergeSepactor node, which defines the structure to be entered without specifying the actual data requirements. It ensures that the node is correctly integrated in the workflow and helps the organization as a whole.
    - Comfy dtype: COMBO[{}]
    - Python dtype: Dict[str, Any]

# Output types
- None
    - This reflects the role of the node as a structural rather than a data-processing element.
    - Comfy dtype: None
    - Python dtype: None

# Usage tips
- Infra type: CPU

# Source code
```
class SeargeSeparator:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {}}
    RETURN_TYPES = ()
    RETURN_NAMES = ()
    FUNCTION = 'do_nothing'
    CATEGORY = UI.CATEGORY_UI

    def do_nothing(self):
        return ()
```