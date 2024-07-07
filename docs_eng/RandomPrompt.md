# Documentation
- Class name: RandomPrompt
- Category: ♾️Mixlab/Prompt
- Output node: True
- Repo Ref: https://github.com/shadowcz007/comfyui-mixlab-nodes.git

The RandomPrompt node is designed to generate a diversity of hints by combining variable and non-variable text elements. It operates by dividing the tips provided into separate words or phrases, and reassembling them with various combinations. The node also provides a function that can be derived from a random sample of parts of the specified maximum count, or returns all hints. The process is designed to create extensive text input for further processing or analysis.

# Input types
## Required
- max_count
    - The parameter'max_count'determines the maximum number of hints to be generated or sampled. It plays a key role in controlling the output size and ensuring that nodes are executed at the required level of diversity, while avoiding crushing downstream processes.
    - Comfy dtype: INT
    - Python dtype: int
- mutable_prompt
    - Parameter'mutable_prompt' is a string that the user can change or combine with other hints during node operations. It is important because it forms a variable basis for generating tips, allowing for a wide range of potential outputs.
    - Comfy dtype: STRING
    - Python dtype: str
- immutable_prompt
    - The parameter 'immutable_prompt' is a fixed string that remains constant during the node execution. As a constant element, it is combined with a variable hint to produce a consistent structure in the final hint concentration.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- random_sample
    - The parameter'random_sample' indicates whether the node should randomly select the subset that generates the hint. When enabled, it introduces the random element for the selection process, which may be useful for some applications that require a diverse but limited set of hints.
    - Comfy dtype: COMBO['enable', 'disable']
    - Python dtype: str
- seed
    - The parameter'seed' is used to initialize the random number generator during random sampling. When providing a given seed value, it ensures the recurrence of the result and allows nodes to achieve consistent results in multiple execution.
    - Comfy dtype: any_type
    - Python dtype: int

# Output types
- prompts
    - Output 'prompts' is a list of text tips generated by a combination of variable and non-variable text elements. It represents the main result of node execution and is important for the application of these tips for further processing or analysis.
    - Comfy dtype: STRING
    - Python dtype: List[str]

# Usage tips
- Infra type: CPU

# Source code
```
class RandomPrompt:
    """
    @crasmethod is a decorator in Python to mark a method as a class method.
    The category approach is related to the category rather than to the example.
    This means that the class approach can be called directly through the class instead of creating an example of the class first.
    """

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'max_count': ('INT', {'default': 9, 'min': 1, 'max': 1000}), 'mutable_prompt': ('STRING', {'multiline': True, 'default': default_prompt1}), 'immutable_prompt': ('STRING', {'multiline': True, 'default': 'sticker, Cartoon, ``'}), 'random_sample': (['enable', 'disable'],)}, 'optional': {'seed': (any_type, {'default': 0, 'min': 0, 'max': 18446744073709551615})}}
    RETURN_TYPES = ('STRING',)
    FUNCTION = 'run'
    CATEGORY = '♾️Mixlab/Prompt'
    OUTPUT_IS_LIST = (True,)
    OUTPUT_NODE = True

    def run(self, max_count, mutable_prompt, immutable_prompt, random_sample, seed=0):
        words1 = mutable_prompt.split('\n')
        words2 = immutable_prompt.split('\n')
        pbar = comfy.utils.ProgressBar(len(words1) * len(words2))
        prompts = []
        for w1 in words1:
            w1 = w1.strip()
            for w2 in words2:
                w2 = w2.strip()
                if '``' not in w2:
                    if w2 == '':
                        w2 = '``'
                    else:
                        w2 = w2 + ',``'
                if w1 != '' and w2 != '':
                    prompts.append(w2.replace('``', w1))
                pbar.update(1)
        if len(prompts) == 0:
            prompts.append(immutable_prompt)
        if random_sample == 'enable':
            prompts = random.sample(prompts, min(max_count, len(prompts)))
        else:
            prompts = prompts[:min(max_count, len(prompts))]
        prompts = [elem.strip() for elem in prompts if elem.strip()]
        return {'ui': {'prompts': prompts}, 'result': (prompts,)}
```