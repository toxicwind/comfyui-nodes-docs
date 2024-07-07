# Documentation
- Class name: CR_TextListSimple
- Category: Comfyroll/Animation/Legacy
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

The CR_TextListSimple node is designed to efficiently manage and group multiple text types into a single list. It applies to applications that require text aggregation, such as preparing lot-processed data or generating group text output. The node is known for its simplicity and flexibility and allows for easy integration of text sources into a unified structure.

# Input types
## Optional
- text_1
    - The parameter 'text_1'is an optional input that allows users to contribute a line of text to the list. It plays an important role in the process of aggregation and enhances the ability of nodes to process diverse text input.
    - Comfy dtype: STRING
    - Python dtype: str
- text_2
    - The parameter 'text_2' is another optional input that can be used to add a line of text to the list. It is essential in a scenario where multiple text entries are required to form a comprehensive data set.
    - Comfy dtype: STRING
    - Python dtype: str
- text_3
    - The parameter 'text_3'is used to include another line of text in the list. It contributes to the overall function of the node by providing more text content options for users.
    - Comfy dtype: STRING
    - Python dtype: str
- text_4
    - Parameter 'text_4' allows the inclusion of another line of text in the list, further expanding the range of text input that can be integrated by nodes.
    - Comfy dtype: STRING
    - Python dtype: str
- text_5
    - The parameter 'text_5'is an optional field where the user can add another line of text to the list. It is an important part of the node design to adapt to various text input.
    - Comfy dtype: STRING
    - Python dtype: str
- text_list_simple
    - Parameter 'text_list_simple' is an optional input that allows for a pre-existing list of text lines. This is very useful for users who want to expand or modify the existing list of text without having to start from scratch.
    - Comfy dtype: TEXT_LIST_SIMPLE
    - Python dtype: List[str]

# Output types
- TEXT_LIST_SIMPLE
    - Output 'TEXT_LIST_SIMPLE' is a consolidated list of all text inputs to nodes. It represents the main result of node operations as a polymer text data set prepared for further processing or analysis.
    - Comfy dtype: TEXT_LIST_SIMPLE
    - Python dtype: List[str]
- show_help
    - Output'show_help' provides a URL link to the node document page, allowing users direct access to additional information and guidance on the effective use of the node.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_TextListSimple:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {}, 'optional': {'text_1': ('STRING', {'multiline': False, 'default': ''}), 'text_2': ('STRING', {'multiline': False, 'default': ''}), 'text_3': ('STRING', {'multiline': False, 'default': ''}), 'text_4': ('STRING', {'multiline': False, 'default': ''}), 'text_5': ('STRING', {'multiline': False, 'default': ''}), 'text_list_simple': ('TEXT_LIST_SIMPLE',)}}
    RETURN_TYPES = ('TEXT_LIST_SIMPLE', 'STRING')
    RETURN_NAMES = ('TEXT_LIST_SIMPLE', 'show_help')
    FUNCTION = 'text_list_simple'
    CATEGORY = icons.get('Comfyroll/Animation/Legacy')

    def text_list_simple(self, text_1, text_2, text_3, text_4, text_5, text_list_simple=None):
        texts = list()
        if text_list_simple is not None:
            texts.extend((l for l in text_list_simple))
        if text_1 != '' and text_1 != None:
            (texts.append(text_1),)
        if text_2 != '' and text_2 != None:
            texts.append(text_2)
        if text_3 != '' and text_3 != None:
            texts.append(text_3)
        if text_4 != '' and text_4 != None:
            (texts.append(text_4),)
        if text_5 != '' and text_5 != None:
            (texts.append(text_5),)
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/List-Nodes#cr-text-list-simple'
        return (texts, show_help)
```