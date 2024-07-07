# Load Checkpoint w/ Noise Select 🎭🅐🅓
## Documentation
- Class name: CheckpointLoaderSimpleWithNoiseSelect
- Category: Animate Diff 🎭🅐🅓/extras
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved.git

This node is dedicated to loading model check points, with a focus on noise selection, allowing for more detailed control of the initialization and behaviour of the model in generating tasks. It expands the standard check point load function to meet advanced custom needs by combining Beta's planned adjusted and optional noise zoom factors.

## Input types
### Required
- ckpt_name
    - Specifies the name of the check point that you want to load. This parameter is essential for identifying a specific model check point file from the predefined list of available check points.
    - Comfy dtype: COMBO[STRING]
    - Python dtype: str
- beta_schedule
    - This parameter allows you to adjust the sampling behaviour of the model and enhances the flexibility of model performance.
    - Comfy dtype: COMBO[STRING]
    - Python dtype: str

### Optional
- use_custom_scale_factor
    - A boolean sign indicates whether to apply a custom noise zoom factor. When set to True, it can fine-tune the impact of noise on model output.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- scale_factor
    - Defines the size of the noise zoom factor if 'use_custom_scape_factor' is true. It allows accurate control of the noise level applied to the model.
    - Comfy dtype: FLOAT
    - Python dtype: float

## Output types
- model
    - Comfy dtype: MODEL
    - Loaded models are configured according to the specified Beta plan and noise scaling options.
    - Python dtype: torch.nn.Module
- clip
    - Comfy dtype: CLIP
    - If applicable, load the relevant CLIP model at the checkpoint.
    - Python dtype: torch.nn.Module
- vae
    - Comfy dtype: VAE
    - If applicable, load the VAE models associated with the checkpoint.
    - Python dtype: torch.nn.Module

## Usage tips
- Infra type: GPU
<!-- - Common nodes:
    - [LoraLoader](../../Comfy/Nodes/LoraLoader.md)
    - [CLIPTextEncode](../../Comfy/Nodes/CLIPTextEncode.md)
    - [ADE_AnimateDiffLoaderWithContext](../../ComfyUI-AnimateDiff-Evolved/Nodes/ADE_AnimateDiffLoaderWithContext.md)
    - [BatchPromptSchedule](../../ComfyUI_FizzNodes/Nodes/BatchPromptSchedule.md)
    - [CLIPSetLastLayer](../../Comfy/Nodes/CLIPSetLastLayer.md)
    - [Lora Loader Stack (rgthree)](../../rgthree-comfy/Nodes/Lora Loader Stack (rgthree).md)
    - IPAdapterApply
    - [ToBasicPipe](../../ComfyUI-Impact-Pack/Nodes/ToBasicPipe.md) -->

## Source code
```python
class CheckpointLoaderSimpleWithNoiseSelect:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "ckpt_name": (folder_paths.get_filename_list("checkpoints"), ),
                "beta_schedule": (BetaSchedules.ALIAS_LIST, {"default": BetaSchedules.USE_EXISTING}, )
            },
            "optional": {
                "use_custom_scale_factor": ("BOOLEAN", {"default": False}),
                "scale_factor": ("FLOAT", {"default": 0.18215, "min": 0.0, "max": 1.0, "step": 0.00001})
            }
        }
    RETURN_TYPES = ("MODEL", "CLIP", "VAE")
    FUNCTION = "load_checkpoint"

    CATEGORY = "Animate Diff 🎭🅐🅓/extras"

    def load_checkpoint(self, ckpt_name, beta_schedule, output_vae=True, output_clip=True, use_custom_scale_factor=False, scale_factor=0.18215):
        ckpt_path = folder_paths.get_full_path("checkpoints", ckpt_name)
        out = load_checkpoint_guess_config(ckpt_path, output_vae=True, output_clip=True, embedding_directory=folder_paths.get_folder_paths("embeddings"))
        # register chosen beta schedule on model - convert to beta_schedule name recognized by ComfyUI
        new_model_sampling = BetaSchedules.to_model_sampling(beta_schedule, out[0])
        if new_model_sampling is not None:
            out[0].model.model_sampling = new_model_sampling
        if use_custom_scale_factor:
            out[0].model.latent_format.scale_factor = scale_factor
        return out