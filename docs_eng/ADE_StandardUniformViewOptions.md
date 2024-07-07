# Documentation
- Class name: StandardUniformViewOptionsNode
- Category: Animate Diff 🎭🅐🅓/context opts/view opts
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved.git

StandardUniformViewOptionsNode aims to generate a single set of view options for animating variations. It focuses on creating a structured approach to the animation process that ensures consistency and uniformity in the animation process. The node abstractes the complexity of viewing scheduling and provides users with a direct method of defining and applying view parameters.

# Input types
## Required
- view_length
    - The view_length parameter defines the length of each view in the animation sequence. It is essential to determine the scope and detail of each individual view, thus affecting the quality and composition of the overall animation.
    - Comfy dtype: INT
    - Python dtype: int
- view_stride
    - The view_standard parameter specifies the interval between successive views in the animation. It plays an important role in controlling the animated rhythm and ensuring consistency in the transition between views and attracting people visualally.
    - Comfy dtype: INT
    - Python dtype: int
- view_overlap
    - View_overlap parameters indicate the amount of overlap between adjacent views in the animation. This is important for creating a seamless and smooth animation experience, in which the transition between views is not sudden.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- fuse_method
    - The fuse_method parameter determines the method used to integrate the view in the animation. It provides flexibility in how the view is combined, allowing for different visual effects and creative control of the final output.
    - Comfy dtype: ContextFuseMethod.LIST
    - Python dtype: str

# Output types
- view_options
    - The view_options output provides a set of structured options to define the view properties in the animation. It covers parameters such as view length, length and overlap, which are essential for animating execution and final appearance.
    - Comfy dtype: VIEW_OPTS
    - Python dtype: ContextOptions

# Usage tips
- Infra type: CPU

# Source code
```
class StandardUniformViewOptionsNode:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'view_length': ('INT', {'default': 16, 'min': 1, 'max': LENGTH_MAX}), 'view_stride': ('INT', {'default': 1, 'min': 1, 'max': STRIDE_MAX}), 'view_overlap': ('INT', {'default': 4, 'min': 0, 'max': OVERLAP_MAX})}, 'optional': {'fuse_method': (ContextFuseMethod.LIST,)}}
    RETURN_TYPES = ('VIEW_OPTS',)
    CATEGORY = 'Animate Diff 🎭🅐🅓/context opts/view opts'
    FUNCTION = 'create_options'

    def create_options(self, view_length: int, view_overlap: int, view_stride: int, fuse_method: str=ContextFuseMethod.PYRAMID):
        view_options = ContextOptions(context_length=view_length, context_stride=view_stride, context_overlap=view_overlap, context_schedule=ContextSchedules.UNIFORM_STANDARD, fuse_method=fuse_method)
        return (view_options,)
```