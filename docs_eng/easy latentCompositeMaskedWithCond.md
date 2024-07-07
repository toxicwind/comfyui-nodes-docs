# Documentation
- Class name: latentCompositeMaskedWithCond
- Category: EasyUse/Latent
- Output node: True
- Repo Ref: https://github.com/yolain/ComfyUI-Easy-Use.git

The node integrates the process of combining text input with potential expressions to generate conditional output. It hides and composites the potential space according to the text conditions, making it possible to create customized results.

# Input types
## Required
- pipe
    - The pipe parameter is the primary data and settings source for node operations. It is essential for the proper operation of the node, as it contains the necessary information for the node to perform the task and generate the output required.
    - Comfy dtype: PIPE_LINE
    - Python dtype: Dict[str, Any]
- text_combine
    - This parameter saves a list of text elements associated with potential data. It plays an important role in shaping the final output, as it directly affects the reconciliation process.
    - Comfy dtype: LIST
    - Python dtype: List[str]
- source_latent
    - The source_latent parameter is essential for the operation of the node, as it provides an initial potential indication that will be compounded and reconciled.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
- source_mask
    - This parameter is critical to shielding the process, as it determines how potential data are reconciled. It influences the final output by controlling the modified area in potential space.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor
- destination_mask
    - Designation_mask parameters play a key role in defining potential space areas that will be updated. They work with the source mask to refine the potential for eventual compounding.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor
- text_combine_mode
    - This parameter determines how the text is combined with the existing hint, influencing the reconciliation process and the final output. It is essential to control the behaviour of node processing text input.
    - Comfy dtype: COMBO[add, replace, cover]
    - Python dtype: str
## Optional
- replace_text
    - The replace_text parameter allows changes to a particular text in the hint. It is important for customizing the reconciliation process without changing the entire hint structure.
    - Comfy dtype: STRING
    - Python dtype: str
- prompt
    - Prompt parameters provide additional text settings that can be used to further refine the reconciliation process. They are useful for adding specific nuances to the final output.
    - Comfy dtype: PROMPT
    - Python dtype: str
- extra_pnginfo
    - This parameter contains supplementary image information that can be used to enhance the reconciliation process. It is particularly suitable for integrating visual elements into the final output.
    - Comfy dtype: EXTRA_PNGINFO
    - Python dtype: Any
- my_unique_id
    - My_unique_id parameter is used to track and identify specific examples of node operations. It is important to maintain the integrity of the process and ensure accurate results.
    - Comfy dtype: UNIQUE_ID
    - Python dtype: str

# Output types
- pipe
    - Pipe output is an updated version of the input pipe, which now contains the latest sample and modified loader settings. It is important because it represents the progress of the flow line and the integration of node processing.
    - Comfy dtype: PIPE_LINE
    - Python dtype: Dict[str, Any]
- latent
    - Potential output represents potential space after compounding and reconciliation. It is critical because it is a direct result of node operations and serves as a basis for further processing or analysis.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor
- conditioning
    - Regulating output is a set of conditions that have been applied to potential space. It is important to understand how nodes deal with input and ensure that the required characteristics are present in the final output.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Tuple[torch.Tensor, Dict[str, Any]]]

# Usage tips
- Infra type: GPU

# Source code
```
class latentCompositeMaskedWithCond:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'pipe': ('PIPE_LINE',), 'text_combine': ('LIST',), 'source_latent': ('LATENT',), 'source_mask': ('MASK',), 'destination_mask': ('MASK',), 'text_combine_mode': (['add', 'replace', 'cover'], {'default': 'add'}), 'replace_text': ('STRING', {'default': ''})}, 'hidden': {'prompt': 'PROMPT', 'extra_pnginfo': 'EXTRA_PNGINFO', 'my_unique_id': 'UNIQUE_ID'}}
    OUTPUT_IS_LIST = (False, False, True)
    RETURN_TYPES = ('PIPE_LINE', 'LATENT', 'CONDITIONING')
    RETURN_NAMES = ('pipe', 'latent', 'conditioning')
    FUNCTION = 'run'
    OUTPUT_NODE = True
    CATEGORY = 'EasyUse/Latent'

    def run(self, pipe, text_combine, source_latent, source_mask, destination_mask, text_combine_mode, replace_text, prompt=None, extra_pnginfo=None, my_unique_id=None):
        positive = None
        clip = pipe['clip']
        destination_latent = pipe['samples']
        conds = []
        for text in text_combine:
            if text_combine_mode == 'cover':
                positive = text
            elif text_combine_mode == 'replace' and replace_text != '':
                positive = pipe['loader_settings']['positive'].replace(replace_text, text)
            else:
                positive = pipe['loader_settings']['positive'] + ',' + text
            positive_token_normalization = pipe['loader_settings']['positive_token_normalization']
            positive_weight_interpretation = pipe['loader_settings']['positive_weight_interpretation']
            a1111_prompt_style = pipe['loader_settings']['a1111_prompt_style']
            positive_cond = pipe['positive']
            log_node_warn
            steps = pipe['loader_settings']['steps'] if 'steps' in pipe['loader_settings'] else 1
            positive_embeddings_final = advanced_encode(clip, positive, positive_token_normalization, positive_weight_interpretation, w_max=1.0, apply_to_pooled='enable', a1111_prompt_style=a1111_prompt_style, steps=steps)
            (cond_1,) = ConditioningSetMask().append(positive_cond, source_mask, 'default', 1)
            (cond_2,) = ConditioningSetMask().append(positive_embeddings_final, destination_mask, 'default', 1)
            positive_cond = cond_1 + cond_2
            conds.append(positive_cond)
        (samples,) = LatentCompositeMasked().composite(destination_latent, source_latent, 0, 0, False)
        new_pipe = {**pipe, 'samples': samples, 'loader_settings': {**pipe['loader_settings'], 'positive': positive}}
        del pipe
        return (new_pipe, samples, conds)
```