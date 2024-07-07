# Documentation
- Class name: EditBasicPipe
- Category: ImpactPack/Pipe
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The 'doit' method of the Edit Basic Pipe class is designed to modify the components of the basic pipe. It allows for the selective replacement of elements such as models, clips, VAEs and condition input with new values, if new values are provided. The flexibility of the method ensures that the pipe can be adapted to specific needs without changing the infrastructure.

# Input types
## Required
- basic_pipe
    - The 'basic_pipe' parameter is a cluster of elements containing the core elements of the pipeline. It is essential because it forms the basis for the changes. The method uses this input to retain the existing structure or to integrate new components according to the specified component.
    - Comfy dtype: BASIC_PIPE
    - Python dtype: Tuple[Any, ...]
## Optional
- model
    - The'model' parameter is an optional input that allows the user to assign a new model to the pipeline. If provided, it will replace the existing model in the pipeline, thus enabling customization to suit different analytical or predictive tasks.
    - Comfy dtype: MODEL
    - Python dtype: Optional[Any]
- clip
    - The 'clip' parameter is another optional element that can be updated. It is particularly useful when a pipeline requires different cropping mechanisms or integration with various data-processing technologies.
    - Comfy dtype: CLIP
    - Python dtype: Optional[Any]
- vae
    - The 'vae' parameter allows for the inclusion or updating of the variable coder in the pipe. This may be important for tasks involving the reduction of dimensions or the generation of models.
    - Comfy dtype: VAE
    - Python dtype: Optional[Any]
- positive
    - The 'positive' parameter represents a condition input that can be replaced if necessary. It plays an important role in the pipeline when the task involves intensive learning or requires specific guidance on model behaviour.
    - Comfy dtype: CONDITIONING
    - Python dtype: Optional[Any]
- negative
    - The 'negative' parameter is used to assign a negative condition input to the pipeline. This is important when models need to learn from examples of what should not be done, which is essential for some types of comparative learning.
    - Comfy dtype: CONDITIONING
    - Python dtype: Optional[Any]

# Output types
- basic_pipe
    - Output 'basic_pe' is a modified version of the conduit that reflects any update of its components. It is important because it represents a pipe with a new configuration that is prepared for further use or deployment.
    - Comfy dtype: BASIC_PIPE
    - Python dtype: Tuple[Any, ...]

# Usage tips
- Infra type: CPU

# Source code
```
class EditBasicPipe:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'basic_pipe': ('BASIC_PIPE',)}, 'optional': {'model': ('MODEL',), 'clip': ('CLIP',), 'vae': ('VAE',), 'positive': ('CONDITIONING',), 'negative': ('CONDITIONING',)}}
    RETURN_TYPES = ('BASIC_PIPE',)
    RETURN_NAMES = ('basic_pipe',)
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Pipe'

    def doit(self, basic_pipe, model=None, clip=None, vae=None, positive=None, negative=None):
        (res_model, res_clip, res_vae, res_positive, res_negative) = basic_pipe
        if model is not None:
            res_model = model
        if clip is not None:
            res_clip = clip
        if vae is not None:
            res_vae = vae
        if positive is not None:
            res_positive = positive
        if negative is not None:
            res_negative = negative
        pipe = (res_model, res_clip, res_vae, res_positive, res_negative)
        return (pipe,)
```