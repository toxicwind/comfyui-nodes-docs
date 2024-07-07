# Documentation
- Class name: TiledDiffusion
- Category: _for_testing
- Output node: False
- Repo Ref: https://github.com/shiimizu/ComfyUI-TiledDiffusion

The TiledDiffusion class serves as a framework for applying proliferation models in a levelled manner to enhance processing by dividing large images into smaller segments, which improves computational efficiency and allows for more finer particle size control of the diffusion process.

# Input types
## Required
- model
    - Model parameters are essential because it defines the diffusion model to be used within the node. It is the core component that controls the behaviour and output of the TiledDiffusion process.
    - Comfy dtype: MODEL
    - Python dtype: comfy.model_patcher.ModelPatcher
- method
    - The methodological parameters determine the specific diffusion technology to be used, affecting the overall performance and quality of the output. It is a key factor in adapting the node function to the desired outcome.
    - Comfy dtype: COMBO[('MultiDiffusion', 'Mixture of Diffusers')]
    - Python dtype: str
- tile_width
    - The tile_width parameter determines the width of each tile in the sheeting process, directly affecting the particle size of the diffuse application. It is essential to optimize the balance between processing time and outcome detail.
    - Comfy dtype: INT
    - Python dtype: int
- tile_height
    - The tile_height parameter sets the height of each tile and, together with the tile_width, determines the levelling strategy. This parameter is essential for managing the calculation of loads and ensuring the efficiency of the diffusion process.
    - Comfy dtype: INT
    - Python dtype: int
- tile_overlap
    - The tile_overlap parameter defines overlap between adjacent tiles and ensures seamless integration of diffuse effects across the image. It plays a vital role in maintaining the consistency and quality of the final output.
    - Comfy dtype: INT
    - Python dtype: int
- tile_batch_size
    - The tile_batch_size parameter specifies the number of tiles per batch, which is essential for managing memory use and accelerating the diffusion process. It directly affects the calculation of the trade-off between resources and processing speed.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- model
    - The output model is a modified version of the input model, which is now equipped with a layered diffusion function. It represents the outcome of node processing and encapsulates the enhanced ability to process large images using diffuse methods.
    - Comfy dtype: MODEL
    - Python dtype: comfy.model_patcher.ModelPatcher

# Usage tips
- Infra type: GPU

# Source code
```
class TiledDiffusion:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'method': (['MultiDiffusion', 'Mixture of Diffusers'], {'default': 'Mixture of Diffusers'}), 'tile_width': ('INT', {'default': 96 * opt_f, 'min': 16, 'max': MAX_RESOLUTION, 'step': 16}), 'tile_height': ('INT', {'default': 96 * opt_f, 'min': 16, 'max': MAX_RESOLUTION, 'step': 16}), 'tile_overlap': ('INT', {'default': 8 * opt_f, 'min': 0, 'max': 256 * opt_f, 'step': 4 * opt_f}), 'tile_batch_size': ('INT', {'default': 4, 'min': 1, 'max': MAX_RESOLUTION, 'step': 1})}}
    RETURN_TYPES = ('MODEL',)
    FUNCTION = 'apply'
    CATEGORY = '_for_testing'

    def apply(self, model: ModelPatcher, method, tile_width, tile_height, tile_overlap, tile_batch_size):
        if method == 'Mixture of Diffusers':
            implement = MixtureOfDiffusers()
        else:
            implement = MultiDiffusion()
        implement.tile_width = tile_width // opt_f
        implement.tile_height = tile_height // opt_f
        implement.tile_overlap = tile_overlap // opt_f
        implement.tile_batch_size = tile_batch_size
        model = model.clone()
        model.set_model_unet_function_wrapper(implement)
        model.model_options['tiled_diffusion'] = True
        return (model,)
```