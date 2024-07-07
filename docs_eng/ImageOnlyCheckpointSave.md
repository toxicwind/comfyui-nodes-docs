# Documentation
- Class name: ImageOnlyCheckpointSave
- Category: _for_testing
- Output node: True
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The ImageOnlyCheckpointSave node is designed to simplify the process of saving only the image check point. It covers the process of preserving the model status, ensuring that it can be retrieved at a later stage and used for image generation or further processing. This node is essential to maintain continuity in model operations and to preserve the model status at a given point in time.

# Input types
## Required
- model
    - Model parameters are essential for the ImageOnlyCheckpointSave node, as it represents the core component to be saved. It is the main input and determines the content of the node execution and the checkpoint to be generated.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- clip_vision
    - The clip_vision parameter is the key input to the node, providing visual components associated with the model. It is essential for the function of the check point to ensure that the visual aspects of the model are preserved as well.
    - Comfy dtype: CLIP_VISION
    - Python dtype: comfy.sd.CLIPVision
- vae
    - The vae parameter specifies the variable encoder to be included in the check point. It plays an important role in the operation of the node, as it ensures the inclusion of the VAE state in order to carry out the potential reconfiguring tasks.
    - Comfy dtype: VAE
    - Python dtype: AutoencoderKL
- filename_prefix
    - The filename_prefix parameter determines the prefix to be used to save the check point file. It is a key aspect of the node function, as it allows the check point to be organized and identified in the file system.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- prompt
    - The optional prompt parameter can be used to connect a given hint to the check point. This is useful for remembering the context or example of the model when saving.
    - Comfy dtype: PROMPT
    - Python dtype: str
- extra_pnginfo
    - Extra_pnginfo parameters allow for additional information to be included in the check point. This is useful for storing metadata or other detailed information related to model status.
    - Comfy dtype: EXTRA_PNGINFO
    - Python dtype: dict

# Output types
- checkpoint
    - The check point output represents the preservation state of the model, including all necessary components for its future use. It marks the successful completion of node operations and the state of preservation of the model at a given point in time.
    - Comfy dtype: CHECKPOINT
    - Python dtype: Dict[str, torch.Tensor]

# Usage tips
- Infra type: CPU

# Source code
```
class ImageOnlyCheckpointSave(comfy_extras.nodes_model_merging.CheckpointSave):
    CATEGORY = '_for_testing'

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'clip_vision': ('CLIP_VISION',), 'vae': ('VAE',), 'filename_prefix': ('STRING', {'default': 'checkpoints/ComfyUI'})}, 'hidden': {'prompt': 'PROMPT', 'extra_pnginfo': 'EXTRA_PNGINFO'}}

    def save(self, model, clip_vision, vae, filename_prefix, prompt=None, extra_pnginfo=None):
        comfy_extras.nodes_model_merging.save_checkpoint(model, clip_vision=clip_vision, vae=vae, filename_prefix=filename_prefix, output_dir=self.output_dir, prompt=prompt, extra_pnginfo=extra_pnginfo)
        return {}
```