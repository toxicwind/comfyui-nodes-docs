# Documentation
- Class name: CR_XYList
- Category: Comfyroll/XY Grid
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

The CR_XYList node is designed to cross-link the two lists and generate a combined grid. It increases the flexibility of output by adding prefixes and suffix strings to the list element. The node also provides comments and trigger mechanisms to indicate the completion of grid generation.

# Input types
## Required
- index
    - Index parameters are essential for determining where the current combination is located in the grid. It influences the execution of nodes by deciding which elements in the input list are to be exported.
    - Comfy dtype: INT
    - Python dtype: int
- list1
    - List1 is the first input list for cross-connection operations. It plays a key role in the function of the node by contributing to the generation of horizontal elements of the grid.
    - Comfy dtype: STRING
    - Python dtype: str
- list2
    - List2 is the second input list for cross-connection operations, which is essential for creating vertical elements of the grid.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- x_prepend
    - The x_prepend parameter allows the prefix to be added to each element in list1. This can be used to define the output format or to add context to the element.
    - Comfy dtype: STRING
    - Python dtype: str
- x_append
    - x_append parameters are used to add a suffix to each element in list1 to provide further customisation of the output element.
    - Comfy dtype: STRING
    - Python dtype: str
- x_annotation_prepend
    - x_annotation_prepend parameters are used to add comment prefixes to each element in list1 at the time the comment is generated. It enhances the descriptive nature of the comment.
    - Comfy dtype: STRING
    - Python dtype: str
- y_prepend
    - y_prepend parameters allow the prefix to be added to each element in list2 and allow the output of custom vertical elements.
    - Comfy dtype: STRING
    - Python dtype: str
- y_append
    - y_append parameters are used to add a suffix to each element in list2 to provide additional control over the final format of the vertical element.
    - Comfy dtype: STRING
    - Python dtype: str
- y_annotation_prepend
    - y_announcement_prepend parameters allow for the addition of comment prefixes for each element in list2 at the time the comment is generated, thus increasing the amount of information in the comment.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- X
    - X Output represents the horizontal grouping of elements of list 1 under the current index. It is a key component of the grid line.
    - Comfy dtype: STRING
    - Python dtype: str
- Y
    - Y Output represents a vertical combination of elements for list2 under the corresponding index. It is a key component of the grid.
    - Comfy dtype: STRING
    - Python dtype: str
- x_annotation
    - An annotated version of the list1 element is provided at the end of the grid generation of x_annotation output, which enhances the interpretability of the result.
    - Comfy dtype: STRING
    - Python dtype: str
- y_annotation
    - The y_annotation output provides an annotated version of the list2 element upon completion of grid generation, adding context to the interpretation of the result.
    - Comfy dtype: STRING
    - Python dtype: str
- trigger
    - The trigger output indicates when the grid generation is complete and marks the end of the cross-linking process.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- show_help
    - Show_help output provides a URL link to the document for further help and guidance on using this node.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_XYList:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'index': ('INT', {'default': 0.0, 'min': 0.0, 'max': 9999.0, 'step': 1.0}), 'list1': ('STRING', {'multiline': True, 'default': 'x'}), 'x_prepend': ('STRING', {'multiline': False, 'default': ''}), 'x_append': ('STRING', {'multiline': False, 'default': ''}), 'x_annotation_prepend': ('STRING', {'multiline': False, 'default': ''}), 'list2': ('STRING', {'multiline': True, 'default': 'y'}), 'y_prepend': ('STRING', {'multiline': False, 'default': ''}), 'y_append': ('STRING', {'multiline': False, 'default': ''}), 'y_annotation_prepend': ('STRING', {'multiline': False, 'default': ''})}}
    RETURN_TYPES = ('STRING', 'STRING', 'STRING', 'STRING', 'BOOLEAN', 'STRING')
    RETURN_NAMES = ('X', 'Y', 'x_annotation', 'y_annotation', 'trigger', 'show_help')
    FUNCTION = 'cross_join'
    CATEGORY = icons.get('Comfyroll/XY Grid')

    def cross_join(self, list1, list2, x_prepend, x_append, x_annotation_prepend, y_prepend, y_append, y_annotation_prepend, index):
        index -= 1
        trigger = False
        listx = re.split(',(?=(?:[^"]*"[^"]*")*[^"]*$)', list1)
        listy = re.split(',(?=(?:[^"]*"[^"]*")*[^"]*$)', list2)
        listx = [item.strip() for item in listx]
        listy = [item.strip() for item in listy]
        lenx = len(listx)
        leny = len(listy)
        grid_size = lenx * leny
        x = index % lenx
        y = int(index / lenx)
        x_out = x_prepend + listx[x] + x_append
        y_out = y_prepend + listy[y] + y_append
        x_ann_out = ''
        y_ann_out = ''
        if index + 1 == grid_size:
            x_ann_out = [x_annotation_prepend + item + ';' for item in listx]
            y_ann_out = [y_annotation_prepend + item + ';' for item in listy]
            x_ann_out = ''.join([str(item) for item in x_ann_out])
            y_ann_out = ''.join([str(item) for item in y_ann_out])
            trigger = True
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/XY-Grid-Nodes#cr-xy-list'
        return (x_out, y_out, x_ann_out, y_ann_out, trigger, show_help)
```