# Documentation
- Class name: WAS_Image_Bounds_to_Console
- Category: WAS Suite/Debug
- Output node: True
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Image_Bounds_to_Console node is designed to facilitate the debugging process by exporting image boundary information to the control table. It enhances the visibility of the image processing phase by providing a clear, formatted boundary display, which helps to analyse and validate image operation workflows.

# Input types
## Required
- image_bounds
    - The Image_Bounds parameter is essential for the operation of the node because it defines the interest area within the image. It is used to identify and isolate certain parts of the image for further processing or analysis, and thus plays an important role in the execution of the node and the results it produces.
    - Comfy dtype: IMAGE_BOUNDS
    - Python dtype: List[Tuple[int, int, int, int]]
## Optional
- label
    - The label parameter is used as a descriptive identifier for debugging output. Although not mandatory, it can be used to define the output from the control table to make it easier to distinguish between different debugging messages that are particularly useful in complex debugging scenarios.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- image_bounds
    - The output image_bounds parameter retains the image boundary data entered to ensure that debugging information is accurately reflected in the control counter output. This parameter is important because it allows the image boundary to be verified after node processing.
    - Comfy dtype: IMAGE_BOUNDS
    - Python dtype: List[Tuple[int, int, int, int]]

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Image_Bounds_to_Console:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'image_bounds': ('IMAGE_BOUNDS',), 'label': ('STRING', {'default': 'Debug to Console', 'multiline': False})}}
    RETURN_TYPES = ('IMAGE_BOUNDS',)
    OUTPUT_NODE = True
    FUNCTION = 'debug_to_console'
    CATEGORY = 'WAS Suite/Debug'

    def debug_to_console(self, image_bounds, label):
        label_out = 'Debug to Console'
        if label.strip() != '':
            label_out = label
        bounds_out = 'Empty'
        if len(bounds_out) > 0:
            bounds_out = ', \n    '.join(('\t(rmin={}, rmax={}, cmin={}, cmax={})'.format(a, b, c, d) for (a, b, c, d) in image_bounds))
        cstr(f'\x1b[33m{label_out}\x1b[0m:\n[\n{bounds_out}\n]\n').msg.print()
        return (image_bounds,)

    @classmethod
    def IS_CHANGED(cls, **kwargs):
        return float('NaN')
```