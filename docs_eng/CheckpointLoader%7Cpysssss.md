# Checkpoint Loader 🐍
## Documentation
- Class name: CheckpointLoader|pysssss
- Category: loaders
- Output node: False
- Repo Ref: https://github.com/pythongosssss/ComfyUI-Custom-Scripts

This node is a special version of the CheckpointLoader Simple, which enhances the processing capacity of images and the processing of checkpoint names. It helps load model check points, focusing on image-related configurations that apply to scenarios where visual content is the main focus.

## Input types
### Required
- ckpt_name
    - Specifies the name of the check point that you want to load. This parameter is essential because it determines which particular check point you will try to load, thus influencing the configuration of the model and its subsequent performance.
    - Comfy dtype: COMBO[STRING]
    - Python dtype: str

## Output types
- model
    - Comfy dtype: MODEL
    - Loaded model objects, the main output of the loading process at the check point. It represents the whole of the model and is prepared for further use or analysis.
    - Python dtype: torch.nn.Module
- clip
    - Comfy dtype: CLIP
    - The CLIP model associated with the loaded check point (if applicable). This is relevant for tasks involving text and image interpretation or generation.
    - Python dtype: torch.nn.Module
- vae
    - Comfy dtype: VAE
    - The VAE (distributive encoder) component is loaded from the check point. This is essential for tasks involving image generation or operation.
    - Python dtype: torch.nn.Module

## Usage tips
- Infra type: CPU
<!-- - Common nodes:
    - [LoraLoader|pysssss](../../ComfyUI-Custom-Scripts/Nodes/LoraLoader|pysssss.md)
    - [VAEDecode](../../Comfy/Nodes/VAEDecode.md)
    - [VAEEncodeForInpaint](../../Comfy/Nodes/VAEEncodeForInpaint.md)
    - [CLIPTextEncode](../../Comfy/Nodes/CLIPTextEncode.md)
    - [VAEEncode](../../Comfy/Nodes/VAEEncode.md)
    - [Anything Everywhere3](../../cg-use-everywhere/Nodes/Anything Everywhere3.md)
    - [ImpactWildcardEncode](../../ComfyUI-Impact-Pack/Nodes/ImpactWildcardEncode.md)
    - [Anything Everywhere](../../cg-use-everywhere/Nodes/Anything Everywhere.md)
    - Reroute
    - Junction -->

## Source code
```python
class CheckpointLoaderSimpleWithImages(CheckpointLoaderSimple):
    @classmethod
    def INPUT_TYPES(s):
        types = super().INPUT_TYPES()
        names = types["required"]["ckpt_name"][0]
        populate_items(names, "checkpoints")
        return types

    def load_checkpoint(self, **kwargs):
        kwargs["ckpt_name"] = kwargs["ckpt_name"]["content"]
        return super().load_checkpoint(**kwargs)