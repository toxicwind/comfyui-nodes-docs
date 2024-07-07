# 🚫AnimateDiff Loader (Advanced) [DEPRECATED] 🎭🅐🅓
## Documentation
- Class name: ADE_AnimateDiffLoaderV1Advanced
- Category: 
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The node is designed to load the AnimatéDiff model at an advanced level, especially for disposal and legacy configurations. It supports the integration and use of the old AnimatéDiff model in the current workflow in the abstract, ensuring compatibility and access to historical model functions.

# Input types
## Required
- model
    - Specifies the AnimateDiff model to be loaded, focusing on the disposal model for specific legacy applications.
    - Comfy dtype: MODEL
    - Python dtype: str
- latents
    - Defines the potential configuration to be applied during the loading of the AnimatéDiff model and allows the behaviour of the self-defined model.
    - Comfy dtype: LATENT
    - Python dtype: str
- model_name
    - The name of the particular AnimatéDiff model to be loaded is determined to allow an accurate selection of the legacy model.
    - Comfy dtype: COMBO[STRING]
    - Python dtype: str
- unlimited_area_hack
    - A Boolean logo to enable or disable unlimited area hackers and to provide solutions for specific loading scenarios.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- context_length
    - Specifies the context length to be used during the model load, and affects the manner in which the model is processed for input.
    - Comfy dtype: INT
    - Python dtype: int
- context_stride
    - Sets the scale of the context, influences the load and processing efficiency of the model.
    - Comfy dtype: INT
    - Python dtype: int
- context_overlap
    - Defines the overlap between the following segments during the time the model is loaded and optimizes the model's understanding of the sequence data.
    - Comfy dtype: INT
    - Python dtype: int
- context_schedule
    - Select the plan to be applied in context, allowing flexibility to accommodate a variety of loading requirements.
    - Comfy dtype: COMBO[STRING]
    - Python dtype: str
- closed_loop
    - A boolean parameter that indicates whether the model load should be operated in a closed ring and influences the initialization process of the model.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- beta_schedule
    - Select the Beta plan to be used during the loading of the model to influence the adaptation and performance of the model.
    - Comfy dtype: COMBO[STRING]
    - Python dtype: str

# Output types
- model
    - Output the loaded AnimateDiff model for further processing or application.
    - Comfy dtype: MODEL
    - Python dtype: str
- latent
    - Provide potential configurations to be applied during model loading, reflecting customization of model behaviour.
    - Comfy dtype: LATENT
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```python
class AnimateDiffLoaderAdvanced_Deprecated:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "model": ("MODEL",),
                "latents": ("LATENT",),
                "model_name": (get_available_motion_models(),),
                "unlimited_area_hack": ("BOOLEAN", {"default": False},),
                "context_length": ("INT", {"default": 16, "min": 0, "max": 1000}),
                "context_stride": ("INT", {"default": 1, "min": 1, "max": 1000}),
                "context_overlap": ("INT", {"default": 4, "min": 0, "max": 1000}),
                "context_schedule": (ContextSchedules.LEGACY_UNIFORM_SCHEDULE_LIST,),
                "closed_loop": ("BOOLEAN", {"default": False},),
                "beta_schedule": (BetaSchedules.get_alias_list_with_first_element(BetaSchedules.SQRT_LINEAR),),
            },
        }

    RETURN_TYPES = ("MODEL", "LATENT")
    CATEGORY = ""
    FUNCTION = "load_mm_and_inject_params"

    def load_mm_and_inject_params(self,
            model: ModelPatcher,
            latents: Dict[str, torch.Tensor],
            model_name: str, unlimited_area_hack: bool,
            context_length: int, context_stride: int, context_overlap: int, context_schedule: str, closed_loop: bool,
            beta_schedule: str,
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
        context_group = ContextOptionsGroup()
        context_group.add(
            ContextOptions(
                context_length=context_length,
                context_stride=context_stride,
                context_overlap=context_overlap,
                context_schedule=context_schedule,
                closed_loop=closed_loop,
                )
            )
        # set context settings
        params.set_context(context_options=context_group)
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

