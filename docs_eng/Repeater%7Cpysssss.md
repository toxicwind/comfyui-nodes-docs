# Repeater 🐍
## Documentation
- Class name: Repeater|pysssss
- Category: utils
- Output node: False
- Repo Ref: https://github.com/pythongosssss/ComfyUI-Custom-Scripts

The Repeater node is intended to repeat the given input source in a number of times, and can be exported as a single node or multiple nodes according to the selected mode. It abstractes the function of repeating data and facilitates the creation of multiple data examples or nodes in the workflow.

## Input types
### Required
- source
    - indicates the source input of the data to be duplicated. Its role is crucial, as it determines the basic elements to be repeated on the basis of the specified number of repetitions.
    - Comfy dtype: *
    - Python dtype: AnyType
- repeats
    - Specifies the number of times the source input should be repeated. This parameter directly affects the output and determines the number of duplicate data.
    - Comfy dtype: INT
    - Python dtype: int
- output
    - Determine whether duplicate data should be exported as individual nodes or multiple nodes, influencing the structure of the output.
    - Comfy dtype: COMBO[STRING]
    - Python dtype: str
- node_mode
    - Controls whether the duplicate nodes are reused or newly created, affecting how the nodes are added to the chart when sequenced.
    - Comfy dtype: COMBO[STRING]
    - Python dtype: str

## Output types
- *
    - Comfy dtype: *
    - Output is a list of duplicate data that can be structured differently according to the output and node_mode parameters.
    - Python dtype: List[AnyType]

## Usage tips
- Infra type: CPU
- Common nodes: unknown

## Source code
```python
class Repeater:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
            "source": (any, {}),
            "repeats": ("INT", {"min": 0, "max": 5000, "default": 2}),
            "output": (["single", "multi"], {}),
            "node_mode": (["reuse", "create"], {}),
        }}

    RETURN_TYPES = (any,)
    FUNCTION = "repeat"
    OUTPUT_NODE = False
    OUTPUT_IS_LIST = (True,)

    CATEGORY = "utils"

    def repeat(self, repeats, output, node_mode, **kwargs):
        if output == "multi":
            # Multi outputs are split to indiviual nodes on the frontend when serializing
            return ([kwargs["source"]],)
        elif node_mode == "reuse":
            # When reusing we have a single input node, repeat that N times
            return ([kwargs["source"]] * repeats,)
        else:
            # When creating new nodes, they'll be added dynamically when the graph is serialized
            return ((list(kwargs.values())),)