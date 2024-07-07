# LoRA Hook Keyframe 🎭🅐🅓
## Documentation
- Class name: ADE_LoraHookKeyframe
- Category: Animate Diff 🎭🅐🅓/conditioning/schedule lora hooks
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved.git

This node is used to create the LoRA linkage key frame, which is the mechanism for adjusting the impact of the LoRA (low-altitude adaptation) linkage at a given point in the animation sequence. It allows dynamic dispatching of the intensity of the LoRA connection, thereby precisely controlling its effects during the animation process.

## Input types
### Required
- strength_model
    - Specify the strength of the LoRA link at the key frame, and the effect of the link on model behaviour in the animation.
    - Comfy dtype: FLOAT
    - Python dtype: float
- start_percent
    - The determination of the starting point for the key frame effect, as a percentage of the total animation length, allows for the precise control of the LoRA linkage impact.
    - Comfy dtype: FLOAT
    - Python dtype: float
- guarantee_steps
    - The minimum number of steps to be applied to ensure that the impact of LoRA linkages will be maintained at least for this duration.
    - Comfy dtype: INT
    - Python dtype: int

### Optional
- prev_hook_kf
    - The first selected LoRA to link the key frame group will be added to the new key frame, allowing chains to connect multiple key frames to achieve complex animation effects.
    - Comfy dtype: LORA_HOOK_KEYFRAMES
    - Python dtype: LoraHookKeyframeGroup

## Output types
- HOOK_KF
    - Comfy dtype: LORA_HOOK_KEYFRAMES
    - Returns a set of LoRA-linked key frames, including newly created key frames, to facilitate the management and application of multiple key frames in animations.
    - Python dtype: LoraHookKeyframeGroup

## Usage tips
- Infra type: CPU
- Common nodes: unknown

## Source code
```python
class CreateLoraHookKeyframe:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "strength_model": ("FLOAT", {"default": 1.0, "min": -20.0, "max": 20.0, "step": 0.01}),
                "start_percent": ("FLOAT", {"default": 0.0, "min": 0.0, "max": 1.0, "step": 0.001}),
                "guarantee_steps": ("INT", {"default": 1, "min": 0, "max": BIGMAX}),
            },
            "optional": {
                "prev_hook_kf": ("LORA_HOOK_KEYFRAMES",),
            }
        }
    
    RETURN_TYPES = ("LORA_HOOK_KEYFRAMES",)
    RETURN_NAMES = ("HOOK_KF",)
    CATEGORY = "Animate Diff 🎭🅐🅓/conditioning/schedule lora hooks"
    FUNCTION = "create_hook_keyframe"

    def create_hook_keyframe(self, strength_model: float, start_percent: float, guarantee_steps: float,
                             prev_hook_kf: LoraHookKeyframeGroup=None):
        if prev_hook_kf:
            prev_hook_kf = prev_hook_kf.clone()
        else:
            prev_hook_kf = LoraHookKeyframeGroup()
        keyframe = LoraHookKeyframe(strength=strength_model, start_percent=start_percent, guarantee_steps=guarantee_steps)
        prev_hook_kf.add(keyframe)
        return (prev_hook_kf,)