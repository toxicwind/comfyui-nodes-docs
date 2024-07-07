# Documentation
- Class name: FromBasicPipe_v2
- Category: ImpactPack/Pipe
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

From BasicPipe_v2 the 'doit' method is designed to process and return structured output from the given basic pipe. It covers the essence of the data flow in ImpactPack and ensures that the necessary components, such as models, clips and VAE, are ready for downstream tasks.

# Input types
## Required
- basic_pipe
    - The `basic_pipe' parameter is the key input of the node, as it represents the basic pipeline containing the essential elements necessary for processing. It is essential for the implementation of the node and has a direct impact on the outcome of the operation.
    - Comfy dtype: BASIC_PIPE
    - Python dtype: Tuple[Any, ...]

# Output types
- basic_pipe
    - The `basic_pipe' output is an input reflection that marks the successful processing and retention of the basic pipeline in node operations. It is a key component of a follow-on task that relies on the integrity of the initial data structure.
    - Comfy dtype: BASIC_PIPE
    - Python dtype: Tuple[Any, ...]
- model
    - The `model' output represents a machine-learning model derived from the basic pipeline, which is essential for forecasting analysis and decision-making within the system.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- clip
    - The `clip' output represents a component that may involve the operation or extraction of data features and plays an important role in the overall function of the node.
    - Comfy dtype: CLIP
    - Python dtype: Any
- vae
    - The `vae' output marks the existence of a variable-based encoder in the node, which is essential for tasks involving no supervisory learning and data reduction.
    - Comfy dtype: VAE
    - Python dtype: torch.nn.Module
- positive
    - The `positive' output indicates a positive reconciliation factor that may be used to guide or influence the behaviour of the follow-up process within the node.
    - Comfy dtype: CONDITIONING
    - Python dtype: Any
- negative
    - The `negative' output corresponds to a negative adjustment factor, which may be critical in controlling or modifying the direction of subsequent operations.
    - Comfy dtype: CONDITIONING
    - Python dtype: Any

# Usage tips
- Infra type: CPU

# Source code
```
class FromBasicPipe_v2:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'basic_pipe': ('BASIC_PIPE',)}}
    RETURN_TYPES = ('BASIC_PIPE', 'MODEL', 'CLIP', 'VAE', 'CONDITIONING', 'CONDITIONING')
    RETURN_NAMES = ('basic_pipe', 'model', 'clip', 'vae', 'positive', 'negative')
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Pipe'

    def doit(self, basic_pipe):
        (model, clip, vae, positive, negative) = basic_pipe
        return (basic_pipe, model, clip, vae, positive, negative)
```