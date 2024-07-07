# Documentation
- Class name: RegionalSeedExplorerColorMask
- Category: InspirePack/Regional
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Inspire-Pack.git

The node explores image areas based on colour masks and feed tips and is able to generate changes, control noise and enhance specific features in the given area.

# Input types
## Required
- color_mask
    - The colour mask is essential to define the areas of the image that will be subject to change and noise exploration. It is the basis for node operations.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image or torch.Tensor
- noise
    - Noise is the basic input for introducing change, which allows for diversified outcomes and a richer generation of image sets.
    - Comfy dtype: NOISE
    - Python dtype: torch.Tensor
- seed_prompt
    - Seed tips play an important role in guiding change by providing a specific direction for nodes to generate target changes in images.
    - Comfy dtype: STRING
    - Python dtype: str
- enable_additional
    - This parameter determines whether to apply additional seed tips, thus affecting the complexity and diversity of image changes.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- noise_mode
    - Noise patterns determine the computing resources used to process noise, and the GPU provides faster calculations for model-intensive tasks, while the CPU is better suited for less complex operations.
    - Comfy dtype: COMBO[GPU(=A1111), CPU]
    - Python dtype: str
## Optional
- mask_color
    - Mask colour parameters are essential for identifying a particular colour in the colour mask that will be used to create a binary mask for the selection of the area.
    - Comfy dtype: STRING
    - Python dtype: str
- additional_seed
    - When enabled, additional seeds provide another layer of control for the change process, allowing further customization of the generated content.
    - Comfy dtype: INT
    - Python dtype: int
- additional_strength
    - This parameter adjusts the impact of additional seeds to allow the user to fine-tune the intensity of changes in the image.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- noise
    - Output noise represents processed noise with application changes, which is a key component in generating diverse image results.
    - Comfy dtype: NOISE
    - Python dtype: torch.Tensor
- mask
    - The mask output is the binary expression of the selected area, which is essential for segregating and applying specific changes to the image.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class RegionalSeedExplorerColorMask:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'color_mask': ('IMAGE',), 'mask_color': ('STRING', {'multiline': False, 'default': '#FFFFFF'}), 'noise': ('NOISE',), 'seed_prompt': ('STRING', {'multiline': True, 'dynamicPrompts': False, 'pysssss.autocomplete': False}), 'enable_additional': ('BOOLEAN', {'default': True, 'label_on': 'true', 'label_off': 'false'}), 'additional_seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615}), 'additional_strength': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'noise_mode': (['GPU(=A1111)', 'CPU'],)}}
    RETURN_TYPES = ('NOISE', 'MASK')
    FUNCTION = 'doit'
    CATEGORY = 'InspirePack/Regional'

    def doit(self, color_mask, mask_color, noise, seed_prompt, enable_additional, additional_seed, additional_strength, noise_mode):
        device = comfy.model_management.get_torch_device()
        noise_device = 'cpu' if noise_mode == 'CPU' else device
        color_mask = color_mask.to(device)
        noise = noise.to(device)
        mask = color_to_mask(color_mask, mask_color)
        original_mask = mask
        mask = torch.nn.functional.interpolate(mask.reshape((-1, 1, mask.shape[-2], mask.shape[-1])), size=(noise.shape[2], noise.shape[3]), mode='bilinear').squeeze(0)
        mask = mask.to(device)
        try:
            seed_prompt = seed_prompt.replace('\n', '')
            items = seed_prompt.strip().split(',')
            if items == ['']:
                items = []
            if enable_additional:
                items.append((additional_seed, additional_strength))
            noise = prompt_support.SeedExplorer.apply_variation(noise, items, noise_device, mask)
        except Exception:
            print(f'[ERROR] IGNORED: RegionalSeedExplorerColorMask is failed.')
            traceback.print_exc()
        color_mask.cpu()
        noise = noise.cpu()
        original_mask = original_mask.cpu()
        return (noise, original_mask)
```