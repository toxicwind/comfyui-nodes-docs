# Documentation
- Class name: AnimateDiffLoraLoader
- Category: Animate Diff 🎭🅐🅓
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved.git

The AnimatéDiffLoraLoader node is designed to easily load and apply the motion Lora model to the body. It allows for fine control of animations by mixing different Loa models according to the specified intensity. This node is essential for character animation missions that need to combine multiple effects of motion.

# Input types
## Required
- lora_name
    - The parameter 'lora_name' is essential for the identification of a particular motor Lora model to be loaded. It ensures that the model is correctly selected from the available options, which is essential for the operation of the node and for the eventual animation effect.
    - Comfy dtype: STRING
    - Python dtype: str
- strength
    - The parameter'strength' determines the intensity of the motion loa influence on animation. It is a key factor in micromobilization to achieve the desired effect, allowing for a balance between different layers of motion.
    - Comfy dtype: FLOAT
    - Python dtype: float
## Optional
- prev_motion_lora
    - The parameter'prev_motion_lora' is used to provide the state of the former motion loa model. It is important to maintain the consistency of the animation sequence and allows multiple Loa models to be added to the complex animation effect.
    - Comfy dtype: MOTION_LORA
    - Python dtype: MotionLoraList

# Output types
- MOTION_LORA
    - The output 'MOTION_LORA' indicates that the results of the Lora model were applied with the specified strength and blended with any previous loa model. It is important for subsequent animation steps and serves as a basis for further role animation.
    - Comfy dtype: MOTION_LORA
    - Python dtype: MotionLoraList

# Usage tips
- Infra type: CPU

# Source code
```
class AnimateDiffLoraLoader:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'lora_name': (get_available_motion_loras(),), 'strength': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 10.0, 'step': 0.001})}, 'optional': {'prev_motion_lora': ('MOTION_LORA',)}}
    RETURN_TYPES = ('MOTION_LORA',)
    CATEGORY = 'Animate Diff 🎭🅐🅓'
    FUNCTION = 'load_motion_lora'

    def load_motion_lora(self, lora_name: str, strength: float, prev_motion_lora: MotionLoraList=None):
        if prev_motion_lora is None:
            prev_motion_lora = MotionLoraList()
        else:
            prev_motion_lora = prev_motion_lora.clone()
        lora_path = get_motion_lora_path(lora_name)
        if not Path(lora_path).is_file():
            raise FileNotFoundError(f"Motion lora with name '{lora_name}' not found.")
        lora_info = MotionLoraInfo(name=lora_name, strength=strength)
        prev_motion_lora.add_lora(lora_info)
        return (prev_motion_lora,)
```