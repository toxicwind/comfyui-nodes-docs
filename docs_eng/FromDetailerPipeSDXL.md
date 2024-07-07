# Documentation
- Class name: FromDetailerPipe_SDXL
- Category: ImpactPack/Pipe
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The `doit' method for the FromDetailer Pipe_SDXL node is designed to organize processing pipes (e.g. models, conditioners and detectors) by unpackaging and organizing various components from detailer pipe. It plays a key role in the data and functional process within the ImpactPack framework to ensure seamless integration between the different modules.

# Input types
## Required
- detailer_pipe
    - The parameter 'detailer_pipe' is necessary because it serves as a channel to the structured assembly of the components required for its operation. It is the main input and determines the execution path and subsequent output of the node.
    - Comfy dtype: DETAILER_PIPE
    - Python dtype: Tuple[DETAILER_PIPE, MODEL, CLIP, VAE, CONDITIONING, CONDITIONING, BBOX_DETECTOR, SAM_MODEL, SEGM_DETECTOR, DETAILER_HOOK]

# Output types
- detailer_pipe
    - The output 'detailer_pipe' is a structured assembly of node processing and organization. It is important because it forms the basis for further treatment in the subsequent phase of the pipeline.
    - Comfy dtype: DETAILER_PIPE
    - Python dtype: DETAILER_PIPE
- model
    - Output'model' means a machine learning model used in node processing pipes. It is a key component for a task that requires prediction analysis or model identification.
    - Comfy dtype: MODEL
    - Python dtype: MODEL
- clip
    - Output 'clip' is a component that may involve text or image processing, which helps nodes to process and interpret contextual data.
    - Comfy dtype: CLIP
    - Python dtype: CLIP
- vae
    - Output 'vae' represents a variable coder, a type of neural network that is used without a supervised learning task. It plays an important role in the ability of nodes to generate or reconstruct data.
    - Comfy dtype: VAE
    - Python dtype: VAE
- bbox_detector
    - Output 'bbox_detector' is a module that detects boundary frames in images or videos. It is important for applications that require spatial positioning of objects or areas of interest.
    - Comfy dtype: BBOX_DETECTOR
    - Python dtype: BBOX_DETECTOR
- sam_model_opt
    - The output of'sam_model_opt' is an optimised version of the landscape attention model, which enhances the ability of nodes to focus on and process specific areas in the data.
    - Comfy dtype: SAM_MODEL
    - Python dtype: SAM_MODEL
- segm_detector_opt
    - The output'segm_detector_opt' is an optimized partition detector that is essential for tasks involving the identification and separation of different areas in the image.
    - Comfy dtype: SEGM_DETECTOR
    - Python dtype: SEGM_DETECTOR
- detailer_hook
    - Output 'detailer_hook' is a mechanism that allows customisation or extension of node functions and provides flexibility to handle specific cases.
    - Comfy dtype: DETAILER_HOOK
    - Python dtype: DETAILER_HOOK
- refiner_model
    - Output'refinder_model' is another machine learning model that may be used to refine or enhance the output of the main model in the node workflow.
    - Comfy dtype: MODEL
    - Python dtype: MODEL

# Usage tips
- Infra type: CPU

# Source code
```
class FromDetailerPipe_SDXL:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'detailer_pipe': ('DETAILER_PIPE',)}}
    RETURN_TYPES = ('DETAILER_PIPE', 'MODEL', 'CLIP', 'VAE', 'CONDITIONING', 'CONDITIONING', 'BBOX_DETECTOR', 'SAM_MODEL', 'SEGM_DETECTOR', 'DETAILER_HOOK', 'MODEL', 'CLIP', 'CONDITIONING', 'CONDITIONING')
    RETURN_NAMES = ('detailer_pipe', 'model', 'clip', 'vae', 'positive', 'negative', 'bbox_detector', 'sam_model_opt', 'segm_detector_opt', 'detailer_hook', 'refiner_model', 'refiner_clip', 'refiner_positive', 'refiner_negative')
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Pipe'

    def doit(self, detailer_pipe):
        (model, clip, vae, positive, negative, wildcard, bbox_detector, segm_detector_opt, sam_model_opt, detailer_hook, refiner_model, refiner_clip, refiner_positive, refiner_negative) = detailer_pipe
        return (detailer_pipe, model, clip, vae, positive, negative, bbox_detector, sam_model_opt, segm_detector_opt, detailer_hook, refiner_model, refiner_clip, refiner_positive, refiner_negative)
```