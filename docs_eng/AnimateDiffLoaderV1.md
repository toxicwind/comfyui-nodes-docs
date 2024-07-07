# 🚫AnimateDiff Loader [DEPRECATED] 🎭🅐🅓
## Documentation
- Class name: AnimateDiffLoaderV1
- Category: 
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved.git

This node is used to initialize and prepare the AnimatateDiff model for animation tasks. It abstractes the complexity of the loaded model and ensures its correct set-up for subsequent use.

## Input types
### Required
- model
    - This parameter is used to specify the AnimatéDiff model to be loaded to enable nodes to properly initialize and prepare models for animation tasks.
    - Comfy dtype: MODEL
    - Python dtype: str
- latents
    - This parameter allows the identification of potential vectors that the initialization model may require, and provides a method to define the initial state of the self-defined model.
    - Comfy dtype: LATENT
    - Python dtype: str
- model_name
    - To select a specific motion model from the available options, the parameter ensures that the correct version of the AnimateDiff model is loaded according to the name provided.
    - Comfy dtype: COMBO[STRING]
    - Python dtype: str
- unlimited_area_hack
    - A boolean parameter, which applies specific hacking techniques to bypass the limits of animated areas at the time of commissioning, provides more flexibility for animated tasks.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- beta_schedule
    - Specifies the Beta plan to be used during the operation of the model to influence the behaviour and performance of the AnimateDiff model.
    - Comfy dtype: COMBO[STRING]
    - Python dtype: str

## Output types
- model
    - Comfy dtype: MODEL
    - Indicates the AnimatéDiff model that has been loaded and is prepared to perform animating tasks.
    - Python dtype: str
- latent
    - Comfy dtype: LATENT
    - The output of potential vectors associated with the loaded model can be used for further self-defined or animated processes.
    - Python dtype: str

## Usage tips
- Infra type: CPU
- Common nodes: unknown

## Source code
```python
class AnimateDiffLoader_Deprecated:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "model": ("MODEL",),
                "latents": ("LATENT",),
                "model_name": (get_available_motion_models(),),
                "unlimited_area_hack": ("BOOLEAN", {"default": False},),
                "beta_schedule": (BetaSchedules.get_alias_list_with_first_element(BetaSchedules.SQRT_LINEAR),),
            },
        }

    RETURN_TYPES = ("MODEL", "LATENT")
    CATEGORY = ""
    FUNCTION = "load_mm_and_inject_params"

    def load_mm_and_inject_params(
        self,
        model: ModelPatcher,
        latents: Dict[str, torch.Tensor],
        model_name: str, unlimited_area_hack: bool, beta_schedule: str,
    ):
        # load motion module
        motion_model = load_motion_module_gen1(model_name, model)
        # get total frames
        init_frames_len = len(latents["samples"])  # deprecated - no longer used for anything lol
        # set injection params
        params = InjectionParams(
                unlimited_area_hack=unlimited_area_hack,
                apply_mm_groupnorm_hack=True,
                model_name=model_name,
                apply_v2_properly=False,
        )
        # inject for use in sampling code
        model = ModelPatcherAndInjector.create_from(model, hooks_only=True)
        model.motion_models = MotionModelGroup(motion_model)
        model.motion_injection_params = params

        # save model sampling from BetaSchedule as object patch
        # if autoselect, get suggested beta_schedule from motion model
        if beta_schedule == BetaSchedules.AUTOSELECT and not model.motion_models.is_empty():
            beta_schedule = model.motion_models[0].model.get_best_beta_schedule(log=True)
        new_model_sampling = BetaSchedules.to_model_sampling(beta_schedule, model)
        if new_model_sampling is not None:
            model.add_object_patch("model_sampling", new_model_sampling)

        del motion_model
        return (model, latents)