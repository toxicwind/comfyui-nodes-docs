# Documentation
- Class name: KfApplyCurveToCond
- Category: CONDITIONING
- Output node: False
- Repo Ref: https://github.com/dmarx/ComfyUI-Keyframed

This node adjusts the strength of the conditional data according to the dynamics of the given curve and allows for minor control of the effect of the condition variable during the generation process.

# Input types
## Required
- curve
    - Curve input is a series of values that will be used to reconcile the condition data and represent the expected adjustment of the strength of the condition over time or other variables.
    - Comfy dtype: KEYFRAMED_CURVE
    - Python dtype: List[float]
- cond
    - The condition data to be adjusted will be entered into the curve, usually including the mass and the metadata associated with it, to provide context for the generation process.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Tuple[torch.Tensor, Dict]]
## Optional
- latents
    - Optional potential data can be used to further refine the application of curves to condition data and to enhance the adaptability of nodes to different cases.
    - Comfy dtype: LATENT
    - Python dtype: Dict
- start_t
    - The starting index of the curve to be applied can be used to control the segments of the curve that affect the condition data.
    - Comfy dtype: INT
    - Python dtype: int
- n
    - The number of samples to be generated, if potential data are provided, can be extrapolated to determine the length of the curve fragments to be applied to the condition data.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- cond_out
    - The output is the modified condition data, the strength of which has been adjusted to the input curve, thus providing a more customized effect during the generation process.
    - Comfy dtype: CONDITIONING
    - Python dtype: List[Tuple[torch.Tensor, Dict]]

# Usage tips
- Infra type: CPU

# Source code
```
class KfApplyCurveToCond:
    CATEGORY = CATEGORY
    FUNCTION = 'main'
    RETURN_TYPES = ('CONDITIONING',)

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'curve': ('KEYFRAMED_CURVE', {'forceInput': True}), 'cond': ('CONDITIONING', {'forceInput': True})}, 'optional': {'latents': ('LATENT', {}), 'start_t': ('INT', {'default': 0}), 'n': ('INT', {})}}

    def main(self, curve, cond, latents=None, start_t=0, n=0):
        curve = deepcopy(curve)
        cond = deepcopy(cond)
        if isinstance(latents, dict):
            if 'samples' in latents:
                n = latents['samples'].shape[0]
        cond_out = []
        for (c_tensor, c_dict) in cond:
            m = c_tensor.shape[0]
            if c_tensor.shape[0] == 1:
                c_tensor = c_tensor.repeat(n, 1, 1)
                m = n
            weights = [curve[start_t + i] for i in range(m)]
            weights = torch.tensor(weights, device=c_tensor.device)
            c_tensor = c_tensor * weights.view(m, 1, 1)
            if 'pooled_output' in c_dict:
                c_dict = deepcopy(c_dict)
                pooled = c_dict['pooled_output']
                if pooled.shape[0] == 1:
                    pooled = pooled.repeat(m, 1)
                c_dict['pooled_output'] = pooled * weights.view(m, 1)
            cond_out.append((c_tensor, c_dict))
        return (cond_out,)
```