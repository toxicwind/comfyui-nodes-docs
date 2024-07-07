# Lora Loader 🐍
## Documentation
- Class name: LoraLoader|pysssss
- Category: loaders
- Output node: False
- Repo Ref: https://github.com/pythongosssss/ComfyUI-Custom-Scripts

This node is dedicated to loading and applying LoRA (low adaptation) to models and CLIP, enhancing its functionality or changing its behaviour according to the specified LoRA configuration. It expands the basic loader function and also processes image-specific LoRA configurations to make them multifunctional in multimedia applications.

## Input types
### Required
- model
    - The model adjusted by LoRA will be applied. It is essential to define the base structure that will be enhanced or modified by LoRA.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- clip
    - The CLAIP model, adjusted by LoRA, will be applied to allow for enhanced or changed multi-model understandings and expressions.
    - Comfy dtype: CLIP
    - Python dtype: torch.nn.Module
- lora_name
    - Specifies the name of the LoRA configuration to be applied and determines the specific adjustments and enhancements of the model and CLIP.
    - Comfy dtype: COMBO[STRING]
    - Python dtype: str
- strength_model
    - Defines the intensity of the LoRA adjustment applied to the model and allows fine-tuning of the changes.
    - Comfy dtype: FLOAT
    - Python dtype: float
- strength_clip
    - The strength of the LoRA adjustment applied to the CLIP model can be defined with precise control of the enhancement.
    - Comfy dtype: FLOAT
    - Python dtype: float

## Output types
- model
    - Comfy dtype: MODEL
    - Apply the LoRA adjusted model to reflect enhanced or changed functionality.
    - Python dtype: torch.nn.Module
- clip
    - Comfy dtype: CLIP
    - Use the LoRA-adjusted CLIP model to demonstrate enhanced or changed multi-model understandings and expressions.
    - Python dtype: torch.nn.Module

## Usage tips
- Infra type: GPU
<!-- - Common nodes:
    - [LoraLoader|pysssss](../../ComfyUI-Custom-Scripts/Nodes/LoraLoader|pysssss.md)
    - [ModelSamplingDiscrete](../../Comfy/Nodes/ModelSamplingDiscrete.md)
    - Reroute
    - [CLIPTextEncode](../../Comfy/Nodes/CLIPTextEncode.md)
    - IPAdapterApply
    - [Anything Everywhere](../../cg-use-everywhere/Nodes/Anything Everywhere.md) -->

## Source code
```python
class LoraLoaderWithImages(LoraLoader):
    @classmethod
    def INPUT_TYPES(s):
        types = super().INPUT_TYPES()
        names = types["required"]["lora_name"][0]
        populate_items(names, "loras")
        return types

    def load_lora(self, **kwargs):
        kwargs["lora_name"] = kwargs["lora_name"]["content"]
        return super().load_lora(**kwargs)