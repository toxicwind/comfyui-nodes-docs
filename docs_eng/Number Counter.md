# Documentation
- Class name: WAS_Number_Counter
- Category: WAS Suite/Number
- Output node: False
- Repo Ref: https://github.com/WASasquatch/was-node-suite-comfyui

The WAS_Number_Counter node is designed to manage and operate values according to the specified operating mode. It effectively handles incremental, decreasing and border control count operations. This node applies in particular to applications that require sequence generation or iterative value adjustments.

# Input types
## Required
- number_type
    - The `number_type' parameter determines the type of value that the node will process, which may be integer or floating point numbers. This selection affects accuracy and the type of arithmetic operation that can be performed.
    - Comfy dtype: STRING
    - Python dtype: str
- mode
    - The'mode'parameter indicates how the counter value will be modified. It can be set as an increment, decrease, increase to a stop value, or decrease to a stop value, which is essential for controlling counting behaviour.
    - Comfy dtype: STRING
    - Python dtype: str
- start
    - The `start' parameter sets the initial value of the counter. This is a basic setting that sets the starting point for all counting operations performed by nodes.
    - Comfy dtype: FLOAT
    - Python dtype: Union[int, float]
- stop
    - The'stop'parameter defines the boundary value of the operation of the count. When this value is reached, the increment or reduction will be stopped according to the selected mode.
    - Comfy dtype: FLOAT
    - Python dtype: Union[int, float]
- step
    - The'step' parameter specifies the increment or impairment value to be applied to the counter during each operation. It directly affects the rate of change in the value series.
    - Comfy dtype: FLOAT
    - Python dtype: float
- unique_id
    - The `unique_id' parameter is the only identifier for each counter managed by the node. It ensures that each count operation is independently tracked and operated.
    - Comfy dtype: UNIQUE_ID
    - Python dtype: str
## Optional
- reset_bool
    - The `reset_bol' parameter allows the counter to be reset to its initial value when set to a value greater than or equal to one. It provides a way to restart counting operations.
    - Comfy dtype: NUMBER
    - Python dtype: Optional[Union[int, bool]]

# Output types
- number
    - The 'number'output provides an integer of the current value of the post-operational counter. It is particularly useful when integer accuracy is required.
    - Comfy dtype: INT
    - Python dtype: int
- float
    - The 'float'output provides a floating point for the current value of the counter. It applies to scenarios where decimal accuracy is required.
    - Comfy dtype: FLOAT
    - Python dtype: float
- int
    - The `int' output returns the integer value of the counter, similar to the `number' output, ensuring that the result is presented in the integer type.
    - Comfy dtype: INT
    - Python dtype: int

# Usage tips
- Infra type: CPU

# Source code
```
class WAS_Number_Counter:

    def __init__(self):
        self.counters = {}

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'number_type': (['integer', 'float'],), 'mode': (['increment', 'decrement', 'increment_to_stop', 'decrement_to_stop'],), 'start': ('FLOAT', {'default': 0, 'min': -18446744073709551615, 'max': 18446744073709551615, 'step': 0.01}), 'stop': ('FLOAT', {'default': 0, 'min': -18446744073709551615, 'max': 18446744073709551615, 'step': 0.01}), 'step': ('FLOAT', {'default': 1, 'min': 0, 'max': 99999, 'step': 0.01})}, 'optional': {'reset_bool': ('NUMBER',)}, 'hidden': {'unique_id': 'UNIQUE_ID'}}

    @classmethod
    def IS_CHANGED(cls, **kwargs):
        return float('NaN')
    RETURN_TYPES = ('NUMBER', 'FLOAT', 'INT')
    RETURN_NAMES = ('number', 'float', 'int')
    FUNCTION = 'increment_number'
    CATEGORY = 'WAS Suite/Number'

    def increment_number(self, number_type, mode, start, stop, step, unique_id, reset_bool=0):
        counter = int(start) if mode == 'integer' else start
        if self.counters.__contains__(unique_id):
            counter = self.counters[unique_id]
        if round(reset_bool) >= 1:
            counter = start
        if mode == 'increment':
            counter += step
        elif mode == 'deccrement':
            counter -= step
        elif mode == 'increment_to_stop':
            counter = counter + step if counter < stop else counter
        elif mode == 'decrement_to_stop':
            counter = counter - step if counter > stop else counter
        self.counters[unique_id] = counter
        result = int(counter) if number_type == 'integer' else float(counter)
        return (result, float(counter), int(counter))
```