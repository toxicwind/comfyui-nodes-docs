# Documentation
- Class name: DPJinja
- Category: Prompt Generation
- Output node: False
- Repo Ref: https://github.com/adieyal/comfyui-dynamicprompts.git

DPJinja nodes are designed to generate tips using the syntax of the Jinja template. Using JinjaGenerator to create a set of tips based on providing text and template configurations, it provides a flexible approach to generating dynamic tips tailored to specific needs.

# Input types
## Required
- text
    - The " text " parameter is the source material from which the Jinja template will generate the hint. It is essential because it directly affects the content and diversity in which the reminder is generated.
    - Comfy dtype: "str"
    - Python dtype: str

# Output types
- prompts
    - The " propts " output is a list of tips generated from input text and the Jinja template. It represents the main result of the node function and contains the dynamic properties of the reminder generation process.
    - Comfy dtype: COMBO["str"]
    - Python dtype: List[str]

# Usage tips
- Infra type: CPU

# Source code
```
class DPJinja(DPGeneratorNode):

    def generate_prompt(self, text):
        prompt_generator = JinjaGenerator()
        all_prompts = prompt_generator.generate(text, 1) or ['']
        return str(all_prompts[0])
```