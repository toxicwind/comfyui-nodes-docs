# Documentation
- Class name: FromDetailerPipe_v2
- Category: ImpactPack/Pipe
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

FromDetailer Pipe_v2 is designed to coordinate the flow of information and resources in complex processing pipes. It serves as a gateway for various components, such as models, detectors and hooks, to ensure that they are properly integrated and used in the system. The node plays a key role in simplifying operations and improving the overall efficiency of the pipeline.

# Input types
## Required
- detailer_pipe
    - The detailer_pipe parameter is essential because it covers the core components required for node operations. It serves as a conduit to provide nodes with the necessary data and configuration for processing. Effective handling of this parameter is essential for nodes to function effectively and achieve their intended purpose.
    - Comfy dtype: DETAILER_PIPE
    - Python dtype: Tuple[Any, ...]

# Output types
- detailer_pipe
    - The output detailer_pipe is a key element that encapsifies the processed data and configuration and is prepared for transmission to the pipeline for subsequent stages. It represents the outcome of the node process and is essential to maintain continuity and integrity of the workflow.
    - Comfy dtype: DETAILER_PIPE
    - Python dtype: Tuple[Any, ...]
- model
    - The model output represents the machine learning or statistical model used in the pipe. It is a basic component that contributes to the system's analytical capabilities and allows prediction, classification or other extrapolation based on input data.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- clip
    - Clip output indicates that a segment or part of the data has been extracted for specific analysis or processing. It is an important element in node operations and is usually used for focused tasks that require complete data subsets.
    - Comfy dtype: CLIP
    - Python dtype: torch.Tensor
- vae
    - The vae output refers to a variable-based encoder, a type of neural network that can learn and encode data into low-dimensional expressions. It plays an important role in node functions by providing effective means of compressing and decompressing information.
    - Comfy dtype: VAE
    - Python dtype: torch.nn.Module
- positive
    - A positive output indicates a set of positive conditions or factors that affect the process of the node. It is used to guide the node to generate or recognize the desired result in the system.
    - Comfy dtype: CONDITIONING
    - Python dtype: torch.Tensor
- negative
    - Negative output indicates a set of negative conditions or factors considered during the node operation. It helps to refine the node’s decision-making process by providing a comparison with positive conditions.
    - Comfy dtype: CONDITIONING
    - Python dtype: torch.Tensor
- bbox_detector
    - The bbox_detector output is a key component of the task that requires object detection or spatial perception.
    - Comfy dtype: BBOX_DETECTOR
    - Python dtype: torch.nn.Module
- sam_model_opt
    - The sam_model_opt output refers to optional examples of sample models that may be used to sample or generate data points in the pipeline. It increases the flexibility of nodes by allowing a combination of sampling techniques.
    - Comfy dtype: SAM_MODEL
    - Python dtype: Optional[torch.nn.Module]
- segm_detector_opt
    - The output of segm_detector_opt is an optional component dedicated to the partitioning of parts of images or data for further analysis. It enhances the function of nodes by enabling more fine particle processing of visual or structured data.
    - Comfy dtype: SEGM_DETECTOR
    - Python dtype: Optional[torch.nn.Module]
- detailer_hook
    - The detailer_hook output is a custom-made hook that allows for the integration of additional functions or extensions into nodes. It provides a method by which nodes can be customised according to a particular case or request behaviour.
    - Comfy dtype: DETAILER_HOOK
    - Python dtype: Callable[..., Any]

# Usage tips
- Infra type: CPU

# Source code
```
class FromDetailerPipe_v2:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'detailer_pipe': ('DETAILER_PIPE',)}}
    RETURN_TYPES = ('DETAILER_PIPE', 'MODEL', 'CLIP', 'VAE', 'CONDITIONING', 'CONDITIONING', 'BBOX_DETECTOR', 'SAM_MODEL', 'SEGM_DETECTOR', 'DETAILER_HOOK')
    RETURN_NAMES = ('detailer_pipe', 'model', 'clip', 'vae', 'positive', 'negative', 'bbox_detector', 'sam_model_opt', 'segm_detector_opt', 'detailer_hook')
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Pipe'

    def doit(self, detailer_pipe):
        (model, clip, vae, positive, negative, wildcard, bbox_detector, segm_detector_opt, sam_model_opt, detailer_hook, _, _, _, _) = detailer_pipe
        return (detailer_pipe, model, clip, vae, positive, negative, bbox_detector, sam_model_opt, segm_detector_opt, detailer_hook)
```