# Documentation
- Class name: RegionalSeedExplorerMask
- Category: InspirePack/Regional
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Inspire-Pack.git

The RegionalSeed Explorer Mask node is designed to enhance the creative process by introducing changes in the noise field based on specified seed tips and additional parameters. It operates noise to generate diverse visual elements that can be used in various arts and design applications.

# Input types
## Required
- mask
    - The mask parameter is essential because it defines the areas in the noise field that will be affected by the seed exploration process. It serves as a guide for nodes to understand where changes will be applied.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor
- noise
    - Noise parameters are the basic noise that nodes will operate. It is essential for generating the output of change, as it forms the basis for the application of seed exploration.
    - Comfy dtype: NOISE
    - Python dtype: torch.Tensor
- seed_prompt
    - Seed hint is a string that contains a change feed. It is a key input because it directly affects the type of change that will be introduced into the noise field.
    - Comfy dtype: STRING
    - Python dtype: str
- enable_additional
    - This parameter controls whether to use additional feed hints. It is important because it determines the complexity and diversity of changes applied to the noise field.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- noise_mode
    - Noise mode parameters determine the computing device used to process noise. It is important to determine the degree and efficiency of the application of change.
    - Comfy dtype: COMBO[GPU(=A1111), CPU]
    - Python dtype: str
## Optional
- additional_seed
    - Additional feed parameters, when used, provide an additional level of control over the change process. It allows for the introduction of more specific changes based on the seeds provided.
    - Comfy dtype: INT
    - Python dtype: int
- additional_strength
    - The additional strength parameter adjusts the strength of the additional change. It is important because it allows fine-tuning of the change effects on the noise field.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- noise
    - The output of noise is the result of a seed exploration process. It represents a changing noise field that can be used further downstream.
    - Comfy dtype: NOISE
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class RegionalSeedExplorerMask:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'mask': ('MASK',), 'noise': ('NOISE',), 'seed_prompt': ('STRING', {'multiline': True, 'dynamicPrompts': False, 'pysssss.autocomplete': False}), 'enable_additional': ('BOOLEAN', {'default': True, 'label_on': 'true', 'label_off': 'false'}), 'additional_seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615}), 'additional_strength': ('FLOAT', {'default': 0.0, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'noise_mode': (['GPU(=A1111)', 'CPU'],)}}
    RETURN_TYPES = ('NOISE',)
    FUNCTION = 'doit'
    CATEGORY = 'InspirePack/Regional'

    def doit(self, mask, noise, seed_prompt, enable_additional, additional_seed, additional_strength, noise_mode):
        device = comfy.model_management.get_torch_device()
        noise_device = 'cpu' if noise_mode == 'CPU' else device
        noise = noise.to(device)
        mask = mask.to(device)
        if len(mask.shape) == 2:
            mask = mask.unsqueeze(0)
        mask = torch.nn.functional.interpolate(mask.reshape((-1, 1, mask.shape[-2], mask.shape[-1])), size=(noise.shape[2], noise.shape[3]), mode='bilinear').squeeze(0)
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
        noise = noise.cpu()
        mask.cpu()
        return (noise,)
```