# Documentation
- Class name: ImpactSetWidgetValue
- Category: ImpactPack/Logic/_for_test
- Output node: True
- Repo Ref: https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

The 'doit' method of the ImpactSetWidgetValue node is designed to process the assignment of values from different data types to the specified control. It streamlines the interaction with the control in the ImpactPack package by determining the type of data and then applying the corresponding values to the control, managing the complexity of setting the control value in abstract terms.

# Input types
## Required
- signal
    - The `signal' parameter is essential for the operation of the node because it represents the control signal that triggers the process of giving the control value. The node is necessary for it to function correctly.
    - Comfy dtype: any_typ
    - Python dtype: Any
- node_id
    - The `node_id' parameter is essential because it is the only node in the system that allows the control value to be accurately located. It plays a key role in ensuring that the control is correctly operated.
    - Comfy dtype: INT
    - Python dtype: int
- widget_name
    - The `widget_name' parameter is essential for the function of the node, as it specifies the name of the control to be given the value. It is the key message for the successful implementation of the node purpose.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- boolean_value
    - When the `boolean_value' parameter is provided, the node is allowed to assign the boolean value to the specified control, which enhances the multifunctionality of node operations.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- int_value
    - When using the `int_value' parameter, enable the node to set the whole value for the control and contribute to the ability of the node to process various data types.
    - Comfy dtype: INT
    - Python dtype: int
- float_value
    - If the `float_value' parameter is provided, the indicator node assigns the number of floating points to the control, demonstrating the ability of the node to manage different numeric formats.
    - Comfy dtype: FLOAT
    - Python dtype: float
- string_value
    - When providing `string_value' parameters, allows nodes to assign strings to the control, highlighting the flexibility of nodes in processing string data for the control configuration.
    - Comfy dtype: STRING
    - Python dtype: str

# Output types
- signal_opt
    - The `signal_opt' output parameter represents the optional control signal that may be returned by the node after the control value has been given, indicating the completion of the operation.
    - Comfy dtype: any_typ
    - Python dtype: Any

# Usage tips
- Infra type: CPU

# Source code
```
class ImpactSetWidgetValue:

    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {'signal': (any_typ,), 'node_id': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615}), 'widget_name': ('STRING', {'multiline': False})}, 'optional': {'boolean_value': ('BOOLEAN', {'forceInput': True}), 'int_value': ('INT', {'forceInput': True}), 'float_value': ('FLOAT', {'forceInput': True}), 'string_value': ('STRING', {'forceInput': True})}}
    FUNCTION = 'doit'
    CATEGORY = 'ImpactPack/Logic/_for_test'
    RETURN_TYPES = (any_typ,)
    RETURN_NAMES = ('signal_opt',)
    OUTPUT_NODE = True

    def doit(self, signal, node_id, widget_name, boolean_value=None, int_value=None, float_value=None, string_value=None):
        kind = None
        if boolean_value is not None:
            value = boolean_value
            kind = 'BOOLEAN'
        elif int_value is not None:
            value = int_value
            kind = 'INT'
        elif float_value is not None:
            value = float_value
            kind = 'FLOAT'
        elif string_value is not None:
            value = string_value
            kind = 'STRING'
        else:
            value = None
        if value is not None:
            PromptServer.instance.send_sync('impact-node-feedback', {'node_id': node_id, 'widget_name': widget_name, 'type': kind, 'value': value})
        return (signal,)
```