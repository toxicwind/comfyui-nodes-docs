# Documentation
- Class name: GeneralInversedSwitch
- Category: ImpactPack/Util
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The GeneralInversedSwitch node is designed to selectively process input data according to the selected parameter. It operates through an iterative input from'select' and adds 'input' data to the result list under conditions. The function of the node is to return the original input when the iterative number matches the'select' value, otherwise it will add 'Noone'. This node is particularly useful in scenarios where conditional data are displayed or filtered without changing the original data structure.

# Input types
## Required
- select
    - The parameter'select' determines the number of rotations in node operations. It is vital because it determines when the 'input' data is included in the output of the node. The significance of'select' is that it is able to control the flow of the data through nodes, so that conditions are processed according to the iterative index.
    - Comfy dtype: INT
    - Python dtype: int
- input
    - The parameter 'input' represents data that may be processed and included in its output under certain conditions. It is important because it is the subject of node conditions logic, and the node decides whether to add 'input' or 'Noone' is based on'select' values.
    - Comfy dtype: any_typ
    - Python dtype: Any
## Optional
- unique_id
    - Parameter'unique_id' is the identifier for node operations. Although it does not directly affect the main function of node, it may be used to track or associate node output with specific examples or identifiers in a broader system.
    - Comfy dtype: UNIQUE_ID
    - Python dtype: str

# Output types
- result
    - Output'redult' is a list that contains the original 'input' data or 'Noone' based on the value and iterative index of the'select' parameter. This output is important because it summarizes the decision-making process of the node and reflects the purpose of the node conditional data.
    - Comfy dtype: COMBO[any_typ]
    - Python dtype: List[Any]

# Usage tips
- Infra type: CPU

# Source code
```
class GeneralInversedSwitch:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'select': ('INT', {'default': 1, 'min': 1, 'max': 999999, 'step': 1}), 'input': (any_typ,)}, 'hidden': {'unique_id': 'UNIQUE_ID'}}
    RETURN_TYPES = ByPassTypeTuple((any_typ,))
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Util'

    def doit(self, select, input, unique_id):
        res = []
        for i in range(0, select):
            if select == i + 1:
                res.append(input)
            else:
                res.append(None)
        return res
```