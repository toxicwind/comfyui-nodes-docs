# Documentation
- Class name: CR_SeedToInt
- Category: Comfyroll/Essential/Legacy
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

The CR_SeedToInt node is designed to convert seed objects into integer numbers. It plays a key role in the conversion process, ensuring data integrity and availability. The node abstractes the complexity of seed conversions and provides a simple interface for further data operation and analysis.

# Input types
## Required
- seed
    - The feed parameter is essential to the operation of the node because it is the original input for the node process. It directly influences the output of the node by determining the initial value of the conversion to integer.
    - Comfy dtype: SEED
    - Python dtype: Dict[str, Any]

# Output types
- INT
    - The INT output represents the converted whole value from the input feed. It is important because it is the main result of the node function and can be used for subsequent calculation tasks.
    - Comfy dtype: INT
    - Python dtype: int
- show_help
    - Show_help output provides a URL link to a document for further help. This is useful for users seeking more information about node operations and their context in the wider system.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_SeedToInt:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'seed': ('SEED',)}}
    RETURN_TYPES = ('INT', 'STRING')
    RETURN_NAMES = ('INT', 'show_help')
    FUNCTION = 'seed_to_int'
    CATEGORY = icons.get('Comfyroll/Essential/Legacy')

    def seed_to_int(self, seed):
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Conversion-Nodes#cr-seed-to-int'
        return (seed.get('seed'), show_help)
```