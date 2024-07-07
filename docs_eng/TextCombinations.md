# Documentation
- Class name: TextCombinations2
- Category: Mikey/Text
- Output node: False
- Repo Ref: https://github.com/bash-j/mikey_nodes

TextCombinations node 2 is designed to generate a series of text operations that combine two input text in a defined operation. It facilitates the creation of the output text by performing the specified action on input and providing flexibility in text processing.

# Input types
## Required
- text1
    - The 'text1' parameter is the first input text to be used in a combination operation. It plays a key role in determining the final output, as it is one of the main elements of the operation.
    - Comfy dtype: STRING
    - Python dtype: str
- text2
    - The 'text2' parameter is a second input text that combines 'text1' with defined operations. Its content is essential to the output generation process.
    - Comfy dtype: STRING
    - Python dtype: str
- operation
    - The 'option' parameter defines the specific combination operation to be performed on the input text. It is vital because it determines how to convert 'text1' and 'text2' into the required output.
    - Comfy dtype: COMBO['text1 to output1', 'text2 to output2']
    - Python dtype: str
## Optional
- delimiter
    - The 'delimiter'parameter specifies that a character or string is used to connect a text component during the operation. It affects the formatting of the final output.
    - Comfy dtype: STRING
    - Python dtype: str
- use_seed
    - The 'use_seed'parameter determines whether a torrent value should be used to select an operation from the predefined list of operations. It adds randomity or specificity to the operation selection process.
    - Comfy dtype: COMBO['true', 'false']
    - Python dtype: str
- seed
    - The'seed' parameter is an integer value that is used to select a deflection operation when 'use_seed' is set to True. It ensures that a given operation is selected according to the integer provided.
    - Comfy dtype: INT
    - Python dtype: int
- extra_pnginfo
    - The 'extra_pnginfo'parameter saves additional information that may need to be used for certain operations. It is used to influence the behaviour of nodes based on additional contextual data.
    - Comfy dtype: EXTRA_PNGINFO
    - Python dtype: Union[Dict, str]
- prompt
    - The 'prompt' parameter provides guidance or additional context for nodes, which may change the way they process text input. It is particularly useful for nodes that require interactive or conditional behaviour.
    - Comfy dtype: PROMPT
    - Python dtype: Union[Dict, str]

# Output types
- output1
    - The 'output1'parameter represents the first result text after the group operation. It is the direct result of the input and the specified operation.
    - Comfy dtype: STRING
    - Python dtype: str
- output2
    - The 'output2'parameter represents the second result text after a combination operation. It is another output derived from the input and execution operation.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class TextCombinations2:
    texts = ['text1', 'text2', 'text1 + text2']
    outputs = ['output1', 'output2']

    @classmethod
    def generate_combinations(cls, texts, outputs):
        operations = []
        for (output1, output2) in product(texts, repeat=len(outputs)):
            operation = f'{output1} to {outputs[0]}, {output2} to {outputs[1]}'
            operations.append(operation)
        return operations

    @classmethod
    def INPUT_TYPES(cls):
        cls.operations = cls.generate_combinations(cls.texts, cls.outputs)
        return {'required': {'text1': ('STRING', {'multiline': True, 'default': 'Text 1'}), 'text2': ('STRING', {'multiline': True, 'default': 'Text 2'}), 'operation': (cls.operations, {'default': cls.operations[0]}), 'delimiter': ('STRING', {'default': ' '}), 'use_seed': (['true', 'false'], {'default': 'false'}), 'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615})}, 'hidden': {'extra_pnginfo': 'EXTRA_PNGINFO', 'prompt': 'PROMPT'}}
    RETURN_TYPES = ('STRING', 'STRING')
    RETURN_NAMES = ('output1', 'output2')
    FUNCTION = 'mix'
    CATEGORY = 'Mikey/Text'

    def mix(self, text1, text2, operation, delimiter, use_seed, seed, extra_pnginfo, prompt):
        text1 = search_and_replace(text1, extra_pnginfo, prompt)
        text2 = search_and_replace(text2, extra_pnginfo, prompt)
        text_dict = {'text1': text1, 'text2': text2}
        if use_seed == 'true' and len(self.operations) > 0:
            offset = seed % len(self.operations)
            operation = self.operations[offset]
        ops = operation.split(', ')
        output_texts = [op.split(' to ')[0] for op in ops]
        outputs = []
        for output_text in output_texts:
            components = output_text.split(' + ')
            final_output = delimiter.join((eval(comp, {}, text_dict) for comp in components))
            outputs.append(final_output)
        return tuple(outputs)
```