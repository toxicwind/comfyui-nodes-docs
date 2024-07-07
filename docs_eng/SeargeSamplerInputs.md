# Documentation
- Class name: SeargeSamplerInputs
- Category: Searge/_deprecated_/Inputs
- Output node: False
- Repo Ref: https://github.com/jobunk/SeargeSDXL.git

The node class covers the process of retrieval and configuration of samplers and schedulers, which are essential components of the sampling process. It provides a structured approach to selecting and using different sampling strategies and dispatch methods to control output generation. The node ensures that appropriate algorithms are used based on user choices, thus contributing to the generation of high-quality results.

# Input types
## Required
- sampler_name
    - The sampler_name parameter is essential for determining the type of sampling algorithm to be used. It determines the method by which the output is generated, which may significantly affect the quality and diversity of the results. By selecting a given sampler, the user leads the node to execute and shape the overall results of the sampling process.
    - Comfy dtype: COMBO[str]
    - Python dtype: str
- scheduler
    - The Scheduler parameter plays a key role in managing the flow and rhythm of the sampling process. It adjusts the speed of the sample to ensure that the production process is optimized in terms of speed and efficiency.
    - Comfy dtype: COMBO[str]
    - Python dtype: str

# Output types
- sampler_name
    - The sampler_name output represents the selected sampling algorithm based on input. This selection is essential for the sampling process, as it determines the method by which the output is generated and affects the overall quality and characteristics of the result.
    - Comfy dtype: str
    - Python dtype: str
- scheduler
    - Scheduler output indicates a selected scheduler method that will manage the speed and rhythm of sampling operations. This option is essential for balancing the calculation of efficiency and output quality to ensure that the sampling process is both efficient and resource-oriented.
    - Comfy dtype: str
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class SeargeSamplerInputs:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'sampler_name': (comfy.samplers.KSampler.SAMPLERS, {'default': 'ddim'}), 'scheduler': (comfy.samplers.KSampler.SCHEDULERS, {'default': 'ddim_uniform'})}}
    RETURN_TYPES = ('SAMPLER_NAME', 'SCHEDULER_NAME')
    RETURN_NAMES = ('sampler_name', 'scheduler')
    FUNCTION = 'get_value'
    CATEGORY = 'Searge/_deprecated_/Inputs'

    def get_value(self, sampler_name, scheduler):
        return (sampler_name, scheduler)
```