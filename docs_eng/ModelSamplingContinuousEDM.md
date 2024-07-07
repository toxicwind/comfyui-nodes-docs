# Documentation
- Class name: ModelSamplingContinuousEDM
- Category: sampling
- Output node: False
- Repo Ref: https://github.com/comfyanonymous/ComfyUI

ModelSamplingContinuousEDM is a PyTorch module designed to facilitate sampling in continuous energy distance modelling (EDM). It encapsulates the logic of setting and managing sigma values, which are essential for spreading the process. The node is designed to provide a structured approach to sampling parameters to ensure smooth and efficient sampling processes.

# Input types
## Required
- sigma_min
    - The Sigma minimum defines the lower limit of the sigma value used in the sampling process. It is a key parameter that affects the spread rate and the quality of the sample generated. A properly selected sigma_min ensures a balance between the speed of the sampling and the validity of the result.
    - Comfy dtype: float
    - Python dtype: float
- sigma_max
    - The Sigma maximum value sets a ceiling for the sigma value during the sampling period. It is a key parameter that determines the scale of the diffusion process. A high sigma_max value can produce a more diverse sample, but may require more calculations, while a lower value accelerates the process, but may result in less variability.
    - Comfy dtype: float
    - Python dtype: float
- sigma_data
    - The Sigma data represents the level of noise assumed in the data. It is an important parameter that affects the initial conditions of the sampling process. The correct set-up of sigma_data is essential to align model assumptions with actual data characteristics, thus obtaining more accurate and reliable sampling results.
    - Comfy dtype: float
    - Python dtype: float
## Optional
- model_config
    - Model configuration provides the necessary settings for the sampling process. It is a dictionary that contains parameters such as'sigma_min','sigma_max' and'sigma_data', which define the scope and initial values of sigma. This parameter is essential for initializing the sampling parameters and adjusting the sampling behaviour to the specific requirements of a particular model.
    - Comfy dtype: Optional[Dict[str, Any]]
    - Python dtype: Optional[Dict[str, Any]]

# Output types
- sigmas
    - The sigmas output is a volume containing a series of sigma values from the logarithmic interval between sigma_min and sigma_max. These values are used throughout the sampling process to control proliferation steps. The sigmas mass is an essential component of the sampling strategy, enabling the model to produce a series of samples that are gradually fine-tuned to the target distribution.
    - Comfy dtype: torch.Tensor
    - Python dtype: torch.Tensor
- log_sigmas
    - The log_sigmas output is a volume that represents the natural logarithm of the sigmas. It is used to calculate efficiency during the sampling process, especially when processing index functions. The log_sigmas stretch allows faster calculations, which are an important part of optimizing the sampling process.
    - Comfy dtype: torch.Tensor
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: GPU

# Source code
```
class ModelSamplingContinuousEDM(torch.nn.Module):

    def __init__(self, model_config=None):
        super().__init__()
        if model_config is not None:
            sampling_settings = model_config.sampling_settings
        else:
            sampling_settings = {}
        sigma_min = sampling_settings.get('sigma_min', 0.002)
        sigma_max = sampling_settings.get('sigma_max', 120.0)
        sigma_data = sampling_settings.get('sigma_data', 1.0)
        self.set_parameters(sigma_min, sigma_max, sigma_data)

    def set_parameters(self, sigma_min, sigma_max, sigma_data):
        self.sigma_data = sigma_data
        sigmas = torch.linspace(math.log(sigma_min), math.log(sigma_max), 1000).exp()
        self.register_buffer('sigmas', sigmas)
        self.register_buffer('log_sigmas', sigmas.log())

    @property
    def sigma_min(self):
        return self.sigmas[0]

    @property
    def sigma_max(self):
        return self.sigmas[-1]

    def timestep(self, sigma):
        return 0.25 * sigma.log()

    def sigma(self, timestep):
        return (timestep / 0.25).exp()

    def percent_to_sigma(self, percent):
        if percent <= 0.0:
            return 999999999.9
        if percent >= 1.0:
            return 0.0
        percent = 1.0 - percent
        log_sigma_min = math.log(self.sigma_min)
        return math.exp((math.log(self.sigma_max) - log_sigma_min) * percent + log_sigma_min)
```