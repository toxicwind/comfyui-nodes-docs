# Documentation
- Class name: SEGSLabelFilterDetailerHookProvider
- Category: ImpactPack/Util
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The SEGSLabelFilterDetailer HookProvider node is designed to filter split labels in the system. It plays a key role in ensuring that only the required types of paragraphs are processed, thus increasing the accuracy and relevance of follow-up analysis and operations.

# Input types
## Required
- preset
    - Preset parameters determine the initial setting or configuration of node operations. It is essential because it determines the starting point of node processing and affects the final result.
    - Comfy dtype: STRING
    - Python dtype: str
- labels
    - The label parameter is a list of the types of segments that are indicated to be allowed. It is a key input because it directly affects which segments pass through the filtering process.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- DETAILER_HOOK
    - The output of the node is a hook object that has been configured with a specified label. This hook object is important because it is used to apply filter criteria to split processes.
    - Comfy dtype: OBJECT
    - Python dtype: SEGSLabelFilterDetailerHook

# Usage tips
- Infra type: CPU

# Source code
```
class SEGSLabelFilterDetailerHookProvider:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'segs': ('SEGS',), 'preset': (['all'] + defs.detection_labels,), 'labels': ('STRING', {'multiline': True, 'placeholder': 'List the types of segments to be allowed, separated by commas'})}}
    RETURN_TYPES = ('DETAILER_HOOK',)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Util'

    def doit(self, preset, labels):
        hook = hooks.SEGSLabelFilterDetailerHook(labels)
        return (hook,)
```