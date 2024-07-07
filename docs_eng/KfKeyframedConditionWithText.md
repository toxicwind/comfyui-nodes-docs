# Documentation
- Class name: KfKeyframedConditionWithText
- Category: RootCategory
- Output node: False
- Repo Ref: https://github.com/dmarx/ComfyUI-Keyframed

This node integrates text information into a framework based on the key frame to achieve dynamic adjustments and refinements to key frame conditions based on text input.

# Input types
## Required
- clip
    - The clips entered are necessary because they serve as the basis for the key frame conditions. They are operated on the basis of text input to create a customized visual representation.
    - Comfy dtype: CLIP
    - Python dtype: kf.Clip
- text
    - Text parameters are essential for nodes because they provide the content and context of the key frame conditions. They are used to generate markers that influence the final visual output.
    - Comfy dtype: STRING
    - Python dtype: str
- time
    - Time parameters are important because it determines the time position of the key frame in the sequence. It affects the overall rhythm and structure of the key frame animation.
    - Comfy dtype: FLOAT
    - Python dtype: float
- interpolation_method
    - The plug-in method is important because it determines the style of transition between the frames. It affects the smoothness and visual continuity of the animation.
    - Comfy dtype: COMBO
    - Python dtype: str
## Optional
- schedule
    - When using a plan parameter, it allows automatic adjustments to the key frame over time. It simplifys the process of creating complex animations.
    - Comfy dtype: SCHEDULE
    - Python dtype: dict

# Output types
- keyframed_condition
    - The output provides a structured representation of the key frame conditions, which are essential to the visual narrative of the animation. It covers the combined effects of text input and time placement.
    - Comfy dtype: KEYFRAMED_CONDITION
    - Python dtype: dict
- conditioning
    - This output contains a code for text input and is used to influence key frame conditions. It is a key intermediate step in node operations.
    - Comfy dtype: CONDITIONING
    - Python dtype: list
- schedule
    - The planned output is a structured plan for an automated key frame adjustment. It is important for creating dynamic and responsive animations that are adapted over time.
    - Comfy dtype: SCHEDULE
    - Python dtype: tuple

# Usage tips
- Infra type: GPU

# Source code
```
class KfKeyframedConditionWithText(KfKeyframedCondition):
    """
    Attaches a condition to a keyframe
    """
    CATEGORY = CATEGORY
    FUNCTION = 'main'
    RETURN_TYPES = ('KEYFRAMED_CONDITION', 'CONDITIONING', 'SCHEDULE')

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'clip': ('CLIP',), 'text': ('STRING', {'multiline': True, 'default': ''}), 'time': ('FLOAT', {'default': 0, 'step': 1}), 'interpolation_method': (list(kf.interpolation.EASINGS.keys()), {'default': 'linear'})}, 'optional': {'schedule': ('SCHEDULE', {})}}

    def main(self, clip, text, time, interpolation_method, schedule=None):
        tokens = clip.tokenize(text)
        (cond, pooled) = clip.encode_from_tokens(tokens, return_pooled=True)
        conditioning = [[cond, {'pooled_output': pooled}]]
        keyframed_condition = super().main(conditioning, time, interpolation_method)[0]
        keyframed_condition['kf_cond_t'].label = text
        schedule = set_keyframed_condition(keyframed_condition, schedule)
        return (keyframed_condition, conditioning, schedule)
```