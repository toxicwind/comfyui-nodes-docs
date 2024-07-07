# Documentation
- Class name: ListCounter
- Category: InspirePack/Util
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Inspire-Pack.git

The ListCounter node is intended to increase the number of unique identifiers, providing a method for tracking events or items in the sequence. It maintains the count associated with each unique identifier by using a map structure. This node is particularly suitable for scenarios that require sequential tracking, such as log records, event processing or inventory management.

# Input types
## Required
- signal
    - The signal parameter is the input that triggers the counting process. Its existence marks an event or item that needs to be counted. The significance of the parameter is that it is the starting factor for node operations, without which the counting mechanism will not be activated.
    - Comfy dtype: ANY
    - Python dtype: Any
- base_value
    - Base_value parameters are the initial count values that start as nodes before increment. It is essential because it sets the basis for counting and can be used to adjust the starting point of the sequence to provide flexibility in counting operations.
    - Comfy dtype: INT
    - Python dtype: int
- unique_id
    - The unique_id parameter is the key identifier used to distinguish between different sequences or items that are being tracked. It is essential for the function of the node, as it allows each unique sequence or item to be distinguished and counted separately.
    - Comfy dtype: UNIQUE_ID
    - Python dtype: str

# Output types
- count
    - Count output reflects the current count after node processing input. It indicates the number of occurrences or events that have been counted to date. This output is important because it provides the final results of node operations and insights into sequence progress.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class ListCounter:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'signal': (utils.any_typ,), 'base_value': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615})}, 'hidden': {'unique_id': 'UNIQUE_ID'}}
    RETURN_TYPES = ('INT',)
    FUNCTION = 'doit'
    CATEGORY = 'InspirePack/Util'

    def doit(self, signal, base_value, unique_id):
        if unique_id not in list_counter_map:
            count = 0
        else:
            count = list_counter_map[unique_id]
        list_counter_map[unique_id] = count + 1
        return (count + base_value,)
```