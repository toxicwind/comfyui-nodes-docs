# Documentation
- Class name: SeargeLatentMuxer3
- Category: Searge/_deprecated_/FlowControl
- Output node: False
- Repo Ref: https://github.com/jobunk/SeargeSDXL.git

SeergeLatentMuxer3 is a node for managing potential data streams that controls data flows by selecting one of the three potential inputs provided, depending on the value of the input selection. This node is essential to control data flows in a complex network that requires a conditional route.

# Input types
## Required
- input0
    - The first potential input, the node can be selected and routed to the output. It plays a key role in the decision-making process at the node when the input selection does not indicate any other input.
    - Comfy dtype: "LATENT"
    - Python dtype: np.ndarray or a similar array type representing latent data
- input1
    - Node's second potential input option. When the input selection is set to 1, it becomes an output and guides the data stream accordingly.
    - Comfy dtype: "LATENT"
    - Python dtype: np.ndarray or a similar array type representing latent data
- input2
    - The third potential input that can be selected by the node. When the value of the input selection is 2, it is selected for output, so that the data flow path is determined.
    - Comfy dtype: "LATENT"
    - Python dtype: np.ndarray or a similar array type representing latent data
- input_selector
    - This integer parameter determines which potential input is selected as an output. It is essential in the operation of the node, as it directly influences the route.
    - Comfy dtype: "INT"
    - Python dtype: int

# Output types
- output
    - The output of the node is a potential input based on the value selection of the input selector. This output carries data that will continue to be transmitted through the network.
    - Comfy dtype: "LATENT"
    - Python dtype: np.ndarray or a similar array type representing the selected latent data

# Usage tips
- Infra type: CPU

# Source code
```
class SeargeLatentMuxer3:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'input0': ('LATENT',), 'input1': ('LATENT',), 'input2': ('LATENT',), 'input_selector': ('INT', {'default': 0, 'min': 0, 'max': 2})}}
    RETURN_TYPES = ('LATENT',)
    RETURN_NAMES = ('output',)
    FUNCTION = 'mux'
    CATEGORY = 'Searge/_deprecated_/FlowControl'

    def mux(self, input0, input1, input2, input_selector):
        if input_selector == 1:
            return (input1,)
        elif input_selector == 2:
            return (input2,)
        else:
            return (input0,)
```