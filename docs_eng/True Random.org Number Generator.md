# Documentation
- Class name: WAS_True_Random_Number
- Category: WAS Suite/Number
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_True_Random_Nummer node is designed to generate random numbers with high security and reliability. It uses RANDOM.ORG API to provide users with real random numbers to ensure a high degree of unpredictability and fairness in applications where randomness is essential.

# Input types
## Required
- api_key
    - API keys are essential for accessing RANDOM.ORG services. They verify user requests and enable random numbers to be generated. Nodes cannot perform their intended functions without valid API keys.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- minimum
    - The minimum value parameter defines the lower limit of the range within which a random number is generated. It ensures that the output number meets the specified minimum criterion, which is essential for applications with specific numerical requirements.
    - Comfy dtype: FLOAT
    - Python dtype: float
- maximum
    - The maximum value parameter sets a ceiling on the random number range generated. This is important to control the size of the number and to align it with the needs of the application.
    - Comfy dtype: FLOAT
    - Python dtype: float
- mode
    - Model parameters determine whether random numbers are generated by random or fixed sequences. This affects the predictability and usage of numbers and is an important choice for users.
    - Comfy dtype: COMBO[random, fixed]
    - Python dtype: str

# Output types
- number
    - The output number is the core result of the node operation. It represents the true random number generated within the specified range and is the basic element that requires random applications.
    - Comfy dtype: COMBO[NUMBER, FLOAT, INT]
    - Python dtype: Union[int, float]

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_True_Random_Number:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'api_key': ('STRING', {'default': '00000000-0000-0000-0000-000000000000', 'multiline': False}), 'minimum': ('FLOAT', {'default': 0, 'min': -18446744073709551615, 'max': 18446744073709551615}), 'maximum': ('FLOAT', {'default': 10000000, 'min': -18446744073709551615, 'max': 18446744073709551615}), 'mode': (['random', 'fixed'],)}}
    RETURN_TYPES = ('NUMBER', 'FLOAT', 'INT')
    FUNCTION = 'return_true_randm_number'
    CATEGORY = 'WAS Suite/Number'

    def return_true_randm_number(self, api_key=None, minimum=0, maximum=10):
        number = self.get_random_numbers(api_key=api_key, minimum=minimum, maximum=maximum)[0]
        return (number,)

    def get_random_numbers(self, api_key=None, amount=1, minimum=0, maximum=10, mode='random'):
        """Get random number(s) from random.org"""
        if api_key in [None, '00000000-0000-0000-0000-000000000000', '']:
            cstr('No API key provided! A valid RANDOM.ORG API key is required to use `True Random.org Number Generator`').error.print()
            return [0]
        url = 'https://api.random.org/json-rpc/2/invoke'
        headers = {'Content-Type': 'application/json'}
        payload = {'jsonrpc': '2.0', 'method': 'generateIntegers', 'params': {'apiKey': api_key, 'n': amount, 'min': minimum, 'max': maximum, 'replacement': True, 'base': 10}, 'id': 1}
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        if response.status_code == 200:
            data = response.json()
            if 'result' in data:
                return (data['result']['random']['data'], float(data['result']['random']['data']), int(data['result']['random']['data']))
        return [0]

    @classmethod
    def IS_CHANGED(cls, api_key, mode, **kwargs):
        m = hashlib.sha256()
        m.update(api_key)
        if mode == 'fixed':
            return m.digest().hex()
        return float('NaN')
```