# Documentation
- Class name: WAS_Text_Random_Prompt
- Category: WAS Suite/Text
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Text_Random_Prompt class `random_prompt'method is designed to generate a random texttip based on the given search feed, using a set of default hints if the search torrent is not available. It uses external API to get a list of images associated with the query and returns a random hint associated with a given image in the list.

# Input types
## Required
- search_seed
    - The parameter `search_seed'is used to define the initial query for generating random text tips. It is essential because it directly affects the type of hint generated and the follow-up images retrieved from external API.
    - Comfy dtype: STRING
    - Python dtype: Union[str, None]

# Output types
- prompt
    - The parameter `prompt'represents the output of the `random_prompt'method, a texttip based on random selection of input queries. It is important because it forms the basis for any follow-up or analysis of the resulting tips.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Text_Random_Prompt:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'search_seed': ('STRING', {'multiline': False})}}

    @classmethod
    def IS_CHANGED(cls, **kwargs):
        return float('NaN')
    RETURN_TYPES = (TEXT_TYPE,)
    FUNCTION = 'random_prompt'
    CATEGORY = 'WAS Suite/Text'

    def random_prompt(self, search_seed=None):
        if search_seed in ['', ' ']:
            search_seed = None
        return (self.search_lexica_art(search_seed),)

    def search_lexica_art(self, query=None):
        if not query:
            query = random.choice(['portrait', 'landscape', 'anime', 'superhero', 'animal', 'nature', 'scenery'])
        url = f'https://lexica.art/api/v1/search?q={query}'
        try:
            response = requests.get(url, proxies=config.get_proxies())
            data = response.json()
            images = data.get('images', [])
            if not images:
                return '404 not found error'
            random_image = random.choice(images)
            prompt = random_image.get('prompt')
        except Exception:
            cstr('Unable to establish connection to Lexica API.').error.print()
            prompt = '404 not found error'
        return prompt
```