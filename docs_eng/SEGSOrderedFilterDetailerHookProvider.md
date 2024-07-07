# Documentation
- Class name: SEGSOrderedFilterDetailerHookProvider
- Category: ImpactPack/Util
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

SEGSOrderedFilterDetailer HookProvider is designed to apply a specific filter and sorting mechanism to a group of splits. It allows customizing filtering criteria according to size and space coordinates, and provides options for sorting results in ascending or descending order. This node is particularly suitable for the output of a refined split task to meet specific requirements.

# Input types
## Required
- target
    - The target parameter defines the criteria for filter partitioning. It can be based on the coordinates of the area, width, height or corner of the partition. This parameter is essential because it directly affects which partitions are selected for further processing.
    - Comfy dtype: COMBO[area(=w*h), width, height, x1, y1, x2, y2]
    - Python dtype: Union[str, int, Tuple[int, int]]
- order
    - Sorts the parameters to determine the order of partitioning of the filter. When set to True, the result is sorted in descending order; when set to False, sorted in ascending order. This is important for applications that require a particular order of partition.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
## Optional
- take_start
    - The take_start parameter specifies the starting index for the split range to be considered. When you only need to filter the subset of results, it is particularly useful, allowing for efficient data processing and reducing unnecessary processing.
    - Comfy dtype: INT
    - Python dtype: int
- take_count
    - The take_count parameter defines the number of partitions to be obtained from the filter result that starts with the index specified by Take_start. It is essential to control the amount of data processed and can be used to limit output to manageable size.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- DETAILER_HOOK
    - The output of SEGSOrderedFilterDetaylHookProvider is a fine hook that covers the logic of applying the specified filter and sorting operation. This hook can be used downstream of the processing process to further fine-tune and organize splits of results.
    - Comfy dtype: DETAILER_HOOK
    - Python dtype: SEGSOrderedFilterDetailerHook

# Usage tips
- Infra type: CPU

# Source code
```
class SEGSOrderedFilterDetailerHookProvider:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'target': (['area(=w*h)', 'width', 'height', 'x1', 'y1', 'x2', 'y2'],), 'order': ('BOOLEAN', {'default': True, 'label_on': 'descending', 'label_off': 'ascending'}), 'take_start': ('INT', {'default': 0, 'min': 0, 'max': sys.maxsize, 'step': 1}), 'take_count': ('INT', {'default': 1, 'min': 0, 'max': sys.maxsize, 'step': 1})}}
    RETURN_TYPES = ('DETAILER_HOOK',)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Util'

    def doit(self, target, order, take_start, take_count):
        hook = hooks.SEGSOrderedFilterDetailerHook(target, order, take_start, take_count)
        return (hook,)
```