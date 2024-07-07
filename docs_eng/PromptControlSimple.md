# Documentation
- Class name: PromptControlSimple
- Category: promptcontrol
- Output node: False
- Repo Ref: https://github.com/asagi4/comfyui-prompt-control.git

This type of node covers the management and application of the tip plan and the filtering of the model, thereby controlling the generation process. It gives an abstract view of the complexity of the hint operation and provides a structured approach to fine-tune model output according to the specified conditions.

# Input types
## Required
- model
    - Model parameters are essential because it defines the AI system that will process input and generate output. It is the core component that drives the entire operation of the node.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- clip
    - The clip parameter is essential to manage the context and structure of the input data and to ensure that the model processes the information within the desired framework.
    - Comfy dtype: CLIP
    - Python dtype: ClipModel
- positive
    - Positive input as a positive reminder guides model generation towards desired outcomes and shapes the direction of output.
    - Comfy dtype: STRING
    - Python dtype: str
- negative
    - Negative input as a constraint prevents models from generating undesirable content and ensures that the output is consistent with the specified boundary.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- tags
    - The label is used to classify and filter the generated content and allows for targeted control of specific aspects of the output.
    - Comfy dtype: STRING
    - Python dtype: str
- start
    - The starting parameter defines the starting point of the hint plan and determines when the effect of the hint begins.
    - Comfy dtype: FLOAT
    - Python dtype: float
- end
    - End parameters mark the end point of the reminder, and when the effect of the reminder is established.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- model
    - The output model is an updated AI system that combines applied tips and filters to generate content consistent with the specified guidance.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- positive
    - Positive output represents a refined hint that has been processed and is now part of the model guidance system.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Tuple[str, Dict]]
- negative
    - Negative outputs include applied constraints to ensure that the content generated complies with defined limitations.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Tuple[str, Dict]]
- model_filtered
    - The filtered model output is an AI system that has been adjusted to the specified label and percentage range to fine-tune its generation capacity.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- pos_filtered
    - The positive filter output indicates that the filtering is based on the hint of the label and the percentage range, so that the model is generated on the desired element.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Tuple[str, Dict]]
- neg_filtered
    - Negative filter outputs represent constraints refined through labelling and percentage range filtering, increasing the ability of models to avoid content that they do not want.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Tuple[str, Dict]]

# Usage tips
- Infra type: CPU

# Source code
```
class PromptControlSimple:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'clip': ('CLIP',), 'positive': ('STRING', {'multiline': True}), 'negative': ('STRING', {'multiline': True})}, 'optional': {'tags': ('STRING', {'default': ''}), 'start': ('FLOAT', {'min': 0.0, 'max': 1.0, 'step': 0.1, 'default': 0.0}), 'end': ('FLOAT', {'min': 0.0, 'max': 1.0, 'step': 0.1, 'default': 1.0})}}
    RETURN_TYPES = ('MODEL', 'CONDITIONING', 'CONDITIONING', 'MODEL', 'CONDITIONING', 'CONDITIONING')
    RETURN_NAMES = ('model', 'positive', 'negative', 'model_filtered', 'pos_filtered', 'neg_filtered')
    CATEGORY = 'promptcontrol'
    FUNCTION = 'apply'

    def apply(self, model, clip, positive, negative, tags='', start=0.0, end=1.0):
        lora_cache = {}
        cond_cache = {}
        pos_sched = parse_prompt_schedules(positive)
        pos_cond = pos_filtered = control_to_clip_common(self, clip, pos_sched, lora_cache, cond_cache)
        neg_sched = parse_prompt_schedules(negative)
        neg_cond = neg_filtered = control_to_clip_common(self, clip, neg_sched, lora_cache, cond_cache)
        new_model = model_filtered = schedule_lora_common(model, pos_sched, lora_cache)
        if [tags.strip(), start, end] != ['', 0.0, 1.0]:
            pos_filtered = control_to_clip_common(self, clip, pos_sched.with_filters(tags, start, end), lora_cache, cond_cache)
            neg_filtered = control_to_clip_common(self, clip, neg_sched.with_filters(tags, start, end), lora_cache, cond_cache)
            model_filtered = schedule_lora_common(model, pos_sched.with_filters(tags, start, end), lora_cache)
        return (new_model, pos_cond, neg_cond, model_filtered, pos_filtered, neg_filtered)
```