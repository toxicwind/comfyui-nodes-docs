# Documentation
- Class name: NoisyLatentImage
- Category: latent/noise
- Output node: False
- Repo Ref: https://github.com/BlenderNeko/ComfyUI_Noise.git

The node generates the potential variables of noise, which are essential for the generation of images of various models. It introduces noise in potential spaces, helping to create diversified output from trained models. The node is designed to ensure that noise is generated in accordance with procedures and can be adapted to the needs of different models.

# Input types
## Required
- source
    - The source parameter determines whether the calculation is performed on the CPU or GPU. This option significantly affects the performance of the node, and the GPU can speed up the execution of tasks involving a large amount of data and complex computing tasks.
    - Comfy dtype: COMBO[('CPU', 'GPU'),]
    - Python dtype: str
- seed
    - Seed parameters are essential for the repeatability of noise generation processes. It ensures that the same random numbers are used for each implementation node and that the results are consistent.
    - Comfy dtype: INT
    - Python dtype: int
- width
    - The width parameter specifies the desired width to generate the image. It affects the resolution and, in turn, the level of detail and the computational resources required during the process of generation.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - The header parameter is set to generate the height of the image. Similar to width, it affects resolution and computational needs, with higher values leading to more detailed images and increased processing requirements.
    - Comfy dtype: INT
    - Python dtype: int
- batch_size
    - Batch processing size determines the number of images to be processed in parallel. An increase in the volume of Batch processing would increase efficiency, but would require more memory and computational resources.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- samples
    - The samples output contains the generated noise potential variables that are used as input to the subsequent generation model. These potential variables are the basis for creating a diversified output range, and their quality and characteristics are essential for the end result.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class NoisyLatentImage:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'source': (['CPU', 'GPU'],), 'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615}), 'width': ('INT', {'default': 512, 'min': 64, 'max': MAX_RESOLUTION, 'step': 8}), 'height': ('INT', {'default': 512, 'min': 64, 'max': MAX_RESOLUTION, 'step': 8}), 'batch_size': ('INT', {'default': 1, 'min': 1, 'max': 64})}}
    RETURN_TYPES = ('LATENT',)
    FUNCTION = 'create_noisy_latents'
    CATEGORY = 'latent/noise'

    def create_noisy_latents(self, source, seed, width, height, batch_size):
        torch.manual_seed(seed)
        if source == 'CPU':
            device = 'cpu'
        else:
            device = comfy.model_management.get_torch_device()
        noise = torch.randn((batch_size, 4, height // 8, width // 8), dtype=torch.float32, device=device).cpu()
        return ({'samples': noise},)
```