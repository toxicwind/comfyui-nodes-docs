# Documentation
- Class name: CreateMagicMask
- Category: KJNodes/masking/generate
- Output node: False
- Repo Ref: https://github.com/kijai/ComfyUI-KJNodes.git

The CreateMagicmask node is designed to generate a mask with varying degrees of complexity and detail. It uses the principles of programification to create visually attractive patterns that can be used for a wide range of applications from visual effects to artistic works. The node operates using a set of parameters that define the characteristics that generate the mask, such as frame size, transition, depth, distortion, seeds and frame size. The result is a dynamic, custom-made mask that can be reversed to produce multiple effects.

# Input types
## Required
- frames
    - The 'frames' parameter determines the total number of frames generated for the mask sequence. It is a key factor in defining the length and complexity of the animation. The larger the frame number, the smoother the transition, the more complex the pattern, but it also increases the calculation load.
    - Comfy dtype: INT
    - Python dtype: int
- transitions
    - The `transitions' parameter specifies the number of transitions within the mask sequence. Each transition introduces a pattern change that helps the overall visual dynamic. It affects the diversity and speed of the mask's appearance over time.
    - Comfy dtype: INT
    - Python dtype: int
- depth
    - The `depth' parameter controls the level of detail that generates the mask by specifying the number of variations that should be applied to the base coordinates. Greater depth adds to the complexity of the pattern and creates more embedded and complex structures.
    - Comfy dtype: INT
    - Python dtype: int
- distortion
    - The `distortion' parameter affects the irregularity of the masked pattern. It introduces variability to the shape and form generated, allowing for a wide range of visual effects. Higher distortions can lead to more abstract and unpredictable patterns.
    - Comfy dtype: FLOAT
    - Python dtype: float
- seed
    - The `seed' parameter is used to initialize the random number generator to ensure that the masking process is repeated. When using the same settings to rerun nodes, it is essential to obtain a consistent result.
    - Comfy dtype: INT
    - Python dtype: int
- frame_width
    - The `frame_width' parameter defines the width of each frame in the mask sequence. It plays an important role in determining the resolution and size of the visual output. A larger frame width can accommodate more detail, but may require more memory and processing capability.
    - Comfy dtype: INT
    - Python dtype: int
- frame_height
    - The 'frame_height' parameter sets the height of each frame in the mask sequence, complements the frame_width by creating the overall size of the visual canvas. It is a key factor in the presentation and frame generation content.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- mask
    - The'mask'output provides a frame stacking of the generation mask sequence, each of which represents a phase of the mask's evolution. It is a key component that is further processed or directly used in visual applications.
    - Comfy dtype: TORCH_TENSOR
    - Python dtype: torch.Tensor
- mask_inverted
    - The'mask_inverted'output shows the reversal of the creation of the mask sequence and provides an alternative visual effect that can be used to create comparisons or highlight different aspects of the content.
    - Comfy dtype: TORCH_TENSOR
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class CreateMagicMask:
    RETURN_TYPES = ('MASK', 'MASK')
    RETURN_NAMES = ('mask', 'mask_inverted')
    FUNCTION = 'createmagicmask'
    CATEGORY = 'KJNodes/masking/generate'

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'frames': ('INT', {'default': 16, 'min': 2, 'max': 4096, 'step': 1}), 'depth': ('INT', {'default': 12, 'min': 1, 'max': 500, 'step': 1}), 'distortion': ('FLOAT', {'default': 1.5, 'min': 0.0, 'max': 100.0, 'step': 0.01}), 'seed': ('INT', {'default': 123, 'min': 0, 'max': 99999999, 'step': 1}), 'transitions': ('INT', {'default': 1, 'min': 1, 'max': 20, 'step': 1}), 'frame_width': ('INT', {'default': 512, 'min': 16, 'max': 4096, 'step': 1}), 'frame_height': ('INT', {'default': 512, 'min': 16, 'max': 4096, 'step': 1})}}

    def createmagicmask(self, frames, transitions, depth, distortion, seed, frame_width, frame_height):
        from .magictex import coordinate_grid, random_transform, magic
        rng = np.random.default_rng(seed)
        out = []
        coords = coordinate_grid((frame_width, frame_height))
        frames_per_transition = frames // transitions
        base_params = {'coords': random_transform(coords, rng), 'depth': depth, 'distortion': distortion}
        for t in range(transitions):
            params1 = base_params.copy()
            params2 = base_params.copy()
            params1['coords'] = random_transform(coords, rng)
            params2['coords'] = random_transform(coords, rng)
            for i in range(frames_per_transition):
                alpha = i / frames_per_transition
                params = params1.copy()
                params['coords'] = (1 - alpha) * params1['coords'] + alpha * params2['coords']
                tex = magic(**params)
                dpi = frame_width / 10
                fig = plt.figure(figsize=(10, 10), dpi=dpi)
                ax = fig.add_subplot(111)
                plt.subplots_adjust(left=0, right=1, bottom=0, top=1)
                ax.get_yaxis().set_ticks([])
                ax.get_xaxis().set_ticks([])
                ax.imshow(tex, aspect='auto')
                fig.canvas.draw()
                img = np.array(fig.canvas.renderer._renderer)
                plt.close(fig)
                pil_img = Image.fromarray(img).convert('L')
                mask = torch.tensor(np.array(pil_img)) / 255.0
                out.append(mask)
        return (torch.stack(out, dim=0), 1.0 - torch.stack(out, dim=0))
```