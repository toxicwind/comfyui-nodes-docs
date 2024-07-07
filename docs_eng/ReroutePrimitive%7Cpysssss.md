# Reroute Primitive 🐍
## Documentation
- Class name: ReroutePrimitive|pysssss
- Category: utils
- Output node: False
- Repo Ref: https://github.com/pythongosssss/ComfyUI-Custom-Scripts

The ReroutePrimitive node is intended to transmit any given input without modification and to serve as a common connector in the data flow architecture. It abstractes the complexity of the data type and allows flexibility in rerouting the data flow.

## Input types
### Required
- value
    - The 'value'parameter, as a node, does not modify the common input of the transmission. It is the core of the node function, enabling it to act as a multifunctional connector in various data-processing scenarios.
    - Comfy dtype: *
    - Python dtype: AnyType

## Output types
- *
    - Comfy dtype: *
    - Output is a group that contains unmodified input values and promotes seamless data rerouting.
    - Python dtype: Tuple[AnyType]

## Usage tips
- Infra type: CPU
<!-- - Common nodes:
    - [ImageUpscaleWithModel](../../Comfy/Nodes/ImageUpscaleWithModel.md)
    - [CLIPTextEncodeSDXL](../../Comfy/Nodes/CLIPTextEncodeSDXL.md)
    - [CLIPTextEncode](../../Comfy/Nodes/CLIPTextEncode.md)
    - [ColorCorrect](../../comfyui-art-venture/Nodes/ColorCorrect.md)
    - [ImageCompositeMasked](../../Comfy/Nodes/ImageCompositeMasked.md)
    - [ReroutePrimitive|pysssss](../../ComfyUI-Custom-Scripts/Nodes/ReroutePrimitive|pysssss.md)
    - [SaveImage](../../Comfy/Nodes/SaveImage.md) -->

## Source code
```python
class ReroutePrimitive:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {"value": (any, )},
        }

    @classmethod
    def VALIDATE_INPUTS(s, **kwargs):
        return True

    RETURN_TYPES = (any,)
    FUNCTION = "route"
    CATEGORY = "utils"

    def route(self, value):
        return (value,)