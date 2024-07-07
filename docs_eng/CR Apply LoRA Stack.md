# Documentation
- Class name: CR_ApplyLoRAStack
- Category: Comfyroll/LoRA
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_ApplyLoRAStack is designed to apply a series of LORA (low-adaptation) modifications to models and their associated clips. It enhances the capabilities of models by adding multiple LORA adjustments, allowing fine-tuning of specific features without significantly increasing the size of models or calculating loads.

# Input types
## Required
- model
    - Model parameters are essential because they represent the main object of the LoRA modification. It is the basis for the LoRA stack operation, and each layer of the stack may change its behaviour.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- clip
    - The cut parameters are essential because they complement the model by providing contextual information that can be used in conjunction with the LoRA warehouse to influence the final output.
    - Comfy dtype: CLIP
    - Python dtype: torch.Tensor
## Optional
- lora_stack
    - The lora_stack parameter is the collection of the series of LoRA configurations, which determines how models and clips are adjusted. Each element in the stack contributes to the overall transformation.
    - Comfy dtype: LORA_STACK
    - Python dtype: List[Tuple[str, float, float]]

# Output types
- MODEL
    - The output model represents a modified version of the application of the LoRA post-store input model. It contains enhancements made through the LORA adjustment.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- CLIP
    - The output clip is a modified version of the input clip, which has been adjusted with the model to reflect the impact of the LoRA stack.
    - Comfy dtype: CLIP
    - Python dtype: torch.Tensor
- show_help
    - Show_help output provides a URL link to a document to further assist and understand the LoRA stacking process.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: GPU

# Source code
```
class CR_ApplyLoRAStack:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'model': ('MODEL',), 'clip': ('CLIP',), 'lora_stack': ('LORA_STACK',)}}
    RETURN_TYPES = ('MODEL', 'CLIP', 'STRING')
    RETURN_NAMES = ('MODEL', 'CLIP', 'show_help')
    FUNCTION = 'apply_lora_stack'
    CATEGORY = icons.get('Comfyroll/LoRA')

    def apply_lora_stack(self, model, clip, lora_stack=None):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/LoRA-Nodes#cr-apply-lora-stack'
        lora_params = list()
        if lora_stack:
            lora_params.extend(lora_stack)
        else:
            return (model, clip, show_help)
        model_lora = model
        clip_lora = clip
        for tup in lora_params:
            (lora_name, strength_model, strength_clip) = tup
            lora_path = folder_paths.get_full_path('loras', lora_name)
            lora = comfy.utils.load_torch_file(lora_path, safe_load=True)
            (model_lora, clip_lora) = comfy.sd.load_lora_for_models(model_lora, clip_lora, lora, strength_model, strength_clip)
        return (model_lora, clip_lora, show_help)
```