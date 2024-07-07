# Documentation
- Class name: CR_ConditioningMixer
- Category: Comfyroll/Essential/Core
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

The CR_ConditioningMixer node is designed to mix or group different conditions. It provides a method for consolidating or average condition data, which is essential for some machine learning applications, where input conditions are key to model performance. The function of the node is abstracted to ensure flexibility and allows users to choose combinations, averages or connection conditions to enter to achieve the desired results.

# Input types
## Required
- conditioning_1
    - The first condition input is essential for the operation of the node, as it represents one of the main data sources that will enter the operation or combination with another condition. It plays a key role in determining the final output of the node.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Tuple[torch.Tensor, Dict[str, torch.Tensor]]]
- conditioning_2
    - The second condition input is another key element of the node function. It is used with the first condition input to create a mixed or mixed output based on the selected mix method.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Tuple[torch.Tensor, Dict[str, torch.Tensor]]]
- mix_method
    - Mixed method parameters define how to combine a condition input. It is a key determinant of node operations and allows for different strategies, such as grouping, average or connection input.
    - Comfy dtype: COMBO['Combine', 'Average', 'Concatenate']
    - Python dtype: str
## Optional
- average_strength
    - When the mix is set to 'Average', the average strength parameters are used. It controls the mix ratio between the two conditions, affecting the final output according to the specified strength.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- CONDITIONING
    - The output condition is the application of the chosen mix method to the result of the input condition. It contains consolidated or processed data ready for further use in machine learning pipes.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Tuple[torch.Tensor, Dict[str, torch.Tensor]]]
- show_help
    - Show_help provides a URL link to the node document. It is a useful reference for users seeking more information on how to use the node effectively.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class CR_ConditioningMixer:

    @classmethod
    def INPUT_TYPES(cls):
        mix_methods = ['Combine', 'Average', 'Concatenate']
        return {'required': {'conditioning_1': ('CONDITIONING',), 'conditioning_2': ('CONDITIONING',), 'mix_method': (mix_methods,), 'average_strength': ('FLOAT', {'default': 0.5, 'min': 0.0, 'max': 1.0, 'step': 0.01})}}
    RETURN_TYPES = ('CONDITIONING', 'STRING')
    RETURN_NAMES = ('CONDITIONING', 'show_help')
    FUNCTION = 'conditioning'
    CATEGORY = icons.get('Comfyroll/Essential/Core')

    def conditioning(self, mix_method, conditioning_1, conditioning_2, average_strength):
        conditioning_from = conditioning_1
        conditioning_to = conditioning_2
        conditioning_to_strength = average_strength
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Core-Nodes#cr-conditioning-mixer'
        if mix_method == 'Combine':
            return (conditioning_1 + conditioning_2, show_help)
        if mix_method == 'Average':
            out = []
            if len(conditioning_from) > 1:
                print('Warning: ConditioningAverage conditioning_from contains more than 1 cond, only the first one will actually be applied to conditioning_to.')
            cond_from = conditioning_from[0][0]
            pooled_output_from = conditioning_from[0][1].get('pooled_output', None)
            for i in range(len(conditioning_to)):
                t1 = conditioning_to[i][0]
                pooled_output_to = conditioning_to[i][1].get('pooled_output', pooled_output_from)
                t0 = cond_from[:, :t1.shape[1]]
                if t0.shape[1] < t1.shape[1]:
                    t0 = torch.cat([t0] + [torch.zeros((1, t1.shape[1] - t0.shape[1], t1.shape[2]))], dim=1)
                tw = torch.mul(t1, conditioning_to_strength) + torch.mul(t0, 1.0 - conditioning_to_strength)
                t_to = conditioning_to[i][1].copy()
                if pooled_output_from is not None and pooled_output_to is not None:
                    t_to['pooled_output'] = torch.mul(pooled_output_to, conditioning_to_strength) + torch.mul(pooled_output_from, 1.0 - conditioning_to_strength)
                elif pooled_output_from is not None:
                    t_to['pooled_output'] = pooled_output_from
                n = [tw, t_to]
                out.append(n)
            return (out, show_help)
        if mix_method == 'Concatenate':
            out = []
            if len(conditioning_from) > 1:
                print('Warning: ConditioningConcat conditioning_from contains more than 1 cond, only the first one will actually be applied to conditioning_to.')
            cond_from = conditioning_from[0][0]
            for i in range(len(conditioning_to)):
                t1 = conditioning_to[i][0]
                tw = torch.cat((t1, cond_from), 1)
                n = [tw, conditioning_to[i][1].copy()]
                out.append(n)
            return (out, show_help)
```