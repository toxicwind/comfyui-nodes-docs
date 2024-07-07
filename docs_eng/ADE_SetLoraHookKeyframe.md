# Set LoRA Hook Keyframes 🎭🅐🅓
## Documentation
- Class name: ADE_SetLoraHookKeyframe
- Category: Animate Diff 🎭🅐🅓/conditioning
- Output node: False
- Repo Ref: https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved.git

This node is used to assign a set of LoRA-associated frames to a specific LoRA-association group. It allows customizing and dynamically adjusting LoRA-association behaviour on animated time lines, thus controlling the response of the model precisely at different stages of the animation process.

## Input types
### Required
- lora_hook
    - Links the LoRA group to which the key frame is applied. This parameter is essential for identifying the target group that will receive the new key frame settings.
    - Comfy dtype: LORA_HOOK
    - Python dtype: LoraHookGroup
- hook_kf
    - This parameter defines the time, intensity and other characteristics of the LoRA connection on the animated time line.
    - Comfy dtype: LORA_HOOK_KEYFRAMES
    - Python dtype: LoraHookKeyframeGroup

## Output types
- lora_hook
    - Comfy dtype: LORA_HOOK
    - The updated LoRA link group has been applied to the new key set. This output reflects the changes made to the LoRA connection and contains the specified key frame settings.
    - Python dtype: LoraHookGroup

## Usage tips
- Infra type: CPU
- Common nodes: unknown

## Source code
```python
class SetLoraHookKeyframes:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "lora_hook": ("LORA_HOOK",), 
                "hook_kf": ("LORA_HOOK_KEYFRAMES",),
            }
        }
    
    RETURN_TYPES = ("LORA_HOOK",)
    CATEGORY = "Animate Diff 🎭🅐🅓/conditioning"
    FUNCTION = "set_hook_keyframes"

    def set_hook_keyframes(self, lora_hook: LoraHookGroup, hook_kf: LoraHookKeyframeGroup):
        new_lora_hook = lora_hook.clone()
        new_lora_hook.set_keyframes_on_hooks(hook_kf=hook_kf)
        return (new_lora_hook,)