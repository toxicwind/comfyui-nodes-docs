# Empty Latent Image (Big Batch) 🎭🅐🅓
## Documentation
- Class name: ADE_EmptyLatentImageLarge
- Category: Animate Diff 🎭🅐🅓/extras
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved.git

ADE_EmptyLentImageLarge is designed to initialize a large potential image load filled with zero. This volume is used as a blank canvas for the further generation process, allowing the creation and operation of images at a potential level.

## Input types
### Required
- width
    - Specifies the width of the potential image that you want to generate. It determines the horizontal dimension of the mass generated.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - Determines the height of the potential image. It affects the vertical dimensions of the volume generated.
    - Comfy dtype: INT
    - Python dtype: int
- batch_size
    - Controls the number of potential images generated at a single time. It affects the first dimension of the volume generated and allows batch processing of multiple images.
    - Comfy dtype: INT
    - Python dtype: int

## Output types
- latent
    - Comfy dtype: LATENT
    - Output is the volume of a potential blank image. Each image is initialized at zero and is prepared for subsequent generation modification.
    - Python dtype: torch.Tensor

## Usage tips
- Infra type: GPU
<!-- - Common nodes:
    - [BatchPromptScheduleLatentInput](../../ComfyUI_FizzNodes/Nodes/BatchPromptScheduleLatentInput.md)
    - [KSampler](../../Comfy/Nodes/KSampler.md) -->

## Source code
```python
class EmptyLatentImageLarge:
    def __init__(self, device="cpu"):
        self.device = device

    @classmethod
    def INPUT_TYPES(s):
        return {"required": { "width": ("INT", {"default": 512, "min": 64, "max": comfy_nodes.MAX_RESOLUTION, "step": 8}),
                              "height": ("INT", {"default": 512, "min": 64, "max": comfy_nodes.MAX_RESOLUTION, "step": 8}),
                              "batch_size": ("INT", {"default": 1, "min": 1, "max": 262144})}}
    RETURN_TYPES = ("LATENT",)
    FUNCTION = "generate"

    CATEGORY = "Animate Diff 🎭🅐🅓/extras"

    def generate(self, width, height, batch_size=1):
        latent = torch.zeros([batch_size, 4, height // 8, width // 8])
        return ({"samples":latent}, )