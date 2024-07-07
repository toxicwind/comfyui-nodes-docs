# Documentation
- Class name: AnimateDiffLoraLoader
- Category: Animate Diff
- Output node: False
- Repo Ref: https://github.com/ArtVentureX/comfyui-animatediff.git

The node is designed to integrate animated differences into the model by loading and processing the Lora file, adding dynamic elements to the model's appearance or behaviour. It focuses on seamless integration of motion and transformation of data to improve the overall animated quality without compromising the structural integrity of the model.

# Input types
## Required
- lora_name
    - The lora_name parameter is essential because it specifies the only identifier for the Lora file to be loaded, which contains the movement and transformation data required for the animation process. The correct use of this parameter ensures the accurate selection and application of the animation differences required.
    - Comfy dtype: STRING
    - Python dtype: str
- alpha
    - The alpha parameter controls the intensity of the animated effects applied to the model. It is essential to adjust the visibility of the animated differences in the final output and allows fine-tuning of visual effects.
    - Comfy dtype: FLOAT
    - Python dtype: float
## Optional
- lora_stack
    - The lora_stack parameter is an optional list that accumulates Lora data and its component groups that correspond to alpha values. It plays a role in managing multiple animated variance layers and provides a structured way to process and organize animation sequences.
    - Comfy dtype: LIST[tuple]
    - Python dtype: List[Tuple[str, float]]

# Output types
- lora_stack
    - The output lora_stack is a group list of processed Lora data and their corresponding alpha values. This list is essential for further processing and integration into the model as the main output of animation differences.
    - Comfy dtype: LIST[tuple]
    - Python dtype: List[Tuple[str, float]]

# Usage tips
- Infra type: CPU

# Source code
```
class AnimateDiffLoraLoader:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'lora_name': (get_available_loras(),), 'alpha': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 10.0, 'step': 0.001})}, 'optional': {'lora_stack': ('MOTION_LORA_STACK',)}}
    RETURN_TYPES = ('MOTION_LORA_STACK',)
    CATEGORY = 'Animate Diff'
    FUNCTION = 'load_lora'

    def load_lora(self, lora_name: str, alpha: float, lora_stack: List=None):
        if not lora_stack:
            lora_stack = []
        lora = load_lora(lora_name)
        lora_stack.append((lora, alpha))
        return (lora_stack,)
```