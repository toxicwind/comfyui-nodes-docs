# Documentation
- Class name: DPMagicPrompt
- Category: Sampling
- Output node: False
- Repo Ref: https://github.com/adieyal/comfyui-dynamicprompts.git

DPMagicPrompt is a node designed to generate creativity and context-related tips using random and magic generation techniques. It uses the power of pre-training language models to generate diverse and attractive text content based on the input text and parameters provided.

# Input types
## Required
- text
    - Entering text is the basis for node operations and guides the creation of tips. It is important because it directly affects the context and relevance of the content generated.
    - Comfy dtype: str
    - Python dtype: str
## Optional
- seed
    - Seed parameters are essential to control randomity in the creation of tips and to ensure replicability and consistency between different operations.
    - Comfy dtype: int
    - Python dtype: int
- autorefresh
    - Automatically refreshs parameters to determine whether nodes should generate new tips based on the most recent input text, contributing to the dynamic nature of content creation.
    - Comfy dtype: str
    - Python dtype: str

# Output types
- prompt
    - The output hint is the result of a node operation and contains the generated content that is both creative and relevant to the input text.
    - Comfy dtype: str
    - Python dtype: str

# Usage tips
- Infra type: GPU

# Source code
```
class DPMagicPrompt(DPAbstractSamplerNode):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._random_generator = RandomPromptGenerator(wildcard_manager=self._wildcard_manager)
        self._prompt_generator = MagicPromptGenerator(prompt_generator=self._random_generator)

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