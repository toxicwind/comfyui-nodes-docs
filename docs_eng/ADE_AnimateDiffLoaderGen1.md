# AnimateDiff Loader 🎭🅐🅓①
## Documentation
- Class name: `ADE_AnimateDiffLoaderGen1`
- Category: `Animate Diff 🎭🅐🅓/① Gen1 nodes ①`
- Output node: `False`
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved.git


ADE_AnimatéDiffLoaderGen1 is designed to load and initialize the first generation AnimatéDiff model, laying the foundation for subsequent animation or image-processing tasks. It encapsulates the complexity of the model loading and configuration and provides a simplified interface for generating dynamic content.
## Input types
### Required
- **`model`**
    - This input specifies the AnimatéDiff model that you want to load, which is the core of the initial animation or image processing process.
    - Comfy dtype: `MODEL`
    - Python dtype: `str`
- **`model_name`**
    - The model_name parameter allows the selection of a specific AnimatéDiff model by name, thus achieving a more targeted initialization.
    - Comfy dtype: `COMBO[STRING]`
    - Python dtype: `str`
- **`beta_schedule`**
    - Beta_schedule parameters determine the beta-value schedule during proliferation, affecting the quality and properties of the content generated.
    - Comfy dtype: `COMBO[STRING]`
    - Python dtype: `str`
### Optional
- **`context_options`**
    - Provides additional context or preference settings for model loading, allowing custom initialization.
    - Comfy dtype: `CONTEXT_OPTIONS`
    - Python dtype: `str`
- **`motion_lora`**
    - Specifies the LoRA parameters of the motion model, allowing fine-tuning of animation dynamics.
    - Comfy dtype: `MOTION_LORA`
    - Python dtype: `str`
- **`ad_settings`**
    - Customizes the animation and diffusion settings of the AnimateDiff model's behaviour during loading.
    - Comfy dtype: `AD_SETTINGS`
    - Python dtype: `str`
- **`ad_keyframes`**
    - Defines the key frame of the animation and guides the model to generate dynamic content within the specified time interval.
    - Comfy dtype: `AD_KEYFRAMES`
    - Python dtype: `str`
- **`sample_settings`**
    - To influence the settings of the sampling process, such as temperature and top-k filters, in order to optimize the generation of output.
    - Comfy dtype: `SAMPLE_SETTINGS`
    - Python dtype: `str`
- **`scale_multival`**
    - Multipliers that are used to scale the strength of a particular effect in the content.
    - Comfy dtype: `MULTIVAL`
    - Python dtype: `str`
- **`effect_multival`**
    - The multipliers used to adjust the specific effect strength in the content generated provide creative control of the output.
    - Comfy dtype: `MULTIVAL`
    - Python dtype: `str`
## Output types
- **`model`**
    - Comfy dtype: `MODEL`
    - This is the loaded AnimatéDiff model for animation or image-processing tasks.
    - Python dtype: `str`
## Usage tips
- Infra type: `CPU`
<!-- - Common nodes:
    - [KSampler](../../Comfy/Nodes/KSampler.md) -->

## Source code
```python
class AnimateDiffLoaderGen1:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "model": ("MODEL",),
                "model_name": (get_available_motion_models(),),
                "beta_schedule": (BetaSchedules.ALIAS_LIST, {"default": BetaSchedules.AUTOSELECT}),
                #"apply_mm_groupnorm_hack": ("BOOLEAN", {"default": True}),
            },
            "optional": {
                "context_options": ("CONTEXT_OPTIONS",),
                "motion_lora": ("MOTION_LORA",),
                "ad_settings": ("AD_SETTINGS",),
                "ad_keyframes": ("AD_KEYFRAMES",),
                "sample_settings": ("SAMPLE_SETTINGS",),
                "scale_multival": ("MULTIVAL",),
                "effect_multival": ("MULTIVAL",),
            }
        }

    RETURN_TYPES = ("MODEL",)
    CATEGORY = "Animate Diff 🎭🅐🅓/① Gen1 nodes ①"
    FUNCTION = "load_mm_and_inject_params"

    def load_mm_and_inject_params(self,
        model: ModelPatcher,
        model_name: str, beta_schedule: str,# apply_mm_groupnorm_hack: bool,
        context_options: ContextOptionsGroup=None, motion_lora: MotionLoraList=None, ad_settings: AnimateDiffSettings=None,
        sample_settings: SampleSettings=None, scale_multival=None, effect_multival=None, ad_keyframes: ADKeyframeGroup=None,
    ):
        # load motion module and motion settings, if included
        motion_model = load_motion_module_gen2(model_name=model_name, motion_model_settings=ad_settings)
        # confirm that it is compatible with SD model
        validate_model_compatibility_gen2(model=model, motion_model=motion_model)
        # apply motion model to loaded_mm
        if motion_lora is not None:
            for lora in motion_lora.loras:
                load_motion_lora_as_patches(motion_model, lora)
        motion_model.scale_multival = scale_multival
        motion_model.effect_multival = effect_multival
        motion_model.keyframes = ad_keyframes.clone() if ad_keyframes else ADKeyframeGroup()

        # create injection params
        params = InjectionParams(unlimited_area_hack=False, model_name=motion_model.model.mm_info.mm_name)
        # apply context options
        if context_options:
            params.set_context(context_options)

        # set motion_scale and motion_model_settings
        if not ad_settings:
            ad_settings = AnimateDiffSettings()
        ad_settings.attn_scale = 1.0
        params.set_motion_model_settings(ad_settings)

        # backwards compatibility to support old way of masking scale
        if params.motion_model_settings.mask_attn_scale is not None:
            motion_model.scale_multival = get_combined_multival(scale_multival, (params.motion_model_settings.mask_attn_scale * params.motion_model_settings.attn_scale))

        # need to use a ModelPatcher that supports injection of motion modules into unet
        model = ModelPatcherAndInjector.create_from(model, hooks_only=True)
        model.motion_models = MotionModelGroup(motion_model)
        model.sample_settings = sample_settings if sample_settings is not None else SampleSettings()
        model.motion_injection_params = params

        if model.sample_settings.custom_cfg is not None:
            logger.info("[Sample Settings] custom_cfg is set; will override any KSampler cfg values or patches.")

        if model.sample_settings.sigma_schedule is not None:
            logger.info("[Sample Settings] sigma_schedule is set; will override beta_schedule.")
            model.add_object_patch("model_sampling", model.sample_settings.sigma_schedule.clone().model_sampling)
        else:
            # save model sampling from BetaSchedule as object patch
            # if autoselect, get suggested beta_schedule from motion model
            if beta_schedule == BetaSchedules.AUTOSELECT and not model.motion_models.is_empty():
                beta_schedule = model.motion_models[0].model.get_best_beta_schedule(log=True)
            new_model_sampling = BetaSchedules.to_model_sampling(beta_schedule, model)
            if new_model_sampling is not None:
                model.add_object_patch("model_sampling", new_model_sampling)

        del motion_model
        return (model,)

