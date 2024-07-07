# Documentation
- Class name: CR_XYInterpolate
- Category: Comfyroll/XY Grid
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

The CR_XYInterpolate node is designed to generate a gradient on the XY grid. It calculates the plug value along the X-axis and Y-axis and provides a smooth transition between the specified starting point and the end point. This node applies in particular to the creation of complex gradients and allows the use of custom label comment grid points.

# Input types
## Required
- x_columns
    - x_columns parameters define the number of columns in the grid. It is essential to determine the horizontal spacing and overall structure of the grid layout.
    - Comfy dtype: INT
    - Python dtype: int
- x_start_value
    - x_start_value sets the initial value of the X-axis plug value. It is important because it establishes the starting point for the gradient calculation on the grid.
    - Comfy dtype: FLOAT
    - Python dtype: float
- x_step
    - x_step parameters specify the increment between successive X values in the grid. It is essential to control the rate of change along the horizontal axis.
    - Comfy dtype: FLOAT
    - Python dtype: float
- y_rows
    - y_rows parameters specify the number of rows in the grid. It is essential for building the vertical structure and spacing within the grid.
    - Comfy dtype: INT
    - Python dtype: int
- y_start_value
    - y_start_value sets the initial value of the Y-axis plug value. It is a key parameter for determining the starting point for the calculation of the gradient on the grid line.
    - Comfy dtype: FLOAT
    - Python dtype: float
- y_step
    - y_step parameters determine the increment between successive Y values in the grid. It is important to control the progress of the vertical gradient.
    - Comfy dtype: FLOAT
    - Python dtype: float
- index
    - The index parameter is used to refer to the specific location in the grid. It determines which plugs are calculated and returned.
    - Comfy dtype: INT
    - Python dtype: int
- gradient_profile
    - The gradient_profile parameter selects the type of gradient profile to be used. It affects how the value is executed.
    - Comfy dtype: COMBO['Lerp']
    - Python dtype: str
## Optional
- x_annotation_prepend
    - x_annotation_prepend allows the addition of custom prefixes to each X note. This can be used to include additional context or information in the note.
    - Comfy dtype: STRING
    - Python dtype: str
- y_annotation_prepend
    - y_announcement_prepend parameters allow for the addition of custom prefixes to each Y note and the enhancement of notes by additional details or context.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- X
    - X output provides a plug value X value for the specified grid position. It is the key result of the gradient calculation process.
    - Comfy dtype: FLOAT
    - Python dtype: float
- Y
    - Y output provides a plug-in value of Y for the specified grid position. It represents an important result of the gradient plug-in value.
    - Comfy dtype: FLOAT
    - Python dtype: float
- x_annotation
    - x_annotation returns the string that represents the X-value comment on the grid. It is used to mark the grid points and provide context.
    - Comfy dtype: STRING
    - Python dtype: str
- y_annotation
    - y_annotation produces a string for the comment of the Y value in the grid. It helps to identify and position the vertical points of the grid.
    - Comfy dtype: STRING
    - Python dtype: str
- trigger
    - Trigger output indicates when a specific condition is met, such as reaching the last grid point. It can be used to start further action or process.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- show_help
    - Show_help provides a URL link to the node document page. It provides direct access to more detailed information and to the node.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_XYInterpolate:

    @classmethod
    def INPUT_TYPES(s):
        gradient_profiles = ['Lerp']
        return {'required': {'x_columns': ('INT', {'default': 5.0, 'min': 0.0, 'max': 9999.0, 'step': 1.0}), 'x_start_value': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 9999.0, 'step': 0.01}), 'x_step': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 9999.0, 'step': 0.01}), 'x_annotation_prepend': ('STRING', {'multiline': False, 'default': ''}), 'y_rows': ('INT', {'default': 5.0, 'min': 0.0, 'max': 9999.0, 'step': 1.0}), 'y_start_value': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 9999.0, 'step': 0.01}), 'y_step': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 9999.0, 'step': 0.01}), 'y_annotation_prepend': ('STRING', {'multiline': False, 'default': ''}), 'index': ('INT', {'default': 0.0, 'min': 0.0, 'max': 9999.0, 'step': 1.0}), 'gradient_profile': (gradient_profiles,)}}
    RETURN_TYPES = ('FLOAT', 'FLOAT', 'STRING', 'STRING', 'BOOLEAN', 'STRING')
    RETURN_NAMES = ('X', 'Y', 'x_annotation', 'y_annotation', 'trigger', 'show_help')
    FUNCTION = 'gradient'
    CATEGORY = icons.get('Comfyroll/XY Grid')

    def gradient(self, x_columns, x_start_value, x_step, x_annotation_prepend, y_rows, y_start_value, y_step, y_annotation_prepend, index, gradient_profile):
        index -= 1
        trigger = False
        grid_size = x_columns * y_rows
        x = index % x_columns
        y = int(index / x_columns)
        x_float_out = round(x_start_value + x * x_step, 3)
        y_float_out = round(y_start_value + y * y_step, 3)
        x_ann_out = ''
        y_ann_out = ''
        if index + 1 == grid_size:
            for i in range(0, x_columns):
                x = index % x_columns
                x_float_out = x_start_value + i * x_step
                x_float_out = round(x_float_out, 3)
                x_ann_out = x_ann_out + x_annotation_prepend + str(x_float_out) + '; '
            for j in range(0, y_rows):
                y = int(index / x_columns)
                y_float_out = y_start_value + j * y_step
                y_float_out = round(y_float_out, 3)
                y_ann_out = y_ann_out + y_annotation_prepend + str(y_float_out) + '; '
            x_ann_out = x_ann_out[:-1]
            y_ann_out = y_ann_out[:-1]
            print(x_ann_out, y_ann_out)
            trigger = True
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/XY-Grid-Nodes#cr-xy-interpolate'
        return (x_float_out, y_float_out, x_ann_out, y_ann_out, trigger, show_help)
```