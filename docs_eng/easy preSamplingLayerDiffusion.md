# Documentation
- Class name: layerDiffusionSettings
- Category: EasyUse/PreSampling
- Output node: True
- Repo Ref: https://github.com/yolain/ComfyUI-Easy-Use.git

The node is used for custom layer spreading settings in neural network waterlines to enable users to define methods of inter-layer interaction and parameters that influence the generation process.

# Input types
## Required
- pipe
    - The `pipe' parameter, as the main input, transmits the necessary data and settings through nodes. It is essential for the proper operation of nodes to ensure that follow-up operations are carried out in the correct context.
    - Comfy dtype: PIPE_LINE
    - Python dtype: Dict
- method
    - The'method' parameter determines how the layer spreads, which is the core of node operations. It determines how the different layers of the model interact and contribute to the final output.
    - Comfy dtype: COMBO[LayerMethod]
    - Python dtype: Enum[LayerMethod]
- weight
    - The 'weight' parameter adjusts the impact of the layer diffusion process. It plays an important role in fine-tuning the balance of contributions generated from different layers.
    - Comfy dtype: FLOAT
    - Python dtype: float
- steps
    - The `steps' parameter defines the number of overlaps to be experienced by the stratum diffusion process. It is critical in terms of the depth and particle size of interactions between the control layers.
    - Comfy dtype: INT
    - Python dtype: int
- cfg
    - The `cfg' parameter sets the configuration value of the layer diffusion process, which is essential for adjusting the behaviour of the model and achieving the desired results.
    - Comfy dtype: FLOAT
    - Python dtype: float
- sampler_name
    - The `sampler_name' parameter specifies the sampling methods to be used in layer diffusion, which is essential for the diversity and quality of the results generated.
    - Comfy dtype: COMBO[comfy.samplers.KSampler.SAMPLERS]
    - Python dtype: Enum[comfy.samplers.KSampler.SAMPLERS]
- scheduler
    - The `scheduler' parameters define the dispatch strategy of the layer-diffusion process, which is essential for managing computing resources and achieving efficient implementation.
    - Comfy dtype: COMBO[comfy.samplers.KSampler.SCHEDULERS]
    - Python dtype: Enum[comfy.samplers.KSampler.SCHEDULERS]
- denoise
    - The level of noise reduction applied during the spreading of the `denoise' parameter. It plays an important role in the quality of the final output by influencing the clarity and detail of the content generated.
    - Comfy dtype: FLOAT
    - Python dtype: float
- seed
    - The `seed' parameter introduces randomity in layer diffusion. It is important to ensure that results are not duplicated and provide multiple possible outcomes.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- image
    - The `image' parameter provides visual input into the stratum diffusion process. It is important in determining the content and context in which the output is generated.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image or np.ndarray
- blended_image
    - The `blended_image' parameter is used to mix different layers or elements into the final output. It helps to generate the complexity and richness of vision.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image or np.ndarray
- mask
    - The `mask' parameter is used to define the image range that should be retained or operated during layer diffusion. It is essential for restoration and selective editing tasks.
    - Comfy dtype: MASK
    - Python dtype: PIL.Image or np.ndarray
- prompt
    - The `prompt' parameter provides text guidance for layer diffusion processes, influencing the thematic direction and style of content generation.
    - Comfy dtype: PROMPT
    - Python dtype: str
- extra_pnginfo
    - The `extra_pnginfo' parameter contains additional information relevant to the image that can be used to refine the layer diffusion process and achieve more accurate results.
    - Comfy dtype: EXTRA_PNGINFO
    - Python dtype: str
- my_unique_id
    - The `my_unique_id' parameter is used as the sole identity for tracking and management proliferation processes to ensure the traceability and personalization of results.
    - Comfy dtype: UNIQUE_ID
    - Python dtype: str

# Output types
- pipe
    - The `pipe' output is an updated version of the input that contains the results of the layer diffusion process and the adjusted settings for further streaming operations.
    - Comfy dtype: PIPE_LINE
    - Python dtype: Dict

# Usage tips
- Infra type: CPU

# Source code
```
class layerDiffusionSettings:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'pipe': ('PIPE_LINE',), 'method': ([LayerMethod.FG_ONLY_ATTN.value, LayerMethod.FG_ONLY_CONV.value, LayerMethod.EVERYTHING.value, LayerMethod.FG_TO_BLEND.value, LayerMethod.BG_TO_BLEND.value],), 'weight': ('FLOAT', {'default': 1.0, 'min': -1, 'max': 3, 'step': 0.05}), 'steps': ('INT', {'default': 20, 'min': 1, 'max': 10000}), 'cfg': ('FLOAT', {'default': 8.0, 'min': 0.0, 'max': 100.0}), 'sampler_name': (comfy.samplers.KSampler.SAMPLERS, {'default': 'euler'}), 'scheduler': (comfy.samplers.KSampler.SCHEDULERS, {'default': 'normal'}), 'denoise': ('FLOAT', {'default': 1.0, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'seed': ('INT', {'default': 0, 'min': 0, 'max': MAX_SEED_NUM})}, 'optional': {'image': ('IMAGE',), 'blended_image': ('IMAGE',), 'mask': ('MASK',)}, 'hidden': {'prompt': 'PROMPT', 'extra_pnginfo': 'EXTRA_PNGINFO', 'my_unique_id': 'UNIQUE_ID'}}
    RETURN_TYPES = ('PIPE_LINE',)
    RETURN_NAMES = ('pipe',)
    OUTPUT_NODE = True
    FUNCTION = 'settings'
    CATEGORY = 'EasyUse/PreSampling'

    def get_layer_diffusion_method(self, method, has_blend_latent):
        method = LayerMethod(method)
        if has_blend_latent:
            if method == LayerMethod.BG_TO_BLEND:
                method = LayerMethod.BG_BLEND_TO_FG
            elif method == LayerMethod.FG_TO_BLEND:
                method = LayerMethod.FG_BLEND_TO_BG
        return method

    def settings(self, pipe, method, weight, steps, cfg, sampler_name, scheduler, denoise, seed, image=None, blended_image=None, mask=None, prompt=None, extra_pnginfo=None, my_unique_id=None):
        blend_samples = pipe['blend_samples'] if 'blend_samples' in pipe else None
        vae = pipe['vae']
        batch_size = pipe['loader_settings']['batch_size'] if 'batch_size' in pipe['loader_settings'] else 1
        method = self.get_layer_diffusion_method(method, blend_samples is not None or blended_image is not None)
        if image is not None or 'image' in pipe:
            image = image if image is not None else pipe['image']
            if mask is not None:
                print('inpaint')
                (samples,) = VAEEncodeForInpaint().encode(vae, image, mask)
            else:
                samples = {'samples': vae.encode(image[:, :, :, :3])}
            samples = RepeatLatentBatch().repeat(samples, batch_size)[0]
            images = image
        elif 'samp_images' in pipe:
            samples = {'samples': vae.encode(pipe['samp_images'][:, :, :, :3])}
            samples = RepeatLatentBatch().repeat(samples, batch_size)[0]
            images = pipe['samp_images']
        else:
            if method not in [LayerMethod.FG_ONLY_ATTN, LayerMethod.FG_ONLY_CONV, LayerMethod.EVERYTHING]:
                raise Exception('image is missing')
            samples = pipe['samples']
            images = pipe['images']
        if method in [LayerMethod.BG_BLEND_TO_FG, LayerMethod.FG_BLEND_TO_BG]:
            if blended_image is None and blend_samples is None:
                raise Exception('blended_image is missing')
            elif blended_image is not None:
                blend_samples = {'samples': vae.encode(blended_image[:, :, :, :3])}
                blend_samples = RepeatLatentBatch().repeat(blend_samples, batch_size)[0]
        new_pipe = {'model': pipe['model'], 'positive': pipe['positive'], 'negative': pipe['negative'], 'vae': pipe['vae'], 'clip': pipe['clip'], 'samples': samples, 'blend_samples': blend_samples, 'images': images, 'seed': seed, 'loader_settings': {**pipe['loader_settings'], 'steps': steps, 'cfg': cfg, 'sampler_name': sampler_name, 'scheduler': scheduler, 'denoise': denoise, 'add_noise': 'enabled', 'layer_diffusion_method': method, 'layer_diffusion_weight': weight}}
        del pipe
        return {'ui': {'value': [seed]}, 'result': (new_pipe,)}
```