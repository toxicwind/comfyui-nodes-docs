# Documentation
- Class name: ChatGPTNode
- Category: ♾️Mixlab/GPT
- Output node: False
- Repo Ref: https://github.com/shadowcz007/comfyui-mixlab-nodes.git

The ChatGPTNode class is designed to generate context-sensitive text using large-scale language models provided by OpenAI. It manages session history to maintain a dialogue process, allowing for more coherent and relevant responses. The node is good at integrating models and APIs to ensure flexibility and adaptability in different application scenarios.

# Input types
## Required
- api_key
    - API key is essential for validating and authorizing access to language model services. It plays a central role in ensuring secure communication with API, enabling nodes to access and process language model responses.
    - Comfy dtype: KEY
    - Python dtype: str
- api_url
    - API URL specifies the endpoint of the language model service. It is essential to point node requests to the right service, affecting the interaction of nodes with language models and the ability to retrieve data from language models.
    - Comfy dtype: URL
    - Python dtype: str
- prompt
    - A reminder is the input query or statement that the language model uses to generate a response. It is the key element for node operations, as it directly affects the content and direction of the text generated.
    - Comfy dtype: STRING
    - Python dtype: str
- system_content
    - System content provides a systematic command or context for a language model, which influences the style and tone of the response. It is an optional parameter that can be used to customise the behaviour of nodes.
    - Comfy dtype: STRING
    - Python dtype: str
- model
    - Model parameters select the language-specific model to be used by the node. It determines the complexity and ability of the language model to interact, the quality and the type of response it produces.
    - Comfy dtype: COMBO[gpt-3.5-turbo, gpt-35-turbo, gpt-3.5-turbo-16k, gpt-3.5-turbo-16k-0613, gpt-4-0613, gpt-4-1106-preview, glm-4]
    - Python dtype: str
- seed
    - Seeds provide a starting point for random numbers to be generated in a language model. They can be used to produce repeatable results by ensuring the consistent initial state of the random process of the model.
    - Comfy dtype: INT
    - Python dtype: int
- context_size
    - The context size determines the number of previous exchanges that will be taken into account in generating the response. It affects the depth of the context of the dialogue and the relevance of producing the text.
    - Comfy dtype: INT
    - Python dtype: int
- unique_id
    - The only ID is an optional identifier that can be used to track or quote specific interactions with language models. It does not affect the execution of nodes, but may be useful for recording or debugging purposes.
    - Comfy dtype: UNIQUE_ID
    - Python dtype: str
- extra_pnginfo
    - Additional PNG information is an optional parameter that provides additional context or data for a language model. It is used in specific applications and enhances the ability of nodes to generate more detailed or specific responses.
    - Comfy dtype: EXTRA_PNGINFO
    - Python dtype: str

# Output types
- text
    - Text output represents the language model's response to the input hint. It is the main result of the node operation and reflects the ability of the node to generate consistent text that is relevant to the context.
    - Comfy dtype: STRING
    - Python dtype: str
- messages
    - Message output is a JSON-format string that contains the history of dialogue before the current sound. It includes system commands, user tips and helper responses, providing an interactive and comprehensive view.
    - Comfy dtype: STRING
    - Python dtype: str
- session_history
    - The session history output is a string in a JSON format that records the entire conversation session with the language model. As a record of the dialogue, it can be used to analyse or maintain context in multiple interactions.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class ChatGPTNode:

    def __init__(self):
        self.session_history = []
        self.system_content = 'You are ChatGPT, a large language model trained by OpenAI. Answer as concisely as possible.'

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'api_key': ('KEY', {'default': '', 'multiline': True, 'dynamicPrompts': False}), 'api_url': ('URL', {'default': '', 'multiline': True, 'dynamicPrompts': False}), 'prompt': ('STRING', {'multiline': True, 'dynamicPrompts': False}), 'system_content': ('STRING', {'default': 'You are ChatGPT, a large language model trained by OpenAI. Answer as concisely as possible.', 'multiline': True, 'dynamicPrompts': False}), 'model': (['gpt-3.5-turbo', 'gpt-35-turbo', 'gpt-3.5-turbo-16k', 'gpt-3.5-turbo-16k-0613', 'gpt-4-0613', 'gpt-4-1106-preview', 'glm-4'], {'default': 'gpt-3.5-turbo'}), 'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615, 'step': 1}), 'context_size': ('INT', {'default': 1, 'min': 0, 'max': 30, 'step': 1})}, 'hidden': {'unique_id': 'UNIQUE_ID', 'extra_pnginfo': 'EXTRA_PNGINFO'}}
    RETURN_TYPES = ('STRING', 'STRING', 'STRING')
    RETURN_NAMES = ('text', 'messages', 'session_history')
    FUNCTION = 'generate_contextual_text'
    CATEGORY = '♾️Mixlab/GPT'
    INPUT_IS_LIST = False
    OUTPUT_IS_LIST = (False, False, False)

    def generate_contextual_text(self, api_key, api_url, prompt, system_content, model, seed, context_size, unique_id=None, extra_pnginfo=None):
        if system_content:
            self.system_content = system_content
        if is_azure_url(api_url):
            client = azure_client(api_key, api_url)
        elif model == 'glm-4':
            client = ZhipuAI_client(api_key)
            print('using Zhipuai interface')
        else:
            client = openai_client(api_key, api_url)
            print('using ChatGPT interface')

        def crop_list_tail(lst, size):
            if size >= len(lst):
                return lst
            elif size == 0:
                return []
            else:
                return lst[-size:]
        session_history = crop_list_tail(self.session_history, context_size)
        messages = [{'role': 'system', 'content': self.system_content}] + session_history + [{'role': 'user', 'content': prompt}]
        response_content = chat(client, model, messages)
        self.session_history = self.session_history + [{'role': 'user', 'content': prompt}] + [{'role': 'assistant', 'content': response_content}]
        return (response_content, json.dumps(messages, indent=4), json.dumps(self.session_history, indent=4))
```