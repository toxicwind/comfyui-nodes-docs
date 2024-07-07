# Documentation
- Class name: DPRandomGenerator
- Category: Sampling
- Output node: False
- Repo Ref: https://github.com/adieyal/comfyui-dynamicprompts.git

The DPRandomGenerator node is designed to produce multiple outputs based on a set of given rules and variables. By interpreting the command structure and using sampling methods to generate diversified results, it ensures extensive exploration of possible outcomes.

# Input types
## Required
- command
    - The command parameter is essential because it defines the structure and content of the node that will be generated. It is the blueprint for the sampling process and directly affects the diversity and nature of the output.
    - Comfy dtype: Command
    - Python dtype: dynamicprompts.commands.Command
## Optional
- num_prompts
    - Num_prompts parameters specify the maximum number of hints that nodes will generate. It plays an important role in controlling the output range, allowing the output range to be concentrated or extensive depending on the value set.
    - Comfy dtype: int
    - Python dtype: int

# Output types
- prompts
    - The output tips are the result of node execution, reflecting the application of input commands and sampling methods. They represent the diversity and associated results based on the success of the initial input.
    - Comfy dtype: List[SamplingResult]
    - Python dtype: List[dynamicprompts.SamplingResult]

# Usage tips
- Infra type: CPU

# Source code
```
class DPRandomGenerator(DPAbstractSamplerNode):

    @property
    @lru_cache(maxsize=1)
    def context(self) -> SamplingContext:
        return SamplingContext(wildcard_manager=self._wildcard_manager, default_sampling_method=SamplingMethod.RANDOM)
```