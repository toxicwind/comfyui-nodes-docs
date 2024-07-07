# Documentation
- Class name: RegionalIPAdapterEncodedMask
- Category: InspirePack/Regional
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Inspire-Pack.git

The RegionalIPAdapterEncoded Mask class is designed to apply the area mask to the image-processing adaptor, allowing the image generated to be conditioned according to the specified mask. By focusing on specific areas of interest in the image, the node enhances control over the image-generation process. It allows fine-tuning of image properties and style shifts to ensure that the content generated closely matches the visual elements required.

# Input types
## Required
- mask
    - A mask parameter is essential to define which areas of the image will be the focus of the node. It serves as a guide to the image generation process, ensuring that the specified areas are highlighted or modified according to the user's intent.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor
- embeds
    - Embedding vectors provide a way to integrate additional context and information into the image generation process. They capture nuances and details that may not exist simply by masking and improve the overall quality and relevance of the images generated.
    - Comfy dtype: embeds
    - Python dtype: torch.Tensor
- weight
    - By adjusting this value, the user can control the impact of the mask and the embedded vector on the final output, thus balancing the desired visual elements with the natural processes of generation.
    - Comfy dtype: FLOAT
    - Python dtype: float
- weight_type
    - The weight type parameters determine how the weight is applied to the mask and the embedded vector. Each type provides a different method of mixing user input and model output, affecting the style and appearance of the final image.
    - Comfy dtype: COMBO[original, linear, channel penalty]
    - Python dtype: str
- start_at
    - Start_at parameters define where the mask affects the image. It helps to control the spatial distribution of the mask effect and ensures that it is accurately located in the target area.
    - Comfy dtype: FLOAT
    - Python dtype: float
- end_at
    - End_at parameters specify the end position for the image effects of the mask. It is used in conjunction with start_at, defines the range of applications for the mask effects and allows precise control over the regionalization of the images generated.
    - Comfy dtype: FLOAT
    - Python dtype: float
## Optional
- unfold_batch
    - Unfold_batch parameters allow batch dimensions to be manipulated when applying masks and embedded vectors. This is very useful for the efficient processing of a large number of image batches and optimizes the performance and throughput of nodes.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- REGIONAL_IPADAPTER
    - The output of the RegionalIPAdapterEncoded Mask node is a conditional image adapter modified according to input mask, embedded vectors and other parameters. This output can be used as a building block for further image generation or operation tasks, seamlessly integrated into the creative workflow.
    - Comfy dtype: REGIONAL_IPADAPTER
    - Python dtype: IPAdapterConditioning

# Usage tips
- Infra type: GPU

# Source code
```
class RegionalIPAdapterEncodedMask:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'mask': ('MASK',), 'embeds': ('embeds',), 'weight': ('FLOAT', {'default': 0.7, 'min': -1, 'max': 3, 'step': 0.05}), 'weight_type': (['original', 'linear', 'channel penalty'],), 'start_at': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1.0, 'step': 0.001}), 'end_at': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.001}), 'unfold_batch': ('BOOLEAN', {'default': False})}}
    RETURN_TYPES = ('REGIONAL_IPADAPTER',)
    FUNCTION = 'doit'
    CATEGORY = 'InspirePack/Regional'

    def doit(self, mask, embeds, weight, weight_type, start_at=0.0, end_at=1.0, unfold_batch=False):
        cond = IPAdapterConditioning(mask, weight, weight_type, embeds=embeds, start_at=start_at, end_at=end_at, unfold_batch=unfold_batch)
        return (cond,)
```