# Documentation
- Class name: CFGGuider
- Category: sampler
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

The CFGGuider node is designed to guide the sampling process in the generation model by adjusting the conditions and controlling noise predictions. It encapsulates the logic of setting the conditions and configuring the guiding factors, which are essential to guide the model towards the desired results.

# Input types
## Required
- model_patcher
    - The model_patcher parameter is essential for CFGGuider because it provides the model options and functions required for the sampling process. It is responsible for managing the model's state and ensuring that the conditions are correctly applied during the sampling.
    - Comfy dtype: comfy.model_patcher.ModelPatcher
    - Python dtype: comfy.model_patcher.ModelPatcher
## Optional
- positive
    - They play an important role in shaping the final output through the decision-making process of impact models.
    - Comfy dtype: List[comfy.conds.Condition]
    - Python dtype: List[comfy.conds.Condition]
- negative
    - Negative conditions are used to prevent certain features or elements from appearing in the content that is generated. They are essential to refine the output and ensure that it meets the required specifications.
    - Comfy dtype: List[comfy.conds.Condition]
    - Python dtype: List[comfy.conds.Condition]
- cfg
    - The cfg parameter, which represents the guiding factor, is a key component of the CFGGuider. It determines the intensity of the conditions in the sampling process and allows fine-tuning of model behaviour.
    - Comfy dtype: float
    - Python dtype: float

# Output types
- output
    - The output of the CFGGuider node is a volume that represents the potential image of the sample. It is the result of guiding the sampling process and encapsulating the resulting content according to the conditions and settings provided.
    - Comfy dtype: torch.Tensor
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class CFGGuider:

    def __init__(self, model_patcher):
        self.model_patcher = model_patcher
        self.model_options = model_patcher.model_options
        self.original_conds = {}
        self.cfg = 1.0

    def set_conds(self, positive, negative):
        self.inner_set_conds({'positive': positive, 'negative': negative})

    def set_cfg(self, cfg):
        self.cfg = cfg

    def inner_set_conds(self, conds):
        for k in conds:
            self.original_conds[k] = comfy.sampler_helpers.convert_cond(conds[k])

    def __call__(self, *args, **kwargs):
        return self.predict_noise(*args, **kwargs)

    def predict_noise(self, x, timestep, model_options={}, seed=None):
        return sampling_function(self.inner_model, x, timestep, self.conds.get('negative', None), self.conds.get('positive', None), self.cfg, model_options=model_options, seed=seed)

    def inner_sample(self, noise, latent_image, device, sampler, sigmas, denoise_mask, callback, disable_pbar, seed):
        if latent_image is not None and torch.count_nonzero(latent_image) > 0:
            latent_image = self.inner_model.process_latent_in(latent_image)
        self.conds = process_conds(self.inner_model, noise, self.conds, device, latent_image, denoise_mask, seed)
        extra_args = {'model_options': self.model_options, 'seed': seed}
        samples = sampler.sample(self, sigmas, extra_args, callback, noise, latent_image, denoise_mask, disable_pbar)
        return self.inner_model.process_latent_out(samples.to(torch.float32))

    def sample(self, noise, latent_image, sampler, sigmas, denoise_mask=None, callback=None, disable_pbar=False, seed=None):
        if sigmas.shape[-1] == 0:
            return latent_image
        self.conds = {}
        for k in self.original_conds:
            self.conds[k] = list(map(lambda a: a.copy(), self.original_conds[k]))
        (self.inner_model, self.conds, self.loaded_models) = comfy.sampler_helpers.prepare_sampling(self.model_patcher, noise.shape, self.conds)
        device = self.model_patcher.load_device
        if denoise_mask is not None:
            denoise_mask = comfy.sampler_helpers.prepare_mask(denoise_mask, noise.shape, device)
        noise = noise.to(device)
        latent_image = latent_image.to(device)
        sigmas = sigmas.to(device)
        output = self.inner_sample(noise, latent_image, device, sampler, sigmas, denoise_mask, callback, disable_pbar, seed)
        comfy.sampler_helpers.cleanup_models(self.conds, self.loaded_models)
        del self.inner_model
        del self.conds
        del self.loaded_models
        return output
```