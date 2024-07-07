# Documentation
- Class name: pipeOut
- Category: EasyUse/Pipe
- Output node: False
- Repo Ref: https://github.com/yolain/ComfyUI-Easy-Use.git

The pipeoot node is designed to simplify the output of the flow line and ensure that the results are efficiently managed and organized. It serves as a central hub for processing various data types, facilitating the transition from processing to analysis or storage. By processing the final phase of the data stream, the node maintains the integrity and accessibility of the output.

# Input types
## Required
- pipe
    - The `pipe' parameter is essential, and it represents the flow line from which data are extracted and managed. It is the main source of information for nodes, determining the type and structure of output.
    - Comfy dtype: PIPE_LINE
    - Python dtype: Dict[str, Any]
## Optional
- my_unique_id
    - The `my_unique_id' parameter is used as the identifier for tracking and linking specific outputs to the sole request or process. It facilitates the organization and retrieval of data within the system.
    - Comfy dtype: UNIQUE_ID
    - Python dtype: str

# Output types
- pipe
    - The `pipe' output is a comprehensive collection of post-processing data that contains all the results in the stream line. It is the crystallization of node functions and provides a structured and well-organized data set for further use.
    - Comfy dtype: PIPE_LINE
    - Python dtype: Dict[str, Any]
- model
    - The `model' output represents a machine learning or neurological network model used in the flow line. It is a key component of understanding the basis for processing the data and the methods used.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- pos
    - The `pos' output consists of positive reconciliation data to guide and refine model predictions. It plays a key role in the generation process, ensuring that the output is consistent with the desired results.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Any]
- neg
    - The `neg' output contains negative adjustment data that are used to compare and filter results that are not desired in model predictions. It is an important part of maintaining the quality and relevance of the output.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Any]
- latent
    - The `latent' output represents the intermediate expression or embedding derived from the model. These potential features are essential for understanding the underlying structure of the data and can be used for further analysis or processing.
    - Comfy dtype: LATENT
    - Python dtype: List[torch.Tensor]
- vae
    - ‘vae’ output refers to the changing self-encoder component in the stream line, which is responsible for generating new data points from the learning to the potential space. It is a key innovation in creating new and diversified output.
    - Comfy dtype: VAE
    - Python dtype: torch.nn.Module
- clip
    - The `clip' output is derived from the CLAIP model for multi-modular understanding and generation. It enhances the ability of nodes by providing context and meaning for the output.
    - Comfy dtype: CLIP
    - Python dtype: torch.nn.Module
- image
    - The `image' output consists of visual data, which are the direct result of model processing. Its importance lies in the physical and visual representation of the data, which allows immediate interpretation and analysis.
    - Comfy dtype: IMAGE
    - Python dtype: List[PIL.Image.Image]
- seed
    - `Seed' output is a value used to ensure repeatability and consistency in the generation process. It is essential for debugging and maintaining the reliability of the output.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class pipeOut:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'pipe': ('PIPE_LINE',)}, 'hidden': {'my_unique_id': 'UNIQUE_ID'}}
    RETURN_TYPES = ('PIPE_LINE', 'MODEL', 'CONDITIONING', 'CONDITIONING', 'LATENT', 'VAE', 'CLIP', 'IMAGE', 'INT')
    RETURN_NAMES = ('pipe', 'model', 'pos', 'neg', 'latent', 'vae', 'clip', 'image', 'seed')
    FUNCTION = 'flush'
    CATEGORY = 'EasyUse/Pipe'

    def flush(self, pipe, my_unique_id=None):
        model = pipe.get('model')
        pos = pipe.get('positive')
        neg = pipe.get('negative')
        latent = pipe.get('samples')
        vae = pipe.get('vae')
        clip = pipe.get('clip')
        image = pipe.get('images')
        seed = pipe.get('seed')
        return (pipe, model, pos, neg, latent, vae, clip, image, seed)
```