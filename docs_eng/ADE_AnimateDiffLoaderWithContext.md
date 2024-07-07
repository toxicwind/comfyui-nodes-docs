---

tags:
- AnimateDiff
- AnimateDiffContext
- Animation

---

# AnimateDiff Loader [Legacy] 🎭🅐🅓①
## Documentation
- Class name: ADE_AnimateDiffLoaderWithContext
- Category: Animate Diff 🎭🅐🅓/① Gen1 nodes ①
- Output node: False

This node is intended to add the AnimatéDiff model and its specific context to help integrate additional information or settings that influence the animation process. It provides a bridge between the traditional AnimatéDiff model and the updated context perception function, ensuring compatibility and enhancing control over animation generation.

## Input types
### Required
- model
    - Specifies the AnimatéDiff model to be loaded as the core component of the animation process.
    - Comfy dtype: MODEL
    - Python dtype: str
- model_name
    - Identify specific AnimateDiff models by name, allowing accurate selection among available options.
    - Comfy dtype: COMBO[STRING]
    - Python dtype: str
- beta_schedule
    - Adjusting the animated beta schedule to influence the diffusion process.
    - Comfy dtype: COMBO[STRING]
    - Python dtype: str

### Optional
- context_options
    - Provides context-specific options to modify the AnimatateDiff model processing animation to allow custom animating behaviour.
    - Comfy dtype: CONTEXT_OPTIONS
    - Python dtype: str
- motion_lora
    - Specifies the LoRA parameters of the motion and enhances the ability of the model to generate dynamic animations.
    - Comfy dtype: MOTION_LORA
    - Python dtype: str
- ad_settings
    - Defines the AnimatéDiff settings, adjusts the animation process to meet specific requirements.
    - Comfy dtype: AD_SETTINGS
    - Python dtype: str
- sample_settings
    - Determines the sampling settings for animations and influences the quality and characteristics of the creation of animations.
    - Comfy dtype: SAMPLE_SETTINGS
    - Python dtype: str
- motion_scale
    - Controls the size of the motion in the animation and allows for more fine-tuning of the intensity of the motion.
    - Comfy dtype: FLOAT
    - Python dtype: str
- apply_v2_models_properly
    - Ensure the correct application of version 2 models to optimize compatibility and performance.
    - Comfy dtype: BOOLEAN
    - Python dtype: str
- ad_keyframes
    - Specifies the key frame for the animation and directs the AnimatéDiff model to produce the target animation sequence.
    - Comfy dtype: AD_KEYFRAMES
    - Python dtype: str

## Output types
- model
    - Comfy dtype: MODEL
    - Loaded AnimatéDiff models ready to generate animations with specified context and settings.
    - Python dtype: str

## Usage tips
- Infra type: CPU
<!-- - Common nodes:
    - [KSampler](./KSampler.md)
    - [FreeU_V2](./FreeU_V2.md)
    - [KSamplerAdvanced](../../Comfy/Nodes/KSamplerAdvanced.md)
    - [LoraLoaderModelOnly](../../Comfy/Nodes/LoraLoaderModelOnly.md)
    - [LoraLoader](../../Comfy/Nodes/LoraLoader.md)
    - [ToBasicPipe](../../ComfyUI-Impact-Pack/Nodes/ToBasicPipe.md)
    - IPAdapterApply
    - DynamicThresholdingSimple
    - Reroute -->

## Source code
```python
class LegacyAnimateDiffLoaderWithContext:
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
                "sample_settings": ("SAMPLE_SETTINGS",),
                "motion_scale": ("FLOAT", {"default": 1.0, "min": 0.0, "step": 0.001}),
                "apply_v2_models_properly": ("BOOLEAN", {"default": True}),
                "ad_keyframes": ("AD_KEYFRAMES",),
            }
        }
    
    RETURN_TYPES = ("MODEL",)
    CATEGORY = "Animate Diff 🎭🅐🅓/① Gen1 nodes ①"
    FUNCTION = "load_mm_and_inject_params"


    def load_mm_and_inject_params(self,
        model: ModelPatcher,
        model_name: str, beta_schedule: str,# apply_mm_groupnorm_hack: bool,
        context_options: ContextOptionsGroup=None, motion_lora: MotionLoraList=None, ad_settings: AnimateDiffSettings=None, motion_model_settings: AnimateDiffSettings=None,
        sample_settings: SampleSettings=None, motion_scale: float=1.0, apply_v2_models_properly: bool=False, ad_keyframes: ADKeyframeGroup=None,
    ):
        if ad_settings is not None:
            motion_model_settings = ad_settings
        # load motion module
        motion_model = load_motion_module_gen1(model_name, model, motion_lora=motion_lora, motion_model_settings=motion_model_settings)
        # set injection params
        params = InjectionParams(
                unlimited_area_hack=False,
                model_name=model_name,
                apply_v2_properly=apply_v2_models_properly,
        )
        if context_options:
            params.set_context(context_options)
        # set motion_scale and motion_model_settings
        if not motion_model_settings:
            motion_model_settings = AnimateDiffSettings()
        motion_model_settings.attn_scale = motion_scale
        params.set_motion_model_settings(motion_model_settings)

        if params.motion_model_settings.mask_attn_scale is not None:
            motion_model.scale_multival = params.motion_model_settings.mask_attn_scale * params.motion_model_settings.attn_scale
        else:
            motion_model.scale_multival = params.motion_model_settings.attn_scale

        motion_model.keyframes = ad_keyframes.clone() if ad_keyframes else ADKeyframeGroup()

        model = ModelPatcherAndInjector.create_from(model, hooks_only=True)
        model.motion_models = MotionModelGroup(motion_model)
        model.sample_settings = sample_settings if sample_settings is not None else SampleSettings()
        model.motion_injection_params = params

        # save model sampling from BetaSchedule as object patch
        # if autoselect, get suggested beta_schedule from motion model
        if beta_schedule == BetaSchedules.AUTOSELECT and not model.motion_models.is_empty():
            beta_schedule = model.motion_models[0].model.get_best_beta_schedule(log=True)
        new_model_sampling = BetaSchedules.to_model_sampling(beta_schedule, model)
        if new_model_sampling is not None:
            model.add_object_patch("model_sampling", new_model_sampling)

        del motion_model
        return (model,)