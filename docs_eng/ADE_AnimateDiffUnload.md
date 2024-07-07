# AnimateDiff Unload 🎭🅐🅓
## Documentation
- Class name: ADE_AnimateDiffUnload
- Category: Animate Diff 🎭🅐🅓/extras
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved.git

This node is intended to unmount or release resources related to the AnimatéDiff model from the memory, ensure effective resource management and release memory for subsequent tasks.

## Input types
### Required
- model
    - Specifies the AnimateDiff model to be unloaded and allows the release of its resources.
    - Comfy dtype: MODEL
    - Python dtype: AnimateDiffModel

## Output types
- model
    - Comfy dtype: MODEL
    - Confirms that the designated AnimateDiff model has been successfully offloaded to ensure that its resources are released.
    - Python dtype: NoneType

## Usage tips
- Infra type: CPU
- Common nodes: unknown

## Source code
```python
class AnimateDiffUnload:
    def __init__(self) -> None:
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"model": ("MODEL",)}}

    RETURN_TYPES = ("MODEL",)
    CATEGORY = "Animate Diff 🎭🅐🅓/extras"
    FUNCTION = "unload_motion_modules"

    def unload_motion_modules(self, model: ModelPatcher):
        # return model clone with ejected params
        #model = eject_params_from_model(model)
        model = get_vanilla_model_patcher(model)
        return (model.clone(),)