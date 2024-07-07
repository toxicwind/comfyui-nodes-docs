# LoRA Hook Keyframes Interpolation 🎭🅐🅓
## Documentation
- Class name: ADE_LoraHookKeyframeInterpolation
- Category: Animate Diff 🎭🅐🅓/conditioning/schedule lora hooks
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved.git

This node is used to create the login key frame for the plug value, thereby dynamically adjusting model behaviour over time. It generates a series of key frames based on the specified starting and ending percentage, strength and plug-in method, thus achieving fine particle size control of model parameters.

## Input types
### Required
- start_percent
    - Defines the starting percentage of the plug value and sets the starting point for generating the key frame sequence.
    - Comfy dtype: FLOAT
    - Python dtype: float
- end_percent
    - Specifies the end percentage of the plug value and determines the end point for the generation of the key frame sequence.
    - Comfy dtype: FLOAT
    - Python dtype: float
- strength_start
    - Sets the initial strength value of the plug value, and marks the start of the strength adjustment range.
    - Comfy dtype: FLOAT
    - Python dtype: float
- strength_end
    - Determines the end strength value of the plug value and adjusts the range of end strength.
    - Comfy dtype: FLOAT
    - Python dtype: float
- interpolation
    - Select the plug-in method used to generate the key frame sequence to influence the transition between the start and end values.
    - Comfy dtype: COMBO[STRING]
    - Python dtype: InterpolationMethod
- intervals
    - Specifies the number of intervals (or key frames) between the starting and the end point that affect the particle size of the plug value.
    - Comfy dtype: INT
    - Python dtype: int
- print_keyframes
    - Optional. Controls whether to record the key frames generated help debug and visualize the plug-in process.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

### Optional
- prev_hook_kf
    - Optional. Allows a group of LoRAs, as previously defined, to be linked to the key frame, to which the new plug-in key frame will be added.
    - Comfy dtype: LORA_HOOK_KEYFRAMES
    - Python dtype: LoraHookKeyframeGroup

## Output types
- HOOK_KF
    - Comfy dtype: LORA_HOOK_KEYFRAMES
    - Returns a set of LoRA key frames, including pre-existing and new plugs, to be applied in model conditions.
    - Python dtype: LoraHookKeyframeGroup

## Usage tips
- Infra type: CPU
- Common nodes: unknown

## Source code
```python
class CreateLoraHookKeyframeInterpolation:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "start_percent": ("FLOAT", {"default": 0.0, "min": 0.0, "max": 1.0, "step": 0.001}),
                "end_percent": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 1.0, "step": 0.001}),
                "strength_start": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 10.0, "step": 0.001}, ),
                "strength_end": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 10.0, "step": 0.001}, ),
                "interpolation": (InterpolationMethod._LIST, ),
                "intervals": ("INT", {"default": 5, "min": 2, "max": 100, "step": 1}),
                "print_keyframes": ("BOOLEAN", {"default": False}),
            },
            "optional": {
                "prev_hook_kf": ("LORA_HOOK_KEYFRAMES",),
            }
        }
    
    RETURN_TYPES = ("LORA_HOOK_KEYFRAMES",)
    RETURN_NAMES = ("HOOK_KF",)
    CATEGORY = "Animate Diff 🎭🅐🅓/conditioning/schedule lora hooks"
    FUNCTION = "create_hook_keyframes"

    def create_hook_keyframes(self,
                              start_percent: float, end_percent: float,
                              strength_start: float, strength_end: float, interpolation: str, intervals: int,
                              prev_hook_kf: LoraHookKeyframeGroup=None, print_keyframes=False):
        if prev_hook_kf:
            prev_hook_kf = prev_hook_kf.clone()
        else:
            prev_hook_kf = LoraHookKeyframeGroup()
        percents = InterpolationMethod.get_weights(num_from=start_percent, num_to=end_percent, length=intervals, method=interpolation)
        strengths = InterpolationMethod.get_weights(num_from=strength_start, num_to=strength_end, length=intervals, method=interpolation)
        
        is_first = True
        for percent, strength in zip(percents, strengths):
            guarantee_steps = 0
            if is_first:
                guarantee_steps = 1
                is_first = False
            prev_hook_kf.add(LoraHookKeyframe(strength=strength, start_percent=percent, guarantee_steps=guarantee_steps))
            if print_keyframes:
                logger.info(f"LoraHookKeyframe - start_percent:{percent} = {strength}")
        return (prev_hook_kf,)