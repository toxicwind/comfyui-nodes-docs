# Documentation
- Class name: FromBasicPipe
- Category: ImpactPack/Pipe
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The `doit' method for the From BasicPipe node is a key channel in the data processing pipeline, which extracts and organizes core elements such as models, clips and converters (VAE). It ensures that the necessary data structures are efficiently retrieved and prepared for seamless integration of different data components in the workflow.

# Input types
## Required
- basic_pipe
    - The 'basic_pipe' parameter is essential for the 'doit' method, because it contains the basic data structure required for node operations. It is a channel that is guided by its models, clippings and VAE components, highlighting its key role in making nodes function effectively.
    - Comfy dtype: BASIC_PIPE
    - Python dtype: Tuple[Any, Any, Any, Any, Any]

# Output types
- model
    - The'model'output represents a key component of the node data processing framework, representing a machine learning model that is essential for node functions. It plays an important role in shaping the node's overall contribution to the workflow, emphasizing its importance in the data pipeline.
    - Comfy dtype: MODEL
    - Python dtype: Any
- clip
    - The 'clip'output represents a segment of the data that is essential for node operations. It is used to extract and operate specific parts of the information, emphasizing its importance in the node's ability to process and manage data effectively.
    - Comfy dtype: CLIP
    - Python dtype: Any
- vae
    - The 'vae'output indicates the existence of a variable self-encoder in the node structure, which is a key component of the coding and decoding data expression. Its inclusion is essential to the ability of the node to convert and interpret complex data structures.
    - Comfy dtype: VAE
    - Python dtype: Any
- positive
    - The 'positive'output demonstrates a conditionality factor that guides nodes to deal with logic. It plays an important role in guiding nodes to produce desired results, highlighting their strategic importance in node operations.
    - Comfy dtype: CONDITIONING
    - Python dtype: Any
- negative
    - The 'negative'output represents a counter-conditional factor that is essential to the node decision-making process. It is essential in defining the boundaries of node operations and ensuring that node implementation is consistent with the intended objective.
    - Comfy dtype: CONDITIONING
    - Python dtype: Any

# Usage tips
- Infra type: CPU

# Source code
```
class FromBasicPipe:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'basic_pipe': ('BASIC_PIPE',)}}
    RETURN_TYPES = ('MODEL', 'CLIP', 'VAE', 'CONDITIONING', 'CONDITIONING')
    RETURN_NAMES = ('model', 'clip', 'vae', 'positive', 'negative')
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Pipe'

    def doit(self, basic_pipe):
        (model, clip, vae, positive, negative) = basic_pipe
        return (model, clip, vae, positive, negative)
```