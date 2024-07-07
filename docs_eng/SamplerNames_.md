# Documentation
- Class name: CreateSampler_names
- Category: ♾️Mixlab/Utils
- Output node: False
- Repo Ref: https://github.com/shadowcz007/comfyui-mixlab-nodes.git

The node simplifys the process of generating a list of sampler names that can be used in various sample applications. It emphasizes the role of nodes in preparing and cleaning inputs to extract valid sampler names, ensuring that the output is a clean and usable collection of identifiers.

# Input types
## Required
- sampler_names
    - This parameter is essential because it provides the original text from which the name of the sampler will be extracted. It has a significant impact on node implementation, as the quality and format of the input text directly affects the accuracy and utility of the name of the sampler generated.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- sampler_names
    - Output represents a list of valid sampler names that are refined to remove all unnecessary information. This list is essential to the downstream process that relies on the correct sampler identifiers to properly run.
    - Comfy dtype: LIST
    - Python dtype: List[str]

# Usage tips
- Infra type: CPU

# Source code
```
class CreateSampler_names:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'sampler_names': ('STRING', {'multiline': True, 'default': '\n'.join(comfy.samplers.KSampler.SAMPLERS), 'dynamicPrompts': False})}}
    RETURN_TYPES = (any_type,)
    RETURN_NAMES = ('sampler_names',)
    INPUT_IS_LIST = False
    OUTPUT_IS_LIST = (True,)
    FUNCTION = 'run'
    CATEGORY = '♾️Mixlab/Utils'

    def run(self, sampler_names):
        sampler_names = sampler_names.split('\n')
        sampler_names = [name for name in sampler_names if name.strip()]
        return (sampler_names,)
```