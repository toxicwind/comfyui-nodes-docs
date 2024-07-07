# Documentation
- Class name: pipeIn
- Category: EasyUse/Pipe
- Output node: False
- Repo Ref: https://github.com/yolain/ComfyUI-Easy-Use.git

The main function of the node is to ensure that the necessary components are transmitted efficiently, enabling follow-up operations to be carried out as expected.

# Input types
## Required
- pipe
    - The pipe parameter is essential because it represents the primary data and command source for the pipeIn node. It contains all the necessary elements, such as models, condition data and other relevant information, which determines the operation and outcome of the node.
    - Comfy dtype: PIPE_LINE
    - Python dtype: Dict[str, Any]
## Optional
- model
    - The model parameter is important because it defines the core algorithm or neural network structure to be used in the PipeIn node processing. This is essential for the correct function of the node and for producing accurate results.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- pos
    - Positive condition data, known as 'pos', play a crucial role in guiding the behavior of PipeIn nodes. It provides the necessary context for models to generate or process data in the desired way.
    - Comfy dtype: CONDITIONING
    - Python dtype: Any
- neg
    - Negative condition data, or 'neg', are equally important because it sets boundaries for model output. It helps nodes refine their operations and ensures that results are consistent with expected results.
    - Comfy dtype: CONDITIONING
    - Python dtype: Any
- latent
    - The latent parameter is critical when processing unobserved or potential data. It enables the PipeIn node to include hidden variables in its treatment, which can significantly influence the final output.
    - Comfy dtype: LATENT
    - Python dtype: Any
- vae
    - The vae parameter is essential for the function of the node in coding and decoding data. It represents a variable-to-encoder model and is necessary for the pipeIn node to perform tasks related to data compression and generation.
    - Comfy dtype: VAE
    - Python dtype: torch.nn.Module
- clip
    - When the pipeIn node needs to align the resulting data to a specific context or content, the clip parameter is important. It is a CLAIP model that is essential for understanding and generating images or text that match the given description.
    - Comfy dtype: CLIP
    - Python dtype: torch.nn.Module
- image
    - When the pipeIn node involves visual data processing, the image parameter is essential. It carries visual information that the node will operate or analyse in order to achieve the desired result.
    - Comfy dtype: IMAGE
    - Python dtype: torch.Tensor
- xyplot
    - The xyplot parameter is used to define the drawing settings of the pipeIn node. It is important for the visual expression and analysis of data, allowing nodes to generate meaningful visualization and helping to understand the structure and trends of the data.
    - Comfy dtype: XYPLOT
    - Python dtype: Any
- my_unique_id
    - My_unique_id parameter is the only identifier for the PipeIn node example. It is important for tracking and managing nodes in a complex system to ensure that each example can be monitored and controlled separately.
    - Comfy dtype: UNIQUE_ID
    - Python dtype: str

# Output types
- pipe
    - Output Pipe is a refined and structured data set processed by the PipeIn node. It encapsifies the results and any modifications during the node execution as a basis for further operation or analysis within the pipe.
    - Comfy dtype: PIPE_LINE
    - Python dtype: Dict[str, Any]

# Usage tips
- Infra type: CPU

# Source code
```
class pipeIn:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {}, 'optional': {'pipe': ('PIPE_LINE',), 'model': ('MODEL',), 'pos': ('CONDITIONING',), 'neg': ('CONDITIONING',), 'latent': ('LATENT',), 'vae': ('VAE',), 'clip': ('CLIP',), 'image': ('IMAGE',), 'xyPlot': ('XYPLOT',)}, 'hidden': {'my_unique_id': 'UNIQUE_ID'}}
    RETURN_TYPES = ('PIPE_LINE',)
    RETURN_NAMES = ('pipe',)
    FUNCTION = 'flush'
    CATEGORY = 'EasyUse/Pipe'

    def flush(self, pipe=None, model=None, pos=None, neg=None, latent=None, vae=None, clip=None, image=None, xyplot=None, my_unique_id=None):
        model = model if model is not None else pipe.get('model')
        if model is None:
            log_node_warn(f'pipeIn[{my_unique_id}]', 'Model missing from pipeLine')
        pos = pos if pos is not None else pipe.get('positive')
        if pos is None:
            log_node_warn(f'pipeIn[{my_unique_id}]', 'Pos Conditioning missing from pipeLine')
        neg = neg if neg is not None else pipe.get('negative')
        if neg is None:
            log_node_warn(f'pipeIn[{my_unique_id}]', 'Neg Conditioning missing from pipeLine')
        vae = vae if vae is not None else pipe.get('vae')
        if vae is None:
            log_node_warn(f'pipeIn[{my_unique_id}]', 'VAE missing from pipeLine')
        clip = clip if clip is not None else pipe.get('clip')
        if clip is None:
            log_node_warn(f'pipeIn[{my_unique_id}]', 'Clip missing from pipeLine')
        if latent is not None:
            samples = latent
        elif image is None:
            samples = pipe.get('samples') if pipe is not None else None
            image = pipe.get('images') if pipe is not None else None
        elif image is not None:
            if pipe is None:
                batch_size = 1
            else:
                batch_size = pipe['loader_settings']['batch_size'] if 'batch_size' in pipe['loader_settings'] else 1
            samples = {'samples': vae.encode(image[:, :, :, :3])}
            samples = RepeatLatentBatch().repeat(samples, batch_size)[0]
        if pipe is None:
            pipe = {'loader_settings': {'positive': '', 'negative': '', 'xyplot': None}}
        xyplot = xyplot if xyplot is not None else pipe['loader_settings']['xyplot'] if xyplot in pipe['loader_settings'] else None
        new_pipe = {**pipe, 'model': model, 'positive': pos, 'negative': neg, 'vae': vae, 'clip': clip, 'samples': samples, 'images': image, 'seed': pipe.get('seed') if pipe is not None and 'seed' in pipe else None, 'loader_settings': {**pipe['loader_settings'], 'xyplot': xyplot}}
        del pipe
        return (new_pipe,)
```