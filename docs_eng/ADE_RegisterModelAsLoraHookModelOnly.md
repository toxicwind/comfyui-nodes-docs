# Register Model as LoRA Hook (MO) 🎭🅐🅓
## Documentation
- Class name: ADE_RegisterModelAsLoraHookModelOnly
- Category: Animate Diff 🎭🅐🅓/conditioning/register lora hooks
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved.git

This node is dedicated to linking model registration to LoRA, with a focus on model modifications only. It allows the integration of LoRA (low-adaptation) technologies into specific models, enhancing their adaptability and performance in order to perform specific tasks without affecting other components.

## Input types
### Required
- model
    - Models for adaptation using LoRA technology. As the main objective of applying low-level adaptation, it aims to enhance its performance or adaptability to perform specific tasks.
    - Comfy dtype: MODEL
    - Python dtype: ModelPatcher
- ckpt_name
    - This parameter specifies the LoRA adaptation set to be used to guide the custom of model behaviour.
    - Comfy dtype: COMBO[STRING]
    - Python dtype: str
- strength_model
    - A floating point value determines the intensity of LoRA's adaptation to the model. It regulates the extent to which the LoRA parameters affect model behaviour.
    - Comfy dtype: FLOAT
    - Python dtype: float

## Output types
- model
    - Comfy dtype: MODEL
    - Apply the models that specify how LoRA adapts. This output reflects an enhanced version that is customized through LoRA technology.
    - Python dtype: ModelPatcher
- lora_hook
    - Comfy dtype: LORA_HOOK
    - The output provides access to the application of the LoRA adaptation for further operation or analysis.
    - Python dtype: LoraHook

## Usage tips
- Infra type: CPU
- Common nodes: unknown

## Source code
```python
class MaskableSDModelLoaderModelOnly(MaskableSDModelLoader):
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "model": ("MODEL",),
                "ckpt_name": (folder_paths.get_filename_list("checkpoints"), ),
                "strength_model": ("FLOAT", {"default": 1.0, "min": -20.0, "max": 20.0, "step": 0.01}),
            }
        }
    
    RETURN_TYPES = ("MODEL", "LORA_HOOK")
    CATEGORY = "Animate Diff 🎭🅐🅓/conditioning/register lora hooks"
    FUNCTION = "load_model_as_lora_model_only"

    def load_model_as_lora_model_only(self, model: ModelPatcher, ckpt_name: str, strength_model: float):
        model_lora, clip_lora, lora_hook = self.load_model_as_lora(model=model, clip=None, ckpt_name=ckpt_name,
                                                                   strength_model=strength_model, strength_clip=0)
        return (model_lora, lora_hook)