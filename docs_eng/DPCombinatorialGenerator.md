# Documentation
- Class name: DPCombinatorialGenerator
- Category: sampling
- Output node: False
- Repo Ref: https://github.com/adieyal/comfyui-dynamicprompts.git

DPCombinarialGenerator node is designed to generate a combination of tips based on the given context. It uses SamplingContext to determine the appropriate method for generating the tips and, if necessary, to ensure a combination approach. This node is essential in a scenario that requires a detailed input combination to allow a thorough sampling.

# Input types
## Required
- wildcard_manager
    - The wildcard manager is essential to handle placeholders in the hint template. It affects how nodes interpret and replace wildcards, and thus directly affects the diversity of processes and output tips.
    - Comfy dtype: WildcardManager
    - Python dtype: WildcardManager
- default_sampling_method
    - The default sampling method determines the method that is used to generate the reminder when no specific method is specified. It is important because it sets the basis for the sampling behaviour of the node and affects the overall strategy of the reminder generation.
    - Comfy dtype: SamplingMethod
    - Python dtype: SamplingMethod

# Output types
- prompts
    - The output tips represent the combinations generated on the basis of input context and sampling methods. They are important because they are the direct result of node operations and contain the essence of the assembly generation process.
    - Comfy dtype: Iterable[str]
    - Python dtype: Iterable[str]

# Usage tips
- Infra type: CPU

# Source code
```
class DPCombinatorialGenerator(DPAbstractSamplerNode):

    @property
    @lru_cache(maxsize=1)
    def context(self) -> SamplingContext:
        return SamplingContext(wildcard_manager=self._wildcard_manager, default_sampling_method=SamplingMethod.COMBINATORIAL)
```