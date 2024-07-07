# Documentation
- Class name: CR_EncodeScheduledPrompts
- Category: Comfyroll/Animation/Prompt
- Output node: False
- Repo Ref: https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes

CR_EncodeScheduledPrompts Node is designed to manage the encoding of the hints in the animation sequence. It mixs the current and next hints intelligently according to the assigned weights to ensure a smooth transition between states. This node is essential for creating consistent and informative animations.

# Input types
## Required
- clip
    - The clip parameter is essential because it represents the core input of the encoded process. It is the raw data that will be marked and encoded to generate the hint.
    - Comfy dtype: CLIP
    - Python dtype: torch.Tensor
- current_prompt
    - The current_prompt parameter is the text input used in the current animation. It is a key component of the encoding process, as it defines the starting point of the transition.
    - Comfy dtype: STRING
    - Python dtype: str
- next_prompt
    - Next_prompt parameters represent the upcoming text input that the animation will transition to. It plays a vital role in determining the direction of the hint code.
    - Comfy dtype: STRING
    - Python dtype: str
- weight
    - The weight parameter is used to control the mix of the current and next hints. It directly influences the coding process by determining the intensity of the transition.
    - Comfy dtype: FLOAT
    - Python dtype: float

# Output types
- CONDITIONING
    - CONDITONING output stands for encoded hints and is prepared for animation. It is a key output because it provides the necessary data for subsequent animation steps.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Tuple[torch.Tensor, Dict[str, torch.Tensor]]]
- show_help
    - Show_help output provides a URL link to the document to further assist and understand how to use the node effectively.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: GPU

# Source code
```
class CR_EncodeScheduledPrompts:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'clip': ('CLIP',), 'current_prompt': ('STRING', {'multiline': True}), 'next_prompt': ('STRING', {'multiline': True}), 'weight': ('FLOAT', {'default': 0.0, 'min': -9999.0, 'max': 9999.0, 'step': 0.01})}}
    RETURN_TYPES = ('CONDITIONING', 'STRING')
    RETURN_NAMES = ('CONDITIONING', 'show_help')
    FUNCTION = 'condition'
    CATEGORY = icons.get('Comfyroll/Animation/Prompt')

    def condition(self, clip, current_prompt, next_prompt, weight):
        tokens = clip.tokenize(str(next_prompt))
        (cond_from, pooled_from) = clip.encode_from_tokens(tokens, return_pooled=True)
        tokens = clip.tokenize(str(current_prompt))
        (cond_to, pooled_to) = clip.encode_from_tokens(tokens, return_pooled=True)
        print(weight)
        conditioning_to_strength = weight
        conditioning_from = [[cond_from, {'pooled_output': pooled_from}]]
        conditioning_to = [[cond_to, {'pooled_output': pooled_to}]]
        out = []
        if len(conditioning_from) > 1:
            print('Warning: Conditioning from contains more than 1 cond, only the first one will actually be applied to conditioning_to.')
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
        show_help = 'https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Prompt-Nodes#cr-encode-scheduled-prompts'
        return (out, show_help)
```