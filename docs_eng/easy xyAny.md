# Documentation
- Class name: xyAny
- Category: EasyUse/Logic
- Output node: False
- Repo Ref: https://github.com/yolain/ComfyUI-Easy-Use.git

The node class facilitates the reorganization of the input data into a structured format that is aligned to the horizontal or vertical direction. It is designed to simplify the data operation tasks by efficiently aligning the elements based on a given direction and to enhance the usefulness of the data in subsequent processing steps.

# Input types
## Required
- X
    - The parameter 'X' represents the first set of elements and will match the elements in 'Y'. It is important to create the side of the data pair, which is essential for the operation of nodes and the structure of the data generated.
    - Comfy dtype: COMBO[*]
    - Python dtype: List[Any]
- Y
    - The parameter 'Y' represents the second set of elements and is intended to match the elements in 'X'. It plays a vital role in the function of the node, as it determines the other side of the data pair, directly influences the final order of output.
    - Comfy dtype: COMBO[*]
    - Python dtype: List[Any]
- direction
    - The parameter 'direction' specifies the direction of the data pair, which can be 'horizontal' or'vertical'. It is very important because it defines the structure of the output and guides how the elements of 'X' and 'Y' are arranged into the desired format.
    - Comfy dtype: [str]
    - Python dtype: Union[str, AlwaysEqualProxy]

# Output types
- X
    - The output 'X' is a re-structured sequence of elements in the original 'X' input, which now matches the elements in the 'Y' according to the given direction. It represents half of the node output and has been converted to meet the horizontal or vertical requirements.
    - Comfy dtype: COMBO[*]
    - Python dtype: List[Any]
- Y
    - The output 'Y' is structurally similar to the output 'X', but consists of elements in the 'Y' input. It forms the other half of the node output and completes a combination of data sets based on the chosen direction.
    - Comfy dtype: COMBO[*]
    - Python dtype: List[Any]

# Usage tips
- Infra type: CPU

# Source code
```
class xyAny:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'X': (AlwaysEqualProxy('*'), {}), 'Y': (AlwaysEqualProxy('*'), {}), 'direction': (['horizontal', 'vertical'], {'default': 'horizontal'})}}
    RETURN_TYPES = (AlwaysEqualProxy('*'), AlwaysEqualProxy('*'))
    RETURN_NAMES = ('X', 'Y')
    INPUT_IS_LIST = True
    OUTPUT_IS_LIST = (True, True)
    CATEGORY = 'EasyUse/Logic'
    FUNCTION = 'to_xy'

    def to_xy(self, X, Y, direction):
        new_x = list()
        new_y = list()
        if direction[0] == 'horizontal':
            for y in Y:
                for x in X:
                    new_x.append(x)
                    new_y.append(y)
        else:
            for x in X:
                for y in Y:
                    new_x.append(x)
                    new_y.append(y)
        return (new_x, new_y)
```