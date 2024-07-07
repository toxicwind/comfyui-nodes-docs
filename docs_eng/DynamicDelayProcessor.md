# Documentation
- Class name: DynamicDelayProcessor
- Category: ♾️Mixlab/Utils
- Output node: False
- Repo Ref: https://github.com/shadowcz007/comfyui-mixlab-nodes.git

DynamicDelayProcessor is a node designed to introduce controlled delays in the process. It allows for the timing of implementation to be adjusted to input parameters and provides flexibility for processing time-sensitive operations. This node is particularly suitable for scenarios where the output generation time needs to be synchronized with an external event or controlled to match a given speed.

# Input types
## Required
- delay_seconds
    - The delay_seconds parameter determines the basic delay duration to be introduced before processing input. It is a fundamental aspect of node operations, as it directly affects the timing of node execution and the moment of output generation.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- delay_by_text
    - The delay_by_text parameter allows the delay to be adjusted according to the length of the text provided. This is an optional feature that adds a layer of customization to the node delay function to enable it to adapt to various text-based input and related delays.
    - Comfy dtype: STRING
    - Python dtype: str
- words_per_seconds
    - Words_per_seconds parameters are used in conjunction with delay_by_text to calculate additional delays based on the length of the text. It plays a key role in the delayed behaviour of the microreconciliation point to accommodate different text length and rhythm requirements.
    - Comfy dtype: FLOAT
    - Python dtype: float
- replace_output
    - The replace_output parameter determines whether the output of the post-delay node should be replaced with the specified value. This function provides an additional level of control over the output, allowing the node either to transmit the original input or to replace it with a predefined value.
    - Comfy dtype: COMBO
    - Python dtype: Union[str, None]
- replace_value
    - The replace_value parameter specifies the value to be used if the replace_output parameter is set to 'enable'. It is essential to achieve the replacement function, ensuring that the output is accurately modified according to the user's specifications.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- output
    - The output parameter represents the result of the node operation. Depending on the configuration, it can be a transfer from the original input, or a replacement value specified for the replace_output and replace_value parameters. It encapsifies the final result of the node delayed processing.
    - Comfy dtype: ANY
    - Python dtype: Any

# Usage tips
- Infra type: CPU

# Source code
```
class DynamicDelayProcessor:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'delay_seconds': ('INT', {'default': 1, 'min': 0, 'max': 1000000})}, 'optional': {'any_input': (any_type,), 'delay_by_text': ('STRING', {'multiline': True, 'dynamicPrompts': False}), 'words_per_seconds': ('FLOAT', {'default': 1.5, 'min': 0.0, 'max': 1000.0, 'display': 'Chars per second?'}), 'replace_output': (['disable', 'enable'],), 'replace_value': ('INT', {'default': -1, 'min': 0, 'max': 1000000, 'display': 'Replacement value'})}}

    @classmethod
    def calculate_words_length(cls, text):
        chinese_char_pattern = re.compile('[\\u4e00-\\u9fff]')
        english_word_pattern = re.compile('\\b[a-zA-Z]+\\b')
        number_pattern = re.compile('\\b[0-9]+\\b')
        words_length = 0
        for segment in text.split():
            if chinese_char_pattern.search(segment):
                words_length += len(segment)
            elif number_pattern.match(segment):
                words_length += len(segment)
            elif english_word_pattern.match(segment):
                words_length += 1
        return words_length
    FUNCTION = 'run'
    RETURN_TYPES = (any_type,)
    RETURN_NAMES = ('output',)
    CATEGORY = '♾️Mixlab/Utils'

    def run(self, any_input, delay_seconds, delay_by_text, words_per_seconds, replace_output, replace_value):
        start_time = time.time()
        delay_time = delay_seconds
        if delay_by_text and isinstance(delay_by_text, str) and (words_per_seconds > 0):
            words_length = self.calculate_words_length(delay_by_text)
            print(f'Delay text: {delay_by_text}, Length: {words_length}')
            delay_time += words_length / words_per_seconds
        (f'delayed execution: {delay_time})
        time.sleep(delay_time)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f'actual delay: {elapsed_time}second')
        return (max(0, replace_value),) if replace_output == 'enable' else (any_input,)
```