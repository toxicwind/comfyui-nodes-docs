# Documentation
- Class name: SEGSRangeFilterDetailerHookProvider
- Category: ImpactPack/Util
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

SEGSRangeFilterDetailer HookProvider is designed to apply filtering mechanisms to split processes. It ensures that only those parts that meet the definition criteria are considered according to the specified range filter. This node enhances the accuracy of partitions by focusing on the relevant area of the user-defined parameters.

# Input types
## Required
- target
    - The 'target' parameter defines the area of interest in the split process. It is vital because it determines which segments will be filtered. Nodes operate according to the dimensions and coordinates provided, making this parameter the core of the process.
    - Comfy dtype: COMBO[area(=w*h), width, height, x1, y1, x2, y2, length_percent]
    - Python dtype: Union[str, Tuple[int, int]]
- mode
    - The'mode' parameter determines whether the target area should be preserved or whether the segment should be out of the area. This is a binary option that significantly influences the results of the partition and allows accurate control of the filtering criteria.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- min_value
    - The'min_value'parameter sets a minimum threshold for a segment value. It plays a key role in filtering a paragraph that does not meet the minimum standard value, thus refining the split result.
    - Comfy dtype: INT
    - Python dtype: int
- max_value
    - The'max_value 'parameter sets the maximum limit on the value of the segment. It ensures that the section beyond this limit is removed from the final partition and retains the integrity of the filter output.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- DETAILER_HOOK
    - The output 'DETAILER_HOOK' is a hook object that covers the filter criteria and applies them to the partition process. It is important because it represents the result of node operations and provides a way to integrate the filter logic into a wider split workflow.
    - Comfy dtype: DETAILER_HOOK
    - Python dtype: SEGSRangeFilterDetailerHook

# Usage tips
- Infra type: CPU

# Source code
```
class SEGSRangeFilterDetailerHookProvider:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'target': (['area(=w*h)', 'width', 'height', 'x1', 'y1', 'x2', 'y2', 'length_percent'],), 'mode': ('BOOLEAN', {'default': True, 'label_on': 'inside', 'label_off': 'outside'}), 'min_value': ('INT', {'default': 0, 'min': 0, 'max': sys.maxsize, 'step': 1}), 'max_value': ('INT', {'default': 67108864, 'min': 0, 'max': sys.maxsize, 'step': 1})}}
    RETURN_TYPES = ('DETAILER_HOOK',)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Util'

    def doit(self, target, mode, min_value, max_value):
        hook = hooks.SEGSRangeFilterDetailerHook(target, mode, min_value, max_value)
        return (hook,)
```