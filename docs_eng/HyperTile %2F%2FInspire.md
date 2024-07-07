# Documentation
- Class name: HyperTileInspire
- Category: InspirePack/__for_testing
- Output node: False
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Inspire-Pack.git

The HyperTileInspire node is designed to enhance the functionality of the model by dynamically fine-tuning the features of the given model. It changes the spatial dimensions of model input by introducing a random but systematic approach, which is particularly useful in optimizing the performance of the model on tasks that benefit from different input resolutions. The node is designed to provide a flexible and efficient way to explore different flattening strategies without the need for manual intervention or predefined configurations.

# Input types
## Required
- model
    - Model parameters are essential because they represent a machine-learning model that will be enhanced by the laying process. The ability of nodes to modify models to enter them directly affects the way model processing and learning data can lead to performance enhancement in certain tasks.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module
- tile_size
    - The tile_size parameter determines the base size on which the model input will be divided. It plays a key role in the stubble process, as it sets the initial scale for the division of the input space. This parameter allows customizing the particle size of the stubble, which can be adjusted to the specific needs of different tasks.
    - Comfy dtype: INT
    - Python dtype: int
- swap_size
    - The swap_size parameter specifies the maximum number of divides that can be used to adjust the size of the flattening. It is an important factor in the smoothing randomization process, as it controls the possible size of the flattening. This adds to the variability of the operation of the nodes, which may be useful for tasks that require diversified input configurations.
    - Comfy dtype: INT
    - Python dtype: int
- max_depth
    - The max_depth parameter specifies the maximum number of times that can be applied backwards. It is a key factor in controlling the complexity of the flattening operation. By adjusting the parameter, the user can manage the trade-off between the level of detail to be levelled and the computational resources required to perform the operation.
    - Comfy dtype: INT
    - Python dtype: int
- scale_depth
    - The scale_depth parameter is a boolean symbol that, when set to True, allows tile sizes to be scalded according to the depth of the laying process. This can lead to a more detailed and self-adapted flattening strategy that allows models to better adapt to different levels of detail in the input data.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- seed
    - Seed parameters are used to initialize random number generators to ensure that the flattening process is recreated. This is particularly important in scenarios where nodes are expected to achieve consistent results in multiple operations. By providing seeds, users can control randomity in the flats to achieve specific results.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- model
    - The output model is an enhanced version of the input model, and the attention mechanism is modified to include the dynamic flattening of the input. This allows the model to process information at different scales, which is essential for some types of analysis or feature extraction.
    - Comfy dtype: MODEL
    - Python dtype: torch.nn.Module

# Usage tips
- Infra type: GPU

# Source code
```
class HyperTileInspire:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'model': ('MODEL',), 'tile_size': ('INT', {'default': 256, 'min': 1, 'max': 2048}), 'swap_size': ('INT', {'default': 2, 'min': 1, 'max': 128}), 'max_depth': ('INT', {'default': 0, 'min': 0, 'max': 10}), 'scale_depth': ('BOOLEAN', {'default': False}), 'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615})}}
    RETURN_TYPES = ('MODEL',)
    FUNCTION = 'patch'
    CATEGORY = 'InspirePack/__for_testing'

    def patch(self, model, tile_size, swap_size, max_depth, scale_depth, seed):
        latent_tile_size = max(32, tile_size) // 8
        temp = None
        rand_obj = random.Random()
        rand_obj.seed(seed)

        def hypertile_in(q, k, v, extra_options):
            nonlocal temp
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
                nh = random_divisor(h, latent_tile_size * factor, swap_size, rand_obj)
                nw = random_divisor(w, latent_tile_size * factor, swap_size, rand_obj)
                print(f'factor: {factor} <--- params.depth: {apply_to.index(model_chans)} / scale_depth: {scale_depth} / latent_tile_size={latent_tile_size}')
                if nh * nw > 1:
                    q = rearrange(q, 'b (nh h nw w) c -> (b nh nw) (h w) c', h=h // nh, w=w // nw, nh=nh, nw=nw)
                    temp = (nh, nw, h, w)
                print(f'q={q} / k={k} / v={v}')
                return (q, k, v)
            return (q, k, v)

        def hypertile_out(out, extra_options):
            nonlocal temp
            if temp is not None:
                (nh, nw, h, w) = temp
                temp = None
                out = rearrange(out, '(b nh nw) hw c -> b nh nw hw c', nh=nh, nw=nw)
                out = rearrange(out, 'b nh nw (h w) c -> b (nh h nw w) c', h=h // nh, w=w // nw)
            return out
        m = model.clone()
        m.set_model_attn1_patch(hypertile_in)
        m.set_model_attn1_output_patch(hypertile_out)
        return (m,)
```