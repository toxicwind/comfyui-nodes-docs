# Documentation
- Class name: NNLatentUpscale
- Category: latent
- Output node: False
- Repo Ref: https://github.com/Ttl/ComfyUi_NNLatentUpscale

NNlatentUpscale, a class that aims to upgrade low-dimensional potential resolution through neurological networks, provides a method of generating high-fiscal images from compressed data.

# Input types
## Required
- latent
    - The latent parameter, which represents a compressed form of data that needs to be magnified, serves as the main input for the neurological network to carry out its enhancements.
    - Comfy dtype: LATENT
    - Python dtype: Dict[str, torch.Tensor]
- version
    - The version parameters determine the models used for the magnification process, ensuring compatibility and accuracy of neurological network operations.
    - Comfy dtype: COMBO
    - Python dtype: Union[str, List[str]]
## Optional
- upscale
    - Upscale parameters are fine-tuned to apply to the enhanced level of potential data to influence the resolution and quality of the final output.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- samples
    - The output `samples' represents the potential expression of magnification and now has a higher resolution and is prepared for further processing or analysis.
    - Comfy dtype: LATENT
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class NNLatentUpscale:
    """
    Upscales SDXL latent using neural network
    """

    def __init__(self):
        self.local_dir = os.path.dirname(os.path.realpath(__file__))
        self.scale_factor = 0.13025
        self.dtype = torch.float32
        if model_management.should_use_fp16():
            self.dtype = torch.float16
        self.weight_path = {'SDXL': os.path.join(self.local_dir, 'sdxl_resizer.pt'), 'SD 1.x': os.path.join(self.local_dir, 'sd15_resizer.pt')}
        self.version = 'none'

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'latent': ('LATENT',), 'version': (['SDXL', 'SD 1.x'],), 'upscale': ('FLOAT', {'default': 1.5, 'min': 1.0, 'max': 2.0, 'step': 0.01, 'display': 'number'})}}
    RETURN_TYPES = ('LATENT',)
    FUNCTION = 'upscale'
    CATEGORY = 'latent'

    def upscale(self, latent, version, upscale):
        device = model_management.get_torch_device()
        samples = latent['samples'].to(device=device, dtype=self.dtype)
        if version != self.version:
            self.model = LatentResizer.load_model(self.weight_path[version], device, self.dtype)
            self.version = version
        self.model.to(device=device)
        latent_out = self.model(self.scale_factor * samples, scale=upscale) / self.scale_factor
        if self.dtype != torch.float32:
            latent_out = latent_out.to(dtype=torch.float32)
        latent_out = latent_out.to(device='cpu')
        self.model.to(device=model_management.vae_offload_device())
        return ({'samples': latent_out},)
```