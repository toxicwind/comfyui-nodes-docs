# Documentation
- Class name: HyperTile
- Category: model_patches
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The HyperTile node is designed to modify the behaviour of the model by changing the sheeting of the data entered during dynamic adjustment processing. It does so by achieving a repair mechanism that changes the model’s focus mechanism to deal with the flattening of the specified size. This node applies in particular to optimizing the model’s performance in different data particles without changing the model structure.

# Input types
## Required
- model
    - Model parameters are necessary because they represent the machine learning model that will be repaired. The process of remediating the internal working methods of the model and processing the data in a flat format are essential for certain types of data-processing tasks.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
## Optional
- tile_size
    - The tile_size parameter determines the size of the flat size in which the input data will be divided. It is important for controlling the particle size of the data processing and can significantly influence the efficiency and output quality of the model.
    - Comfy dtype: INT
    - Python dtype: int
- swap_size
    - The swap_size parameter impact model is re-arranged internally. It is a key factor in the optimization process, as it directly affects the ability of the model to process data efficiently.
    - Comfy dtype: INT
    - Python dtype: int
- max_depth
    - The max_depth parameter sets limits on the depth of the flattening process. It is important to control the complexity of the data structure that the model needs to process, to prevent excessive complexity and to maintain performance.
    - Comfy dtype: INT
    - Python dtype: int
- scale_depth
    - This is an important consideration for optimizing the performance of the model for data properties.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- model
    - The output of the HyperTile node is a modified model, which now contains the logic of a focus mechanism to process the flattening of the data. This allows for more efficient processing of the data in different particle sizes.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module

# Usage tips
- Infra type: GPU

# Source code
```
class HyperTile:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'tile_size': ('INT', {'default': 256, 'min': 1, 'max': 2048}), 'swap_size': ('INT', {'default': 2, 'min': 1, 'max': 128}), 'max_depth': ('INT', {'default': 0, 'min': 0, 'max': 10}), 'scale_depth': ('BOOLEAN', {'default': False})}}
    RETURN_TYPES = ('MODEL',)
    FUNCTION = 'patch'
    CATEGORY = 'model_patches'

    def patch(self, model, tile_size, swap_size, max_depth, scale_depth):
        model_channels = model.model.model_config.unet_config['model_channels']
        latent_tile_size = max(32, tile_size) // 8
        self.temp = None

        def hypertile_in(q, k, v, extra_options):
            model_chans = q.shape[-2]
            orig_shape = extra_options['original_shape']
            apply_to = []
            for i in range(max_depth + 1):
                apply_to.append(orig_shape[-2] / 2 ** i * (orig_shape[-1] / 2 ** i))
            if model_chans in apply_to:
                shape = extra_options['original_shape']
                aspect_ratio = shape[-1] / shape[-2]
                hw = q.size(1)
                (h, w) = (round(math.sqrt(hw * aspect_ratio)), round(math.sqrt(hw / aspect_ratio)))
                factor = 2 ** apply_to.index(model_chans) if scale_depth else 1
                nh = random_divisor(h, latent_tile_size * factor, swap_size)
                nw = random_divisor(w, latent_tile_size * factor, swap_size)
                if nh * nw > 1:
                    q = rearrange(q, 'b (nh h nw w) c -> (b nh nw) (h w) c', h=h // nh, w=w // nw, nh=nh, nw=nw)
                    self.temp = (nh, nw, h, w)
                return (q, k, v)
            return (q, k, v)

        def hypertile_out(out, extra_options):
            if self.temp is not None:
                (nh, nw, h, w) = self.temp
                self.temp = None
                out = rearrange(out, '(b nh nw) hw c -> b nh nw hw c', nh=nh, nw=nw)
                out = rearrange(out, 'b nh nw (h w) c -> b (nh h nw w) c', h=h // nh, w=w // nw)
            return out
        m = model.clone()
        m.set_model_attn1_patch(hypertile_in)
        m.set_model_attn1_output_patch(hypertile_out)
        return (m,)
```