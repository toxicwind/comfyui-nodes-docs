# Documentation
- Class name: ShowCachedInfo
- Category: InspirePack/Backend
- Output node: True
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Inspire-Pack.git

The node is intended to display cache information and provide a clear and orderly view by classifying cache content by string and numeric key.

# Input types
## Required
- cache_info
    - The cache_info parameter is the cached text, which is formatted and displayed by the node. This is essential for the node to run, as it determines the content to be displayed to the user.
    - Comfy dtype: STRING
    - Python dtype: str
- unique_id
    - The unique_id parameter is the only example of identifying nodes in the system to ensure that the correct cache information is displayed for the intended user.
    - Comfy dtype: UNIQUE_ID
    - Python dtype: str
## Optional
- key
    - The key parameter is used to filter the cache information according to a given key. It is important to allow users to focus on specific cache entries.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- feedback
    - The feedback parameter contains information about node operations and the cache data displayed. It is important to provide a record of node execution.
    - Comfy dtype: DICT
    - Python dtype: Dict[str, Any]

# Usage tips
- Infra type: CPU

# Source code
```
class ShowCachedInfo:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'cache_info': ('STRING', {'multiline': True, 'default': ''}), 'key': ('STRING', {'multiline': False, 'default': ''})}, 'hidden': {'unique_id': 'UNIQUE_ID'}}
    RETURN_TYPES = ()
    FUNCTION = 'doit'
    CATEGORY = 'InspirePack/Backend'
    OUTPUT_NODE = True

    @staticmethod
    def get_data():
        global cache
        text1 = '---- [String Key Caches] ----\n'
        text2 = '---- [Number Key Caches] ----\n'
        for (k, v) in cache.items():
            if v[0] == '':
                tag = 'N/A(tag)'
            else:
                tag = v[0]
            if isinstance(k, str):
                text1 += f'{k}: {tag}\n'
            else:
                text2 += f'{k}: {tag}\n'
        return text1 + '\n' + text2

    def doit(self, cache_info, key, unique_id):
        text = ShowCachedInfo.get_data()
        PromptServer.instance.send_sync('inspire-node-feedback', {'node_id': unique_id, 'widget_name': 'cache_info', 'type': 'text', 'data': text})
        return {}

    @classmethod
    def IS_CHANGED(cls, **kwargs):
        return float('NaN')
```