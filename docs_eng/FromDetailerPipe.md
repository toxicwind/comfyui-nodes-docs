# Documentation
- Class name: FromDetailerPipe
- Category: ImpactPack/Pipe
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The 'doit' method for the FromDetailer Pipe node is designed to extract and organize various components from a detailed pipeline. It serves as a conduit for integrating different elements, such as models, clips and detectors, into the follow-up phase of the shock analysis process.

# Input types
## Required
- detailer_pipe
    - The parameter 'detailer_pipe' is necessary because it provides an input conduit containing all components required for node work. It is the main source of node extraction models, clips and other relevant data for further processing.
    - Comfy dtype: DETAILER_PIPE
    - Python dtype: Tuple[Any, ...]

# Output types
- model
    - The'model' output represents the core of the calculation model used in the pipeline, which plays a key role in data analysis and processing.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- clip
    - `clip' output is a key component for generating and operating visual expressions and is usually used with models for feature extraction.
    - Comfy dtype: CLIP
    - Python dtype: torch.Tensor
- vae
    - The `vae' output represents a variable-to-encoder model, which is essential for tasks involving data coding and decoding.
    - Comfy dtype: VAE
    - Python dtype: torch.nn.Module
- positive
    - The 'positive' output as a form of conditional data has a positive impact on the behaviour of subsequent models or algorithms.
    - Comfy dtype: CONDITIONING
    - Python dtype: torch.Tensor
- negative
    - The 'negative' output is similar to the 'positive' output, but the conditions data provided have a negative impact on model behaviour.
    - Comfy dtype: CONDITIONING
    - Python dtype: torch.Tensor
- bbox_detector
    - The 'bbox_detector' output, which identifies and locates the interest areas in the image, is usually used for target detection missions.
    - Comfy dtype: BBOX_DETECTOR
    - Python dtype: torch.nn.Module
- sam_model_opt
    - The'sam_model_opt' output refers to an optional scenario perception model that can be used for more complex scenario analysis and understanding.
    - Comfy dtype: SAM_MODEL
    - Python dtype: Optional[torch.nn.Module]
- segm_detector_opt
    - The'segm_detector_opt' output is an optional component for the partition of images and contributes to tasks requiring detailed image analysis.
    - Comfy dtype: SEGM_DETECTOR
    - Python dtype: Optional[torch.nn.Module]
- detailer_hook
    - The 'detailer_hook' output is an additional hook that can be used to extend or customize the function of the node to suit specific cases.
    - Comfy dtype: DETAILER_HOOK
    - Python dtype: Any

# Usage tips
- Infra type: CPU

# Source code
```
class FromDetailerPipe:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'detailer_pipe': ('DETAILER_PIPE',)}}
    RETURN_TYPES = ('MODEL', 'CLIP', 'VAE', 'CONDITIONING', 'CONDITIONING', 'BBOX_DETECTOR', 'SAM_MODEL', 'SEGM_DETECTOR', 'DETAILER_HOOK')
    RETURN_NAMES = ('model', 'clip', 'vae', 'positive', 'negative', 'bbox_detector', 'sam_model_opt', 'segm_detector_opt', 'detailer_hook')
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Pipe'

    def doit(self, detailer_pipe):
        (model, clip, vae, positive, negative, wildcard, bbox_detector, segm_detector_opt, sam_model_opt, detailer_hook, _, _, _, _) = detailer_pipe
        return (model, clip, vae, positive, negative, bbox_detector, sam_model_opt, segm_detector_opt, detailer_hook)
```