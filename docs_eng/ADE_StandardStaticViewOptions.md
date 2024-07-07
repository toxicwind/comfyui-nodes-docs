# Documentation
- Class name: StandardStaticViewOptionsNode
- Category: Animate Diff 🎭🅐🅓/context opts/view opts
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved.git

StandardStaticViewOptionsNode aims to generate a set of options for static viewings in the context of animations. It allows custom view lengths and overlaps to ensure seamless and consistent animation experiences. This node plays a key role in defining how different frames or segments of animations are presented to the audience.

# Input types
## Required
- view_length
    - The view_length parameter determines the number of frames or elements displayed in each view. It is essential for setting the scope and level of detail of the animation, affecting the overall viewing experience.
    - Comfy dtype: INT
    - Python dtype: int
- view_overlap
    - View_overlap parameters specify the degree of overlap between adjacent views. This is important for continuity and can help create smooth transitions between different parts of the animation.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- fuse_method
    - The fuse_method parameter defines the method used to group or integrate different views in the animation. It may significantly affect the final appearance and the way information is communicated through the animation sequence.
    - Comfy dtype: ContextFuseMethod.LIST
    - Python dtype: str

# Output types
- view_options
    - The view_options output provides a structured set of options that determine the configuration of the view in the animation. It encapsulates the parameters of the user settings and is essential for the animation implementation.
    - Comfy dtype: VIEW_OPTS
    - Python dtype: ContextOptions

# Usage tips
- Infra type: CPU

# Source code
```
class StandardStaticViewOptionsNode:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'view_length': ('INT', {'default': 16, 'min': 1, 'max': LENGTH_MAX}), 'view_overlap': ('INT', {'default': 4, 'min': 0, 'max': OVERLAP_MAX})}, 'optional': {'fuse_method': (ContextFuseMethod.LIST,)}}
    RETURN_TYPES = ('VIEW_OPTS',)
    CATEGORY = 'Animate Diff 🎭🅐🅓/context opts/view opts'
    FUNCTION = 'create_options'

    def create_options(self, view_length: int, view_overlap: int, fuse_method: str=ContextFuseMethod.FLAT):
        view_options = ContextOptions(context_length=view_length, context_stride=None, context_overlap=view_overlap, context_schedule=ContextSchedules.STATIC_STANDARD, fuse_method=fuse_method)
        return (view_options,)
```