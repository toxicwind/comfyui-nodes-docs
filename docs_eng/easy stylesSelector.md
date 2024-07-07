# Documentation
- Class name: stylesPromptSelector
- Category: EasyUse/Prompt
- Output node: True
- Repo Ref: https://github.com/yolain/ComfyUI-Easy-Use.git

The node manages the selection and application of styled tips in the abstract to guide the generation process and to ensure thematic consistency and style diversity, rather than specific realization details.

# Input types
## Required
- styles
    - The Style parameter is essential because it determines the style direction of the output. It allows nodes to be selected from predefined styles, thus affecting the overall aesthetic and thematic outcomes that generate content.
    - Comfy dtype: COMBO[fooocus_styles, bar_styles, baz_styles]
    - Python dtype: Union[str, List[str]]
## Optional
- positive
    - The " positive " parameter guides the node to include certain elements or themes in the output. It refines the production process by focusing on the desired aspects, increasing the relevance and attractiveness of the end result.
    - Comfy dtype: STRING
    - Python dtype: Optional[str]
- negative
    - The “negative” parameter is essential in defining what should be excluded from the output. It helps nodes avoid undesirable elements or themes and ensures that the end result is consistent with the desired vision.
    - Comfy dtype: STRING
    - Python dtype: Optional[str]
- prompt
    - The " hint " parameter is a hidden input that provides additional context to the node when it exists in the input section of "my_unique_id ". It can contain specific commands or preferences, customizing output further to the user's needs.
    - Comfy dtype: PROMPT
    - Python dtype: Dict[str, Any]
- extra_pnginfo
    - When providing additional _pnginfo parameters, it can provide additional information that nodes can use to improve the details and quality of output. It plays a role in refining the generation process to meet specific user needs.
    - Comfy dtype: EXTRA_PNGINFO
    - Python dtype: Any
- my_unique_id
    - The "my_unique_id " parameter is a hidden input for the sole identification request. It enables nodes to manage and relate to the input requested by a specific user, ensuring personalization and targeted output generation.
    - Comfy dtype: UNIQUE_ID
    - Python dtype: Any

# Output types
- positive
    - The " positive " output represents a styled hint that is customised and selected according to input criteria. It is a key component of the final output, ensuring that the content generated is consistent with the desired theme and elements.
    - Comfy dtype: STRING
    - Python dtype: str
- negative
    - The “negative” output captures elements or themes that are explicitly excluded from the generation process. This ensures that the end result is free from undesirable interference and that user specifications are strictly followed.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class stylesPromptSelector:

    @classmethod
    def INPUT_TYPES(s):
        styles = ['fooocus_styles']
        styles_dir = FOOOCUS_STYLES_DIR
        for file_name in os.listdir(styles_dir):
            file = os.path.join(styles_dir, file_name)
            if os.path.isfile(file) and file_name.endswith('.json') and ('styles' in file_name.split('.')[0]):
                styles.append(file_name.split('.')[0])
        return {'required': {'styles': (styles, {'default': 'fooocus_styles'})}, 'optional': {'positive': ('STRING', {'forceInput': True}), 'negative': ('STRING', {'forceInput': True})}, 'hidden': {'prompt': 'PROMPT', 'extra_pnginfo': 'EXTRA_PNGINFO', 'my_unique_id': 'UNIQUE_ID'}}
    RETURN_TYPES = ('STRING', 'STRING')
    RETURN_NAMES = ('positive', 'negative')
    CATEGORY = 'EasyUse/Prompt'
    FUNCTION = 'run'
    OUTPUT_NODE = True

    def replace_repeat(self, prompt):
        prompt = prompt.replace('，', ',')
        arr = prompt.split(',')
        if len(arr) != len(set(arr)):
            all_weight_prompt = re.findall(re.compile('[(](.*?)[)]', re.S), prompt)
            if len(all_weight_prompt) > 0:
                return prompt
            else:
                for i in range(len(arr)):
                    arr[i] = arr[i].strip()
                arr = list(set(arr))
                return ', '.join(arr)
        else:
            return prompt

    def run(self, styles, positive='', negative='', prompt=None, extra_pnginfo=None, my_unique_id=None):
        values = []
        all_styles = {}
        (positive_prompt, negative_prompt) = ('', negative)
        if styles == 'fooocus_styles':
            file = os.path.join(RESOURCES_DIR, styles + '.json')
        else:
            file = os.path.join(FOOOCUS_STYLES_DIR, styles + '.json')
        f = open(file, 'r', encoding='utf-8')
        data = json.load(f)
        f.close()
        for d in data:
            all_styles[d['name']] = d
        if my_unique_id in prompt:
            if prompt[my_unique_id]['inputs']['select_styles']:
                values = prompt[my_unique_id]['inputs']['select_styles'].split(',')
        has_prompt = False
        if len(values) == 0:
            return (positive, negative)
        for (index, val) in enumerate(values):
            if 'prompt' in all_styles[val]:
                if '{prompt}' in all_styles[val]['prompt'] and has_prompt == False:
                    positive_prompt = all_styles[val]['prompt'].format(prompt=positive)
                    has_prompt = True
                else:
                    positive_prompt += ', ' + all_styles[val]['prompt'].replace(', {prompt}', '').replace('{prompt}', '')
            if 'negative_prompt' in all_styles[val]:
                negative_prompt += ', ' + all_styles[val]['negative_prompt'] if negative_prompt else all_styles[val]['negative_prompt']
        if has_prompt == False and positive:
            positive_prompt = positive + ', '
        positive_prompt = self.replace_repeat(positive_prompt) if positive_prompt else ''
        negative_prompt = self.replace_repeat(negative_prompt) if negative_prompt else ''
        return (positive_prompt, negative_prompt)
```