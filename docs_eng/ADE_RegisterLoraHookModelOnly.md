# Register LoRA Hook (Model Only) 🎭🅐🅓
## Documentation
- Class name: ADE_RegisterLoraHookModelOnly
- Category: Animate Diff 🎭🅐🅓/conditioning/register lora hooks
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved.git

This node aims to link the model to LoRA (low adaptation) and focuses on the model rather than on any CLIP model. It adapts and enhances model behaviour through LoRA technology, providing a simplified way to integrate LoRA into the model to achieve advanced customization and performance improvement.

## Input types
### Required
- model
    - The LoRA linkage model is to be registered. It is the main objective of LoRA adaptation and determines the scope and impact of the application of the modifications.
    - Comfy dtype: MODEL
    - Python dtype: Union[ModelPatcher, ModelPatcherAndInjector]
- lora_name
    - The name of the LoRA configuration that you want to apply. Specifies the specific LoRA adaptation settings and parameters that you want to use, and guides the customization process.
    - Comfy dtype: COMBO[STRING]
    - Python dtype: str
- strength_model
    - A floating point value indicates that LoRA adapts to the strength of the model. This parameter controls the intensity of the LoRA modifications applied and allows fine-tuning of model behaviour.
    - Comfy dtype: FLOAT
    - Python dtype: float

## Output types
- model
    - Comfy dtype: MODEL
    - A LoRA-linked model is registered. This output reflects the modified state of the model and shows the effects of LoRA adaptation.
    - Python dtype: ModelPatcher
- lora_hook
    - Comfy dtype: LORA_HOOK
    - This output represents the LoRA adaptation mechanism applied to facilitate further customization and performance improvement.
    - Python dtype: LoraHook

## Usage tips
- Infra type: CPU
- Common nodes: unknown

## Source code
```python
class MaskableLoraLoaderModelOnly(MaskableLoraLoader):
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "model": ("MODEL",),
                "lora_name": (folder_paths.get_filename_list("loras"), ),
                "strength_model": ("FLOAT", {"default": 1.0, "min": -20.0, "max": 20.0, "step": 0.01}),
            }
        }

    RETURN_TYPES = ("MODEL", "LORA_HOOK")
    CATEGORY = "Animate Diff 🎭🅐🅓/conditioning/register lora hooks"
    FUNCTION = "load_lora_model_only"

    def load_lora_model_only(self, model: ModelPatcher, lora_name: str, strength_model: float):
        model_lora, clip_lora, lora_hook = self.load_lora(mod