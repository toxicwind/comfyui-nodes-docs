# Documentation
- Class name: DPFeelingLucky
- Category: Sampling
- Output node: False
- Repo Ref: https://github.com/adieyal/comfyui-dynamicprompts.git

The node is designed to generate creative and potentially unexpected tips using random seeds and lucky senses. It is designed to introduce variability and innovation into the sampling process and contribute to the diversity of output outcomes.

# Input types
## Required
- text
    - Enter the text as the basis for generating the reminder. It is essential because it provides context and content for the node and directly affects the relevance and creativity of generating the reminder.
    - Comfy dtype: str
    - Python dtype: str
## Optional
- seed
    - Seed parameters are essential to control the randomity in which the tips are generated. It ensures that the same input text produces consistent results when the torrent is fixed, which is very useful for debugging and repossibility.
    - Comfy dtype: int
    - Python dtype: int
- autorefresh
    - Automatically refreshs parameters to determine whether nodes should automatically generate new hints based on changes in the input text. It affects the responsiveness of nodes and the dynamics of the content generation process.
    - Comfy dtype: str
    - Python dtype: str

# Output types
- prompt
    - The output is an generated reminder and the result of node operations. It represents creative and potentially novel content derived from randomity introduced from input text and seeds.
    - Comfy dtype: str
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class DPFeelingLucky(DPAbstractSamplerNode):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._random_generator = RandomPromptGenerator(wildcard_manager=self._wildcard_manager)
        self._prompt_generator = FeelingLuckyGenerator(generator=self._random_generator)

    def get_prompt(self, text: str, seed: int, autorefresh: str) -> tuple[str]:
        """
        Main entrypoint for this node.
        Using the sampling context, generate a new prompt.
        """
        if seed > 0:
            self.context.rand.seed(seed)
        if text.strip() == '':
            return ('',)
        try:
            prompt = self._prompt_generator.generate(text, 1)[0]
            return (str(prompt),)
        except Exception as e:
            logger.exception(e)
            return ('',)

    @property
    def context(self) -> SamplingContext:
        return self._random_generator._context
```