# Documentation
- Class name: MakeInterpolationStateList
- Category: ComfyUI-Frame-Interpolation/VFI
- Output node: False
- Repo Ref: https://github.com/Fannovel16/ComfyUI-Frame-Interpolation

The node is designed to manage and create the plug-in status list, which is essential to the frame-plug-in process. It determines which frames contain or skip in the plug-in process, thereby optimizing the calculation of workload and ensuring smooth and consistent frame transitions.

# Input types
## Required
- frame_indices
    - This parameter specifies a comma-separated list of frame indexes that will be used by the node to determine which frames are contained or skipped during the plug-in. This is essential for the proper running of the node and directly affects the results of the plug-in.
    - Comfy dtype: STRING
    - Python dtype: List[int]
## Optional
- is_skip_list
    - This parameter controls whether the specified frame index should be skipped or included during the plugin process. It plays an important role in the overall operation of the node, as it determines how the node behaves during the frame selection period.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- INTERPOLATION_STATES
    - The output of this node is an Interpolation StateList object that encapsifies decisions about which frames to contain or skip. This object is essential for relying on these decisions to follow up actual frame plugs.
    - Comfy dtype: INTERPOLATION_STATES
    - Python dtype: InterpolationStateList

# Usage tips
- Infra type: CPU

# Source code
```
class MakeInterpolationStateList:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'frame_indices': ('STRING', {'multiline': True, 'default': '1,2,3'}), 'is_skip_list': ('BOOLEAN', {'default': True})}}
    RETURN_TYPES = ('INTERPOLATION_STATES',)
    FUNCTION = 'create_options'
    CATEGORY = 'ComfyUI-Frame-Interpolation/VFI'

    def create_options(self, frame_indices: str, is_skip_list: bool):
        frame_indices_list = [int(item) for item in frame_indices.split(',')]
        interpolation_state_list = InterpolationStateList(frame_indices=frame_indices_list, is_skip_list=is_skip_list)
        return (interpolation_state_list,)
```